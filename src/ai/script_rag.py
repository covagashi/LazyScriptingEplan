# src/ai/script_rag.py
import json
import os
import numpy as np
from pathlib import Path
from typing import List, Dict, Any
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
from .optimized_rag import OptimizedRAG  

class ScriptRAG(OptimizedRAG):
    """RAG specialized in C# EPLAN code and scripts - FIXED"""
    
    def __init__(self):
        super().__init__("scripts")
        self.scripts_path = Path("src/ai/Knowledge/Scripts")
        self.cache_path = Path("src/ai/cache/scripts")
        self.cache_path.mkdir(exist_ok=True, parents=True)
        
        print("✓ Lazy ScriptRAG initialized")
        # Don't call async method from __init__
        self.load_scripts()
    
  
    def load_scripts(self):  # Cambiar de async def a def
        """Load scripts with lazy embeddings"""
        if not self.scripts_path.exists():
            return
        
        scripts = []
        for json_file in self.scripts_path.glob("*.json"):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                script_examples = self._extract_code_examples(data)
                
                for example in script_examples:
                    script_id = len(scripts)
                    code_text = self._create_code_searchable_text(example)
                    
                    script_doc = {
                        'id': script_id,
                        'filename': json_file.name,
                        'example': example,
                        'searchable_text': code_text,
                        'type': 'script'
                    }
                    scripts.append(script_doc)
                    
            except Exception as e:
                print(f"Error loading script file {json_file.name}: {e}")
        
        self._pending_scripts = scripts
        print(f"Loaded {len(scripts)} scripts for lazy processing")
    

    async def ensure_loaded(self):
        """Ensure scripts are loaded with embeddings"""
        if hasattr(self, '_pending_scripts') and self._pending_scripts:
            await self.add_documents_lazy(self._pending_scripts)
            del self._pending_scripts
            print(f"Scripts loaded with lazy embeddings")

    
    async def search_scripts(self, query: str, top_k: int = 3, threshold: float = 0.3):
        return await self.search_async(query, top_k, threshold)

    
    def _load_script_documents(self):
        """Load only documents with C# scripts"""
        if not self.scripts_path.exists():
            print(f"Scripts folder not found: {self.scripts_path}")
            return
        
        for json_file in self.scripts_path.glob("*.json"):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                script_examples = self._extract_code_examples(data)
                
                for example in script_examples:
                    script_id = len(self.scripts)
                    
                    code_text = self._create_code_searchable_text(example)
                    
                    script_doc = {
                        'id': script_id,
                        'filename': json_file.name,
                        'example': example,
                        'code_text': code_text,
                        'type': 'script'
                    }
                    
                    self.scripts.append(script_doc)
                    
                    example_id = example.get('id', '').lower()
                    example_name = example.get('name', '').lower()
                    if example_id:
                        self.script_index[example_id] = script_id
                    if example_name:
                        self.script_index[example_name] = script_id
                        
            except Exception as e:
                print(f"Error loading script file {json_file.name}: {e}")
        
        print(f"Extracted {len(self.scripts)} code examples")
    
    def _extract_code_examples(self, data: Any) -> List[Dict]:
        """Extract only examples with C# code"""
        examples = []
        
        if isinstance(data, dict):
            if ('script' in data or 'code' in data) and 'name' in data:
                examples.append(data)
            
            for key, value in data.items():
                if key == 'examples' and isinstance(value, list):
                    for item in value:
                        if isinstance(item, dict) and ('script' in item or 'code' in item):
                            examples.append(item)
                else:
                    examples.extend(self._extract_code_examples(value))
                    
        elif isinstance(data, list):
            for item in data:
                examples.extend(self._extract_code_examples(item))
        
        return examples
    
    def _create_code_searchable_text(self, example: Dict) -> str:
        """Create search-optimized text from code"""
        parts = []
        
        parts.append(example.get('name', ''))
        parts.append(example.get('description', ''))
        parts.append(example.get('id', ''))
        
        script_content = example.get('script', example.get('code', []))
        if isinstance(script_content, list):
            code_lines = ' '.join(script_content)
            parts.append(code_lines)
            
            parts.extend(self._extract_csharp_elements(code_lines))
        
        for feature in example.get('features', []):
            if isinstance(feature, str):
                parts.append(feature)
        
        return ' '.join(filter(None, parts))
    
    def _extract_csharp_elements(self, code: str) -> List[str]:
        """Extract specific elements from C# for better search"""
        elements = []
        
        import re
        class_matches = re.findall(r'class\s+(\w+)', code)
        elements.extend(class_matches)
        
        method_matches = re.findall(r'public\s+\w+\s+(\w+)\s*\(', code)
        elements.extend(method_matches)
        
        using_matches = re.findall(r'using\s+([\w\.]+);', code)
        elements.extend(using_matches)
        
        attribute_matches = re.findall(r'\[(\w+)\]', code)
        elements.extend(attribute_matches)
        
        return elements
    
    def _build_script_embeddings(self):
        """Build code-optimized embeddings"""
        if not self.scripts:
            return
        
        print("Building script embeddings...")
        texts = [script['code_text'] for script in self.scripts]
        self.script_embeddings = self.model.encode(texts, show_progress_bar=True)
        print(f"✓ Built embeddings for {len(texts)} scripts")
    
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
            print(f"Failed to save script cache: {e}")
    
    def search_scripts(self, query: str, top_k: int = 3, threshold: float = 0.3) -> List[Dict[str, Any]]:
        """Semantic search of C# scripts"""
        if not self.scripts or self.script_embeddings is None:
            return []
        
        query_lower = query.lower()
        if query_lower in self.script_index:
            script_id = self.script_index[query_lower]
            script = self.scripts[script_id]
            return [{
                'document': script,
                'score': 1.0,
                'match_type': 'exact_script'
            }]
        
        query_embedding = self.model.encode([query])
        similarities = cosine_similarity(query_embedding, self.script_embeddings)[0]
        
        results = []
        for i, score in enumerate(similarities):
            if score >= threshold:
                results.append({
                    'document': self.scripts[i],
                    'score': float(score),
                    'match_type': 'semantic_script'
                })
        
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:top_k]
    
    def find_by_pattern(self, pattern: str) -> List[Dict[str, Any]]:
        """Search for scripts by specific pattern (e.g. 'DeclareAction', 'Progress', etc.)"""
        results = []
        pattern_lower = pattern.lower()
        
        for script in self.scripts:
            code_text = script['code_text'].lower()
            example = script['example']
            
            if pattern_lower in code_text:
                relevance = code_text.count(pattern_lower) / len(code_text.split()) * 100
                
                results.append({
                    'document': script,
                    'score': min(relevance, 1.0),
                    'match_type': 'pattern_match'
                })
        
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:5]
    
    def get_similar_scripts(self, script_example: Dict, top_k: int = 3) -> List[Dict[str, Any]]:
        """Find scripts similar to a given example"""
        if not self.script_embeddings is None:
            return []
        
        ref_text = self._create_code_searchable_text(script_example)
        ref_embedding = self.model.encode([ref_text])
        
        similarities = cosine_similarity(ref_embedding, self.script_embeddings)[0]
        
        results = []
        for i, score in enumerate(similarities):
            if self.scripts[i]['example'] != script_example:
                results.append({
                    'document': self.scripts[i],
                    'score': float(score),
                    'match_type': 'similarity'
                })
        
        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:top_k]
    
    def rebuild_cache(self):
        """Force rebuild of script cache"""
        cache_file = self.cache_path / "script_cache.pkl"
        if cache_file.exists():
            cache_file.unlink()
        
        self.scripts = []
        self.script_embeddings = None
        self.script_index = {}
        
        self.load_scripts()