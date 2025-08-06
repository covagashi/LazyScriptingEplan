# src/agents/project_manager.py
from .base import BaseAgent
from ..orchestrator.types import AgentMessage, TaskContext, AgentType

class ProjectManagerAgent(BaseAgent):
    """Intelligent coordinator - decides which agents to use based on user intent"""
    
    async def process(self, context: TaskContext) -> AgentMessage:
        # AI determines specific EPLAN workflow needed
        workflow_decision = await self._analyze_eplan_workflow(context.user_query)
        
        if workflow_decision == 'script_generation':
            return await self._handle_script_generation(context)
        elif workflow_decision == 'execution':
            return await self._handle_execution_workflow(context)
        elif workflow_decision == 'knowledge':
            return await self._handle_knowledge_workflow(context)
        else:
            # Unclear intent - ask user for clarification
            return await self._ask_for_clarification(context)
    
    async def _analyze_eplan_workflow(self, user_query: str) -> str:
        """AI determines specific EPLAN workflow"""
        prompt = f"""User needs EPLAN help. Determine exact workflow:

Query: "{user_query}"

Choose ONE:
- script_generation: wants script created/generated
- execution: wants to run/execute something in EPLAN  
- knowledge: needs EPLAN documentation/info
- unclear: ambiguous, need clarification

Answer only the category."""
        
        try:
            response = await self.ai_client.generate(prompt)
            return response.strip().lower()
        except:
            return 'unclear'
    
    async def _ask_for_clarification(self, context: TaskContext) -> AgentMessage:
        """Ask user to clarify their intent"""
        return AgentMessage(
            agent_type=AgentType.PROJECT_MANAGER,
            content="Puedo ayudarte con EPLAN de varias formas:\n\n• **Generar script**: Crear código C# para EPLAN\n• **Ejecutar**: Correr acciones en EPLAN\n• **Consultar**: Buscar documentación EPLAN\n\n¿Qué necesitas específicamente?",
            metadata={'needs_clarification': True}
        )
    
    async def _handle_script_generation(self, context: TaskContext) -> AgentMessage:
        """Handle script generation requests"""
        code_result = await self.get_peer_result(AgentType.CODE_GENERATOR)
        code_content = code_result.content if hasattr(code_result, 'content') else str(code_result)
        code_metadata = code_result.metadata if hasattr(code_result, 'metadata') else {}
        
        return AgentMessage(
            agent_type=AgentType.PROJECT_MANAGER,
            content=f"📝 Script Generation:\n\n{code_content}",
            metadata={
                'workflow': 'script_generation',
                'script_ready': code_metadata.get('ready_for_execution', False),
                'action_name': code_metadata.get('action_detected', 'Unknown')
            }
        )
    
    async def _handle_knowledge_workflow(self, context: TaskContext) -> AgentMessage:
        """Handle EPLAN knowledge/documentation queries"""
        knowledge_result = await self.get_peer_result(AgentType.KNOWLEDGE)
        knowledge_content = knowledge_result.content if hasattr(knowledge_result, 'content') else str(knowledge_result)
        
        return AgentMessage(
            agent_type=AgentType.PROJECT_MANAGER,
            content=knowledge_content,
            metadata={'workflow': 'knowledge'}
        )
    
    async def _handle_execution_workflow(self, context: TaskContext) -> AgentMessage:
        """Handle execution requests - coordinates multiple agents"""
        # Get script first
        code_result = await self.get_peer_result(AgentType.CODE_GENERATOR)
        code_metadata = code_result.metadata if hasattr(code_result, 'metadata') else {}
        
        if not code_metadata.get('ready_for_execution'):
            return AgentMessage(
                agent_type=AgentType.PROJECT_MANAGER,
                content="❌ Cannot execute - script generation failed",
                metadata={'workflow': 'execution', 'script_ready': False}
            )
        
        # Execute via ExecutionAgent
        exec_result = await self.get_peer_result(AgentType.EXECUTION)
        
        # Get feedback
        feedback_result = await self.get_peer_result(AgentType.FEEDBACK)
        
        exec_content = exec_result.content if hasattr(exec_result, 'content') else str(exec_result)
        feedback_content = feedback_result.content if hasattr(feedback_result, 'content') else str(feedback_result)
        exec_metadata = exec_result.metadata if hasattr(exec_result, 'metadata') else {}
        
        return AgentMessage(
            agent_type=AgentType.PROJECT_MANAGER,
            content=f"⚡ Execution Result:\n\n{exec_content}\n\n📊 Feedback:\n{feedback_content}",
            metadata={
                'workflow': 'execution',
                'execution_success': exec_metadata.get('success', False)
            }
        )