# src/agents/code_generator.py
import os
from .base import BaseAgent
from ..orchestrator.types import AgentMessage, TaskContext, AgentType

class CodeGeneratorAgent(BaseAgent):
    """Generates C# EPLAN Remoting API code"""
    
    def __init__(self, orchestrator):
        super().__init__(orchestrator)
        self.output_dir = r"C:\temp\Agent"
        os.makedirs(self.output_dir, exist_ok=True)
    
    async def process(self, context: TaskContext) -> AgentMessage:
        # Get knowledge context
        knowledge_context = await self.get_peer_result(AgentType.KNOWLEDGE)
        
        prompt = f"""Generate C# EPLAN script: {context.user_query}

Knowledge Context: {knowledge_context}

Requirements:
- Use ActionCallingContext pattern
- Include error handling
- Make executable
- Return clean code block

Example format:
```csharp
using Eplan.EplApi.Remoting;

ActionCallingContext ctx = new ActionCallingContext();
ctx.AddParameter("PARAMETER", "value");
new CommandLineInterpreter().Execute("ACTION_NAME", ctx);
```"""

        try:
            response = await self.ai_client.generate(prompt)
            
            # Extract code block
            code = self._extract_code_block(response)
            
            # Save to file
            if code:
                filename = self._save_code(code, context.user_query)
            
            return AgentMessage(
                agent_type=AgentType.CODE_GENERATOR,
                content=code,
                metadata={
                    'ready_for_execution': bool(code),
                    'action_detected': self._detect_action(code),
                    'saved_to': filename if code else None
                }
            )
        except Exception as e:
            return AgentMessage(
                agent_type=AgentType.CODE_GENERATOR,
                content=f"Code generation failed: {e}",
                metadata={'ready_for_execution': False}
            )
    
    def _save_code(self, code: str, user_query: str) -> str:
        """Save generated code to C:\temp\Agent"""
        filename = "eplan_script.cs"
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"// Generated for: {user_query}\n\n")
            f.write(code)
        
        return filepath
    
    def _extract_code_block(self, response: str) -> str:
        """Extract C# code from response"""
        if '```csharp' in response:
            start = response.find('```csharp') + 9
            end = response.find('```', start)
            return response[start:end].strip() if end != -1 else ""
        return response.strip()
    
    def _detect_action(self, code: str) -> str:
        """Detect EPLAN action from code"""
        # Parse action from ExecuteAction calls
        lines = code.split('\n')
        for line in lines:
            if 'ExecuteAction' in line and '"' in line:
                start = line.find('"') + 1
                end = line.find('"', start)
                if end > start:
                    return line[start:end]
        return "Unknown"