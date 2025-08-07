# src/ai/documentation_rag.py
import json
import os
import numpy as np
from pathlib import Path
from typing import List, Dict, Any
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

class DocumentationRAG:
    """RAG specialized in EPLAN documentation, concepts and explanations"""
    
    def __init__(self):
        self.api_path = Path("src/ai/Knowledge/API")
        self.cache_path = Path("src/ai/cache/docs")
        self.cache_path.mkdir(exist_ok=True, parents=True)
        
        print("Loading documentation embedding model...")
        try:
            self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2', local_files_only=True)
        except:
            model_path = Path("C:/Users/cd.lopez/.cache/huggingface/transformers/sentence-transformers--all-MiniLM-L6-v2") #static path
            self.model = SentenceTransformer(str(model_path))
        print("✓ Documentation model loaded")
        
        # Storage para documentación
        self.docs = []
        self.doc_embeddings = None
        self.doc_index = {}
        self.action_index = {}
        
        self.load_documentation()
    
    def load_documentation(self):
        """Upload and index documentation"""
        cache_file = self.cache_path / "doc_cache.pkl"
        
        # Intentar cargar desde cache
        if cache_file.exists():
            try:
                with open(cache_file, 'rb') as f:
                    cache_data = pickle.load(f)
                    self.docs = cache_data['docs']
                    self.doc_embeddings = cache_data['embeddings']
                    self.doc_index = cache_data['doc_index']
                    self.action_index = cache_data['action_index']
                    print(f"Loaded {len(self.docs)} docs from cache")
                    return
            except:
                print("Documentation cache corrupted, rebuilding...")
        
        self._load_documentation_files()
        self._build_doc_embeddings()
        self._save_doc_cache(cache_file)
    
    def _load_documentation_files(self):
        """Upload API documentation files"""
        if not self.api_path.exists():
            print(f"API docs folder not found: {self.api_path}")
            return
        
        for json_file in self.api_path.glob("*.json"):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                doc_items = self._extract_documentation_items(data)
                
                for item in doc_items:
                    doc_id = len(self.docs)
                    
                    doc_text = self._create_doc_searchable_text(item)
                    
                    doc_entry = {
                        'id': doc_id,
                        'filename': json_file.name,
                        'item': item,
                        'doc_text': doc_text,
                        'type': 'documentation'
                    }
                    
                    self.docs.append(doc_entry)
                    
                    item_name = item.get('name', '').lower()
                    action_name = item.get('action', '').lower()
                    
                    if item_name:
                        self.doc_index[item_name] = doc_id
                    if action_name:
                        self.action_index[action_name] = doc_id
                        
            except Exception as e:
                print(f"Error loading doc file {json_file.name}: {e}")
        
        print(f"Extracted {len(self.docs)} documentation items")
    
    def _extract_documentation_items(self, data: Any) -> List[Dict]:
        """Extract documentation elements (without code)"""
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
                    if isinstance(member, dict):
                        member_copy = member.copy()
                        member_copy['namespace'] = data.get('namespace', '')
                        if 'script' not in member_copy and 'code' not in member_copy:
                            items.append(member_copy)
            
            for collection_key in ['classes', 'interfaces', 'enums']:
                if collection_key in data:
                    for item in data[collection_key]:
                        if isinstance(item, dict) and 'script' not in item and 'code' not in item:
                            item_copy = item.copy()
                            item_copy['collection_type'] = collection_key[:-1]  
                            items.append(item_copy)
            
            for key, value in data.items():
                if key in ['actions', 'commands', 'parameters', 'concepts', 'attributes']:
                    if isinstance(value, list):
                        for sub_item in value:
                            if isinstance(sub_item, dict) and 'script' not in sub_item and 'code' not in sub_item:
                                items.append(sub_item)
                    elif isinstance(value, dict):
                        items.extend(self._extract_documentation_items(value))
                elif key not in ['examples', 'codeExample', 'codeDeclaration', 'members', 'classes', 'interfaces', 'enums']:
                    items.extend(self._extract_documentation_items(value))
                    
        elif isinstance(data, list):
            for item in data:
                items.extend(self._extract_documentation_items(item))
        
        return items
    
    def _create_doc_searchable_text(self, item: Dict) -> str:
        """Create optimized text for conceptual documentation"""
        parts = []
        
        parts.append(item.get('name', ''))
        parts.append(item.get('action', ''))
        parts.append(item.get('description', ''))
        parts.append(item.get('explanation', ''))
        parts.append(item.get('category', ''))
        parts.append(item.get('purpose', ''))
        
        
        parts.append(item.get('namespace', ''))
        parts.append(item.get('type', ''))
        parts.append(item.get('collection_type', ''))  
        
        for inheritance in item.get('inheritance', []):
            parts.append(inheritance)
        
        for interface in item.get('interfaces', []):
            parts.append(interface)
        
        for attr in item.get('attributes', []):
            if isinstance(attr, str):
                parts.append(attr)
        
        for param in item.get('parameters', []):
            if isinstance(param, dict):
                parts.append(param.get('name', ''))
                parts.append(param.get('description', ''))
                parts.append(param.get('type', ''))
            elif isinstance(param, str):
                parts.append(param)
        
        for note in item.get('notes', []):
            if isinstance(note, str):
                parts.append(note)
        
        parts.append(item.get('remarks', ''))
        parts.append(item.get('usage', ''))
        
        parts.extend(item.get('related_concepts', []))
        parts.extend(item.get('keywords', []))
        
        for use_case in item.get('use_cases', []):
            if isinstance(use_case, str):
                parts.append(use_case)
            elif isinstance(use_case, dict):
                parts.append(use_case.get('description', ''))
        
        return ' '.join(filter(None, parts))
    
    def _build_doc_embeddings(self):
        """Build embeddings for documentation"""
        if not self.docs:
            return
        
        print("Building documentation embeddings...")
        texts = [doc['doc_text'] for doc in self.docs]
        self.doc_embeddings = self.model.encode(texts, show_progress_bar=True)
        print(f"✓ Built embeddings for {len(texts)} docs")
    
    def _save_doc_cache(self, cache_file: Path):
        """Save documentation cache"""
        try:
            cache_data = {
                'docs': self.docs,
                'embeddings': self.doc_embeddings,
                'doc_index': self.doc_index,
                'action_index': self.action_index
            }
            with open(cache_file, 'wb') as f:
                pickle.dump(cache_data, f)
            print("Saved documentation embeddings cache")
        except Exception as e:
            print(f"Failed to save doc cache: {e}")
    
    def search_documentation(self, query: str, top_k: int = 3, threshold: float = 0.3) -> List[Dict[str, Any]]:
        """Semantic search of documentation"""
        if not self.docs or self.doc_embeddings is None:
            return []
        
        query_lower = query.lower()
        
        if query_lower in self.doc_index:
            doc_id = self.doc_index[query_lower]
            doc = self.docs[doc_id]
            return [{
                'document': doc,
                'score': 1.0,
                'match_type': 'exact_doc'
            }]
        
        if query_lower in self.action_index:
            doc_id = self.action_index[query_lower]
            doc = self.docs[doc_id]
            return [{
                'document': doc,
                'score': 1.0,
                'match_type': 'exact_action'
            }]
        
        query_embedding = self.model.encode([query])
        similarities = cosine_similarity(query_embedding, self.doc_embeddings)[0]
        
        results = []
        for i, score in enumerate(similarities):
            if score >= threshold:
                results.append({
                    'document': self.docs[i],
                    'score': float(score),
                    'match_type': 'semantic_doc'
                })
        
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:top_k]
    
    def find_action_documentation(self, action_name: str) -> List[Dict[str, Any]]:
        """Search for specific documentation for an EPLANv action"""
        results = []
        action_lower = action_name.lower()
        
        for doc in self.docs:
            item = doc['item']
            doc_action = item.get('action', '').lower()
            doc_name = item.get('name', '').lower()
            
            if action_lower in doc_action or action_lower in doc_name:
                relevance = 1.0
                if doc_action == action_lower:
                    relevance = 1.0
                elif action_lower in doc_action:
                    relevance = 0.8
                elif action_lower in doc_name:
                    relevance = 0.6
                
                results.append({
                    'document': doc,
                    'score': relevance,
                    'match_type': 'action_doc'
                })
        
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:3]
    
    def find_related_concepts(self, concept: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """Find related concepts"""
        if not self.doc_embeddings is not None:
            return []
        
        concept_embedding = self.model.encode([concept])
        similarities = cosine_similarity(concept_embedding, self.doc_embeddings)[0]
        
        results = []
        for i, score in enumerate(similarities):
            if score > 0.4:  
                results.append({
                    'document': self.docs[i],
                    'score': float(score),
                    'match_type': 'related_concept'
                })
        
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:top_k]
    
    def search_by_category(self, category: str) -> List[Dict[str, Any]]:
        """Search documentation by category"""
        results = []
        category_lower = category.lower()
        
        for doc in self.docs:
            item = doc['item']
            doc_category = item.get('category', '').lower()
            
            if category_lower in doc_category:
                results.append({
                    'document': doc,
                    'score': 1.0,
                    'match_type': 'category_match'
                })
        
        return results
    
    def rebuild_cache(self):
        """Force rebuild of the documentation cache"""
        cache_file = self.cache_path / "doc_cache.pkl"
        if cache_file.exists():
            cache_file.unlink()
        
        self.docs = []
        self.doc_embeddings = None
        self.doc_index = {}
        self.action_index = {}
        
        self.load_documentation()