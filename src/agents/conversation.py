# src/agents/conversation.py
from .base import BaseAgent
from ..orchestrator.types import AgentMessage, TaskContext, AgentType

class ConversationAgent(BaseAgent):
    """Natural conversation + EPLAN intent detection"""
    
    async def process(self, context: TaskContext) -> AgentMessage:
        # AI detects if this needs EPLAN workflow
        needs_eplan_workflow = await self._detect_eplan_workflow_needed(context.user_query)
        
        if needs_eplan_workflow:
            # Send to ProjectManager for coordination
            pm_result = await self.get_peer_result(AgentType.PROJECT_MANAGER)
            pm_content = pm_result.content if hasattr(pm_result, 'content') else str(pm_result)
            return AgentMessage(
                agent_type=AgentType.CONVERSATION,
                content=pm_content,
                metadata={'workflow_used': True}
            )
        
        # Handle normal conversation
        return await self._handle_normal_chat(context)
    
    async def _detect_eplan_workflow_needed(self, query: str) -> bool:
        """AI detects if query needs EPLAN workflow coordination"""
        prompt = f"""Does this query require EPLAN script generation, execution, or technical coordination?

Query: "{query}"

Answer YES if user wants:
- Script creation/generation  
- EPLAN execution/automation
- Complex EPLAN technical help

Answer NO if it's:
- Simple greeting
- General chat
- Basic questions

Answer only: YES or NO"""
        
        try:
            response = await self.ai_client.generate(prompt)
            return 'YES' in response.upper()
        except:
            return False
    
    async def _handle_normal_chat(self, context: TaskContext) -> AgentMessage:
        """Natural conversation for non-workflow queries"""
        prompt = f"""You are an EPLAN assistant. Have a natural conversation.

User said: "{context.user_query}"

If unclear what they want, ask for clarification. Be helpful and conversational."""
        
        try:
            response = await self.ai_client.generate(prompt)
            return AgentMessage(
                agent_type=AgentType.CONVERSATION,
                content=response,
                metadata={'workflow_used': False}
            )
        except:
            return AgentMessage(
                agent_type=AgentType.CONVERSATION,
                content="¿En qué te puedo ayudar?",
                metadata={'workflow_used': False}
            )