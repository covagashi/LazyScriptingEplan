# src/agents/conversation_agent.py
import time
import asyncio
from .mini_agent import MiniAgent
from ..core.message_bus import AgentMessage

class ConversationAgent(MiniAgent):
    def __init__(self, message_bus):
        super().__init__("conversation", message_bus)
        self.user_response = None
    
    def get_specialty(self) -> str:
        return "Natural conversation, user intent detection"
    
    async def handle_user_input(self, user_query: str) -> str:
        # Try direct response first
        direct_response = await self._try_direct_response(user_query)
        if direct_response:
            return direct_response
        
        # Debug: Check which agents are capable
        capable_agents = await self.bus.find_capable_agents(user_query)
        print(f"DEBUG: Query '{user_query}' -> Capable agents: {capable_agents}")
        
        if not capable_agents:
            return "What can I help you with EPLAN?"
        
        await self.send_message(
            capable_agents,
            "user_request",
            {"query": user_query, "requester": "user"}
        )
        
        # wait answers
        response_timeout = 10  # seconds
        start_time = time.time()
        
        while time.time() - start_time < response_timeout:
            if self.user_response:
                result = self.user_response
                self.user_response = None
                return result
            await asyncio.sleep(0.1)
        
        return "Timeout esperando respuesta de agentes"
    
    async def _try_direct_response(self, query: str) -> str:
        prompt = f"""User query: "{query}"
        
        If this is about:
        - EPLAN electrical actions
        - EPLAN electrical technical features
        - Code script eplan electrical generation
        - EPLAN electrical documentation
        Return: "DELEGATE"
        
        If this is general conversation/greeting, respond naturally.
        """
        
        response = await self.ai_client.generate(prompt)
        return None if "DELEGATE" in response else response
    
    async def process_message(self, message: AgentMessage):
        if message.intent == "response_to_user":
            self.user_response = message.payload.get("content", "No answer")

   
    async def can_handle(self, intent: str) -> float:
        prompt = f"""Query: "{intent}"
        
        I handle general conversation about Eplan 2023 electrical software.
        
        If this asks about:
        - Technical API actions.
        - Code generation 
        - Documentation lookup
        Return: 0.1
        
        If this is:
        - Greeting/chat
        - General software questions
        Return: 0.5
        
        Number only:"""
        
        try:
            response = await self.ai_client.generate(prompt)
            return float(response.strip())
        except:
            return 0.1