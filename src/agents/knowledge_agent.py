# src/agents/updated_knowledge_agent.py
from .mini_agent import EnhancedMiniAgent
from ..ai.documentation_rag import DocumentationRAG
from ..core.message_bus import AgentMessage
from ..core.agent_routing import DeterministicRouter, HybridCanHandle

class EplanKnowledgeAgent(EnhancedMiniAgent):
    def __init__(self, message_bus):
        super().__init__("knowledge", message_bus)
        self.doc_rag = DocumentationRAG() 
        
        # Routing específico para KnowledgeAgent
        self._setup_custom_routing()
    
    def _setup_custom_routing(self):
        """Configure specific routing for EPLAN documentation"""
        # Añadir keywords específicos de documentación
        custom_keywords = {
            "high_confidence": [
                "eplan action", "eplan api reference", "action parameters", "namespace"
                "eplan documentation", "api examples", "how to use eplan",
                "eplan commands", "eplan actions", "electrical documentation"
            ],
            "medium_confidence": [
                "eplan", "electrical", "api", "documentation", "examples",
                "reference", "guide", "manual", "help"
            ],
            "low_confidence": [
                "execute", "run script", "generate code", "create file",
                "only code", "just script"
            ]
        }
        
        # Actualizar el router con keywords específicos
        self.router.agent_keywords["knowledge"] = custom_keywords
    
    def get_specialty(self) -> str:
        return "EPLAN electrical software documentation, API examples, code patterns"
    
    async def _get_current_capabilities(self) -> str:
        """Current capacities considering RAG status"""
        doc_count = len(self.doc_rag.docs) if hasattr(self.doc_rag, 'docs') else 0
        rag_status = "loaded" if doc_count > 0 else "loading"
        return f"Documentation RAG {rag_status} ({doc_count} docs), API reference search"
    
    async def process_message_with_context(self, message: AgentMessage, contexts: Dict[str, Any]):
        """Improved processing with resolved context"""
        
        if message.intent in ["enhanced_user_request", "knowledge_request"]:
            # Get query from message or context
            query = message.payload.get("query", "")
            
            enriched_context = None
            for context_data in contexts.values():
                if "user_query" in context_data:
                    query = context_data["user_query"]
                    enriched_context = context_data
                    break
            
            await self.log_to_scratchpad(f"Processing knowledge request: {query[:100]}", "processing")
            
            results = self.doc_rag.search_documentation(query, top_k=3)
            
            if results:
                needs_code = await self._analyze_code_needs(query, enriched_context)
                
                if needs_code:
                    await self._collaborate_with_codecraft(query, results, enriched_context)
                else:
                    content = self._format_knowledge_response(results, query)
                    await self._send_direct_response(content, message)
            else:
                await self._send_no_results_response(query, message)
    
    async def _analyze_code_needs(self, query: str, context: Dict = None) -> bool:
        """Determine if the query needs code generation"""
        
        code_indicators = [
            "generate", "create script", "write code", "script for",
            "code example", "implementation", "programming"
        ]
        
        query_lower = query.lower()
        if any(indicator in query_lower for indicator in code_indicators):
            return True
        
        if context and "intent_analysis" in context:
            intent = context["intent_analysis"]
            if intent.get("primary_intent") == "code_generation":
                return True
        
        # LLM fallback for ambiguous cases
        prompt = f"""Does this query need code generation?

Query: "{query}"
Context: {context.get('conversation_context', 'None') if context else 'None'}

Code indicators: script, generate, create, implementation
Documentation indicators: explain, what is, how to, documentation

Answer YES or NO:"""
        
        try:
            response = await self.ai_client.generate(prompt)
            return "YES" in response.upper()
        except:
            return False
    
    async def _collaborate_with_codecraft(self, query: str, knowledge_results: List, context: Dict):
        """Collaborate with CodeCraftAgent to generate code"""
        
        collaboration_context = {
            "original_query": query,
            "knowledge_results": knowledge_results,
            "conversation_context": context.get("conversation_context") if context else None,
            "requester": "knowledge_via_user"
        }
        
        await self.send_message(
            ["codecraft"],
            "knowledge_for_code",
            {
                "user_query": query,
                "examples_count": len(knowledge_results),
                "collaboration_type": "knowledge_assisted_generation"
            },
            heavy_context=collaboration_context,
            context_metadata={"type": "knowledge_collaboration"}
        )
        
        await self.log_to_scratchpad(
            f"Collaborated with CodeCraft for: {query[:50]}",
            "collaboration"
        )
    
    async def _send_direct_response(self, content: str, original_message: AgentMessage):
        """Send direct response to the user"""
        
        await self.send_message(
            ["conversation"],
            "response_to_user",
            {
                "content": content,
                "source": "knowledge_agent",
                "request_id": original_message.payload.get("request_id")
            }
        )
    
    def _format_knowledge_response(self, results: List, query: str) -> str:
        """Format documentation response"""
        
        content = f"## EPLAN Documentation for: {query}\n\n"
        
        for i, result in enumerate(results[:3], 1):
            doc = result['document']
            score = result['score']
            item = doc.get('item', {})
            
            content += f"### {i}. {item.get('name', 'Documentation')}\n"
            if 'description' in item:
                content += f"**Description:** {item['description']}\n\n"
            
            if 'parameters' in item and item['parameters']:
                content += "**Parameters:**\n"
                for param in item['parameters'][:3]:  # Limit parameters
                    if isinstance(param, dict):
                        content += f"- `{param.get('name', '')}`: {param.get('description', '')}\n"
            
            content += f"*Relevance: {score:.2f}*\n\n"
        
        return content
    
    async def _send_no_results_response(self, query: str, original_message: AgentMessage):
        """Response when no results are found"""
        
        content = f"""I couldn't find specific documentation for "{query}" in the EPLAN knowledge base.

You might try:
- Rephrasing with EPLAN-specific terms
- Asking about general EPLAN concepts
- Requesting code generation if you need a script

Available topics include EPLAN API actions, parameters, and electrical automation patterns."""
        
        await self._send_direct_response(content, original_message)
        
        await self.log_to_scratchpad(f"No results found for: {query}", "search_miss")
    
    # Routing override para casos específicos
    async def can_handle(self, intent: str) -> float:
        """Improved specific routing for KnowledgeAgent"""
        
        # Casos que siempre maneja KnowledgeAgent
        always_handle_patterns = [
            "eplan documentation", "api reference", "xafactionsetting",
            "eplan examples", "electrical documentation"
        ]
        
        intent_lower = intent.lower()
        for pattern in always_handle_patterns:
            if pattern in intent_lower:
                await self.log_to_scratchpad(
                    f"KnowledgeAgent always handles: {pattern}",
                    "routing_override"
                )
                return 0.95
        
        confidence, method = await self.hybrid_handler.can_handle(intent, self.get_specialty())
        
        await self.log_to_scratchpad(
            f"KnowledgeAgent routing: {confidence:.2f} via {method}",
            "routing"
        )
        
        return confidence
