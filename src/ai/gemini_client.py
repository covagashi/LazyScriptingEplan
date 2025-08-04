# src/ai/gemini_client.py
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class GeminiClient:
    """Gemini API wrapper"""
    
    def __init__(self, model_name: str = 'gemini-1.5-flash'):
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)
    
    async def generate(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Gemini error: {e}"