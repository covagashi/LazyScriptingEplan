# test_eplan_ai.py
import requests
import json

def test_ollama_connection():
    """Test if Ollama is running and model is available"""
    try:
        response = requests.get("http://localhost:11434/api/tags")
        models = response.json()
        print("Available models:", [m['name'] for m in models.get('models', [])])
        return True
    except:
        print("Ollama not running. Start with: ollama serve")
        return False

def ask_ai(prompt):
    """Send prompt to Qwen2.5-Coder"""
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "qwen2.5-coder:7b-instruct-q4_K_M",
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=data)
        return response.json()['response']
    except Exception as e:
        return f"Error: {e}"


def chat_loop():
    print("\n🤖 EPLAN AI Assistant (type 'quit' to exit)")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'quit':
            break
        
        response = ask_ai(user_input)
        print(f"AI: {response}")


if __name__ == "__main__":
    if test_ollama_connection():
        chat_loop()