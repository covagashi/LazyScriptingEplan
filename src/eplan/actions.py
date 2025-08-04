# src/eplan/actions.py
import requests
from typing import Dict, List, Optional

class EplanActionsRAG:
    """EPLAN actions from LazyScriptingEplan repository"""
    
    def __init__(self):
        self.github_base = "https://api.github.com/repos/covagashi/LazyScriptingEplan/contents/EplanKnowledge"
        self.actions_cache = {}
        self._load_actions()
    
    def _load_actions(self):
        try:
            session = requests.Session()
            session.verify = False
            
            # Load API folder
            api_url = f"{self.github_base}/API"
            response = session.get(api_url)
            items = response.json()
            
            for item in items:
                if item['type'] == 'file' and item['name'].endswith('.json'):
                    file_response = session.get(item['download_url'])
                    if file_response.status_code == 200:
                        data = file_response.json()
                        self._extract_actions(data, item['name'])
                        
        except Exception as e:
            print(f"Failed to load actions from GitHub: {e}")
    
    def _extract_actions(self, data: dict, filename: str):
        """Extract action info from JSON data"""
        if isinstance(data, dict):
            for key, value in data.items():
                if 'action' in key.lower() or 'execute' in key.lower():
                    self.actions_cache[key] = {
                        'source': filename,
                        'data': value
                    }
    
    def find_action(self, query: str) -> Optional[Dict]:
        """Find action based on query"""
        query_lower = query.lower()
        
        for action_name, action_data in self.actions_cache.items():
            if any(word in action_name.lower() for word in query_lower.split()):
                return {
                    'action': action_name,
                    'source': action_data['source'],
                    'data': action_data['data']
                }
        return None