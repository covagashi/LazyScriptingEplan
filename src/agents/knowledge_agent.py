# src/agents/knowledge_agent.py
import time
from typing import Dict, List, Any
from .mini_agent import MiniAgent
from ..ai.documentation_rag import DocumentationRAG
from ..core.message_bus import AgentMessage, ObservableMessageBus

class EplanKnowledgeAgent(MiniAgent):
    """Knowledge Agent with full observability integration"""
    
    def __init__(self, message_bus: ObservableMessageBus):
        super().__init__("knowledge", message_bus)
        self.doc_rag = DocumentationRAG() 
        
        self.search_metrics = {
            "total_searches": 0,
            "successful_searches": 0,
            "empty_results": 0,
            "collaboration_requests": 0
        }
        
        self._setup_custom_routing()
    
    def _setup_custom_routing(self):
        """Configure specific routing for EPLAN documentation"""
        custom_keywords = {
            "high_confidence": [
                "eplan action", "eplan api reference", "action parameters", "namespace",
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
        
        if hasattr(self, 'router') and hasattr(self.router, 'agent_keywords'):
            self.router.agent_keywords["knowledge"] = custom_keywords
    
    def get_specialty(self) -> str:
        return "EPLAN electrical software documentation, API examples, code patterns"
    
    async def _get_current_capabilities(self) -> str:
        """Current capacities with observability metrics"""
        doc_count = len(self.doc_rag.docs) if hasattr(self.doc_rag, 'docs') else 0
        rag_status = "loaded" if doc_count > 0 else "loading"
        
        search_success_rate = 0
        if self.search_metrics["total_searches"] > 0:
            search_success_rate = (self.search_metrics["successful_searches"] / 
                                 self.search_metrics["total_searches"]) * 100
        
        return (f"Documentation RAG {rag_status} ({doc_count} docs), "
                f"Search success: {search_success_rate:.1f}%, "
                f"Collaborations: {self.search_metrics['collaboration_requests']}")
    
    async def _get_current_state(self) -> Dict:
        """Enhanced state with observability metrics"""
        base_state = await super()._get_current_state()
        base_state.update({
            "search_metrics": self.search_metrics,
            "doc_rag_status": {
                "docs_loaded": len(self.doc_rag.docs) if hasattr(self.doc_rag, 'docs') else 0,
                "cache_status": "active" if hasattr(self.doc_rag, 'doc_embeddings') and 
                              self.doc_rag.doc_embeddings is not None else "inactive"
            }
        })
        return base_state
    
    async def _restore_from_state(self, state: Dict):
        """Restore with observability metrics"""
        if "search_metrics" in state:
            self.search_metrics = state["search_metrics"]
        
        await self._log_structured_event({
            "event_type": "state_restored",
            "metrics_restored": self.search_metrics
        })
    
    async def process_message_with_context(self, message: AgentMessage, contexts: Dict[str, Any]):
        """Enhanced processing with full observability tracking"""
        
        async with await self.measure_performance("message_processing"):
            
            await self._log_structured_event({
                "event_type": "knowledge_request_start",
                "correlation_id": message.correlation_id,
                "intent": message.intent,
                "has_context": len(contexts) > 0
            })
            
            if message.intent in ["enhanced_user_request", "knowledge_request", "collaboration_request"]:
                await self._handle_knowledge_request(message, contexts)
                
            elif message.intent == "knowledge_for_code":
                await self._handle_code_assistance(message, contexts)
                
            elif message.intent == "planned_task":
                await self._handle_planned_task(message, contexts)
                
            else:
                await self._log_structured_event({
                    "event_type": "unhandled_intent",
                    "intent": message.intent,
                    "correlation_id": message.correlation_id
                })
    
    async def _handle_knowledge_request(self, message: AgentMessage, contexts: Dict[str, Any]):
        """Handle knowledge request with observability"""
        
        # Extract query
        query = message.payload.get("query", "")
        enriched_context = None
        
        for context_data in contexts.values():
            if "user_query" in context_data:
                query = context_data["user_query"]
                enriched_context = context_data
                break
        
        if not query:
            await self._send_error_response("No query provided", message)
            return
        
        await self._log_structured_event({
            "event_type": "documentation_search_start",
            "query": query[:100],  # Limit for privacy
            "correlation_id": message.correlation_id,
            "search_id": f"search_{int(time.time() * 1000)}"
        })
        
        async with await self.measure_performance("documentation_search"):
            results = await self._perform_enhanced_search(query)
        
        self.search_metrics["total_searches"] += 1
        
        if results:
            self.search_metrics["successful_searches"] += 1
            
            needs_code = await self._analyze_code_needs(query, enriched_context)
            
            await self._log_structured_event({
                "event_type": "documentation_search_complete",
                "query": query[:100],
                "results_count": len(results),
                "needs_code_collaboration": needs_code,
                "correlation_id": message.correlation_id
            })
            
            if needs_code:
                await self._initiate_code_collaboration(query, results, enriched_context, message)
            else:
                await self._send_knowledge_response(results, query, message)
        else:
            self.search_metrics["empty_results"] += 1
            await self._handle_no_results(query, message)
    
    async def _handle_code_assistance(self, message: AgentMessage, contexts: Dict[str, Any]):
        """Handle code assistance collaboration"""
        
        query = message.payload.get("user_query", "")
        collaboration_type = message.payload.get("collaboration_type", "unknown")
        
        await self._log_structured_event({
            "event_type": "code_assistance_request",
            "query": query[:100],
            "collaboration_type": collaboration_type,
            "correlation_id": message.correlation_id
        })
        
        results = await self._perform_enhanced_search(query)
        
        await self.send_message(
            ["codecraft"],
            "knowledge_results",
            {
                "query": query,
                "results": results,
                "collaboration_type": collaboration_type
            },
            heavy_context={
                "detailed_results": results,
                "search_metadata": {
                    "search_time": time.time(),
                    "results_count": len(results)
                }
            },
            parent_message=message
        )
    
    async def _handle_planned_task(self, message: AgentMessage, contexts: Dict[str, Any]):
        """Handle planned task from PlanningAgent"""
        
        step_number = message.payload.get("step_number")
        action = message.payload.get("action")
        plan_id = message.payload.get("plan_id")
        
        await self._log_structured_event({
            "event_type": "planned_task_received",
            "plan_id": plan_id,
            "step_number": step_number,
            "action": action,
            "correlation_id": message.correlation_id
        })
        
        query = None
        for context_data in contexts.values():
            if "original_query" in context_data:
                query = context_data["original_query"]
                break
        
        if not query:
            await self._send_error_response("No query in planned task", message)
            return
        
        if action == "research_documentation" or action == "find_documentation":
            results = await self._perform_enhanced_search(query)
            
            await self.send_message(
                ["conversation"],
                "planned_task_result",
                {
                    "plan_id": plan_id,
                    "step_number": step_number,
                    "results": results,
                    "content": await self._format_knowledge_response(results, query)
                },
                parent_message=message
            )
            
        elif action == "gather_resources":
            results = await self._perform_enhanced_search(query)
            related = self.doc_rag.find_related_concepts(query, top_k=5)
            
            comprehensive_results = results + related
            
            await self.send_message(
                ["planning", "codecraft"],
                "resources_gathered",
                {
                    "plan_id": plan_id,
                    "step_number": step_number,
                    "query": query,
                    "resources_count": len(comprehensive_results)
                },
                heavy_context={
                    "comprehensive_results": comprehensive_results,
                    "search_metadata": {
                        "primary_results": len(results),
                        "related_concepts": len(related)
                    }
                },
                parent_message=message
            )
        
        await self.send_message(
            ["planning"],
            "step_completed",
            {
                "plan_id": plan_id,
                "step_number": step_number,
                "success": True
            },
            parent_message=message
        )
    
    async def _perform_enhanced_search(self, query: str) -> List[Dict]:
        """Enhanced search with detailed logging"""
        
        search_start = time.time()
        
        try:
            results = self.doc_rag.search_documentation(query, top_k=3)
            
            search_time = time.time() - search_start
            
            await self._log_structured_event({
                "event_type": "rag_search_metrics",
                "query_length": len(query),
                "search_time": search_time,
                "results_found": len(results),
                "search_type": "semantic"
            })
            
            if not results:
                action_results = self.doc_rag.find_action_documentation(query)
                if action_results:
                    results = action_results
                    
                    await self._log_structured_event({
                        "event_type": "rag_search_fallback",
                        "fallback_type": "action_specific",
                        "results_found": len(results)
                    })
            
            return results
            
        except Exception as e:
            search_time = time.time() - search_start
            
            await self._log_structured_event({
                "event_type": "rag_search_error",
                "error": str(e),
                "search_time": search_time
            })
            
            return []
    
    async def _analyze_code_needs(self, query: str, context: Dict = None) -> bool:
        """Enhanced code needs analysis with observability"""
        
        analysis_start = time.time()
        
        code_indicators = [
            "generate", "create script", "write code", "script for",
            "code example", "implementation", "programming"
        ]
        
        query_lower = query.lower()
        has_code_indicators = any(indicator in query_lower for indicator in code_indicators)
        
        context_suggests_code = False
        if context and "intent_analysis" in context:
            intent = context["intent_analysis"]
            context_suggests_code = intent.get("primary_intent") == "code_generation"
        
        llm_suggests_code = False
        if not has_code_indicators and not context_suggests_code:
            try:
                prompt = f"""Does this query need code generation?

Query: "{query}"
Context: {context.get('conversation_context', 'None') if context else 'None'}

Code indicators: script, generate, create, implementation
Documentation indicators: explain, what is, how to, documentation

Answer YES or NO:"""
                
                response = await self.ai_client.generate(prompt)
                llm_suggests_code = "YES" in response.upper()
                
            except Exception as e:
                await self._log_structured_event({
                    "event_type": "llm_analysis_error",
                    "operation": "code_needs_analysis",
                    "error": str(e)
                })
        
        analysis_time = time.time() - analysis_start
        final_decision = has_code_indicators or context_suggests_code or llm_suggests_code
        
        await self._log_structured_event({
            "event_type": "code_needs_analysis",
            "query": query[:50],
            "code_indicators": has_code_indicators,
            "context_suggests": context_suggests_code,
            "llm_suggests": llm_suggests_code,
            "final_decision": final_decision,
            "analysis_time": analysis_time
        })
        
        return final_decision
    
    async def _initiate_code_collaboration(self, query: str, knowledge_results: List, 
                                         context: Dict, original_message: AgentMessage):
        """Enhanced collaboration with observability tracking"""
        
        self.search_metrics["collaboration_requests"] += 1
        
        collaboration_context = {
            "original_query": query,
            "knowledge_results": knowledge_results,
            "conversation_context": context.get("conversation_context") if context else None,
            "requester": "knowledge_via_user",
            "collaboration_id": f"collab_{int(time.time() * 1000)}"
        }
        
        await self._log_structured_event({
            "event_type": "collaboration_initiated",
            "target_agent": "codecraft",
            "collaboration_type": "knowledge_assisted_generation",
            "knowledge_results_count": len(knowledge_results),
            "correlation_id": original_message.correlation_id
        })
        
        await self.send_message(
            ["codecraft"],
            "knowledge_for_code",
            {
                "user_query": query,
                "examples_count": len(knowledge_results),
                "collaboration_type": "knowledge_assisted_generation"
            },
            heavy_context=collaboration_context,
            context_metadata={"type": "knowledge_collaboration"},
            parent_message=original_message
        )
    
    async def _send_knowledge_response(self, results: List, query: str, original_message: AgentMessage):
        """Send knowledge response with tracking"""
        
        content = await self._format_knowledge_response(results, query)
        
        await self._log_structured_event({
            "event_type": "knowledge_response_prepared",
            "response_length": len(content),
            "results_used": len(results),
            "correlation_id": original_message.correlation_id
        })
        
        await self.send_message(
            ["conversation"],
            "response_to_user",
            {
                "content": content,
                "source": "knowledge_agent",
                "request_id": original_message.payload.get("request_id"),
                "results_count": len(results)
            },
            parent_message=original_message
        )
    
    async def _format_knowledge_response(self, results: List, query: str) -> str:
        """Enhanced response formatting with metrics"""
        
        format_start = time.time()
        
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
                for param in item['parameters'][:13]:  # Limit parameters
                    if isinstance(param, dict):
                        content += f"- `{param.get('name', '')}`: {param.get('description', '')}\n"
            
            content += f"*Relevance: {score:.2f}*\n\n"
        
        format_time = time.time() - format_start
        
        await self._log_structured_event({
            "event_type": "response_formatting_complete",
            "format_time": format_time,
            "content_length": len(content),
            "sections_included": len(results)
        })
        
        return content
    
    async def _handle_no_results(self, query: str, original_message: AgentMessage):
        """Handle no results with enhanced logging"""
        
        await self._log_structured_event({
            "event_type": "search_no_results",
            "query": query[:100],
            "correlation_id": original_message.correlation_id
        })
        
        content = f"""I couldn't find specific documentation for "{query}" in the EPLAN knowledge base.

You might try:
- Rephrasing with EPLAN-specific terms
- Asking about general EPLAN concepts
- Requesting code generation if you need a script

Available topics include EPLAN API actions, parameters, and electrical automation patterns."""
        
        await self.send_message(
            ["conversation"],
            "response_to_user",
            {
                "content": content,
                "source": "knowledge_agent",
                "search_status": "no_results"
            },
            parent_message=original_message
        )
    
    async def _send_error_response(self, error_msg: str, original_message: AgentMessage):
        """Send error response with logging"""
        
        await self._log_structured_event({
            "event_type": "knowledge_error_response",
            "error": error_msg,
            "correlation_id": original_message.correlation_id
        })
        
        await self.send_message(
            ["conversation"],
            "response_to_user",
            {
                "content": f"I encountered an error: {error_msg}",
                "source": "knowledge_agent",
                "status": "error"
            },
            parent_message=original_message
        )
    
    # === Enhanced Routing ===
    async def can_handle(self, intent: str) -> float:
        """Enhanced routing with observability"""
        
        routing_start = time.time()
        
        always_handle_patterns = [
            "eplan documentation", "api reference", "xafactionsetting",
            "eplan examples", "electrical documentation"
        ]
        
        intent_lower = intent.lower()
        for pattern in always_handle_patterns:
            if pattern in intent_lower:
                await self._log_structured_event({
                    "event_type": "routing_decision",
                    "decision_type": "high_confidence_pattern",
                    "pattern": pattern,
                    "confidence": 0.95,
                    "routing_time": time.time() - routing_start
                })
                return 0.95
        
        try:
            if hasattr(self, 'hybrid_handler'):
                confidence, method = await self.hybrid_handler.can_handle(intent, self.get_specialty())
            else:
                confidence = await self._basic_can_handle(intent)
                method = "basic_llm"
            
            routing_time = time.time() - routing_start
            
            await self._log_structured_event({
                "event_type": "routing_decision",
                "decision_type": method,
                "confidence": confidence,
                "routing_time": routing_time,
                "intent": intent[:50]
            })
            
            return confidence
            
        except Exception as e:
            routing_time = time.time() - routing_start
            
            await self._log_structured_event({
                "event_type": "routing_error",
                "error": str(e),
                "routing_time": routing_time
            })
            
            return 0.3  # Conservative fallback
    
    async def _basic_can_handle(self, intent: str) -> float:
        """Basic LLM-based routing fallback"""
        
        prompt = f"""Can I help with: "{intent}"?
        
My specialty: {self.get_specialty()}
My current capabilities: {await self._get_current_capabilities()}
        
Return confidence 0.0-1.0:"""
        
        try:
            response = await self.ai_client.generate(prompt)
            confidence = float(response.strip())
            return max(0.0, min(1.0, confidence))
        except:
            return 0.3