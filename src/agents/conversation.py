# src/agents/conversation.py
from typing import List, Dict
from .base import BaseAgent
from ..orchestrator.types import AgentMessage, TaskContext, AgentType

class ConversationAgent(BaseAgent):
    """Natural conversation with EPLAN agent capabilities - Multilingual"""
    
    def __init__(self, orchestrator):
        super().__init__(orchestrator)
        self.messages = {
            'en': {
                'missing_params': "❓ Need more information. Missing parameters: {}",
                'execution_prep': "Understood. Preparing EPLAN execution...",
                'generation_prep': "Understood. Generating EPLAN code...",
                'query_prep': "Understood. Working on your EPLAN query...",
                'default_help': "How can I help you?",
                'error': "How can I help you? (Error: {})"
            },
            'es': {
                'missing_params': "❓ Necesito más información. Parámetros faltantes: {}",
                'execution_prep': "Entendido. Preparando ejecución en EPLAN...",
                'generation_prep': "Entendido. Generando código EPLAN...",
                'query_prep': "Entendido. Trabajando en tu consulta EPLAN...",
                'default_help': "¿En qué te puedo ayudar?",
                'error': "¿En qué te puedo ayudar? (Error: {})"
            }
        }
    
    def detect_language(self, text: str) -> str:
        """Simple language detection"""
        spanish_words = ['qué', 'cómo', 'cuál', 'dónde', 'cuándo', 'por', 'para', 'con', 'sin', 'sobre', 'entre', 'hasta', 'desde', 'hacia', 'según', 'durante', 'mediante', 'contra', 'ante', 'bajo', 'tras', 'español', 'ayuda', 'hola', 'gracias']
        
        text_lower = text.lower()
        spanish_count = sum(1 for word in spanish_words if word in text_lower)
        
        return 'es' if spanish_count > 0 else 'en'
    
    def get_message(self, key: str, lang: str, *args) -> str:
        """Get localized message"""
        return self.messages[lang][key].format(*args)
    
    async def process(self, context: TaskContext) -> AgentMessage:
        # Detect language
        lang = self.detect_language(context.user_query)
        
        # Analyze user intent with Gemini
        analysis_prompt = f"""Analyze this user message: "{context.user_query}"

Language detected: {lang}

Is this related to EPLAN electrical engineering software?
- EPLAN projects, macros, device lists, schematics  
- NOT Excel macros, general programming, other topics

If EPLAN-related, what's the intent?
- question: asking WHAT something does, HOW something works (informational)
- generation: wants CODE/SCRIPT to be created
- execution: wants to RUN/EXECUTE something in EPLAN

Key indicators:
- "¿qué hace?", "what does", "como funciona" = question  
- "genera", "crea script", "create code" = generation
- "ejecuta", "run", "hacer ahora" = execution

If NOT EPLAN-related, respond conversationally in {lang}.

Response format:
EPLAN_RELATED: yes/no
INTENT: execution/generation/question/chat
RESPONSE: [your response in {lang}]"""

        try:
            analysis = await self.ai_client.generate(analysis_prompt)
            
            # Parse response
            lines = analysis.strip().split('\n')
            eplan_related = False
            intent = 'chat'
            ai_response = self.get_message('default_help', lang)
            
            for line in lines:
                if line.startswith('EPLAN_RELATED:'):
                    eplan_related = 'yes' in line.lower()
                elif line.startswith('INTENT:'):
                    intent = line.split(':', 1)[1].strip().lower()
                elif line.startswith('RESPONSE:'):
                    ai_response = line.split(':', 1)[1].strip()
            
            # If not EPLAN-related, return conversational response
            if not eplan_related:
                return AgentMessage(
                    agent_type=AgentType.CONVERSATION,
                    content=ai_response,
                    metadata={'workflow': 'chat', 'route_to': [], 'language': lang}
                )
            
            # EPLAN-related workflow routing
            if intent == 'execution':
                workflow = 'execution'
                route_to = [AgentType.PROJECT_MANAGER]
                response = self.get_message('execution_prep', lang)
            elif intent == 'generation':
                workflow = 'generation'
                route_to = [AgentType.CODE_GENERATOR]
                response = self.get_message('generation_prep', lang)
            elif intent == 'question':
                workflow = 'info'
                route_to = []  # Only Knowledge agent (already executed by orchestrator)
                response = self.get_message('query_prep', lang)
            else:
                workflow = 'generation'
                route_to = [AgentType.CODE_GENERATOR]
                response = self.get_message('query_prep', lang)
            
            return AgentMessage(
                agent_type=AgentType.CONVERSATION,
                content=response,
                metadata={'workflow': workflow, 'route_to': route_to, 'language': lang}
            )
            
        except Exception as e:
            # Fallback for AI errors
            return AgentMessage(
                agent_type=AgentType.CONVERSATION,
                content=self.get_message('error', lang, str(e)),
                metadata={'workflow': 'chat', 'route_to': [], 'language': lang}
            )