# src/agents/knowledge.py
from .base import BaseAgent
from ..orchestrator.types import AgentMessage, TaskContext, AgentType
from ..ai import EplanRAG

class KnowledgeAgent(BaseAgent):
    """EPLAN knowledge agent using RAG service"""
    
    def __init__(self, orchestrator):
        super().__init__(orchestrator)
        self.rag = EplanRAG()
    
    async def process(self, context: TaskContext) -> AgentMessage:
        # Search RAG for relevant documents
        results = self.rag.search(context.user_query, top_k=2)
        
        if results:
            knowledge = "\n## Relevant EPLAN Documentation:\n"
            action_found = None
            
            for result in results:
                doc = result['document']
                knowledge += f"\n### {doc['file']} (relevance: {result['score']}):\n"
                
                # Extract action info if available
                if 'data' in doc and isinstance(doc['data'], dict):
                    action_data = doc['data']
                    
                    if 'name' in action_data:
                        action_found = action_data
                        knowledge += f"**Action**: {action_data.get('name', 'Unknown')}\n"
                        knowledge += f"**Description**: {action_data.get('description', 'No description')}\n"
                        
                        # Show only relevant parameters
                        params = action_data.get('parameters', [])
                        if params:
                            knowledge += f"**Parameters**:\n"
                            for param in params[:3]:  # Show only first 3 params
                                if isinstance(param, dict):
                                    name = param.get('name', 'Unknown')
                                    desc = param.get('description', 'No description')
                                    optional = param.get('optional', True)
                                    knowledge += f"- {name}: {desc} {'(optional)' if optional else '(required)'}\n"
                else:
                    # Fallback to content preview
                    content_preview = doc['content'][:300]
                    knowledge += f"{content_preview}...\n"
            
            # Determine if we have enough info
            needs_clarification = not action_found or self._missing_critical_params(context.user_query, action_found)
            
            return AgentMessage(
                agent_type=AgentType.KNOWLEDGE,
                content=knowledge,
                metadata={
                    'docs_found': len(results),
                    'action_found': action_found.get('name') if action_found else None,
                    'needs_clarification': needs_clarification,
                    'missing_params': []  # Clear the garbled params
                }
            )
        else:
            return AgentMessage(
                agent_type=AgentType.KNOWLEDGE,
                content="No relevant EPLAN documentation found for this query.",
                metadata={'needs_clarification': False}
            )
    
    def _missing_critical_params(self, user_query: str, action_data: dict) -> bool:
        """Check if critical parameters are missing for action execution"""
        if not action_data:
            return False
        
        # Check if action has required parameters
        params = action_data.get('parameters', [])
        required_params = [p for p in params if isinstance(p, dict) and not p.get('optional', True)]
        
        if not required_params:
            return False  # No required params
        
        # Simple check: if user query is very short and action has required params
        query_words = user_query.strip().split()
        return len(query_words) <= 3 and len(required_params) > 0