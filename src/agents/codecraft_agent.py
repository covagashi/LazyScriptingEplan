# src/agents/codecraft_agent.py
import os
from .mini_agent import MiniAgent
from ..core.message_bus import AgentMessage

class CodeCraftAgent(MiniAgent):
    def __init__(self, message_bus):
        super().__init__("codecraft", message_bus)
        self.output_dir = r"C:\temp\Agent"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def get_specialty(self) -> str:
        return "C# EPLAN electrical software script generation, code validation"
    
    async def process_message(self, message: AgentMessage):
        if message.intent in ["user_request", "knowledge_for_code"]:
            query = message.payload.get("query") or message.payload.get("user_query")
            examples = message.payload.get("examples", [])
            
            # Generar código con IA
            script = await self._generate_script(query, examples)
            
            # Decidir si ejecutar o solo mostrar
            should_execute = await self._should_execute(query)
            
            if should_execute:
                filename = self._save_script(script)
                await self.send_message(
                    ["execution"],
                    "execute_script",
                    {"script_path": filename, "action_name": "GeneratedScript"}
                )
            else:
                # Solo mostrar
                await self.send_message(
                    ["conversation"],
                    "response_to_user",
                    {"content": f"✅ Script generado:\n\n```csharp\n{script}\n```"}
                )
    
    async def _generate_script(self, query: str, examples: list) -> str:
        context = ""
        for ex in examples:
            context += f"{ex['document']['content'][:400]}...\n\n"
        
        prompt = f"""Generate EPLAN C# script:
Query: {query}
Examples: {context}
Return only the C# code."""
        
        return await self.ai_client.generate(prompt)
    
    async def _should_execute(self, query: str) -> bool:
        prompt = f'Does "{query}" want to EXECUTE the script? YES/NO'
        response = await self.ai_client.generate(prompt)
        return "YES" in response.upper()
    
    def _save_script(self, script: str) -> str:
        filepath = os.path.join(self.output_dir, "generated_script.cs")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"using Eplan.EplApi.Scripting;\n{script}")
        return filepath