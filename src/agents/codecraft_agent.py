# src/agents/codecraft_agent.py
import os
import time
from pathlib import Path
from typing import Dict, Any, List
from .mini_agent import MiniAgent
from ..core.message_bus import ObservableMessageBus, AgentMessage
from ..ai.script_rag import ScriptRAG

class CodeCraftAgent(MiniAgent):
    """Enhanced CodeCraft Agent with observability integration"""
    
    def __init__(self, message_bus: ObservableMessageBus):
        super().__init__("codecraft", message_bus)
        self.output_dir = Path(r"C:\temp\Agent")
        self.output_dir.mkdir(exist_ok=True)
        self.script_rag = ScriptRAG()
        
        self.generation_metrics = {
            "scripts_generated": 0,
            "successful_generations": 0,
            "knowledge_collaborations": 0,
            "average_generation_time": 0
        }
        
        self._setup_custom_routing()
    
    def _setup_custom_routing(self):
        """Specific routing for CodeCraftAgent"""
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
        success_rate = 0
        if self.generation_metrics["scripts_generated"] > 0:
            success_rate = (self.generation_metrics["successful_generations"] / 
                           self.generation_metrics["scripts_generated"]) * 100
        
        return f"Script RAG loaded ({script_count} examples), C# generation, success rate: {success_rate:.1f}%"
    
    async def _get_current_state(self) -> Dict:
        """Enhanced state with generation metrics"""
        base_state = await super()._get_current_state()
        base_state.update({
            "generation_metrics": self.generation_metrics,
            "script_rag_status": {
                "scripts_loaded": len(self.script_rag.scripts) if hasattr(self.script_rag, 'scripts') else 0
            }
        })
        return base_state
    
    async def _restore_from_state(self, state: Dict):
        """Restore with generation metrics"""
        if "generation_metrics" in state:
            self.generation_metrics = state["generation_metrics"]
        
        await self._log_structured_event({
            "event_type": "state_restored",
            "metrics_restored": self.generation_metrics
        })
    
    async def can_handle(self, intent: str) -> float:
        """Routing específico para generación de código"""
        
        code_patterns = [
            "generate script", "create code", "write script", "c# code",
            "programming", "code generation"
        ]
        
        intent_lower = intent.lower()
        for pattern in code_patterns:
            if pattern in intent_lower:
                await self._log_structured_event({
                    "event_type": "routing_high_confidence",
                    "pattern": pattern,
                    "confidence": 0.95
                })
                return 0.95
        
        base_confidence, method = await self.hybrid_handler.can_handle(intent, self.get_specialty())
        
        programming_terms = ["script", "code", "c#", "generate", "create"]
        boost = sum(0.05 for term in programming_terms if term in intent_lower)
        
        final_confidence = min(1.0, base_confidence + boost)
        
        await self.log_to_scratchpad(
            f"CodeCraft routing: {final_confidence:.2f} (base: {base_confidence:.2f}, boost: {boost:.2f})",
            "routing"
        )
                
        return final_confidence
    
    async def process_message_with_context(self, message: AgentMessage, contexts: Dict[str, Any]):
        """Enhanced processing with observability tracking"""
        
        async with await self.measure_performance("message_processing"):
            
            await self._log_structured_event({
                "event_type": "code_generation_request_start",
                "correlation_id": message.correlation_id,
                "intent": message.intent,
                "has_context": len(contexts) > 0
            })
            
            if message.intent in ["enhanced_user_request", "code_generation_request"]:
                await self._handle_code_generation_request(message, contexts)
                
            elif message.intent == "knowledge_for_code":
                await self._handle_knowledge_assisted_generation(message, contexts)
                
            elif message.intent == "planned_task":
                await self._handle_planned_task(message, contexts)
            elif message.intent == "execute_validated_script":
                await self._handle_validated_script_execution(message, contexts)
                
            else:
                await self._log_structured_event({
                    "event_type": "unhandled_intent",
                    "intent": message.intent,
                    "correlation_id": message.correlation_id
                })
    
    async def _handle_code_generation_request(self, message: AgentMessage, contexts: Dict[str, Any]):
        """Handle direct code generation request"""
        
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
        
        generation_start = time.time()
        await self._log_structured_event({
            "event_type": "script_generation_start",
            "query": query[:100],
            "correlation_id": message.correlation_id,
            "generation_id": f"gen_{int(time.time() * 1000)}"
        })
        
        needs_knowledge = await self._analyze_knowledge_needs(query, enriched_context)
        
        if needs_knowledge:
            await self._request_knowledge_assistance(query, enriched_context, message)
        else:
            await self._generate_script_direct(query, enriched_context, message)
    
    async def _handle_validated_script_execution(self, message: AgentMessage, contexts: Dict[str, Any]):
        validated_script = None
        for context_data in contexts.values():
            if "validated_script" in context_data:
                validated_script = context_data["validated_script"]
                break
        
        if validated_script:
            temp_file = await self._save_validated_script(validated_script)
            success, result = await self._execute_script("ValidatedScript")
            
            self.execution_metrics["total_executions"] += 1
            if success:
                self.execution_metrics["successful_executions"] += 1
            else:
                self.execution_metrics["failed_executions"] += 1
            
            await self._log_structured_event({
                "event_type": "validated_script_execution_complete",
                "success": success,
                "result": result[:100] if result else None
            })
            
            await self.send_message(
                ["feedback"],
                "analyze_execution",
                {
                    "success": success,
                    "result": result,
                    "action": "ValidatedScript",
                    "validation_enhanced": True
                },
                parent_message=message
            )
            
            if temp_file:
                temp_file.unlink(missing_ok=True)



    async def _handle_knowledge_assisted_generation(self, message: AgentMessage, contexts: Dict[str, Any]):
        """Handle code generation with knowledge assistance"""
        
        query = message.payload.get("user_query", "")
        collaboration_type = message.payload.get("collaboration_type", "unknown")
        
        await self._log_structured_event({
            "event_type": "knowledge_assisted_generation_start",
            "query": query[:100],
            "collaboration_type": collaboration_type,
            "correlation_id": message.correlation_id
        })
        
        self.generation_metrics["knowledge_collaborations"] += 1
        
        knowledge_results = []
        for context_data in contexts.values():
            if "knowledge_results" in context_data:
                knowledge_results = context_data["knowledge_results"]
                break
        
        await self._generate_script_with_knowledge(query, knowledge_results, message)
    
    async def _handle_planned_task(self, message: AgentMessage, contexts: Dict[str, Any]):
        """Handle planned task from PlanningAgent"""
        
        step_number = message.payload.get("step_number")
        action = message.payload.get("action")
        plan_id = message.payload.get("plan_id")
        
        await self._log_structured_event({
            "event_type": "planned_code_task_received",
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
        
        if action in ["generate_script", "implement_solution", "create_sample_code"]:
            await self._generate_script_direct(query, contexts, message, plan_id=plan_id)
        
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
    
    async def _analyze_knowledge_needs(self, query: str, context: Dict = None) -> bool:
        """Analyze if knowledge assistance is needed"""
        
        script_results = self.script_rag.search_scripts(query, top_k=1, threshold=0.4)
        
        if script_results:
            await self._log_structured_event({
                "event_type": "knowledge_analysis",
                "decision": "direct_generation",
                "reason": "relevant_examples_found",
                "examples_count": len(script_results)
            })
            return False
        
        eplan_terms = ["action", "API", "namespace", "parameter"]
        has_eplan_terms = any(term in query.lower() for term in eplan_terms)
        
        if has_eplan_terms:
            await self._log_structured_event({
                "event_type": "knowledge_analysis",
                "decision": "needs_knowledge",
                "reason": "complex_eplan_terms",
                "terms_found": [term for term in eplan_terms if term in query.lower()]
            })
            return True
        
        return False
    
    async def _request_knowledge_assistance(self, query: str, context: Dict, original_message: AgentMessage):
        """Request knowledge assistance for code generation"""
        
        await self.send_message(
            ["knowledge"],
            "knowledge_for_code",
            {
                "user_query": query,
                "collaboration_type": "code_assistance_needed"
            },
            heavy_context={
                "original_query": query,
                "conversation_context": context.get("conversation_context") if context else None,
                "requester": "codecraft"
            },
            parent_message=original_message
        )
        
        await self._log_structured_event({
            "event_type": "knowledge_assistance_requested",
            "correlation_id": original_message.correlation_id
        })
    
    async def _generate_script_direct(self, query: str, context: Dict, original_message: AgentMessage, plan_id: str = None):
        """Generate script directly with ScriptRAG"""
        
        generation_start = time.time()
        self.generation_metrics["scripts_generated"] += 1
        
        async with await self.measure_performance("script_generation"):
            
            examples = self.script_rag.search_scripts(query, top_k=3)
            
            script_content = await self._create_script_content(query, examples)
            
            if script_content:
                script_file = await self._save_generated_script(script_content, query)
                
                self.generation_metrics["successful_generations"] += 1
                
                response_content = f"✅ **Generated C# Script**\n\n```csharp\n{script_content}\n```\n\n📁 Saved to: `{script_file}`"
                
                await self.send_message(
                    ["validation"],
                    "validate_script",
                    {
                        "script_content": script_content,
                        "script_purpose": f"Generated for: {query}"
                    },
                    parent_message=original_message
                )
                
                generation_time = time.time() - generation_start
                self._update_generation_metrics(generation_time)
                
                await self._log_structured_event({
                    "event_type": "script_generation_complete",
                    "generation_time": generation_time,
                    "script_lines": len(script_content.split('\n')),
                    "examples_used": len(examples),
                    "correlation_id": original_message.correlation_id
                })
            else:
                await self._send_error_response("Failed to generate script", original_message)
    
    async def _generate_script_with_knowledge(self, query: str, knowledge_results: List, original_message: AgentMessage):
        """Generate script with knowledge assistance"""
        
        generation_start = time.time()
        self.generation_metrics["scripts_generated"] += 1
        
        script_examples = self.script_rag.search_scripts(query, top_k=2)
        
        script_content = await self._create_enhanced_script_content(query, knowledge_results, script_examples)
        
        if script_content:
            script_file = await self._save_generated_script(script_content, query)
            
            self.generation_metrics["successful_generations"] += 1
            
            response_content = f"✅ **Generated Enhanced C# Script** (with EPLAN documentation)\n\n```csharp\n{script_content}\n```\n\n📁 Saved to: `{script_file}`\n\n*Generated using EPLAN API documentation and code examples*"
            
            await self.send_message(
                ["validation"],
                "validate_script",
                {
                    "script_content": script_content,
                    "script_purpose": f"Generated for: {query}"
                },
                parent_message=original_message
            )
            
            generation_time = time.time() - generation_start
            self._update_generation_metrics(generation_time)
            
            await self._log_structured_event({
                "event_type": "knowledge_assisted_generation_complete",
                "generation_time": generation_time,
                "knowledge_results_used": len(knowledge_results),
                "script_examples_used": len(script_examples),
                "correlation_id": original_message.correlation_id
            })
        else:
            await self._send_error_response("Failed to generate enhanced script", original_message)
    
    async def _create_script_content(self, query: str, examples: List) -> str:
        """Create script content using examples"""
        
        prompt = f"""Generate C# EPLAN script for: "{query}"

Available examples:
{self._format_examples_for_prompt(examples)}

Requirements:
- Complete C# class with proper structure
- EPLAN API usage
- Error handling
- Clear documentation

Generate only the C# code:"""
        
        try:
            success, response = await self.error_handler.safe_call(
                self.ai_client.generate,
                f"{self.id}_ai_generation",
                prompt
            )
            if not success:
                return self._get_fallback_response(response)
            return self._clean_generated_code(response)
        except Exception as e:
            await self._log_structured_event({
                "event_type": "script_generation_error",
                "error": str(e)
            })
            return None
    
    async def _create_enhanced_script_content(self, query: str, knowledge_results: List, script_examples: List) -> str:
        """Create enhanced script with knowledge and examples"""
        
        knowledge_context = self._format_knowledge_for_prompt(knowledge_results)
        examples_context = self._format_examples_for_prompt(script_examples)
        
        prompt = f"""Generate enhanced C# EPLAN script for: "{query}"

EPLAN API Documentation:
{knowledge_context}

Code Examples:
{examples_context}

Create a complete, well-documented C# script using the EPLAN API correctly:"""
        
        try:
            success, response = await self.error_handler.safe_call(
                self.ai_client.generate,
                f"{self.id}_ai_generation",
                prompt
            )
            if not success:
                return self._get_fallback_response(response)
            return self._clean_generated_code(response)
        except Exception as e:
            await self._log_structured_event({
                "event_type": "enhanced_generation_error",
                "error": str(e)
            })
            return None
    
    def _get_fallback_response(self, error: str) -> str:
        """Fallback response for this agent"""
        return f"I'm temporarily unavailable ({error[:50]}...). Please try again."

    def _format_examples_for_prompt(self, examples: List) -> str:
        """Format script examples for prompt"""
        formatted = []
        for example in examples[:2]:  # Limit to avoid token overflow
            doc = example['document']
            item = doc.get('example', {})
            if 'script' in item:
                formatted.append(f"Example: {item.get('name', 'Unnamed')}\n{' '.join(item['script'][:20])}")  # First 20 lines
        return '\n\n'.join(formatted)
    
    def _format_knowledge_for_prompt(self, knowledge_results: List) -> str:
        """Format knowledge results for prompt"""
        formatted = []
        for result in knowledge_results[:3]:
            doc = result['document']
            item = doc.get('item', {})
            name = item.get('name', 'API Reference')
            description = item.get('description', '')
            formatted.append(f"{name}: {description}")
        return '\n'.join(formatted)
    
    def _clean_generated_code(self, code: str) -> str:
        """Clean and format generated code"""
        code = code.replace("```csharp", "").replace("```", "")
        
        lines = [line.rstrip() for line in code.split('\n')]
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()
            
        return '\n'.join(lines)
    
    async def _save_generated_script(self, script_content: str, query: str) -> Path:
        """Save generated script to filesystem"""
        timestamp = int(time.time())
        filename = f"generated_script_{timestamp}.cs"
        script_file = self.output_dir / filename
        
        try:
            with open(script_file, 'w', encoding='utf-8') as f:
                f.write(f"// Generated for: {query}\n")
                f.write(f"// Timestamp: {timestamp}\n\n")
                f.write(script_content)
            
            await self._log_structured_event({
                "event_type": "script_saved",
                "file_path": str(script_file),
                "file_size": script_file.stat().st_size
            })
            
            return script_file
            
        except Exception as e:
            await self._log_structured_event({
                "event_type": "script_save_error",
                "error": str(e)
            })
            raise
    
    def _update_generation_metrics(self, generation_time: float):
        """Update average generation time metrics"""
        current_avg = self.generation_metrics["average_generation_time"]
        total_scripts = self.generation_metrics["scripts_generated"]
        
        if total_scripts == 1:
            self.generation_metrics["average_generation_time"] = generation_time
        else:
            self.generation_metrics["average_generation_time"] = (
                (current_avg * (total_scripts - 1) + generation_time) / total_scripts
            )
    
    async def _send_error_response(self, error_msg: str, original_message: AgentMessage):
        """Send error response with logging"""
        
        await self._log_structured_event({
            "event_type": "code_generation_error",
            "error": error_msg,
            "correlation_id": original_message.correlation_id
        })
        
        await self.send_message(
            ["conversation"],
            "response_to_user",
            {
                "content": f"❌ Code generation error: {error_msg}",
                "source": "codecraft_agent",
                "status": "error"
            },
            parent_message=original_message
        )