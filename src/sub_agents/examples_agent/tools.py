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
        
        # Use synchronous wrapper to avoid async issues
        results = script_rag.search_scripts_sync(functionality, top_k=top_k)
        
        if not results:
            return f"No script examples found for '{functionality}'. Try different keywords or check if examples exist."
        
        response = f"## Script Examples: {functionality}\n\n"
        for i, result in enumerate(results, 1):
            example = result['document'].get('example', {})
            score = result['score']
            
            response += f"**{i}. {example.get('name', 'Script Example')}**\n"
            response += f"{example.get('description', 'No description available')}\n"
            
            if 'script' in example:
                code_lines = example['script'][:15]  # First 15 lines
                response += f"```csharp\n{chr(10).join(code_lines)}\n...\n```\n"
            
            response += f"*Relevance: {score:.2f}*\n\n"
        
        return response
        
    except Exception as e:
        logger.error(f"Error in search_script_examples: {e}")
        return f"Error searching script examples: {str(e)}. Please try with different search terms."

def find_pattern_examples(pattern: str) -> str:
    """Find examples by specific pattern with error handling"""
    try:
        script_rag = _get_script_rag()
        results = script_rag.find_by_pattern(pattern)
        
        if not results:
            return f"No examples found for pattern '{pattern}'. Available patterns: DeclareAction, Start, Progress, BaseException."
        
        response = f"## Pattern Examples: {pattern}\n\n"
        for result in results[:2]:  # Limit to 2 examples
            example = result['document'].get('example', {})
            response += f"**{example.get('name', 'Pattern Example')}**\n"
            if 'script' in example:
                code_snippet = example['script'][:10]  # First 10 lines
                response += f"```csharp\n{chr(10).join(code_snippet)}\n```\n\n"
        
        return response
        
    except Exception as e:
        logger.error(f"Error in find_pattern_examples: {e}")
        return f"Error finding pattern examples: {str(e)}. Please verify the pattern name."

