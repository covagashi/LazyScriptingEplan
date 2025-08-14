# src/sub_agents/knowledge_agent/tools.py
from src.ai.documentation_rag import OptimizedDocumentationRAG
import logging

logger = logging.getLogger(__name__)

# Global singleton instances
_doc_rag = None

def _get_doc_rag():
    global _doc_rag
    if _doc_rag is None:
        _doc_rag = OptimizedDocumentationRAG()
    return _doc_rag

def search_eplan_docs(query: str, top_k: int = 3) -> str:
    """Search EPLAN API documentation with strict RAG-only responses"""
    try:
        doc_rag = _get_doc_rag()
        results = doc_rag.search_documentation(query, top_k=top_k)
        
        if not results:
            return f"❌ No se encontró documentación para '{query}' en la base de datos RAG. Verifica que los datos estén cargados correctamente."
        
        response = f"## Documentación EPLAN: {query}\n\n"
        for i, result in enumerate(results, 1):
            item = result['document'].get('item', {})
            score = result['score']
            
            # Only show RAG data, no additional interpretation
            response += f"**{i}. {item.get('name', 'Referencia API')}**\n"
            response += f"**Tipo:** {item.get('type', 'N/A')}\n"
            response += f"**Categoría:** {item.get('category', 'N/A')}\n"
            response += f"**Descripción:** {item.get('description', 'Sin descripción disponible')}\n"
            
            if 'parameters' in item and item['parameters']:
                response += "\n**Parámetros:**\n"
                for param in item['parameters']:
                    if isinstance(param, dict):
                        param_name = param.get('name', 'Desconocido')
                        param_desc = param.get('description', 'Sin descripción')
                        param_type = param.get('type', 'N/A')
                        optional = " (opcional)" if param.get('optional', False) else ""
                        response += f"- `{param_name}` ({param_type}){optional}: {param_desc}\n"
            
            if 'examples' in item and item['examples']:
                response += "\n**Ejemplos:**\n"
                for example in item['examples']:
                    if isinstance(example, dict):
                        if 'command' in example:
                            response += f"```\n{example['command']}\n```\n"
                        if 'description' in example:
                            response += f"{example['description']}\n"
            
            if 'notes' in item and item['notes']:
                response += "\n**Notas:**\n"
                for note in item['notes']:
                    response += f"- {note}\n"
            
            response += f"\n*Relevancia: {score:.2f}*\n\n"
        
        response += "\n⚠️ **IMPORTANTE**: Esta información proviene directamente de la base de datos RAG. No se ha añadido información adicional."
        
        return response
        
    except Exception as e:
        logger.error(f"Error in search_eplan_docs: {e}")
        return f"❌ Error buscando documentación: {str(e)}"

def find_action_docs(action_name: str) -> str:
    """Find documentation for specific EPLAN action - RAG only"""
    try:
        doc_rag = _get_doc_rag()
        results = doc_rag.find_action_documentation(action_name)
        
        if not results:
            return f"❌ No se encontró documentación para la acción '{action_name}' en la base de datos RAG."
        
        response = f"## Documentación de Acción: {action_name}\n\n"
        for result in results:
            item = result['document'].get('item', {})
            response += f"**Nombre:** {item.get('name', action_name)}\n"
            response += f"**Tipo:** {item.get('type', 'acción')}\n"
            response += f"**Descripción:** {item.get('description', 'Sin descripción disponible')}\n"
            
            # Show exact RAG data structure
            response += f"\n**Datos RAG completos:**\n```json\n{item}\n```\n"
        
        response += "\n⚠️ **IMPORTANTE**: Solo se muestra información presente en la base de datos RAG."
        
        return response
        
    except Exception as e:
        logger.error(f"Error in find_action_docs: {e}")
        return f"❌ Error buscando documentación de acción: {str(e)}"