# src/ai/optimized_rag.py
import faiss
import numpy as np
import time
import asyncio
from typing import List, Dict, Any, Optional
from pathlib import Path
import pickle
from .lazy_embeddings import LazyEmbeddingModel
from ..core.intelligent_cache import cache_manager
from ..ai.lazy_embeddings import LazyRAG

class OptimizedRAG(LazyRAG):
    """RAG with FAISS vectorization and query optimization"""
    
    def __init__(self, name: str):
        self.name = name
        self.embedding_model = LazyEmbeddingModel()
        self.documents = []
        
        # FAISS optimization
        self.faiss_index = None
        self.embedding_dim = 384  # MiniLM dimension
        self.index_built = False
        
        # Query optimization
        self.query_cache = cache_manager.get_cache(f"queries_{name}")
        self.synonym_map = self._build_synonym_map()
        
        # Memory management
        self.max_documents = 10000
        self.last_cleanup = time.time()
        self.cleanup_interval = 3600  # 1 hour
    
    async def add_documents_batch(self, documents: List[Dict], rebuild_index: bool = True):
        """Add documents with automatic memory management"""
        self.documents.extend(documents)
        
        # Memory management
        if len(self.documents) > self.max_documents:
            await self._cleanup_old_documents()
        
        if rebuild_index:
            await self._build_faiss_index()
    
    async def _build_faiss_index(self):
        """Build optimized FAISS index"""
        if not self.documents:
            return
        
        # Extract texts
        texts = []
        for doc in self.documents:
            text = doc.get('searchable_text', doc.get('text', str(doc)))
            texts.append(text)
        
        # Get embeddings
        embeddings = await self.embedding_model.encode_batch_async(texts, batch_size=64)
        embeddings = np.array(embeddings).astype('float32')
        
        # Build FAISS index
        if self.faiss_index is None:
            self.faiss_index = faiss.IndexFlatIP(self.embedding_dim)
        else:
            self.faiss_index.reset()
        
        # Normalize for cosine similarity
        faiss.normalize_L2(embeddings)
        self.faiss_index.add(embeddings)
        
        self.index_built = True
        print(f"✅ FAISS index built: {len(self.documents)} docs, {self.embedding_dim}D")
    
    async def search_optimized(self, query: str, top_k: int = 5, threshold: float = 0.3) -> List[Dict]:
        """Optimized semantic search with query expansion"""
        
        # Check cache first
        cache_key = f"{query}_{top_k}_{threshold}"
        cached = self.query_cache.get(data=cache_key)
        if cached:
            return cached
        
        # Ensure index is built
        if not self.index_built:
            await self._build_faiss_index()
        
        if not self.index_built:
            return []
        
        # Query expansion
        expanded_queries = self._expand_query(query)
        
        # Search with multiple queries
        all_results = {}
        for expanded_query, weight in expanded_queries:
            results = await self._faiss_search_single(expanded_query, top_k * 2, threshold)
            
            for result in results:
                doc_id = result['document']['id']
                if doc_id not in all_results:
                    all_results[doc_id] = result
                    all_results[doc_id]['score'] *= weight
                else:
                    # Combine scores
                    all_results[doc_id]['score'] = max(
                        all_results[doc_id]['score'], 
                        result['score'] * weight
                    )
        
        # Convert back to list and sort
        final_results = list(all_results.values())
        final_results.sort(key=lambda x: x['score'], reverse=True)
        final_results = final_results[:top_k]
        
        # Rerank top results
        reranked_results = await self._rerank_results(final_results, query)
        
        # Cache results
        self.query_cache.put(reranked_results, data=cache_key, ttl=1800)
        
        return reranked_results
    
    async def _faiss_search_single(self, query: str, top_k: int, threshold: float) -> List[Dict]:
        """Single FAISS search"""
        query_embedding = await self.embedding_model.encode_single_async(query)
        query_embedding = np.array([query_embedding]).astype('float32')
        faiss.normalize_L2(query_embedding)
        
        # Search
        scores, indices = self.faiss_index.search(query_embedding, min(top_k, len(self.documents)))
        
        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx != -1 and score >= threshold:
                results.append({
                    'document': self.documents[idx],
                    'score': float(score),
                    'match_type': 'faiss_semantic'
                })
        
        return results
    
    def _expand_query(self, query: str) -> List[tuple]:
        """Expand query with synonyms and related terms"""
        expanded = [(query, 1.0)]  # Original query with full weight
        
        query_lower = query.lower()
        words = query_lower.split()
        
        # Add synonyms
        for word in words:
            if word in self.synonym_map:
                for synonym in self.synonym_map[word][:2]:  # Top 2 synonyms
                    synonym_query = query_lower.replace(word, synonym)
                    expanded.append((synonym_query, 0.8))
        
        # Add partial matches for technical terms
        technical_terms = [w for w in words if len(w) > 6]
        for term in technical_terms:
            if 'eplan' in term or 'action' in term:
                partial_query = f"{term} {' '.join([w for w in words if w != term])}"
                expanded.append((partial_query.strip(), 0.6))
        
        return expanded[:5]  # Limit expansions
    
    async def _rerank_results(self, results: List[Dict], original_query: str) -> List[Dict]:
        """Rerank results using cross-encoder logic"""
        if len(results) <= 1:
            return results
        
        # Simple reranking based on exact term matches
        query_terms = set(original_query.lower().split())
        
        for result in results:
            doc = result['document']
            text = doc.get('searchable_text', '').lower()
            
            # Bonus for exact term matches
            exact_matches = sum(1 for term in query_terms if term in text)
            term_bonus = (exact_matches / len(query_terms)) * 0.1
            
            # Bonus for document metadata
            if doc.get('type') == 'script' and 'script' in original_query.lower():
                term_bonus += 0.05
            elif doc.get('type') == 'documentation' and 'doc' in original_query.lower():
                term_bonus += 0.05
            
            result['score'] = min(1.0, result['score'] + term_bonus)
        
        results.sort(key=lambda x: x['score'], reverse=True)
        return results
    
    def _build_synonym_map(self) -> Dict[str, List[str]]:
        """Build domain-specific synonym map"""
        return {
            'script': ['code', 'program', 'automation'],
            'generate': ['create', 'build', 'make'],
            'execute': ['run', 'perform', 'launch'],
            'action': ['command', 'operation', 'function'],
            'eplan': ['electrical', 'cad', 'engineering'],
            'project': ['file', 'document', 'design'],
            'parameter': ['setting', 'config', 'option'],
            'validate': ['check', 'verify', 'test'],
            'error': ['issue', 'problem', 'failure'],
            'api': ['interface', 'method', 'function']
        }
    
    async def _cleanup_old_documents(self):
        """Automatic memory management"""
        current_time = time.time()
        
        if current_time - self.last_cleanup < self.cleanup_interval:
            return
        
        # Keep most recent documents and most accessed
        if hasattr(self, '_access_counts'):
            # Sort by access count and recency
            scored_docs = []
            for i, doc in enumerate(self.documents):
                access_score = self._access_counts.get(i, 0)
                recency_score = doc.get('timestamp', 0)
                combined_score = access_score + (recency_score / 1000000)  # Normalize timestamp
                scored_docs.append((combined_score, i, doc))
            
            scored_docs.sort(reverse=True)
            
            # Keep top 80%
            keep_count = int(len(self.documents) * 0.8)
            self.documents = [doc for _, _, doc in scored_docs[:keep_count]]
            
            # Rebuild index
            self.index_built = False
            await self._build_faiss_index()
            
            print(f"🧹 Cleaned up documents: {len(scored_docs)} → {len(self.documents)}")
        
        self.last_cleanup = current_time
    
    def get_optimization_stats(self) -> Dict[str, Any]:
        """Get optimization performance stats"""
        return {
            "faiss_index_built": self.index_built,
            "documents_count": len(self.documents),
            "embedding_dim": self.embedding_dim,
            "query_cache_stats": self.query_cache.get_stats(),
            "last_cleanup": self.last_cleanup,
            "memory_usage_mb": len(self.documents) * 0.1  # Rough estimate
        }