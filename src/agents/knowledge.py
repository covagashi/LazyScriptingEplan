# src/agents/knowledge.py
from .base import BaseAgent
from ..orchestrator.types import AgentMessage, TaskContext, AgentType

class KnowledgeAgent(BaseAgent):
    """EPLAN knowledge agent using RAG service"""
    
    def __init__(self, orchestrator):
        super().__init__(orchestrator)
        from ..ai.rag import EplanRAG
        self.rag = EplanRAG()
    
    async def process(self, context: TaskContext) -> AgentMessage:
        # Pure semantic search
        results = self.rag.search(context.user_query, top_k=2)
        
        if not results:
            return AgentMessage(
                agent_type=AgentType.KNOWLEDGE,
                content="No EPLAN documentation found.",
                metadata={'docs_found': 0}
            )
        
        # Format all results
        knowledge = "## EPLAN Documentation Found:\n"
        
        for result in results:
            doc = result['document']
            action_data = doc.get('action', {})
            
            knowledge += f"\n### {action_data.get('name', 'Unknown')}:\n"
            knowledge += f"**Description**: {action_data.get('description', 'No description')}\n"
            
            # Parameters
            params = action_data.get('parameters', [])
            if params:
                knowledge += "\n**Parameters**:\n"
                for param in params:
                    if isinstance(param, dict):
                        name = param.get('name', 'Unknown')
                        desc = param.get('description', 'No description')
                        optional = param.get('optional', True)
                        knowledge += f"- **/{name}**: {desc} {'(optional)' if optional else '(required)'}\n"
            
            # Examples
            examples = action_data.get('examples', [])
            if examples:
                knowledge += "\n**Examples**:\n"
                for ex in examples[:2]:
                    if isinstance(ex, dict):
                        cmd = ex.get('command', '')
                        if cmd:
                            knowledge += f"```\n{cmd}\n```\n"
        
        return AgentMessage(
            agent_type=AgentType.KNOWLEDGE,
            content=knowledge,
            metadata={
                'docs_found': len(results),
                'score': result['score'],
                'action_name': action_data.get('name')
            }
        )