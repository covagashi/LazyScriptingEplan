# src/agents/base.py
from abc import ABC, abstractmethod
from ..orchestrator.types import AgentMessage, TaskContext, AgentType
from ..ai import GeminiClient

class BaseAgent(ABC):
    """Base class for all EPLAN AI agents"""
    
    def __init__(self, orchestrator):
        self.orchestrator = orchestrator
        self.ai_client = GeminiClient()
    
    @abstractmethod
    async def process(self, context: TaskContext) -> AgentMessage:
        """Process task context and return agent message"""
        pass
    
    async def get_peer_result(self, agent_type: AgentType) -> str:
        """Get result from another agent"""
        result = await self.orchestrator.get_agent_result(agent_type)
        return result.content if result else ""