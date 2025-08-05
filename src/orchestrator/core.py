# src/orchestrator/core.py
import os
from typing import Dict, Optional
import google.generativeai as genai
from dotenv import load_dotenv
from .types import AgentType, AgentMessage, TaskContext, TaskStatus

load_dotenv()

class EplanOrchestrator:
    """Main orchestrator for EPLAN AI Agent system"""
    
    def __init__(self):
        self._setup_ai()
        self.agents: Dict[AgentType, 'BaseAgent'] = {}
        self.session_context = TaskContext(user_query="")
        
    def _setup_ai(self):
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    def register_agent(self, agent_type: AgentType, agent: 'BaseAgent'):
        self.agents[agent_type] = agent
    
    async def process_user_input(self, user_query: str) -> str:
        self.session_context.user_query = user_query
        self.session_context.agent_results.clear()
        
        try:
            # 1. Get conversation classification
            conv_result = await self._execute_agent(AgentType.CONVERSATION)
            workflow = conv_result.metadata.get('workflow', 'chat')
            
            # 2. Handle non-EPLAN chat
            if workflow == 'chat':
                return conv_result.content
            
            # 3. Handle EPLAN queries through ProjectManager
            pm_result = await self._execute_agent(AgentType.PROJECT_MANAGER)
            return f"{conv_result.content}\n\n{pm_result.content}"
            
        except Exception as e:
            return f"Error: {e}"
    
    async def _execute_agent(self, agent_type: AgentType) -> AgentMessage:
        if agent_type not in self.agents:
            return AgentMessage(
                agent_type=agent_type,
                content=f"Agent {agent_type.value} not found",
                status=TaskStatus.FAILED
            )
        
        # Check cache
        if agent_type in self.session_context.agent_results:
            return self.session_context.agent_results[agent_type]
        
        # Execute and cache
        try:
            result = await self.agents[agent_type].process(self.session_context)
            self.session_context.agent_results[agent_type] = result
            return result
        except Exception as e:
            error_result = AgentMessage(
                agent_type=agent_type,
                content=f"Agent error: {e}",
                status=TaskStatus.FAILED
            )
            self.session_context.agent_results[agent_type] = error_result
            return error_result
    
    async def get_agent_result(self, agent_type: AgentType) -> Optional[AgentMessage]:
        if agent_type in self.session_context.agent_results:
            return self.session_context.agent_results[agent_type]
        return await self._execute_agent(agent_type)