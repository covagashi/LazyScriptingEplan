# src/ai/script_rag.py
import json
import asyncio
from pathlib import Path
from typing import List, Dict, Any, Optional
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import numpy as np
import threading
import logging

logger = logging.getLogger(__name__)

class ScriptRAG:
    """RAG specialized in C# EPLAN code and scripts"""
    
    def __init__(self):
        self.scripts_path = Path("src/ai/Knowledge/Scripts")
        self.cache_path = Path("src/ai/cache/scripts")
        self.cache_path.mkdir(exist_ok=True, parents=True)
        
        self.model = None
        self.scripts = []
        self.script_embeddings = None
        self.script_index = {}
        self._loaded = False
        self._loading_lock = threading.Lock()
        
        print("✓ ScriptRAG initialized")
        self._load_sync()
    
    def _load_sync(self):
        """Synchronous loading for initialization"""
        with self._loading_lock:
            if self._loaded:
                return
                
            cache_file = self.cache_path / "script_cache.pkl"
            
            # Try loading from cache first
            if cache_file.exists():
                try:
                    with open(cache_file, 'rb') as f:
                        cache_data = pickle.load(f)
                        self.scripts = cache_data.get('scripts', [])
                        self.script_embeddings = cache_data.get('embeddings', None)
                        self.script_index = cache_data.get('index', {})
                        
                    if self.scripts and self.script_embeddings is not None:
                        self._loaded = True
                        print(f"Loaded {len(self.scripts)} scripts from cache")
                        return
                except Exception as e:
                    logger.warning(f"Cache corrupted, rebuilding: {e}")
            
            # Load from files and build embeddings
            self._load_script_documents()
            if self.scripts:
                self._ensure_model()
                self._build_script_embeddings()
                self._save_script_cache(cache_file)
                self._loaded = True
    
    def _ensure_model(self):
        """Lazy load the model only when needed"""
        if self.model is None:
            print("Loading script embedding model...")
            try:
                self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2', local_files_only=True)
            except:
                model_path = Path("C:/Users/cd.lopez/.cache/huggingface/transformers/sentence-transformers--all-MiniLM-L6-v2")
                if model_path.exists():
                    self.model = SentenceTransformer(str(model_path))
                else:
                    # Fallback to download if local not found
                    self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
            print("✓ Script model loaded")
    
    def search_scripts_sync(self, query: str, top_k: int = 3, threshold: float = 0.3) -> List[Dict[str, Any]]:
        """Synchronous search wrapper for tools that can't handle async"""
        try:
            # Use asyncio.run to handle the async call
            return asyncio.run(self.search_scripts(query, top_k, threshold))
        except RuntimeError as e:
            if "asyncio.run() cannot be called from a running event loop" in str(e):
                # Handle case where we're already in an event loop
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                try:
                    result = loop.run_until_complete(self.search_scripts(query, top_k, threshold))
                    return result
                finally:
                    loop.close()
                    asyncio.set_event_loop(None)
            else:
                raise
    
    async def search_scripts(self, query: str, top_k: int = 3, threshold: float = 0.3) -> List[Dict[str, Any]]:
        """Async semantic search of C# scripts"""
        if not self._loaded:
            logger.warning("ScriptRAG not loaded, returning empty results")
            return []
        
        if not self.scripts or self.script_embeddings is None:
            logger.warning("No scripts or embeddings available")
            return []
        
        # Check for exact matches first
        query_lower = query.lower()
        if query_lower in self.script_index:
            script_id = self.script_index[query_lower]
            if script_id < len(self.scripts):
                script = self.scripts[script_id]
                return [{
                    'document': script,
                    'score': 1.0,
                    'match_type': 'exact_script'
                }]
        
        # Semantic search
        try:
            self._ensure_model()
            query_embedding = self.model.encode([query])
            similarities = cosine_similarity(query_embedding, self.script_embeddings)[0]
            
            results = []
            for i, score in enumerate(similarities):
                if score >= threshold and i < len(self.scripts):
                    results.append({
                        'document': self.scripts[i],
                        'score': float(score),
                        'match_type': 'semantic_script'
                    })
            
            results.sort(key=lambda x: x['score'], reverse=True)
            return results[:top_k]
            
        except Exception as e:
            logger.error(f"Error in semantic search: {e}")
            return []
    
    def find_by_pattern(self, pattern: str) -> List[Dict[str, Any]]:
        """Search for scripts by specific pattern (synchronous)"""
        if not self._loaded or not self.scripts:
            return []
        
        results = []
        pattern_lower = pattern.lower()
        
        for script in self.scripts:
            searchable_text = script.get('searchable_text', '').lower()
            
            if pattern_lower in searchable_text:
                # Calculate relevance based on pattern frequency
                word_count = max(len(searchable_text.split()), 1)
                pattern_count = searchable_text.count(pattern_lower)
                relevance = min(pattern_count / word_count * 10, 1.0)  # Scale to 0-1
                
                results.append({
                    'document': script,
                    'score': relevance,
                    'match_type': 'pattern_match'
                })
        
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:5]
    
    def _load_script_documents(self):
        """Load script documents from JSON files"""
        if not self.scripts_path.exists():
            logger.warning(f"Scripts folder not found: {self.scripts_path}")
            return
        
        self.scripts = []
        self.script_index = {}
        
        for json_file in self.scripts_path.glob("*.json"):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                script_examples = self._extract_code_examples(data)
                
                for example in script_examples:
                    script_id = len(self.scripts)
                    searchable_text = self._create_code_searchable_text(example)
                    
                    script_doc = {
                        'id': script_id,
                        'filename': json_file.name,
                        'example': example,
                        'searchable_text': searchable_text,
                        'type': 'script'
                    }
                    
                    self.scripts.append(script_doc)
                    
                    # Index by name and id for exact matching
                    example_id = example.get('id', '').lower().strip()
                    example_name = example.get('name', '').lower().strip()
                    
                    if example_id:
                        self.script_index[example_id] = script_id
                    if example_name:
                        self.script_index[example_name] = script_id
                        
            except Exception as e:
                logger.error(f"Error loading script file {json_file.name}: {e}")
        
        print(f"Extracted {len(self.scripts)} code examples")
    
    def _extract_code_examples(self, data: Any) -> List[Dict]:
        """Extract only examples with C# code"""
        examples = []
        
        if isinstance(data, dict):
            # Direct example with script/code
            if ('script' in data or 'code' in data) and ('name' in data or 'id' in data):
                examples.append(data)
            
            # Handle nested structures
            for key, value in data.items():
                if key == 'examples' and isinstance(value, list):
                    for item in value:
                        if isinstance(item, dict) and ('script' in item or 'code' in item):
                            examples.append(item)
                elif key in ['categories', 'groups', 'sections'] and isinstance(value, dict):
                    # Handle categorized examples
                    examples.extend(self._extract_code_examples(value))
                elif isinstance(value, (dict, list)) and key not in ['metadata', 'description']:
                    examples.extend(self._extract_code_examples(value))
                    
        elif isinstance(data, list):
            for item in data:
                examples.extend(self._extract_code_examples(item))
        
        return examples
    
    def _create_code_searchable_text(self, example: Dict) -> str:
        """Create search-optimized text from code"""
        parts = []
        
        # Basic metadata
        parts.append(example.get('name', ''))
        parts.append(example.get('description', ''))
        parts.append(example.get('id', ''))
        parts.append(example.get('category', ''))
        
        # Script content
        script_content = example.get('script', example.get('code', []))
        if isinstance(script_content, list):
            code_text = ' '.join(script_content)
            parts.append(code_text)
            # Extract C# specific elements
            parts.extend(self._extract_csharp_elements(code_text))
        elif isinstance(script_content, str):
            parts.append(script_content)
            parts.extend(self._extract_csharp_elements(script_content))
        
        # Additional features
        features = example.get('features', [])
        if isinstance(features, list):
            parts.extend([str(f) for f in features])
        
        # Keywords and tags
        keywords = example.get('keywords', [])
        if isinstance(keywords, list):
            parts.extend(keywords)
        
        tags = example.get('tags', [])
        if isinstance(tags, list):
            parts.extend(tags)
        
        return ' '.join(filter(None, parts))
    
    def _extract_csharp_elements(self, code: str) -> List[str]:
        """Extract specific elements from C# for better search"""
        elements = []
        
        import re
        
        # Class names
        class_matches = re.findall(r'class\s+(\w+)', code, re.IGNORECASE)
        elements.extend(class_matches)
        
        # Method names
        method_matches = re.findall(r'public\s+\w+\s+(\w+)\s*\(', code, re.IGNORECASE)
        elements.extend(method_matches)
        
        # Using statements
        using_matches = re.findall(r'using\s+([\w\.]+);', code)
        elements.extend(using_matches)
        
        # Attributes
        attribute_matches = re.findall(r'\[(\w+)\]', code)
        elements.extend(attribute_matches)
        
        # EPLAN specific patterns
        eplan_patterns = [
            r'Eplan\.EplApi\.(\w+)',
            r'ActionManager',
            r'ActionSetting',
            r'BaseException',
            r'Progress',
            r'StorableObject'
        ]
        
        for pattern in eplan_patterns:
            matches = re.findall(pattern, code)
            elements.extend(matches)
        
        return elements
    
    def _build_script_embeddings(self):
        """Build code-optimized embeddings"""
        if not self.scripts:
            logger.warning("No scripts to build embeddings for")
            return
        
        print("Building script embeddings...")
        try:
            texts = [script['searchable_text'] for script in self.scripts]
            self.script_embeddings = self.model.encode(texts, show_progress_bar=True)
            print(f"✓ Built embeddings for {len(texts)} scripts")
        except Exception as e:
            logger.error(f"Error building embeddings: {e}")
            self.script_embeddings = None
    
    def _save_script_cache(self, cache_file: Path):
        """Save script cache"""
        try:
            cache_data = {
                'scripts': self.scripts,
                'embeddings': self.script_embeddings,
                'index': self.script_index
            }
            with open(cache_file, 'wb') as f:
                pickle.dump(cache_data, f)
            print("Saved script embeddings cache")
        except Exception as e:
            logger.error(f"Failed to save script cache: {e}")
    
    def rebuild_cache(self):
        """Force rebuild of script cache"""
        cache_file = self.cache_path / "script_cache.pkl"
        if cache_file.exists():
            cache_file.unlink()
        
        with self._loading_lock:
            self.scripts = []
            self.script_embeddings = None
            self.script_index = {}
            self._loaded = False
        
        self._load_sync()
    
    def get_stats(self) -> Dict[str, Any]:
        """Get RAG statistics"""
        return {
            'loaded': self._loaded,
            'total_scripts': len(self.scripts),
            'has_embeddings': self.script_embeddings is not None,
            'model_loaded': self.model is not None,
            'indexed_names': len(self.script_index)
        }