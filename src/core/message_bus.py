# src/core/mesage_bus.py
import asyncio
import time
from typing import Dict, List, Optional
from dataclasses import dataclass

@dataclass
class AgentMessage:
    sender: str
    recipients: List[str]
    intent: str
    payload: dict
    priority: int = 1
    timestamp: float = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = time.time()

class MessageBus:
    def __init__(self):
        self.agents: Dict[str, 'MiniAgent'] = {}
        self.running = True
    
    async def register_agent(self, agent_id: str, agent: 'MiniAgent'):
        self.agents[agent_id] = agent
    
    async def broadcast(self, message: AgentMessage):
        for recipient in message.recipients:
            if recipient in self.agents:
                await self.agents[recipient].receive_message(message)
    
    async def find_capable_agents(self, intent: str) -> List[str]:
        capable = []
        for agent_id, agent in self.agents.items():
            confidence = await agent.can_handle(intent)
            print(f"DEBUG: Agent {agent_id} confidence for '{intent}': {confidence}")
            if confidence > 0.5:
                capable.append((agent_id, confidence))
        return [id for id, _ in sorted(capable, key=lambda x: x[1], reverse=True)]