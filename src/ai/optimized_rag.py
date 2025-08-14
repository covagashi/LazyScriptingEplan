# src/ai/optimized_rag.py
import numpy as np
import faiss
import os
import pickle
from pathlib import Path
from typing import List, Dict, Any, Optional
from sentence_transformers import SentenceTransformer
import logging

logger = logging.getLogger(__name__)

class OptimizedRAG:
    """High-performance RAG with quantization and FAISS indexing"""
    
    def __init__(self, embedding_dim: int = 384):
        self.embedding_dim = embedding_dim
        self.model = None
        self.documents = []
        self.index = None
        self.doc_map = {}  # ID to document mapping
        
        # Quantization settings
        self.use_quantization = True
        self.nlist = 100  # Number of clusters for IVF
        self.nprobe = 10  # Search clusters
        
    def _init_model(self):
        """Load model from correct cache path"""
        if self.model is None:
            # Check environment variable first
            cache_path = os.getenv('HUGGINGFACE_HUB_CACHE')
            if cache_path:
                model_path = Path(cache_path) / "sentence-transformers--all-MiniLM-L6-v2"
                if model_path.exists():
                    from sentence_transformers import SentenceTransformer
                    self.model = SentenceTransformer(str(model_path))
                    return
            
            # Fallback to downloading
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
            
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
        """Build optimized vector index"""
        self._init_model()
        
        logger.info(f"Encoding {len(texts)} documents...")
        embeddings = self.model.encode(
            texts, 
            batch_size=32,
            show_progress_bar=True,
            convert_to_numpy=True
        )
        
        # Normalize for cosine similarity
        faiss.normalize_L2(embeddings)
        
        # Create FAISS index
        self.index = self._create_index(embeddings)
        self.index.add(embeddings.astype(np.float32))
        
        # Store documents
        self.documents = documents
        self.doc_map = {i: doc for i, doc in enumerate(documents)}
        
        logger.info(f"Built index with {self.index.ntotal} vectors")
        
    def search(self, query: str, top_k: int = 5, threshold: float = 0.3) -> List[Dict]:
        """Optimized search with FAISS"""
        if self.index is None:
            return []
            
        self._init_model()
        
        # Encode query
        query_embedding = self.model.encode([query], convert_to_numpy=True)
        faiss.normalize_L2(query_embedding)
        
        # Search
        scores, indices = self.index.search(
            query_embedding.astype(np.float32), 
            min(top_k * 2, len(self.documents))  # Get more candidates
        )
        
        # Filter and format results
        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx == -1 or score < threshold:
                continue
                
            results.append({
                'document': self.doc_map[idx],
                'score': float(score),
                'match_type': 'vector_search'
            })
            
            if len(results) >= top_k:
                break
                
        return results
    
    def save_cache(self, cache_path: Path):
        """Save optimized cache"""
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
            
        logger.info(f"Saved optimized cache to {cache_path}")
    
    def load_cache(self, cache_path: Path) -> bool:
        """Load optimized cache"""
        try:
            # Load metadata
            with open(cache_path / "metadata.pkl", 'rb') as f:
                cache_data = pickle.load(f)
            
            self.documents = cache_data['documents']
            self.doc_map = cache_data['doc_map']
            self.embedding_dim = cache_data['embedding_dim']
            
            # Load FAISS index
            index_path = cache_path / "faiss.index"
            if index_path.exists() and cache_data['index_trained']:
                self.index = faiss.read_index(str(index_path))
                logger.info(f"Loaded optimized cache with {len(self.documents)} docs")
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
            'memory_efficient': True
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
        return self.search(query, top_k, threshold=0.3)
    
    def search_scripts_sync(self, query: str, top_k: int = 3) -> List[Dict]:
        """Synchronous wrapper for search_scripts"""
        return self.search_scripts(query, top_k)
    
    def find_by_pattern(self, pattern: str) -> List[Dict]:
        """Find examples by specific pattern"""
        return self.search_scripts(pattern, top_k=3)