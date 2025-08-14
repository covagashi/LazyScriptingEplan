# src/ai/optimized_documentation_rag.py
import numpy as np
import faiss
import pickle
import json
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
        self.doc_map = {}
        self.use_quantization = True
        self.nlist = 100
        self.nprobe = 10
        
    def _init_model(self):
        if self.model is None:
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
            
    def _create_index(self, vectors: np.ndarray) -> faiss.Index:
        n_docs = vectors.shape[0]
        
        if n_docs < 1000:
            index = faiss.IndexFlatIP(self.embedding_dim)
        else:
            quantizer = faiss.IndexFlatIP(self.embedding_dim)
            
            if self.use_quantization:
                index = faiss.IndexIVFPQ(
                    quantizer, 
                    self.embedding_dim, 
                    min(self.nlist, n_docs // 10),
                    8, 8
                )
                index.train(vectors.astype(np.float32))
            else:
                index = faiss.IndexIVFFlat(
                    quantizer,
                    self.embedding_dim,
                    min(self.nlist, n_docs // 10)
                )
                index.train(vectors.astype(np.float32))
            
            index.nprobe = self.nprobe
            
        return index
    
    def build_index(self, documents: List[Dict], texts: List[str]):
        self._init_model()
        
        logger.info(f"Encoding {len(texts)} documents...")
        embeddings = self.model.encode(
            texts, 
            batch_size=32,
            show_progress_bar=True,
            convert_to_numpy=True
        )
        
        faiss.normalize_L2(embeddings)
        self.index = self._create_index(embeddings)
        self.index.add(embeddings.astype(np.float32))
        
        self.documents = documents
        self.doc_map = {i: doc for i, doc in enumerate(documents)}
        
        logger.info(f"Built index with {self.index.ntotal} vectors")
        
    def search(self, query: str, top_k: int = 5, threshold: float = 0.3) -> List[Dict]:
        if self.index is None:
            return []
            
        self._init_model()
        
        query_embedding = self.model.encode([query], convert_to_numpy=True)
        faiss.normalize_L2(query_embedding)
        
        scores, indices = self.index.search(
            query_embedding.astype(np.float32), 
            min(top_k * 2, len(self.documents))
        )
        
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
        cache_data = {
            'documents': self.documents,
            'doc_map': self.doc_map,
            'embedding_dim': self.embedding_dim,
            'index_trained': self.index is not None
        }
        
        with open(cache_path / "metadata.pkl", 'wb') as f:
            pickle.dump(cache_data, f)
        
        if self.index is not None:
            faiss.write_index(self.index, str(cache_path / "faiss.index"))
            
        logger.info(f"Saved optimized cache to {cache_path}")
    
    def load_cache(self, cache_path: Path) -> bool:
        try:
            with open(cache_path / "metadata.pkl", 'rb') as f:
                cache_data = pickle.load(f)
            
            self.documents = cache_data['documents']
            self.doc_map = cache_data['doc_map']
            self.embedding_dim = cache_data['embedding_dim']
            
            index_path = cache_path / "faiss.index"
            if index_path.exists() and cache_data['index_trained']:
                self.index = faiss.read_index(str(index_path))
                logger.info(f"Loaded optimized cache with {len(self.documents)} docs")
                return True
                
        except Exception as e:
            logger.error(f"Failed to load cache: {e}")
            
        return False


class OptimizedDocumentationRAG(OptimizedRAG):
    """Optimized version of DocumentationRAG"""
    
    def __init__(self):
        super().__init__(embedding_dim=384)
        self.api_path = Path("src/ai/Knowledge/API")
        self.cache_path = Path("src/ai/cache/optimized_docs")
        self.cache_path.mkdir(exist_ok=True, parents=True)
        
        self.name_index = {}
        self.action_index = {}
        
        self._load_or_build()
    
    def _load_or_build(self):
        if not self.load_cache(self.cache_path):
            self._build_from_files()
            self.save_cache(self.cache_path)
    
    def _build_from_files(self):
        documents = []
        texts = []
        
        for json_file in self.api_path.glob("*.json"):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                doc_items = self._extract_documentation_items(data)
                
                for item in doc_items:
                    doc_id = len(documents)
                    
                    doc = {
                        'id': doc_id,
                        'filename': json_file.name,
                        'item': item,
                        'type': 'documentation'
                    }
                    
                    text = self._create_searchable_text(item)
                    
                    documents.append(doc)
                    texts.append(text)
                    
                    item_name = item.get('name', '').lower().strip()
                    action_name = item.get('action', '').lower().strip()
                    
                    if item_name:
                        self.name_index[item_name] = doc_id
                    if action_name:
                        self.action_index[action_name] = doc_id
                        
            except Exception as e:
                logger.error(f"Error loading {json_file}: {e}")
        
        if documents:
            self.build_index(documents, texts)
            logger.info(f"Built optimized docs index with {len(documents)} items")
    
    def _extract_documentation_items(self, data: Any) -> List[Dict]:
        items = []
        
        if isinstance(data, dict):
            if ('description' in data or 'explanation' in data) and 'name' in data:
                if 'script' not in data and 'code' not in data:
                    items.append(data)
            
            if 'namespace' in data and 'members' in data:
                namespace_info = {
                    'name': data.get('namespace', ''),
                    'description': data.get('description', ''),
                    'type': 'namespace',
                    'namespace': data.get('namespace', '')
                }
                items.append(namespace_info)
                
                for member in data.get('members', []):
                    if isinstance(member, dict) and 'script' not in member:
                        member_copy = member.copy()
                        member_copy['namespace'] = data.get('namespace', '')
                        items.append(member_copy)
            
            for collection_key in ['classes', 'interfaces', 'enums']:
                if collection_key in data:
                    for item in data[collection_key]:
                        if isinstance(item, dict) and 'script' not in item:
                            item_copy = item.copy()
                            item_copy['collection_type'] = collection_key[:-1]
                            items.append(item_copy)
            
            for key, value in data.items():
                if key in ['actions', 'commands', 'parameters', 'concepts', 'attributes']:
                    if isinstance(value, list):
                        items.extend([item for item in value if isinstance(item, dict) and 'script' not in item])
                    elif isinstance(value, dict):
                        items.extend(self._extract_documentation_items(value))
                elif key not in ['examples', 'codeExample', 'members', 'classes', 'interfaces', 'enums']:
                    items.extend(self._extract_documentation_items(value))
                    
        elif isinstance(data, list):
            for item in data:
                items.extend(self._extract_documentation_items(item))
        
        return items
    
    def _create_searchable_text(self, item: Dict) -> str:
        parts = [
            item.get('name', ''),
            item.get('action', ''),
            item.get('description', ''),
            item.get('explanation', ''),
            item.get('category', ''),
            item.get('purpose', ''),
            item.get('namespace', ''),
            item.get('type', ''),
            item.get('collection_type', ''),
            item.get('remarks', ''),
            item.get('usage', '')
        ]
        
        for key in ['inheritance', 'interfaces', 'attributes', 'related_concepts', 'keywords', 'notes', 'use_cases']:
            items_list = item.get(key, [])
            if isinstance(items_list, list):
                parts.extend([str(x) for x in items_list])
        
        for param in item.get('parameters', []):
            if isinstance(param, dict):
                parts.extend([param.get('name', ''), param.get('description', ''), param.get('type', '')])
            elif isinstance(param, str):
                parts.append(param)
        
        return ' '.join(filter(None, parts))
    
    def search_documentation(self, query: str, top_k: int = 3) -> List[Dict]:
        query_lower = query.lower()
        
        if query_lower in self.name_index:
            doc_id = self.name_index[query_lower]
            if doc_id < len(self.documents):
                return [{
                    'document': self.documents[doc_id],
                    'score': 1.0,
                    'match_type': 'exact_name'
                }]
        
        if query_lower in self.action_index:
            doc_id = self.action_index[query_lower]
            if doc_id < len(self.documents):
                return [{
                    'document': self.documents[doc_id],
                    'score': 1.0,
                    'match_type': 'exact_action'
                }]
        
        return self.search(query, top_k, threshold=0.3)
    
    def find_action_documentation(self, action_name: str) -> List[Dict]:
        action_lower = action_name.lower()
        
        if action_lower in self.action_index:
            doc_id = self.action_index[action_lower]
            return [{
                'document': self.documents[doc_id],
                'score': 1.0,
                'match_type': 'exact_action'
            }]
        
        return self.search(action_name, top_k=3, threshold=0.4)
    
    def save_cache(self, cache_path: Path):
        super().save_cache(cache_path)
        
        index_data = {
            'name_index': self.name_index,
            'action_index': self.action_index
        }
        
        with open(cache_path / "exact_indexes.pkl", 'wb') as f:
            pickle.dump(index_data, f)
    
    def load_cache(self, cache_path: Path) -> bool:
        if not super().load_cache(cache_path):
            return False
        
        try:
            with open(cache_path / "exact_indexes.pkl", 'rb') as f:
                index_data = pickle.load(f)
            
            self.name_index = index_data['name_index']
            self.action_index = index_data['action_index']
            return True
            
        except Exception as e:
            logger.error(f"Failed to load exact indexes: {e}")
            return False