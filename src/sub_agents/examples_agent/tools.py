# src/sub_agents/examples_agent/tools.py 
from src.ai.optimized_rag import OptimizedScriptRAG
import logging

logger = logging.getLogger(__name__)
_script_rag = None

def _get_script_rag():
    global _script_rag
    if _script_rag is None:
        _script_rag = OptimizedScriptRAG()
    return _script_rag

def search_script_examples(functionality: str, top_k: int = 1) -> str:
    """Find C# script examples"""
    try:
        script_rag = _get_script_rag()
        results = script_rag.search_scripts_sync(functionality, top_k=top_k)
        
        if not results:
            return f"❌ No examples for '{functionality}'"
        
        doc = results[0].get('document', {})
        example = doc.get('example', doc)
        
        name = example.get('name', 'Script Example')
        desc = example.get('description', 'No description')[:60]
        
        response = f"**{name}**: {desc}"
        
        # Show code snippet (max 10 lines)
        script_content = example.get('script', [])
        if isinstance(script_content, list) and script_content:
            code_lines = script_content[:10]
            response += f"\n```csharp\n{chr(10).join(code_lines)}\n```"
        elif isinstance(script_content, str):
            response += f"\n```csharp\n{script_content[:300]}\n```"
        
        return response
        
    except Exception as e:
        logger.error(f"Error in search_script_examples: {e}")
        return f"❌ Search error: {str(e)}"

def find_pattern_examples(pattern: str) -> str:
    """Find examples by pattern"""
    try:
        script_rag = _get_script_rag()
        results = script_rag.find_by_pattern(pattern)
        
        if not results:
            return f"❌ No pattern examples for '{pattern}'"
        
        doc = results[0].get('document', {})
        example = doc.get('example', doc)
        
        return f"**{example.get('name', 'Pattern')}**: Found pattern usage"
        
    except Exception as e:
        logger.error(f"Error in find_pattern_examples: {e}")
        return f"❌ Error: {str(e)}"