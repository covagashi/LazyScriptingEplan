# src/sub_agents/knowledge_agent/tools.py
from src.ai.documentation_rag import DocumentationRAG
import logging

logger = logging.getLogger(__name__)

# Global singleton instances
_doc_rag = None

def _get_doc_rag():
    global _doc_rag
    if _doc_rag is None:
        _doc_rag = DocumentationRAG()
    return _doc_rag

def search_eplan_docs(query: str, top_k: int = 3) -> str:
    """Search EPLAN API documentation with error handling"""
    try:
        doc_rag = _get_doc_rag()
        results = doc_rag.search_documentation(query, top_k=top_k)
        
        if not results:
            return f"No documentation found for '{query}'. Try rephrasing your search terms."
        
        response = f"## EPLAN Documentation: {query}\n\n"
        for i, result in enumerate(results, 1):
            item = result['document'].get('item', {})
            score = result['score']
            
            response += f"**{i}. {item.get('name', 'API Reference')}**\n"
            response += f"{item.get('description', 'No description available')}\n"
            
            if 'parameters' in item and item['parameters']:
                response += "\n**Parameters:**\n"
                for param in item['parameters'][:3]:
                    if isinstance(param, dict):
                        param_name = param.get('name', 'Unknown')
                        param_desc = param.get('description', 'No description')
                        response += f"- `{param_name}`: {param_desc}\n"
            
            response += f"\n*Relevance: {score:.2f}*\n\n"
        
        return response
        
    except Exception as e:
        logger.error(f"Error in search_eplan_docs: {e}")
        return f"Error searching documentation: {str(e)}. Please try again with different search terms."

def find_action_docs(action_name: str) -> str:
    """Find documentation for specific EPLAN action with error handling"""
    try:
        doc_rag = _get_doc_rag()
        results = doc_rag.find_action_documentation(action_name)
        
        if not results:
            return f"No action documentation found for '{action_name}'. Verify the action name is correct."
        
        response = f"## Action Documentation: {action_name}\n\n"
        for result in results:
            item = result['document'].get('item', {})
            response += f"**{item.get('name', action_name)}**\n"
            response += f"{item.get('description', 'No description available')}\n\n"
        
        return response
        
    except Exception as e:
        logger.error(f"Error in find_action_docs: {e}")
        return f"Error finding action documentation: {str(e)}. Please verify the action name."

