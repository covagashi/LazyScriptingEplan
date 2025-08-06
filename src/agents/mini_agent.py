# src/agents/mini_agent.py
import asyncio
import time
from abc import ABC, abstractmethod
from typing import List  
from ..ai import GeminiClient
from ..core.message_bus import MessageBus, AgentMessage

class MiniAgent(ABC):
    def __init__(self, agent_id: str, message_bus: MessageBus):
        self.id = agent_id
        self.bus = message_bus
        self.ai_client = GeminiClient()
        self.working = False
        self.message_queue = asyncio.Queue()
    
    async def can_handle(self, intent: str) -> float:
        prompt = f"""Can I help with: "{intent}"?
My specialty: {self.get_specialty()}
Return only 0.0-1.0"""
        
        try:
            response = await self.ai_client.generate(prompt)
            return float(response.strip())
        except:
            return 0.0
    
    async def receive_message(self, message: AgentMessage):
        await self.message_queue.put(message)
        if not self.working:
            asyncio.create_task(self._process_queue())
    
    async def _process_queue(self):
        self.working = True
        try:
            while not self.message_queue.empty():
                message = await self.message_queue.get()
                await self.process_message(message)
        finally:
            self.working = False
    
    async def send_message(self, recipients: List[str], intent: str, payload: dict):
        message = AgentMessage(
            sender=self.id,
            recipients=recipients,
            intent=intent,
            payload=payload
        )
        await self.bus.broadcast(message)
    
    @abstractmethod
    async def process_message(self, message: AgentMessage):
        pass
    
    @abstractmethod
    def get_specialty(self) -> str:
        pass