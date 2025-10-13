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

def _smart_truncate(text: str, max_length: int = 200) -> str:
    """
    Intelligently truncate text at word boundaries.

    Args:
        text: Text to truncate
        max_length: Maximum character length

    Returns:
        Truncated text with ellipsis if needed
    """
    if len(text) <= max_length:
        return text

    # Find the last space before max_length
    truncated = text[:max_length]
    last_space = truncated.rfind(' ')

    if last_space > max_length * 0.8:  # If we're at least 80% of the way
        return truncated[:last_space] + '...'
    else:
        # No good break point, just cut at max_length
        return truncated + '...'

def search_eplan_docs(query: str, top_k: int = 1) -> str:
    """
    Search EPLAN API documentation with improved formatting.

    Args:
        query: Search query
        top_k: Number of results to return (default: 1)

    Returns:
        Formatted search results or error message
    """
    try:
        doc_rag = _get_doc_rag()
        results = doc_rag.search_documentation(query, top_k=top_k)

        if not results:
            return f"❌ No documentation found for '{query}'"

        # Get the actual document structure
        doc = results[0]['document']
        path = doc.get('path', 'N/A')
        content = doc.get('content', 'N/A')
        chunk_info = ""

        # Check if this is a chunked document
        if 'chunk_id' in doc and doc.get('total_chunks', 1) > 1:
            chunk_info = f" (chunk {doc['chunk_id'] + 1}/{doc['total_chunks']})"

        # Extract title from path (last segment)
        source_file = doc.get('source_file', path.split('/')[-1] if path != 'N/A' else 'Documentation')

        # Smart truncation
        desc = _smart_truncate(content, max_length=250) if content != 'N/A' else 'No description available'

        response = f"**{source_file}**{chunk_info}\nPath: {path}\n\n{desc}"

        return response

    except Exception as e:
        logger.error(f"Error in search_eplan_docs: {e}", exc_info=True)
        return f"❌ Search error: {str(e)}"

def find_action_docs(action_name: str) -> str:
    """
    Find specific EPLAN action documentation.

    Args:
        action_name: Name of the action to search for

    Returns:
        Formatted action documentation or error message
    """
    try:
        doc_rag = _get_doc_rag()
        results = doc_rag.find_action_documentation(action_name)

        if not results:
            return f"❌ Action '{action_name}' not found in documentation"

        # Get the actual document structure
        doc = results[0]['document']
        path = doc.get('path', 'N/A')
        content = doc.get('content', 'N/A')
        chunk_info = ""

        # Check if this is a chunked document
        if 'chunk_id' in doc and doc.get('total_chunks', 1) > 1:
            chunk_info = f" (chunk {doc['chunk_id'] + 1}/{doc['total_chunks']})"

        source_file = doc.get('source_file', path.split('/')[-1] if path != 'N/A' else action_name)

        # Smart truncation with slightly shorter length for action docs
        desc = _smart_truncate(content, max_length=200) if content != 'N/A' else 'No description available'

        return f"**{source_file}**{chunk_info}\nPath: {path}\n\n{desc}"

    except Exception as e:
        logger.error(f"Error in find_action_docs: {e}", exc_info=True)
        return f"❌ Error: {str(e)}"