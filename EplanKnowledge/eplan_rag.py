# eplan_rag.py
import os
import json
import requests
from pathlib import Path
from typing import List, Dict
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

class EplanRAG:
    def __init__(self):
        self.github_api_url = "https://api.github.com/repos/covagashi/LazyScriptingEplan/contents/EplanKnowledge"
        
        # Use simple TF-IDF instead of transformers
        print("Setting up TF-IDF vectorizer...")
        self.vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
        
        # Storage
        self.documents = []
        self.doc_vectors = None
        
        # Load knowledge base from GitHub
        self.build_knowledge_base()
    
    def build_knowledge_base(self):
        """Build knowledge base from GitHub repo"""
        print("Loading from GitHub...")
        
        # Load directly from each folder URL
        self._load_github_folder("https://api.github.com/repos/covagashi/LazyScriptingEplan/contents/EplanKnowledge/API", "api")
        self._load_github_folder("https://api.github.com/repos/covagashi/LazyScriptingEplan/contents/EplanKnowledge/Scripts%20cs", "scripts")
        
        print(f"Loaded {len(self.documents)} documents")
        
        # Generate TF-IDF vectors
        if self.documents:
            contents = [doc['content'] for doc in self.documents]
            self.doc_vectors = self.vectorizer.fit_transform(contents)
            print("TF-IDF vectors generated")
    
    def _load_github_folder(self, folder_url: str, folder_type: str):
        """Load files from GitHub folder URL"""
        try:
            response = requests.get(folder_url)
            items = response.json()
            
            print(f"Loading from: {folder_url}")
            print(f"Found {len(items)} items")
            
            for item in items:
                print(f"Processing: {item['name']} - type: {item['type']}")
                if item['type'] == 'file' and item['name'].endswith('.json'):
                    print(f"  -> Downloading JSON file")
                    # Download file content
                    file_response = requests.get(item['download_url'])
                    if file_response.status_code == 200:
                        data = file_response.json()
                        content = self._json_to_text(data)
                        
                        self.documents.append({
                            'type': folder_type,
                            'file': item['name'],
                            'content': content
                        })
                        print(f"  -> Loaded: {item['name']}")
                elif item['type'] == 'dir':
                    self._load_github_folder(item['url'], folder_type)
                    
        except Exception as e:
            print(f"Error loading folder: {e}")

    
    def _json_to_text(self, data) -> str:  
        """Convert JSON to searchable text"""
        if isinstance(data, dict):
            text_parts = []
            for key, value in data.items():
                if isinstance(value, str):
                    text_parts.append(f"{key}: {value}")
                elif isinstance(value, (list, dict)):
                    text_parts.append(f"{key}: {json.dumps(value, indent=2)}")
            return "\n".join(text_parts)
        else:
            return json.dumps(data, indent=2)
    
    def search(self, query: str, top_k: int = 3) -> List[Dict]:
        """Search for relevant documents using TF-IDF"""
        if not self.documents or self.doc_vectors is None:
            return []
        
        # Transform query
        query_vector = self.vectorizer.transform([query])
        
        # Calculate similarities
        similarities = cosine_similarity(query_vector, self.doc_vectors)[0]
        
        # Get top matches
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        results = []
        for idx in top_indices:
            if similarities[idx] > 0.1: 
                results.append({
                    'document': self.documents[idx],
                    'similarity': float(similarities[idx])
                })
        
        return results

class EplanAIAssistant:
    def __init__(self):
        self.rag = EplanRAG()
        self.ollama_url = "http://localhost:11434/api/generate"
        self.model = "qwen2.5-coder:7b-instruct-q4_K_M"
    
    def ask(self, user_query: str) -> str:
        """Ask AI with RAG context"""
        # Search for relevant examples
        relevant_docs = self.rag.search(user_query, top_k=2)
        
        # Build context
        context = ""
        if relevant_docs:
            context = "\n## Relevant EPLAN Examples:\n"
            for doc in relevant_docs:
                context += f"\n### {doc['document']['file']}:\n"
                context += f"{doc['document']['content'][:800]}...\n"
        
        # Build prompt
        prompt = f"""You are an EPLAN automation expert. Help with EPLAN scripting using C#.

{context}

User question: {user_query}

Provide a direct, practical answer focused on EPLAN automation."""

        # Send to AI
        try:
            response = requests.post(self.ollama_url, json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            })
            return response.json()['response']
        except Exception as e:
            return f"Error: {e}"

# Usage
def main():
    assistant = EplanAIAssistant()
    
    print("🤖 EPLAN AI Assistant with RAG")
    print("Type 'quit' to exit\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        
        response = assistant.ask(user_input)
        print(f"AI: {response}\n")

if __name__ == "__main__":
    main()