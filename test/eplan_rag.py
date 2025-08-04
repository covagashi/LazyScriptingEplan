# eplan_rag_gemini.py
import os
import json
import requests
from pathlib import Path
from typing import List, Dict
import google.generativeai as genai
from sklearn.feature_extraction.text import TfidfVectorizer
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class EplanRAG:
    def __init__(self):
        self.github_api_url = "https://api.github.com/repos/covagashi/LazyScriptingEplan/contents/EplanKnowledge"
        
        # TF-IDF vectorizer
        print("Setting up TF-IDF vectorizer...")
        self.vectorizer = TfidfVectorizer(max_features=1000, stop_words='english', ngram_range=(1,2))
        
        # Storage
        self.documents = []
        self.doc_vectors = None
        
        # Load knowledge base from GitHub
        self.build_knowledge_base()
    
    def build_knowledge_base(self):
        """Build knowledge base from GitHub repo"""
        print("Loading from GitHub...")
        
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
            session = requests.Session()
            session.verify = False
            
            response = session.get(folder_url)
            items = response.json()
            
            print(f"Loading from: {folder_url}")
            print(f"Found {len(items)} items")
            
            for item in items:
                print(f"Processing: {item['name']} - type: {item['type']}")
                if item['type'] == 'file' and item['name'].endswith('.json'):
                    print(f"  -> Downloading JSON file")
                    file_response = session.get(item['download_url'])
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
        results = []
        query_lower = query.lower()
        
        for i, doc in enumerate(self.documents):
            content_lower = doc['content'].lower()
            
            if any(word in content_lower for word in query_lower.split() if len(word) > 2):
                results.append({
                    'document': doc,
                    'similarity': 1.0,
                    'score': '1.000'
                })
        
        print(f"Query: '{query}' - Found {len(results)} matches")
        return results[:top_k]

class EplanGeminiAssistant:
    def __init__(self, api_key: str):
        # Configure Gemini API
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Initialize RAG
        self.rag = EplanRAG()
        
        print("✓ Gemini 1.5-flash initialized")
    
    def ask(self, user_query: str) -> str:
        """Ask AI with RAG context"""
        # Search for relevant examples
        relevant_docs = self.rag.search(user_query, top_k=2)
        
        # Build context
        context = ""
        if relevant_docs:
            context = "\n## EPLAN API Examples:\n"
            for doc in relevant_docs:
                context += f"\n### {doc['document']['file']}:\n"
                context += f"{doc['document']['content'][:600]}...\n"
        
        # Enhanced prompt for Gemini
        prompt = f"""You are an expert EPLAN automation assistant. Generate precise C# code using EPLAN Remoting API.

AVAILABLE CONTEXT:
{context}

USER REQUEST: {user_query}

INSTRUCTIONS:
- Generate clean, working C# code for EPLAN Remoting API
- Use ActionCallingContext and CommandLineInterpreter patterns
- Include necessary using statements
- Focus on practical, executable solutions
- If generating macro insertion, use proper file paths
- For project operations, use standard EPLAN commands

RESPONSE FORMAT:
```csharp
// Generated EPLAN code
[your code here]
```

Brief explanation of what the code does."""

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Gemini API Error: {e}"
    
    def generate_eplan_script(self, task_description: str) -> str:
        """Generate specific EPLAN script"""
        prompt = f"""Generate C# code for EPLAN Remoting API based on this task:

TASK: {task_description}

Requirements:
- Use EPLAN Remoting API patterns
- Include ActionCallingContext setup
- Use CommandLineInterpreter.Execute()
- Add error handling
- Make it ready to execute

Return only the C# code block."""

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating script: {e}"

# Usage example
def main():
    # Load API key from .env file
    api_key = os.getenv('GEMINI_API_KEY')
    
    if not api_key:
        print("Please set GEMINI_API_KEY in .env file!")
        return
    
    assistant = EplanGeminiAssistant(api_key)
    
    print("🤖 EPLAN Gemini Assistant with RAG")
    print("Type 'quit' to exit\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        
        response = assistant.ask(user_input)
        print(f"AI: {response}\n")

if __name__ == "__main__":
    main()