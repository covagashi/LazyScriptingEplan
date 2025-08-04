# src/ai/rag.py
import requests
import json
from typing import List, Dict

class EplanRAG:
    """RAG service for EPLAN knowledge base"""
    
    def __init__(self):
        self.github_base = "https://api.github.com/repos/covagashi/LazyScriptingEplan/contents/EplanKnowledge"
        self.documents = []
        self.actions_index = {}  # For fast action lookup
        self._load_knowledge_base()
    
    def _load_knowledge_base(self):
        try:
            session = requests.Session()
            session.verify = False
            
            self._load_github_folder(f"{self.github_base}/API", "api")
            self._load_github_folder(f"{self.github_base}/Scripts%20cs", "scripts")
            
            print(f"Loaded {len(self.documents)} documents")
            self._build_actions_index()
            
        except Exception as e:
            print(f"RAG load error: {e}")
    
    def _load_github_folder(self, folder_url: str, folder_type: str):
        try:
            session = requests.Session()
            session.verify = False
            
            response = session.get(folder_url)
            items = response.json()
            
            for item in items:
                if item['type'] == 'file' and item['name'].endswith('.json'):
                    file_response = session.get(item['download_url'])
                    if file_response.status_code == 200:
                        data = file_response.json()
                        
                        self.documents.append({
                            'type': folder_type,
                            'file': item['name'],
                            'content': self._json_to_text(data),
                            'data': data
                        })
        except Exception as e:
            print(f"Error loading {folder_url}: {e}")
    
    def _build_actions_index(self):
        """Build index of EPLAN actions for fast lookup"""
        for doc in self.documents:
            if doc['type'] == 'api' and 'data' in doc:
                data = doc['data']
                
                # Handle different JSON structures
                if isinstance(data, dict):
                    actions = data.get('actions', [])
                    if not actions and 'action' in data:
                        actions = [data]
                elif isinstance(data, list):
                    actions = data
                else:
                    continue
                
                for action in actions:
                    if isinstance(action, dict):
                        action_name = action.get('name', '').lower()
                        title = action.get('title', '').lower()
                        
                        if action_name:
                            self.actions_index[action_name] = {
                                'action': action,
                                'source': doc['file']
                            }
                        if title and title != action_name:
                            self.actions_index[title] = {
                                'action': action,
                                'source': doc['file']
                            }
    
    def _json_to_text(self, data) -> str:
        if isinstance(data, dict):
            text_parts = []
            for key, value in data.items():
                if isinstance(value, str):
                    text_parts.append(f"{key}: {value}")
                elif isinstance(value, (list, dict)):
                    text_parts.append(f"{key}: {json.dumps(value, indent=2)}")
            return "\n".join(text_parts)
        return json.dumps(data, indent=2)
    
    def search(self, query: str, top_k: int = 3) -> List[Dict]:
        """Enhanced search with action matching"""
        query_lower = query.lower()
        results = []
        
        # 1. Direct action name matching
        action_matches = self._search_actions(query_lower)
        
        # 2. Content search
        content_matches = self._search_content(query_lower)
        
        # Combine and deduplicate
        all_matches = action_matches + content_matches
        seen = set()
        unique_results = []
        
        for match in all_matches:
            key = match['document']['file']
            if key not in seen:
                seen.add(key)
                unique_results.append(match)
        
        return unique_results[:top_k]
    
    def _search_actions(self, query: str) -> List[Dict]:
        """Search specifically in actions index"""
        matches = []
        query_words = query.lower().split()
        
        for action_key, action_info in self.actions_index.items():
            action = action_info['action']
            
            # Score based on multiple fields
            score = 0
            
            # Check action name
            if any(word in action_key for word in query_words):
                score += 10
            
            # Check title and description
            title = action.get('title', '').lower()
            description = action.get('description', '').lower()
            
            for word in query_words:
                if word in title:
                    score += 5
                if word in description:
                    score += 3
            
            if score > 0:
                matches.append({
                    'document': {
                        'type': 'api',
                        'file': action_info['source'],
                        'content': json.dumps(action, indent=2),
                        'data': action
                    },
                    'score': score,
                    'relevance': score / 10
                })
        
        matches.sort(key=lambda x: x['score'], reverse=True)
        return matches
    
    def _search_content(self, query: str) -> List[Dict]:
        """Search in document content"""
        query_words = [word for word in query.split() if len(word) > 2]
        results = []
        
        for doc in self.documents:
            content_lower = doc['content'].lower()
            score = sum(1 for word in query_words if word in content_lower)
            
            if score > 0:
                results.append({
                    'document': doc,
                    'score': score,
                    'relevance': score / len(query_words) if query_words else 0
                })
        
        results.sort(key=lambda x: x['score'], reverse=True)
        return results