# src/agents/codecraft_agent.py
import os
from .mini_agent import MiniAgent
from ..core.message_bus import AgentMessage
from ..ai.script_rag import ScriptRAG

class CodeCraftAgent(EnhancedMiniAgent):
    def __init__(self, message_bus):
        super().__init__("codecraft", message_bus)
        self.output_dir = Path(r"C:\temp\Agent")
        self.output_dir.mkdir(exist_ok=True)
        self.script_rag = ScriptRAG()
        
        # Specific routing for generate code
        self._setup_custom_routing()
    
    def _setup_custom_routing(self):
        """Routing específico para CodeCraftAgent"""
        custom_keywords = {
            "high_confidence": [
                "generate script", "create script", "write code", "c# script",
                "eplan script", "script generation", "code generation",
                "programming", "create code", "write program"
            ],
            "medium_confidence": [
                "script", "code", "c#", "generate", "create", "programming",
                "implementation", "develop"
            ],
            "low_confidence": [
                "just explain", "only documentation", "theory only",
                "no code", "execute", "run only"
            ]
        }
        
        self.router.agent_keywords["codecraft"] = custom_keywords
    
    def get_specialty(self) -> str:
        return "C# EPLAN 2025 electrical software script generation, code validation"
    
    async def _get_current_capabilities(self) -> str:
        """Current capabilities considering ScriptRAG"""
        script_count = len(self.script_rag.scripts) if hasattr(self.script_rag, 'scripts') else 0
        return f"Script RAG loaded ({script_count} examples), C# generation, EPLAN API"
    
    async def can_handle(self, intent: str) -> float:
        """Routing específico para generación de código"""
        
        # Definitive cases for CodeCraft
        code_patterns = [
            "generate script", "create code", "write script", "c# code",
            "programming", "code generation"
        ]
        
        intent_lower = intent.lower()
        for pattern in code_patterns:
            if pattern in intent_lower:
                return 0.95
        
        # Hibrid system
        base_confidence, method = await self.hybrid_handler.can_handle(intent, self.get_specialty())
        
        # Boost if code terms are mentioned
        programming_terms = ["script", "code", "c#", "generate", "create"]
        boost = sum(0.05 for term in programming_terms if term in intent_lower)
        
        final_confidence = min(1.0, base_confidence + boost)
        
        await self.log_to_scratchpad(
            f"CodeCraft routing: {final_confidence:.2f} (base: {base_confidence:.2f}, boost: {boost:.2f})",
            "routing"
        )
                
        return final_confidence
    

