# eplan_orchestrator.py
import os
import json
import asyncio
from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from enum import Enum
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class AgentType(Enum):
    CONVERSATION = "conversation"
    CODE_GENERATOR = "code_generator"
    PROJECT_MANAGER = "project_manager"
    KNOWLEDGE = "knowledge"
    EXECUTION = "execution"
    FEEDBACK = "feedback"

@dataclass
class AgentMessage:
    agent_type: AgentType
    content: str
    metadata: Optional[Dict] = None

@dataclass
class TaskContext:
    user_query: str
    current_project: Optional[str] = None
    session_history: List[str] = None
    eplan_state: Dict = None

class BaseAgent:
    def __init__(self, orchestrator):
        self.orchestrator = orchestrator
        self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    async def process(self, context: TaskContext) -> AgentMessage:
        raise NotImplementedError

class ConversationAgent(BaseAgent):
    async def process(self, context: TaskContext) -> AgentMessage:
        # Detect intent
        intent_keywords = {
            'code': ['genera', 'crea', 'inserta', 'script', 'macro'],
            'project': ['abre', 'cierra', 'proyecto', 'estado'],
            'question': ['qué', 'cómo', 'cuál', 'help']
        }
        
        query_lower = context.user_query.lower()
        intent = 'question'  # default
        
        for intent_type, keywords in intent_keywords.items():
            if any(keyword in query_lower for keyword in keywords):
                intent = intent_type
                break
        
        response = f"Intent detected: {intent}. Routing to appropriate agents..."
        
        return AgentMessage(
            agent_type=AgentType.CONVERSATION,
            content=response,
            metadata={'intent': intent, 'route_to': self._get_route(intent)}
        )
    
    def _get_route(self, intent: str) -> List[AgentType]:
        routes = {
            'code': [AgentType.KNOWLEDGE, AgentType.CODE_GENERATOR],
            'project': [AgentType.PROJECT_MANAGER, AgentType.EXECUTION],
            'question': [AgentType.KNOWLEDGE]
        }
        return routes.get(intent, [AgentType.KNOWLEDGE])

class CodeGeneratorAgent(BaseAgent):
    async def process(self, context: TaskContext) -> AgentMessage:
        # Get context from knowledge agent
        knowledge_context = await self.orchestrator.get_agent_result(AgentType.KNOWLEDGE, context)
        
        prompt = f"""Generate C# EPLAN Remoting API code for: {context.user_query}

Context: {knowledge_context}

Rules:
- Use ActionCallingContext pattern
- Include error handling
- Make executable
- Return only code block"""

        try:
            response = self.model.generate_content(prompt)
            return AgentMessage(
                agent_type=AgentType.CODE_GENERATOR,
                content=response.text,
                metadata={'ready_for_execution': True}
            )
        except Exception as e:
            return AgentMessage(
                agent_type=AgentType.CODE_GENERATOR,
                content=f"Code generation error: {e}",
                metadata={'ready_for_execution': False}
            )

class ProjectManagerAgent(BaseAgent):
    def __init__(self, orchestrator):
        super().__init__(orchestrator)
        self.project_state = {
            'current_project': None,
            'open_pages': [],
            'recent_macros': [],
            'last_action': None
        }
    
    async def process(self, context: TaskContext) -> AgentMessage:
        # Update context with current state
        state_info = f"""Current EPLAN State:
- Project: {self.project_state['current_project'] or 'None'}
- Open Pages: {len(self.project_state['open_pages'])}
- Last Action: {self.project_state['last_action'] or 'None'}"""
        
        return AgentMessage(
            agent_type=AgentType.PROJECT_MANAGER,
            content=state_info,
            metadata=self.project_state
        )
    
    def update_state(self, action: str, result: Any):
        self.project_state['last_action'] = action
        # Update based on action type
        if 'project' in action.lower():
            self.project_state['current_project'] = result

class KnowledgeAgent(BaseAgent):
    def __init__(self, orchestrator):
        super().__init__(orchestrator)
        # Simplified RAG - in production use full implementation
        self.knowledge_base = {
            'macro': 'Use XMacroInsert with MACRONAME parameter',
            'project': 'Use XPrjActionProjectOpen/Close',
            'page': 'Use XPageCreate with PAGENAME'
        }
    
    async def process(self, context: TaskContext) -> AgentMessage:
        query_lower = context.user_query.lower()
        relevant_info = []
        
        for key, info in self.knowledge_base.items():
            if key in query_lower:
                relevant_info.append(info)
        
        knowledge = "\n".join(relevant_info) if relevant_info else "No specific documentation found"
        
        return AgentMessage(
            agent_type=AgentType.KNOWLEDGE,
            content=knowledge,
            metadata={'sources': list(self.knowledge_base.keys())}
        )

class ExecutionAgent(BaseAgent):
    async def process(self, context: TaskContext) -> AgentMessage:
        # Mock execution - integrate with EPLAN Remoting
        code_result = await self.orchestrator.get_agent_result(AgentType.CODE_GENERATOR, context)
        
        if code_result and 'csharp' in code_result.lower():
            # Simulate execution
            execution_result = "✓ Script executed successfully"
            success = True
        else:
            execution_result = "✗ No valid code to execute"
            success = False
        
        return AgentMessage(
            agent_type=AgentType.EXECUTION,
            content=execution_result,
            metadata={'success': success, 'timestamp': 'now'}
        )

class FeedbackAgent(BaseAgent):
    async def process(self, context: TaskContext) -> AgentMessage:
        # Mock EPLAN log reading
        execution_result = await self.orchestrator.get_agent_result(AgentType.EXECUTION, context)
        
        if execution_result and 'successfully' in execution_result:
            feedback = "EPLAN log shows successful operation. No errors detected."
            suggestions = []
        else:
            feedback = "EPLAN log shows errors. Check ActionCallingContext parameters."
            suggestions = ["Verify macro path", "Check project status", "Review permissions"]
        
        return AgentMessage(
            agent_type=AgentType.FEEDBACK,
            content=feedback,
            metadata={'suggestions': suggestions}
        )

class EplanOrchestrator:
    def __init__(self):
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        
        self.agents = {
            AgentType.CONVERSATION: ConversationAgent(self),
            AgentType.CODE_GENERATOR: CodeGeneratorAgent(self),
            AgentType.PROJECT_MANAGER: ProjectManagerAgent(self),
            AgentType.KNOWLEDGE: KnowledgeAgent(self),
            AgentType.EXECUTION: ExecutionAgent(self),
            AgentType.FEEDBACK: FeedbackAgent(self)
        }
        
        self.agent_results = {}
    
    async def process_user_input(self, user_query: str) -> str:
        context = TaskContext(user_query=user_query)
        
        # 1. Conversation agent determines routing
        conv_result = await self.agents[AgentType.CONVERSATION].process(context)
        route_to = conv_result.metadata.get('route_to', [])
        
        # 2. Execute required agents in sequence
        final_response = []
        
        for agent_type in route_to:
            if agent_type in self.agents:
                result = await self.agents[agent_type].process(context)
                self.agent_results[agent_type] = result
                final_response.append(f"{agent_type.value}: {result.content}")
        
        # 3. Always run feedback if execution happened
        if AgentType.EXECUTION in route_to:
            feedback_result = await self.agents[AgentType.FEEDBACK].process(context)
            final_response.append(f"feedback: {feedback_result.content}")
        
        return "\n\n".join(final_response)
    
    async def get_agent_result(self, agent_type: AgentType, context: TaskContext) -> str:
        if agent_type not in self.agent_results:
            result = await self.agents[agent_type].process(context)
            self.agent_results[agent_type] = result
        
        return self.agent_results[agent_type].content

# Usage
async def main():
    orchestrator = EplanOrchestrator()
    
    print("🤖 EPLAN Multi-Agent System")
    print("Agents: Conversation | Code Generator | Project Manager | Knowledge | Execution | Feedback")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'quit':
            break
        
        response = await orchestrator.process_user_input(user_input)
        print(f"\nSystem:\n{response}")

if __name__ == "__main__":
    asyncio.run(main())