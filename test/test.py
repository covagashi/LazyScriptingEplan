# test_gemini.py
import os
import google.generativeai as genai

def test_gemini():
    # Set API key
    api_key = input("Enter your Gemini API key: ")
    genai.configure(api_key=api_key)
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Test basic functionality
    try:
        response = model.generate_content("Generate C# code to close current EPLAN project using Remoting API")
        print("✓ Gemini API working!")
        print("Response:", response.text)
        return True
    except Exception as e:
        print("✗ Error:", e)
        return False

if __name__ == "__main__":
    test_gemini()