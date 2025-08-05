# src/agents/project_manager.py
from .base import BaseAgent
from ..orchestrator.types import AgentMessage, TaskContext, AgentType

class ProjectManagerAgent(BaseAgent):
    """Central coordinator for all EPLAN workflows"""
    
    def __init__(self, orchestrator):
        super().__init__(orchestrator)
    
    async def process(self, context: TaskContext) -> AgentMessage:
        # Get knowledge first
        knowledge_result = await self.get_peer_result(AgentType.KNOWLEDGE)
        
        # Handle case where knowledge_result might be string or AgentMessage
        if isinstance(knowledge_result, str):
            knowledge_content = knowledge_result
        else:
            knowledge_content = knowledge_result.content
        
        # Verify knowledge quality
        if not self._is_useful_response(knowledge_content, context):
            return AgentMessage(
                agent_type=AgentType.PROJECT_MANAGER,
                content="❌ No encontré información útil para tu consulta.",
                metadata={'status': 'no_useful_info'}
            )
        
        # Enrich response with AI context
        enriched_content = await self._enrich_response(knowledge_content, context)
        
        return AgentMessage(
            agent_type=AgentType.PROJECT_MANAGER,
            content=enriched_content,
            metadata={'status': 'info_provided'}
        )
    
    def _is_useful_response(self, content: str, context: TaskContext) -> bool:
        """Verify if knowledge response is useful"""
        # Check for empty or error responses
        if not content or len(content.strip()) < 50:
            return False
        
        # Check for negative indicators
        negative_phrases = [
            "No se encontró", "No encontré", "not found", 
            "Unknown", "Sin descripción", "No description"
        ]
        
        return not any(phrase in content for phrase in negative_phrases)
    
    async def _enrich_response(self, knowledge_content: str, context: TaskContext) -> str:
        """Intelligently enrich knowledge response based on content"""
        # Use AI to add relevant context
        prompt = f"""The user asked: "{context.user_query}"

Knowledge response:
{knowledge_content}

Add helpful context about this EPLAN action. Be concise and practical. Focus on:
- Key usage tips
- Common scenarios  
- Important considerations

Keep it brief (2-3 bullet points max)."""

        try:
            enrichment = await self.ai_client.generate(prompt)
            return f"{knowledge_content}\n\n💡 **Contexto adicional:**\n{enrichment}"
        except:
            return knowledge_content