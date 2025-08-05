# src/agents/conversation.py
from typing import List, Dict
from .base import BaseAgent
from ..orchestrator.types import AgentMessage, TaskContext, AgentType

class ConversationAgent(BaseAgent):
    """Natural conversation with EPLAN agent capabilities"""
    
    def __init__(self, orchestrator):
        super().__init__(orchestrator)
        self.messages = {
            'en': {
                'query_prep': "Working on your EPLAN query...",
                'default_help': "How can I help you?"
            },
            'es': {
                'query_prep': "Trabajando en tu consulta EPLAN...",
                'default_help': "¿En qué te puedo ayudar?"
            }
        }
    
    def detect_language(self, text: str) -> str:
        spanish_words = ['qué', 'cómo', 'cuál', 'hace', 'busca', 'para']
        return 'es' if any(w in text.lower() for w in spanish_words) else 'en'
    
    async def process(self, context: TaskContext) -> AgentMessage:
        lang = self.detect_language(context.user_query)
        query_lower = context.user_query.lower()
        
        # Check for EPLAN-related content
        eplan_keywords = ['eplan', 'project', 'projectopen', 'macro', 'busca']
        is_eplan_related = any(keyword in query_lower for keyword in eplan_keywords)
        
        if not is_eplan_related:
            return AgentMessage(
                agent_type=AgentType.CONVERSATION,
                content=self.messages[lang]['default_help'],
                metadata={'workflow': 'chat', 'language': lang}
            )
        
        # All EPLAN queries go through ProjectManager
        return AgentMessage(
            agent_type=AgentType.CONVERSATION,
            content=self.messages[lang]['query_prep'],
            metadata={'workflow': 'eplan', 'language': lang}
        )