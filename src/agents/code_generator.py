# src/agents/code_generator.py
import os
from .base import BaseAgent
from ..orchestrator.types import AgentMessage, TaskContext, AgentType

class CodeGeneratorAgent(BaseAgent):
    """AI-driven C# EPLAN script generator using RAG knowledge"""
    
    def __init__(self, orchestrator):
        super().__init__(orchestrator)
        self.output_dir = r"C:\temp\Agent"
        os.makedirs(self.output_dir, exist_ok=True)
    
    async def process(self, context: TaskContext) -> AgentMessage:
        print(f"DEBUG CodeGenerator: Processing query: {context.user_query}")
        
        try:
            # Get RAG knowledge first
            knowledge_result = await self.get_peer_result(AgentType.KNOWLEDGE)
            print(f"DEBUG CodeGenerator: Knowledge result type: {type(knowledge_result)}")
            print(f"DEBUG CodeGenerator: Knowledge content: {str(knowledge_result)[:200]}...")
            
            knowledge_content = knowledge_result.content if hasattr(knowledge_result, 'content') else str(knowledge_result)
            
            # AI-driven script generation
            result = await self._generate_script_with_ai(context.user_query, knowledge_content)
            print(f"DEBUG CodeGenerator: Final result type: {type(result)}")
            return result
            
        except Exception as e:
            print(f"DEBUG CodeGenerator: ERROR: {e}")
            return AgentMessage(
                agent_type=AgentType.CODE_GENERATOR,
                content=f"❌ Error in CodeGenerator: {e}",
                metadata={'ready_for_execution': False}
            )
    
    async def _generate_script_with_ai(self, user_query: str, knowledge_content: str) -> AgentMessage:
        """Use AI to understand user intent and generate appropriate EPLAN script"""
        
        # AI determines if user wants execution or just generation
        execution_intent = await self._detect_execution_intent(user_query)
        
        prompt = f"""Generate EPLAN C# script based on user request and available examples.

USER REQUEST: {user_query}

EPLAN KNOWLEDGE BASE:
{knowledge_content}

Use the examples from the knowledge base to create the appropriate script structure and format. Follow the patterns shown in the documentation."""

        try:
            print("DEBUG CodeGenerator: Calling AI...")
            ai_response = await self.ai_client.generate(prompt)
            print(f"DEBUG CodeGenerator: AI response: {ai_response[:200]}...")
            
            script = self._extract_code_block(ai_response)
            if not script:
                script = ai_response.strip()
            
            validated_script = self._validate_script(script)
            
            # Save only if execution intent detected
            filename = None
            if execution_intent:
                filename = self._save_script(validated_script)
                print(f"DEBUG CodeGenerator: Script saved to: {filename}")
            
            return AgentMessage(
                agent_type=AgentType.CODE_GENERATOR,
                content=f"✅ Script generated:\n\n```csharp\n{validated_script}\n```" + 
                        (f"\n\n📁 Saved: {filename}" if filename else ""),
                metadata={
                    'ready_for_execution': bool(filename),
                    'saved_to': filename,
                    'action_detected': "Hello_World_MessageBox"
                }
            )
            
        except Exception as e:
            print(f"DEBUG CodeGenerator: AI generation error: {e}")
            return AgentMessage(
                agent_type=AgentType.CODE_GENERATOR,
                content=f"❌ Error generating script: {e}",
                metadata={'ready_for_execution': False}
            )
    
    async def _detect_execution_intent(self, query: str) -> bool:
        """Detect if user wants to execute the script"""
        prompt = f"""Does the user want to EXECUTE/RUN the script in EPLAN?

Query: "{query}"

Answer YES if they want to run/execute it.
Answer NO if they just want to see/create the script.

Answer only: YES or NO"""
        
        try:
            response = await self.ai_client.generate(prompt)
            return 'YES' in response.upper()
        except:
            return False
    
    def _save_script(self, script: str) -> str:
        """Save script ready for EPLAN execution"""
        filename = "hello_world_script.cs"
        filepath = os.path.join(self.output_dir, filename)
        
        # Ensure proper EPLAN using statements
        full_script = self._add_using_statements(script)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(full_script)
        
        return filepath
    
    def _add_using_statements(self, script: str) -> str:
        """Add required EPLAN using statements"""
        if 'using Eplan' not in script:
            using_statements = """using Eplan.EplApi.ApplicationFramework;
using Eplan.EplApi.Scripting;
using Eplan.EplApi.Base;

"""
            script = using_statements + script
        
        return script
    
    def _validate_script(self, script: str) -> str:
        """Validate and ensure proper EPLAN script structure"""
        # Only ensure [Start] attribute if missing
        if '[Start]' not in script:
            script = '[Start]\n' + script
        
        return script
    
    def _extract_code_block(self, response: str) -> str:
        """Extract C# code from AI response"""
        if '```csharp' in response:
            start = response.find('```csharp') + 9
            end = response.find('```', start)
            return response[start:end].strip() if end != -1 else ""
        elif '```' in response:
            start = response.find('```') + 3
            end = response.find('```', start)
            return response[start:end].strip() if end != -1 else ""
        return response.strip()