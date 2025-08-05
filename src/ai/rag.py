import json
import os
import numpy as np
from pathlib import Path
from typing import List, Dict, Any, Tuple
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

class EplanRAG:
    def __init__(self):
        self.knowledge_path = Path("src/ai/Knowledge")
        self.cache_path = Path("src/ai/cache")
        self.cache_path.mkdir(exist_ok=True)
        
        # Try offline mode first
        import os
        os.environ["TRANSFORMERS_OFFLINE"] = "1"
        os.environ["HF_HUB_OFFLINE"] = "1"
        
        print("Loading embedding model (offline)...")
        try:
            self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2', local_files_only=True)
        except:
            # Fallback: load from specific local path
            model_path = Path("C:/Users/cd.lopez/.cache/huggingface/transformers/sentence-transformers--all-MiniLM-L6-v2")
            self.model = SentenceTransformer(str(model_path))
        print("✓ Model loaded")
        
        # Storage
        self.documents = []
        self.embeddings = None
        self.action_index = {}
        
        self.load_knowledge()
    
    def load_knowledge(self):
        """Load and index documents with embeddings"""
        cache_file = self.cache_path / "rag_cache.pkl"
        
        # Try loading from cache
        if cache_file.exists():
            try:
                with open(cache_file, 'rb') as f:
                    cache_data = pickle.load(f)
                    self.documents = cache_data['documents']
                    self.embeddings = cache_data['embeddings']
                    self.action_index = cache_data['action_index']
                    print(f"Loaded {len(self.documents)} documents from cache")
                    return
            except:
                print("Cache corrupted, rebuilding...")
        
        # Load fresh
        self._load_documents()
        self._build_embeddings()
        self._save_cache(cache_file)
    
    def _load_documents(self):
        """Load JSON documents and extract actions"""
                
        if not self.knowledge_path.exists():
            print(f"Knowledge folder not found: {self.knowledge_path}")
            return
        
        for json_file in self.knowledge_path.glob("*.json"):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                # Extract all actions from JSON
                actions = self._extract_all_actions(data)
                
                for action in actions:
                    doc_id = len(self.documents)
                    
                    # Create searchable text
                    searchable_text = self._create_searchable_text(action)
                    
                    doc = {
                        'id': doc_id,
                        'filename': json_file.name,
                        'action': action,
                        'searchable_text': searchable_text
                    }
                    
                    self.documents.append(doc)
                    
                    # Index by name for exact lookup
                    action_name = action.get('name', '').lower()
                    if action_name:
                        self.action_index[action_name] = doc_id
                        
            except Exception as e:
                print(f"Error loading {json_file.name}: {e}")
        
        print(f"Extracted {len(self.documents)} actions from JSON files")
    
    def _extract_all_actions(self, data: Any) -> List[Dict]:
        """Recursively extract all action objects from JSON"""
        actions = []
        
        if isinstance(data, dict):
            # Check if this is an action object
            if 'name' in data and 'description' in data:
                actions.append(data)
            
            # Recurse
            for key, value in data.items():
                if key == 'actions' and isinstance(value, list):
                    actions.extend(value)
                else:
                    actions.extend(self._extract_all_actions(value))
                    
        elif isinstance(data, list):
            for item in data:
                actions.extend(self._extract_all_actions(item))
        
        return actions
    
    def _create_searchable_text(self, action: Dict) -> str:
        """Create comprehensive searchable text from action"""
        parts = []
        
        # Basic info
        parts.append(action.get('name', ''))
        parts.append(action.get('title', ''))
        parts.append(action.get('description', ''))
        parts.append(action.get('category', ''))
        
        # Parameters
        for param in action.get('parameters', []):
            if isinstance(param, dict):
                parts.append(param.get('name', ''))
                parts.append(param.get('description', ''))
        
        # Examples
        for example in action.get('examples', []):
            if isinstance(example, dict):
                parts.append(example.get('description', ''))
                parts.append(example.get('command', ''))
        
        # Notes
        for note in action.get('notes', []):
            if isinstance(note, str):
                parts.append(note)
        
        return ' '.join(filter(None, parts))
    
    def _build_embeddings(self):
        """Build neural embeddings for all documents"""
        if not self.documents:
            return
        
        print("Building embeddings...")
        texts = [doc['searchable_text'] for doc in self.documents]
        self.embeddings = self.model.encode(texts, show_progress_bar=True)
        print(f"✓ Built embeddings for {len(texts)} documents")
    
    def _save_cache(self, cache_file: Path):
        """Save embeddings and documents to cache"""
        try:
            cache_data = {
                'documents': self.documents,
                'embeddings': self.embeddings,
                'action_index': self.action_index
            }
            with open(cache_file, 'wb') as f:
                pickle.dump(cache_data, f)
            print("Saved embeddings cache")
        except Exception as e:
            print(f"Failed to save cache: {e}")
    
    def search(self, query: str, top_k: int = 3, threshold: float = 0.3) -> List[Dict[str, Any]]:
        """Semantic search using neural embeddings"""
        if not self.documents or self.embeddings is None:
            return []
        
        # Try exact match first
        query_lower = query.lower()
        if query_lower in self.action_index:
            doc_id = self.action_index[query_lower]
            doc = self.documents[doc_id]
            return [{
                'document': doc,
                'score': 1.0,
                'match_type': 'exact'
            }]
        
        # Semantic search
        query_embedding = self.model.encode([query])
        similarities = cosine_similarity(query_embedding, self.embeddings)[0]
        
        # Get top results above threshold
        results = []
        for i, score in enumerate(similarities):
            if score >= threshold:
                results.append({
                    'document': self.documents[i],
                    'score': float(score),
                    'match_type': 'semantic'
                })
        
        # Sort by score and return top_k
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:top_k]
    
    def rebuild_cache(self):
        """Force rebuild embeddings cache"""
        cache_file = self.cache_path / "rag_cache.pkl"
        if cache_file.exists():
            cache_file.unlink()
        
        self.documents = []
        self.embeddings = None
        self.action_index = {}
        
        self.load_knowledge()

    def search_exact(self, action_name: str) -> List[Dict[str, Any]]:
        """Search for exact action name match"""
        action_name_lower = action_name.lower().strip()
        
        for doc in self.documents:
            action_data = doc.get('action', {})
            doc_name = action_data.get('name', '').lower()
            
            if doc_name == action_name_lower:
                return [{
                    'document': doc,
                    'score': 1.0,
                    'match_type': 'exact_name'
                }]
        
        return []