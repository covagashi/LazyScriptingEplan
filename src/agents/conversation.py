# src/agents/conversation.py
from .base import BaseAgent
from ..orchestrator.types import AgentMessage, TaskContext, AgentType

class ConversationAgent(BaseAgent):
    """Conversational AI that understands user intent"""
    
    def __init__(self, orchestrator):
        super().__init__(orchestrator)
    
    async def process(self, context: TaskContext) -> AgentMessage:
        response = await self.ai_client.generate(f"""
User: "{context.user_query}"

You're an EPLAN 2023 assistant. Respond naturally. 

At the end, add exactly one line:
WORKFLOW: eplan (if EPLAN-related) or chat (if general conversation)
""")
        
        # Extract workflow from AI response
        lines = response.strip().split('\n')
        workflow_line = [line for line in lines if line.startswith('WORKFLOW:')]
        
        if workflow_line:
            workflow = 'eplan' if 'eplan' in workflow_line[0].lower() else 'chat'
            content = '\n'.join([line for line in lines if not line.startswith('WORKFLOW:')])
        else:
            workflow = 'chat'
            content = response
        
        return AgentMessage(
            agent_type=AgentType.CONVERSATION,
            content=content.strip(),
            metadata={'workflow': workflow}
        )