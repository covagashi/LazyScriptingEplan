# src/sub_agents/knowledge_agent/tools.py
from src.ai.documentation_rag import OptimizedDocumentationRAG
import logging

logger = logging.getLogger(__name__)
_doc_rag = None

def _get_doc_rag():
    global _doc_rag
    if _doc_rag is None:
        _doc_rag = OptimizedDocumentationRAG()
    return _doc_rag

def search_eplan_docs(query: str, top_k: int = 1) -> str:  # Reduced to 1
    """Search EPLAN API docs"""
    try:
        doc_rag = _get_doc_rag()
        results = doc_rag.search_documentation(query, top_k=top_k)
        
        if not results:
            return f"❌ '{query}' not found in RAG"
        
        # Ultra-compressed format
        item = results[0]['document'].get('item', {})
        name = item.get('name', 'N/A')
        desc = item.get('description', 'N/A')[:80]  # Truncate
        
        response = f"**{name}**: {desc}"
        
        # Single example if available
        if 'examples' in item and item['examples']:
            example = item['examples'][0]
            if isinstance(example, dict) and 'command' in example:
                response += f"\nUsage: `{example['command']}`"
        
        return response
        
    except Exception as e:
        logger.error(f"Error in search_eplan_docs: {e}")
        return f"❌ Search error: {str(e)}"

def find_action_docs(action_name: str) -> str:
    """Find specific action docs"""
    try:
        doc_rag = _get_doc_rag()
        results = doc_rag.find_action_documentation(action_name)
        
        if not results:
            return f"❌ '{action_name}' not found"
        
        item = results[0]['document'].get('item', {})
        return f"**{action_name}**: {item.get('description', 'N/A')}"
        
    except Exception as e:
        logger.error(f"Error in find_action_docs: {e}")
        return f"❌ Error: {str(e)}"