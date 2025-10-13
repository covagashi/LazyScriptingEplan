# src/ai/optimized_rag.py
import numpy as np
import faiss
import os
import pickle
import re
from pathlib import Path
from typing import List, Dict, Any, Optional
from sentence_transformers import SentenceTransformer
from rank_bm25 import BM25Okapi
import logging

logger = logging.getLogger(__name__)

# Common English stopwords for technical documentation
STOPWORDS = {
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'was', 'will', 'with'
}

class OptimizedRAG:
    """High-performance RAG with quantization and FAISS indexing"""

    def __init__(self, embedding_dim: int = 384, use_reranker: bool = True):
        self.embedding_dim = embedding_dim
        self.model = None
        self.reranker_model = None
        self.use_reranker = use_reranker
        self.documents = []
        self.index = None
        self.bm25_index = None
        self.doc_map = {}  # ID to document mapping

        # Quantization settings
        self.use_quantization = True
        self.nlist = 100  # Number of clusters for IVF
        self.nprobe = 10  # Search clusters

        # Re-ranking settings
        self.rerank_candidates = 20  # Number of candidates to retrieve before re-ranking
        self.rerank_final = 5  # Number of final results after re-ranking

    @staticmethod
    def tokenize(text: str) -> List[str]:
        """Advanced tokenization for BM25 with stopword removal"""
        # Convert to lowercase and extract alphanumeric tokens
        # This handles punctuation and preserves technical terms like "API" or "C#"
        tokens = re.findall(r'\b\w+\b', text.lower())

        # Remove stopwords and very short tokens (len < 2)
        tokens = [t for t in tokens if len(t) > 2 and t not in STOPWORDS]

        return tokens

    @staticmethod
    def chunk_text(text: str, chunk_size: int = 512, overlap: int = 50) -> List[str]:
        """
        Split text into overlapping chunks for better semantic search.

        Args:
            text: Text to chunk
            chunk_size: Approximate number of words per chunk
            overlap: Number of words to overlap between chunks

        Returns:
            List of text chunks
        """
        # Split by words while preserving structure
        words = text.split()

        if len(words) <= chunk_size:
            return [text]

        chunks = []
        start = 0

        while start < len(words):
            end = start + chunk_size
            chunk_words = words[start:end]
            chunks.append(' '.join(chunk_words))

            # Move start forward with overlap
            start = end - overlap

            # Prevent infinite loop
            if start >= len(words):
                break

        return chunks
        
    def _init_model(self):
        """
        Initializes the SentenceTransformer model with offline-first strategy.

        Priority:
        1. Local cache in project directory (src/ai/models/)
        2. System-wide HuggingFace cache
        3. Download from HuggingFace (if internet available)
        4. Fallback to TF-IDF if no model available
        """
        if self.model is None:
            from sentence_transformers import SentenceTransformer
            import os

            # Define local model path within project
            local_model_path = Path("src/ai/models/all-MiniLM-L6-v2")

            try:
                # Try loading from local project directory first
                if local_model_path.exists():
                    logger.info(f"Loading model from local cache: {local_model_path}")
                    self.model = SentenceTransformer(str(local_model_path), local_files_only=True)
                    logger.info("✓ Model loaded successfully from local cache")
                else:
                    # Try loading from system cache or download
                    logger.info("Attempting to load model (will use system cache if available)...")
                    try:
                        self.model = SentenceTransformer('all-MiniLM-L6-v2')
                        logger.info("✓ Model loaded successfully")
                    except Exception as e:
                        logger.warning(f"Could not download model (possibly offline): {e}")
                        # Try one more time with local_files_only
                        logger.info("Attempting to load from system cache only...")
                        self.model = SentenceTransformer('all-MiniLM-L6-v2', local_files_only=True)
                        logger.info("✓ Model loaded from system cache")

            except Exception as e:
                logger.error(f"Failed to load embedding model: {e}")
                logger.warning("⚠️  Falling back to BM25-only search (no vector embeddings)")
                self.model = None  # Will use BM25-only mode

    def _init_reranker(self):
        """
        Initializes the Cross-Encoder model for re-ranking.

        Uses a lightweight Cross-Encoder that's more accurate than bi-encoders
        for relevance scoring, but slower (so we use it on a smaller candidate set).
        """
        if not self.use_reranker or self.reranker_model is not None:
            return

        try:
            from sentence_transformers import CrossEncoder

            # Define local reranker path
            local_reranker_path = Path("src/ai/models/ms-marco-MiniLM-L-6-v2")

            # Try loading from local cache first
            if local_reranker_path.exists():
                logger.info(f"Loading re-ranker from local cache: {local_reranker_path}")
                self.reranker_model = CrossEncoder(str(local_reranker_path), max_length=512)
                logger.info("✓ Re-ranker loaded from local cache")
            else:
                # Try downloading or loading from system cache
                logger.info("Loading re-ranker model (cross-encoder/ms-marco-MiniLM-L-6-v2)...")
                try:
                    self.reranker_model = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2', max_length=512)
                    logger.info("✓ Re-ranker loaded successfully")
                except Exception as e:
                    logger.warning(f"Could not download re-ranker (possibly offline): {e}")
                    logger.info("Attempting to load from system cache only...")
                    self.reranker_model = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2', max_length=512, local_files_only=True)
                    logger.info("✓ Re-ranker loaded from system cache")

        except Exception as e:
            logger.warning(f"Failed to load re-ranker model: {e}")
            logger.info("⚠️  Re-ranking disabled - will use hybrid search only")
            self.reranker_model = None
            self.use_reranker = False

    def _create_index(self, vectors: np.ndarray) -> faiss.Index:
        """Create optimized FAISS index with quantization"""
        n_docs = vectors.shape[0]
        
        if n_docs < 1000:
            # Simple flat index for small datasets
            index = faiss.IndexFlatIP(self.embedding_dim)
        else:
            # Quantized index for larger datasets
            quantizer = faiss.IndexFlatIP(self.embedding_dim)
            
            if self.use_quantization:
                # IVF + PQ quantization
                index = faiss.IndexIVFPQ(
                    quantizer, 
                    self.embedding_dim, 
                    min(self.nlist, n_docs // 10),  # Adaptive nlist
                    8,  # PQ segments
                    8   # bits per segment
                )
                # Train the index
                index.train(vectors.astype(np.float32))
            else:
                # Just IVF without PQ
                index = faiss.IndexIVFFlat(
                    quantizer,
                    self.embedding_dim,
                    min(self.nlist, n_docs // 10)
                )
                index.train(vectors.astype(np.float32))
            
            index.nprobe = self.nprobe
            
        return index
    
    def build_index(self, documents: List[Dict], texts: List[str]):
        """
        Build optimized vector index and BM25 index.

        Falls back to BM25-only mode if embedding model is unavailable.
        """
        if not documents or not texts:
            logger.warning("No documents or texts provided for indexing")
            return

        self._init_model()

        # Vector index (only if model available)
        if self.model is not None:
            logger.info(f"Encoding {len(texts)} documents for vector search...")
            try:
                embeddings = self.model.encode(
                    texts,
                    batch_size=32,
                    show_progress_bar=True,
                    convert_to_numpy=True
                )
                faiss.normalize_L2(embeddings)
                self.index = self._create_index(embeddings)
                self.index.add(embeddings.astype(np.float32))
                logger.info(f"✓ Built FAISS vector index with {self.index.ntotal} vectors")
            except Exception as e:
                logger.error(f"Failed to build vector index: {e}")
                logger.warning("⚠️  Vector search disabled, using BM25-only mode")
                self.index = None
        else:
            logger.warning("⚠️  No embedding model available - Vector search disabled")
            logger.info("📝 Using BM25-only mode (keyword search)")
            self.index = None

        # BM25 index with improved tokenization (always available)
        logger.info(f"Creating BM25 index for keyword search...")
        tokenized_corpus = [self.tokenize(doc) for doc in texts]
        self.bm25_index = BM25Okapi(tokenized_corpus)
        logger.info(f"✓ Built BM25 index with {len(tokenized_corpus)} documents")

        # Store documents
        self.documents = documents
        self.doc_map = {i: doc for i, doc in enumerate(documents)}

        # Summary
        if self.index is not None:
            logger.info(f"🚀 Hybrid search ready: FAISS ({self.index.ntotal} vectors) + BM25 ({len(tokenized_corpus)} docs)")
        else:
            logger.info(f"🔍 BM25-only search ready with {len(tokenized_corpus)} documents")
        
    def search(self, query: str, top_k: int = 5, use_reranking: bool = None) -> List[Dict]:
        """
        Performs hybrid search using FAISS (vector) and BM25 (keyword),
        with optional Cross-Encoder re-ranking for improved precision.

        Args:
            query: Search query
            top_k: Number of final results to return
            use_reranking: Override default re-ranking behavior (None = use default)

        Returns:
            List of documents with scores
        """
        if self.bm25_index is None:
            logger.warning("Search attempted before indexes were built.")
            return []

        # Determine if we should use re-ranking
        enable_reranking = self.use_reranker if use_reranking is None else use_reranking

        # If re-ranking is enabled, retrieve more candidates first
        search_k = self.rerank_candidates if enable_reranking else top_k

        result_sets = []

        # 1. Vector Search (FAISS) - if available
        if self.index is not None and self.model is not None:
            try:
                self._init_model()
                query_embedding = self.model.encode([query], convert_to_numpy=True)
                faiss.normalize_L2(query_embedding)
                vector_scores, vector_indices = self.index.search(query_embedding.astype(np.float32), search_k)

                vector_results = list(zip(vector_indices[0], vector_scores[0]))
                result_sets.append(vector_results)
            except Exception as e:
                logger.warning(f"Vector search failed: {e}. Using BM25-only mode.")

        # 2. Keyword Search (BM25) - always available
        tokenized_query = self.tokenize(query)
        bm25_scores = self.bm25_index.get_scores(tokenized_query)
        bm25_indices = np.argsort(bm25_scores)[::-1][:search_k]
        bm25_results = list(zip(bm25_indices, [bm25_scores[i] for i in bm25_indices]))
        result_sets.append(bm25_results)

        # 3. Fuse results (or just use BM25 if only one result set)
        if len(result_sets) > 1:
            # Hybrid: RRF fusion
            fused_results = self._rrf_fusion(result_sets)
        else:
            # BM25-only mode
            fused_results = bm25_results

        # 4. Format candidate documents
        candidate_docs = []
        for doc_id, score in fused_results[:search_k]:
            candidate_docs.append({
                'document': self.doc_map[doc_id],
                'score': score
            })

        # 5. Apply Cross-Encoder re-ranking if enabled
        if enable_reranking and len(candidate_docs) > 0:
            self._init_reranker()  # Lazy load re-ranker
            final_docs = self._rerank_results(query, candidate_docs)
            return final_docs[:top_k]  # Return top_k after re-ranking
        else:
            return candidate_docs[:top_k]  # Return top_k without re-ranking

    def _rrf_fusion(self, result_sets: List[List], k: int = 60) -> List:
        """Performs Reciprocal Rank Fusion on multiple result sets."""
        fused_scores = {}
        for doc_set in result_sets:
            for rank, (doc_id, _) in enumerate(doc_set):
                if doc_id not in fused_scores:
                    fused_scores[doc_id] = 0
                fused_scores[doc_id] += 1 / (k + rank + 1)

        reranked_results = sorted(fused_scores.items(), key=lambda x: x[1], reverse=True)
        return reranked_results

    def _rerank_results(self, query: str, candidate_docs: List[Dict]) -> List[Dict]:
        """
        Re-rank candidate documents using Cross-Encoder for improved precision.

        Args:
            query: The search query
            candidate_docs: List of candidate documents with scores

        Returns:
            Re-ranked list of documents
        """
        if not self.use_reranker or self.reranker_model is None:
            # Re-ranking disabled, return candidates as-is
            return candidate_docs

        try:
            # Prepare query-document pairs for Cross-Encoder
            pairs = []
            for doc_data in candidate_docs:
                doc = doc_data['document']
                # Create text representation for re-ranking
                if doc.get('type') == 'script':
                    # For scripts: use name + description
                    example = doc.get('example', {})
                    text = f"{example.get('name', '')} {example.get('description', '')}"
                else:
                    # For documentation: use content (truncated if needed)
                    text = doc.get('content', '')[:500]  # Truncate to 500 chars for efficiency

                pairs.append([query, text])

            # Score all pairs with Cross-Encoder
            logger.debug(f"Re-ranking {len(pairs)} candidates with Cross-Encoder...")
            scores = self.reranker_model.predict(pairs)

            # Combine original documents with new scores
            reranked = []
            for doc_data, new_score in zip(candidate_docs, scores):
                reranked.append({
                    'document': doc_data['document'],
                    'score': float(new_score),  # Cross-Encoder score
                    'original_score': doc_data['score']  # Keep original for reference
                })

            # Sort by new Cross-Encoder scores
            reranked.sort(key=lambda x: x['score'], reverse=True)

            logger.info(f"✓ Re-ranked {len(reranked)} results with Cross-Encoder")
            return reranked

        except Exception as e:
            logger.warning(f"Re-ranking failed: {e}. Returning original results.")
            return candidate_docs

    
    def save_cache(self, cache_path: Path):
        """Save optimized FAISS and BM25 caches"""
        cache_data = {
            'documents': self.documents,
            'doc_map': self.doc_map,
            'embedding_dim': self.embedding_dim,
            'index_trained': self.index is not None
        }
        
        # Save metadata
        with open(cache_path / "metadata.pkl", 'wb') as f:
            pickle.dump(cache_data, f)
        
        # Save FAISS index
        if self.index is not None:
            faiss.write_index(self.index, str(cache_path / "faiss.index"))
            
        # Save BM25 index
        if self.bm25_index is not None:
            with open(cache_path / "bm25.pkl", 'wb') as f_out:
                pickle.dump(self.bm25_index, f_out)
            
        logger.info(f"Saved optimized caches to {cache_path}")
    
    def load_cache(self, cache_path: Path) -> bool:
        """Load optimized FAISS and BM25 caches"""
        try:
            # Load metadata
            with open(cache_path / "metadata.pkl", 'rb') as f:
                cache_data = pickle.load(f)
            
            self.documents = cache_data['documents']
            self.doc_map = cache_data['doc_map']
            self.embedding_dim = cache_data['embedding_dim']
            
            # Load FAISS index
            faiss_path = cache_path / "faiss.index"
            if not faiss_path.exists() or not cache_data['index_trained']:
                return False
            self.index = faiss.read_index(str(faiss_path))

            # Load BM25 index
            bm25_path = cache_path / "bm25.pkl"
            if bm25_path.exists():
                with open(bm25_path, 'rb') as f_in:
                    self.bm25_index = pickle.load(f_in)

            logger.info(f"Loaded optimized caches with {len(self.documents)} docs")
            return True
                
        except Exception as e:
            logger.error(f"Failed to load cache: {e}")
            
        return False
    
    def get_stats(self) -> Dict:
        """Get performance statistics"""
        index_type = "None"
        if self.index:
            index_type = type(self.index).__name__
            
        return {
            'documents': len(self.documents),
            'index_type': index_type,
            'embedding_dim': self.embedding_dim,
            'quantized': self.use_quantization,
            'memory_efficient': True,
            'bm25_ready': self.bm25_index is not None
        }


class OptimizedScriptRAG(OptimizedRAG):
    """Optimized version of ScriptRAG"""
    
    def __init__(self):
        super().__init__(embedding_dim=384)
        self.scripts_path = Path("src/ai/Knowledge/Scripts")
        self.cache_path = Path("src/ai/cache/optimized_scripts")
        self.cache_path.mkdir(exist_ok=True, parents=True)
        
        self._load_or_build()
    
    def _load_or_build(self):
        """Load from cache or build new index"""
        if not self.load_cache(self.cache_path):
            self._build_from_files()
            self.save_cache(self.cache_path)
    
    def _build_from_files(self):
        """Build index from script files"""
        documents = []
        texts = []
        
        for json_file in self.scripts_path.glob("*.json"):
            try:
                import json
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                script_examples = self._extract_code_examples(data)
                
                for example in script_examples:
                    doc = {
                        'filename': json_file.name,
                        'example': example,
                        'type': 'script'
                    }
                    
                    text = self._create_searchable_text(example)
                    
                    documents.append(doc)
                    texts.append(text)
                    
            except Exception as e:
                logger.error(f"Error loading {json_file}: {e}")
        
        if documents:
            self.build_index(documents, texts)
            logger.info(f"Built optimized script index with {len(documents)} examples")
    
    def _extract_code_examples(self, data: Any) -> List[Dict]:
        """Extract code examples from JSON data"""
        examples = []
        
        if isinstance(data, dict):
            if ('script' in data or 'code' in data) and ('name' in data or 'id' in data):
                examples.append(data)
            
            for key, value in data.items():
                if key == 'examples' and isinstance(value, list):
                    examples.extend([item for item in value if isinstance(item, dict) and ('script' in item or 'code' in item)])
                elif isinstance(value, (dict, list)) and key not in ['metadata', 'description']:
                    examples.extend(self._extract_code_examples(value))
                    
        elif isinstance(data, list):
            for item in data:
                examples.extend(self._extract_code_examples(item))
        
        return examples
    
    def _create_searchable_text(self, example: Dict) -> str:
        """Create optimized searchable text"""
        parts = [
            example.get('name', ''),
            example.get('description', ''),
            example.get('id', ''),
            example.get('category', '')
        ]
        
        # Add script content
        script_content = example.get('script', example.get('code', []))
        if isinstance(script_content, list):
            parts.append(' '.join(script_content))
        elif isinstance(script_content, str):
            parts.append(script_content)
        
        # Add features and keywords
        parts.extend(example.get('features', []))
        parts.extend(example.get('keywords', []))
        parts.extend(example.get('tags', []))
        
        return ' '.join(filter(None, parts))
    
    def search_scripts(self, query: str, top_k: int = 3) -> List[Dict]:
        """Search scripts with optimized index"""
        return self.search(query, top_k)
    
    def search_scripts_sync(self, query: str, top_k: int = 3) -> List[Dict]:
        """Synchronous wrapper for search_scripts"""
        return self.search_scripts(query, top_k)
    
    def find_by_pattern(self, pattern: str) -> List[Dict]:
        """Find examples by specific pattern"""
        return self.search_scripts(pattern, top_k=3)