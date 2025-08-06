# src/agents/knowledge_agent.py
from .mini_agent import MiniAgent
from ..ai.rag import EplanRAG
from ..core.message_bus import AgentMessage  

class EplanKnowledgeAgent(MiniAgent):
    def __init__(self, message_bus):
        super().__init__("knowledge", message_bus)
        self.rag = EplanRAG()
    
    def get_specialty(self) -> str:
        return "EPLAN electrical software documentation, API examples, code patterns"
    
    async def process_message(self, message: AgentMessage):
        if message.intent == "user_request":
            query = message.payload["query"]
            print(f"KnowledgeAgent searching: {query}")  # Debug

            # RAG search
            results = self.rag.search(query, top_k=2)
            print(f"RAG results: {len(results)} found")  # Debug
            
            if results:
                # Si hay resultados y parece que necesita código, colaborar con CodeCraft
                if self._needs_code_generation(query):
                    await self.send_message(
                        ["codecraft"],
                        "knowledge_for_code",
                        {"examples": results, "user_query": query}
                    )
                else:
                    # Solo documentación
                    content = self._format_knowledge(results)
                    await self.send_message(
                        ["conversation"],
                        "response_to_user",
                        {"content": content}
                    )
    
    async def _needs_code_generation(self, query: str) -> bool:
        prompt = f'Does "{query}" need code generation? YES/NO'
        response = await self.ai_client.generate(prompt)
        return "YES" in response.upper()
    
    def _format_knowledge(self, results) -> str:
        content = "## EPLAN Documentation:\n\n"
        for result in results:
            doc = result['document']
            content += f"**{doc.get('file', 'Unknown')}**: {doc.get('content', '')[:200]}...\n\n"
        return content
    
    
    async def can_handle(self, intent: str) -> float:
        prompt = f"""Does this need EPLAN documentation/examples: "{intent}"?
        Examples needing docs:
        - XAfActionSetting explanation
        - EPLAN API usage
        - Action parameters
        - Code examples
        
        Return 0.9 if yes, 0.1 if no"""
        
        try:
            response = await self.ai_client.generate(prompt)
            return float(response.strip())
        except:
            return 0.1