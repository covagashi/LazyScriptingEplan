# src/sub_agents/examples_agent/tools.py
from src.ai.optimized_rag import OptimizedScriptRAG
import logging

logger = logging.getLogger(__name__)

# Global singleton instance
_script_rag = None

def _get_script_rag():
    global _script_rag
    if _script_rag is None:
        _script_rag = OptimizedScriptRAG()
    return _script_rag

def search_script_examples(functionality: str, top_k: int = 3) -> str:
    """Find C# script examples for EPLAN functionality"""
    try:
        script_rag = _get_script_rag()
        
        # Search for examples
        results = script_rag.search_scripts_sync(functionality, top_k=top_k)
        
        if not results:
            return f"❌ No script examples found for '{functionality}' in RAG database."
        
        response = f"## Script Examples: {functionality}\n\n"
        for i, result in enumerate(results, 1):
            # Handle nested structure properly
            doc = result.get('document', {})
            example = doc.get('example', {})
            
            # If example is empty, try to extract from document directly
            if not example:
                example = doc
            
            response += f"**{i}. {example.get('name', 'Script Example')}**\n"
            response += f"{example.get('description', 'No description available')}\n"
            
            # Handle script content
            script_content = example.get('script', [])
            if isinstance(script_content, list) and script_content:
                # Take reasonable number of lines
                code_lines = script_content[:20] if len(script_content) > 20 else script_content
                response += f"```csharp\n{chr(10).join(code_lines)}\n```\n"
            elif isinstance(script_content, str):
                response += f"```csharp\n{script_content}\n```\n"
            
            score = result.get('score', 0)
            response += f"*Relevance: {score:.2f}*\n\n"
        
        return response
        
    except Exception as e:
        logger.error(f"Error in search_script_examples: {e}")
        return f"❌ Error searching examples: {str(e)}"

def find_pattern_examples(pattern: str) -> str:
    """Find examples by specific pattern"""
    try:
        script_rag = _get_script_rag()
        results = script_rag.find_by_pattern(pattern)
        
        if not results:
            return f"❌ No pattern examples found for '{pattern}' in RAG database."
        
        response = f"## Pattern Examples: {pattern}\n\n"
        for result in results[:2]:  # Limit to 2 examples
            doc = result.get('document', {})
            example = doc.get('example', doc)
            
            response += f"**{example.get('name', 'Pattern Example')}**\n"
            response += f"{example.get('description', 'Pattern usage example')}\n"
            
            script_content = example.get('script', [])
            if isinstance(script_content, list) and script_content:
                code_snippet = script_content[:20]  # First 15 lines
                response += f"```csharp\n{chr(10).join(code_snippet)}\n```\n\n"
            elif isinstance(script_content, str):
                response += f"```csharp\n{script_content}\n```\n\n"
        
        return response
        
    except Exception as e:
        logger.error(f"Error in find_pattern_examples: {e}")
        return f"❌ Error searching patterns: {str(e)}"