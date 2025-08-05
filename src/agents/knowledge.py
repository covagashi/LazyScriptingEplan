# src/agents/knowledge.py
from .base import BaseAgent
from ..orchestrator.types import AgentMessage, TaskContext, AgentType
from ..ai import EplanRAG

class KnowledgeAgent(BaseAgent):
    """EPLAN knowledge agent using RAG service"""
    
    def __init__(self, orchestrator):
        super().__init__(orchestrator)
        from ..ai.rag import EplanRAG
        self.rag = EplanRAG()
    
    async def process(self, context: TaskContext) -> AgentMessage:
        # Extract action name if present
        query = context.user_query.lower().strip()
        action_name = None
        
        if "projectopen" in query:
            action_name = "projectopen"
        
        # Try exact search first
        if action_name:
            print(f"DEBUG: Searching exact for '{action_name}'")
            results = self.rag.search_exact(action_name)
            print(f"DEBUG: Exact results: {len(results)}")
            if not results:
                print("DEBUG: Fallback to semantic search")
                results = self.rag.search(context.user_query, top_k=2)
        else:
            results = self.rag.search(context.user_query, top_k=2)
        
        print(f"DEBUG: Final results count: {len(results)}")
        
        if not results:
            return AgentMessage(
                agent_type=AgentType.KNOWLEDGE,
                content="No se encontró documentación EPLAN.",
                metadata={'docs_found': 0}
            )
        
        # Format response
        knowledge = "## Información EPLAN encontrada:\n"
        
        for result in results:
            doc = result['document']
            action_data = doc.get('action', {})
            
            knowledge += f"\n### {action_data.get('name', 'Unknown')}:\n"
            knowledge += f"**Descripción**: {action_data.get('description', 'Sin descripción')}\n"
            
            # Parameters
            params = action_data.get('parameters', [])
            if params:
                knowledge += "\n**Parámetros**:\n"
                for param in params:
                    if isinstance(param, dict):
                        name = param.get('name', 'Unknown')
                        desc = param.get('description', 'Sin descripción')
                        optional = param.get('optional', True)
                        knowledge += f"- **/{name}**: {desc} {'(opcional)' if optional else '(requerido)'}\n"
            
            # Examples
            examples = action_data.get('examples', [])
            if examples:
                knowledge += "\n**Ejemplos**:\n"
                for ex in examples[:2]:
                    if isinstance(ex, dict):
                        cmd = ex.get('command', '')
                        if cmd:
                            knowledge += f"```\n{cmd}\n```\n"
        
        return AgentMessage(
            agent_type=AgentType.KNOWLEDGE,
            content=knowledge,
            metadata={'docs_found': len(results)}
        )