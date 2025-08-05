# src/agents/project_manager.py
from .base import BaseAgent
from ..orchestrator.types import AgentMessage, TaskContext, AgentType

class ProjectManagerAgent(BaseAgent):
    """Central coordinator for all EPLAN workflows"""
    
    def __init__(self, orchestrator):
        super().__init__(orchestrator)
    
    async def process(self, context: TaskContext) -> AgentMessage:
        knowledge_result = await self.get_peer_result(AgentType.KNOWLEDGE)
        knowledge_content = knowledge_result.content if hasattr(knowledge_result, 'content') else str(knowledge_result)
        
        # AI processes everything - filters irrelevant info and gives focused answer
        smart_response = await self._ai_process_response(knowledge_content, context.user_query)
        
        return AgentMessage(
            agent_type=AgentType.PROJECT_MANAGER,
            content=smart_response,
            metadata={'status': 'processed'}
        )
    
    async def _ai_process_response(self, knowledge_content: str, user_query: str) -> str:
        """AI reads user intent and knowledge, returns focused answer"""
        prompt = f"""User question: "{user_query}"

Knowledge documentation:
{knowledge_content}

You are an EPLAN expert. The user asked a specific question. Read the documentation, understand what they want to know, and give them a direct, intelligent answer about only what they asked for. Filter out irrelevant information."""

        try:
            return await self.ai_client.generate(prompt)
        except:
            return knowledge_content