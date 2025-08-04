# src/orchestrator/core.py
import os
import asyncio
from typing import Dict, List, Optional
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
        """Initialize Gemini AI"""
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    def register_agent(self, agent_type: AgentType, agent: 'BaseAgent'):
        """Register an agent with the orchestrator"""
        self.agents[agent_type] = agent
    
    async def process_user_input(self, user_query: str) -> str:
        """Main entry point for processing user requests"""
        self.session_context.user_query = user_query
        self.session_context.agent_results.clear()  # Clear previous results
        
        try:
            # 1. Start with Conversation agent to determine workflow
            conv_result = await self._execute_agent(AgentType.CONVERSATION)
            workflow = conv_result.metadata.get('workflow', 'chat')
            
            # 2. Handle simple chat (non-EPLAN)
            if workflow == 'chat':
                return conv_result.content
            
            # 3. For EPLAN workflows, check knowledge first
            knowledge_result = await self._execute_agent(AgentType.KNOWLEDGE)
            
            # 4. Handle clarification workflow
            if knowledge_result.metadata.get('needs_clarification'):
                missing_params = knowledge_result.metadata.get('missing_params', [])
                return f"❓ Need more information. Missing parameters: {', '.join(missing_params)}\n\n{knowledge_result.content}"
            
            # 5. Handle execution workflow
            if workflow == 'execution':
                pm_result = await self._execute_agent(AgentType.PROJECT_MANAGER)
                
                if pm_result.metadata.get('script_ready'):
                    exec_result = await self._execute_agent(AgentType.EXECUTION)
                    feedback_result = await self._execute_agent(AgentType.FEEDBACK)
                    
                    pm_agent = self.agents[AgentType.PROJECT_MANAGER]
                    conclusion = await pm_agent.process_feedback(feedback_result)
                    
                    return f"{conv_result.content}\n\n{pm_result.content}\n\n{exec_result.content}\n\n{feedback_result.content}\n\n{conclusion}"
                else:
                    return f"{conv_result.content}\n\n{pm_result.content}"
            
            # 6. Handle generation workflow
            else:
                route_plan = conv_result.metadata.get('route_to', [])
                responses = [conv_result.content]
                
                for agent_type in route_plan:
                    if agent_type != AgentType.KNOWLEDGE:  # Already executed
                        result = await self._execute_agent(agent_type)
                        responses.append(result.content)
                
                return "\n\n".join(responses)
            
        except Exception as e:
            return f"System error: {e}"
    
    async def _execute_agent(self, agent_type: AgentType) -> AgentMessage:
        """Execute a specific agent and cache result"""
        if agent_type not in self.agents:
            return AgentMessage(
                agent_type=agent_type,
                content=f"Agent {agent_type.value} not registered",
                status=TaskStatus.FAILED
            )
        
        if agent_type in self.session_context.agent_results:
            return self.session_context.agent_results[agent_type]
        
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
        """Get cached result from specific agent"""
        if agent_type in self.session_context.agent_results:
            return self.session_context.agent_results[agent_type]
                
        return await self._execute_agent(agent_type)
    
    def clear_session(self):
        """Clear current session context"""
        self.session_context = TaskContext(user_query="")
    
    def get_session_history(self) -> List[str]:
        """Get current session history"""
        return self.session_context.session_history