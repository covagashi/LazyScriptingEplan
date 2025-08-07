# src/agents/planning_agent.py
import asyncio
import json
from typing import Dict, List, Any, Optional
from .mini_agent import EnhancedMiniAgent
from ..core.message_bus import AgentMessage

class PlanningAgent(EnhancedMiniAgent):
    """Specialist agent for complex task decomposition and planning"""
    
    def __init__(self, message_bus):
        super().__init__("planning", message_bus)
        self.active_plans = {}
        self.plan_templates = {
            "script_creation_and_execution": [
                {"step": 1, "agent": "knowledge", "action": "research_documentation"},
                {"step": 2, "agent": "codecraft", "action": "generate_script"},
                {"step": 3, "agent": "execution", "action": "execute_script"},
                {"step": 4, "agent": "feedback", "action": "validate_results"}
            ],
            "api_research_with_examples": [
                {"step": 1, "agent": "knowledge", "action": "find_documentation"},
                {"step": 2, "agent": "knowledge", "action": "get_code_examples"},
                {"step": 3, "agent": "codecraft", "action": "create_sample_code"}
            ],
            "comprehensive_eplan_task": [
                {"step": 1, "agent": "planning", "action": "analyze_requirements"},
                {"step": 2, "agent": "knowledge", "action": "gather_resources"},
                {"step": 3, "agent": "codecraft", "action": "implement_solution"},
                {"step": 4, "agent": "execution", "action": "test_implementation"},
                {"step": 5, "agent": "feedback", "action": "evaluate_success"}
            ]
        }
        
        self._setup_custom_routing()
    
    def _setup_custom_routing(self):
        """Configure routing for planning tasks"""
        custom_keywords = {
            "high_confidence": [
                "plan", "steps", "complex task", "multi-step", "workflow",
                "sequence", "breakdown", "organize", "strategy"
            ],
            "medium_confidence": [
                "and then", "after that", "first do", "create and execute",
                "multiple", "several steps", "comprehensive"
            ],
            "low_confidence": [
                "simple", "just", "only", "quick", "direct"
            ]
        }
        
        self.router.agent_keywords["planning"] = custom_keywords
    
    def get_specialty(self) -> str:
        return "Complex task decomposition, multi-step workflow planning, agent coordination"
    
    async def _get_current_capabilities(self) -> str:
        active_plans_count = len(self.active_plans)
        templates_count = len(self.plan_templates)
        return f"{active_plans_count} active plans, {templates_count} plan templates"
    
    async def can_handle(self, intent: str) -> float:
        """Specialized routing for planning tasks"""
        
        # High confidence indicators
        planning_patterns = [
            "create and execute", "generate then run", "step by step",
            "comprehensive", "complete workflow", "multiple steps"
        ]
        
        intent_lower = intent.lower()
        for pattern in planning_patterns:
            if pattern in intent_lower:
                return 0.9
        
        # Count complexity indicators
        complexity_indicators = [
            "and", "then", "after", "first", "next", "finally",
            "also", "additionally", "furthermore"
        ]
        
        complexity_score = sum(0.1 for indicator in complexity_indicators 
                             if indicator in intent_lower)
        
        # Base confidence from hybrid system
        base_confidence, method = await self.hybrid_handler.can_handle(intent, self.get_specialty())
        
        final_confidence = min(1.0, base_confidence + complexity_score)
        
        await self.log_to_scratchpad(
            f"Planning routing: {final_confidence:.2f} (base: {base_confidence:.2f}, complexity: {complexity_score:.2f})",
            "routing"
        )
        
        return final_confidence
    
    async def process_message_with_context(self, message: AgentMessage, contexts: Dict[str, Any]):
        """Process planning requests with context"""
        
        if message.intent in ["enhanced_user_request", "planning_request"]:
            query = message.payload.get("query", "")
            
            # Get enriched context
            enriched_context = None
            for context_data in contexts.values():
                if "user_query" in context_data:
                    query = context_data["user_query"]
                    enriched_context = context_data
                    break
            
            await self.log_to_scratchpad(f"Planning task: {query[:100]}", "processing")
            
            # Analyze and create plan
            plan = await self._create_execution_plan(query, enriched_context)
            
            if plan:
                plan_id = await self._store_plan(plan, query)
                await self._execute_plan(plan_id, plan, enriched_context)
            else:
                await self._handle_simple_task(query, message)
    
    async def _create_execution_plan(self, query: str, context: Dict = None) -> Optional[Dict]:
        """Create execution plan for complex queries"""
        
        # First, analyze task complexity
        complexity_analysis = await self._analyze_task_complexity(query, context)
        
        if complexity_analysis["complexity_level"] == "simple":
            return None  # Let other agents handle directly
        
        # Check for template match
        template_match = self._find_template_match(query, complexity_analysis)
        if template_match:
            return await self._customize_template(template_match, query, complexity_analysis)
        
        # Generate custom plan
        return await self._generate_custom_plan(query, complexity_analysis)
    
    async def _analyze_task_complexity(self, query: str, context: Dict = None) -> Dict:
        """Analyze task complexity and requirements"""
        
        prompt = f"""Analyze this task's complexity and requirements:

Query: "{query}"
Context: {context.get('conversation_context', 'None') if context else 'None'}

Determine:
1. complexity_level: simple, moderate, complex
2. required_agents: list of needed agents
3. task_type: script_creation, documentation_research, execution, comprehensive
4. dependencies: what needs to happen before what
5. estimated_steps: number of steps needed

Return JSON:"""
        
        try:
            response = await self.ai_client.generate(prompt)
            analysis = json.loads(response.strip())
            
            await self.update_scratchpad("last_complexity_analysis", {
                "query": query,
                "analysis": analysis,
                "timestamp": asyncio.get_event_loop().time()
            })
            
            return analysis
        except Exception as e:
            await self.log_to_scratchpad(f"Complexity analysis error: {e}", "error")
            return {
                "complexity_level": "moderate",
                "required_agents": ["knowledge", "codecraft"],
                "task_type": "general",
                "dependencies": [],
                "estimated_steps": 2
            }
    
    def _find_template_match(self, query: str, analysis: Dict) -> Optional[str]:
        """Find matching plan template"""
        
        task_type = analysis.get("task_type", "general")
        required_agents = set(analysis.get("required_agents", []))
        
        # Direct template matches
        if task_type == "script_creation" and "execution" in required_agents:
            return "script_creation_and_execution"
        elif task_type == "documentation_research" and "codecraft" in required_agents:
            return "api_research_with_examples"
        elif analysis.get("complexity_level") == "complex":
            return "comprehensive_eplan_task"
        
        return None
    
    async def _customize_template(self, template_name: str, query: str, analysis: Dict) -> Dict:
        """Customize plan template for specific query"""
        
        base_steps = self.plan_templates[template_name].copy()
        
        # Customize based on analysis
        customized_plan = {
            "plan_id": f"plan_{int(asyncio.get_event_loop().time() * 1000)}",
            "template": template_name,
            "original_query": query,
            "complexity": analysis.get("complexity_level"),
            "estimated_duration": len(base_steps) * 30,  # 30s per step estimate
            "steps": []
        }
        
        for step in base_steps:
            customized_step = step.copy()
            customized_step["query_context"] = query
            customized_step["status"] = "pending"
            customized_step["estimated_time"] = 30
            customized_plan["steps"].append(customized_step)
        
        return customized_plan
    
    async def _generate_custom_plan(self, query: str, analysis: Dict) -> Dict:
        """Generate custom plan using LLM"""
        
        prompt = f"""Create execution plan for this EPLAN task:

Query: "{query}"
Analysis: {json.dumps(analysis, indent=2)}

Available agents:
- knowledge: EPLAN documentation, API reference
- codecraft: C# script generation
- execution: EPLAN Remoting, script execution  
- feedback: Result validation, log analysis

Create step-by-step plan with:
- Sequential steps (some can be parallel)
- Agent assignment per step
- Clear action description
- Dependencies between steps

Return JSON plan:
{{
  "steps": [
    {{"step": 1, "agent": "agent_id", "action": "description", "depends_on": []}},
    ...
  ]
}}"""
        
        try:
            response = await self.ai_client.generate(prompt)
            plan_data = json.loads(response.strip())
            
            custom_plan = {
                "plan_id": f"custom_{int(asyncio.get_event_loop().time() * 1000)}",
                "template": "custom",
                "original_query": query,
                "complexity": analysis.get("complexity_level"),
                "estimated_duration": len(plan_data.get("steps", [])) * 45,
                "steps": []
            }
            
            for step in plan_data.get("steps", []):
                step["status"] = "pending"
                step["estimated_time"] = 45
                step["query_context"] = query
                custom_plan["steps"].append(step)
            
            return custom_plan
            
        except Exception as e:
            await self.log_to_scratchpad(f"Custom plan generation error: {e}", "error")
            return None
    
    async def _store_plan(self, plan: Dict, query: str) -> str:
        """Store execution plan"""
        
        plan_id = plan["plan_id"]
        self.active_plans[plan_id] = plan
        
        # Store in filesystem for persistence
        context_ref = await self.store_heavy_context(
            plan,
            context_id=f"plan_{plan_id}",
            metadata={"type": "execution_plan", "query": query}
        )
        
        await self.log_to_scratchpad(
            f"Created plan {plan_id} with {len(plan['steps'])} steps",
            "planning"
        )
        
        return plan_id
    
    async def _execute_plan(self, plan_id: str, plan: Dict, context: Dict):
        """Execute the plan by coordinating agents"""
        
        await self.log_to_scratchpad(f"Executing plan {plan_id}", "execution")
        
        for step in plan["steps"]:
            step_num = step.get("step", 0)
            agent_id = step.get("agent")
            action = step.get("action")
            depends_on = step.get("depends_on", [])
            
            # Check dependencies
            if not self._dependencies_satisfied(plan_id, depends_on):
                await self.log_to_scratchpad(
                    f"Step {step_num} waiting for dependencies: {depends_on}",
                    "execution"
                )
                continue
            
            # Execute step
            step["status"] = "executing"
            await self._execute_step(plan_id, step, context)
            
            # Small delay between steps
            await asyncio.sleep(1)
        
        await self._finalize_plan(plan_id)
    
    async def _execute_step(self, plan_id: str, step: Dict, context: Dict):
        """Execute individual plan step"""
        
        step_num = step.get("step", 0)
        agent_id = step.get("agent")
        action = step.get("action")
        
        if agent_id == "planning":
            # Self-execution step
            await self._execute_planning_step(step, context)
        else:
            # Delegate to other agent
            step_context = {
                "plan_id": plan_id,
                "step_number": step_num,
                "action": action,
                "original_query": context.get("user_query") if context else step.get("query_context"),
                "plan_context": context
            }
            
            await self.send_message(
                [agent_id],
                "planned_task",
                {
                    "step_number": step_num,
                    "action": action,
                    "plan_id": plan_id
                },
                heavy_context=step_context
            )
        
        step["status"] = "completed"
        await self.log_to_scratchpad(
            f"Completed step {step_num}: {action} via {agent_id}",
            "execution"
        )
    
    async def _execute_planning_step(self, step: Dict, context: Dict):
        """Execute planning-specific steps"""
        
        action = step.get("action")
        
        if action == "analyze_requirements":
            # Detailed analysis
            query = context.get("user_query") if context else step.get("query_context")
            analysis = await self._analyze_task_complexity(query, context)
            
            await self.update_scratchpad("requirement_analysis", {
                "query": query,
                "analysis": analysis,
                "timestamp": asyncio.get_event_loop().time()
            })
    
    def _dependencies_satisfied(self, plan_id: str, depends_on: List) -> bool:
        """Check if step dependencies are satisfied"""
        
        if not depends_on:
            return True
        
        plan = self.active_plans.get(plan_id, {})
        steps = plan.get("steps", [])
        
        for dep_step in depends_on:
            dep_satisfied = False
            for step in steps:
                if step.get("step") == dep_step and step.get("status") == "completed":
                    dep_satisfied = True
                    break
            
            if not dep_satisfied:
                return False
        
        return True
    
    async def _finalize_plan(self, plan_id: str):
        """Finalize plan execution"""
        
        plan = self.active_plans.get(plan_id, {})
        completed_steps = sum(1 for step in plan.get("steps", []) 
                            if step.get("status") == "completed")
        total_steps = len(plan.get("steps", []))
        
        if completed_steps == total_steps:
            status = "✅ Plan completed successfully"
        else:
            status = f"⚠️ Plan partially completed: {completed_steps}/{total_steps} steps"
        
        # Send completion notification
        await self.send_message(
            ["conversation"],
            "response_to_user",
            {
                "content": f"🎯 **Plan Execution Complete**\n{status}\n\nOriginal request: {plan.get('original_query', 'N/A')}",
                "plan_id": plan_id
            }
        )
        
        await self.log_to_scratchpad(
            f"Finalized plan {plan_id}: {completed_steps}/{total_steps} completed",
            "completion"
        )
        
        # Archive completed plan
        if plan_id in self.active_plans:
            del self.active_plans[plan_id]
    
    async def _handle_simple_task(self, query: str, original_message: AgentMessage):
        """Handle simple tasks that don't need planning"""
        
        await self.send_message(
            ["conversation"],
            "response_to_user", 
            {
                "content": f"This seems like a straightforward task. I'll let the specialized agents handle it directly rather than creating a complex plan.",
                "suggestion": "Try asking the specific agents directly for faster results."
            }
        )
        
        await self.log_to_scratchpad(
            f"Delegated simple task: {query[:50]}",
            "delegation"
        )
    
    # === Message Processing ===
    async def process_message(self, message: AgentMessage):
        """Basic message processing"""
        
        if message.intent == "step_completed":
            plan_id = message.payload.get("plan_id")
            step_number = message.payload.get("step_number")
            success = message.payload.get("success", True)
            
            await self._update_step_status(plan_id, step_number, "completed" if success else "failed")
        
        elif message.intent == "plan_status_request":
            plan_id = message.payload.get("plan_id")
            await self._send_plan_status(plan_id, message.sender)
        
        else:
            await self.log_to_scratchpad(
                f"Received message: {message.intent} from {message.sender}",
                "message_processing"
            )
    
    async def _update_step_status(self, plan_id: str, step_number: int, status: str):
        """Update step status in active plan"""
        
        if plan_id in self.active_plans:
            for step in self.active_plans[plan_id].get("steps", []):
                if step.get("step") == step_number:
                    step["status"] = status
                    break
            
            await self.log_to_scratchpad(
                f"Updated plan {plan_id} step {step_number}: {status}",
                "status_update"
            )
    
    async def _send_plan_status(self, plan_id: str, requester: str):
        """Send current plan status"""
        
        if plan_id not in self.active_plans:
            await self.send_message(
                [requester],
                "plan_not_found",
                {"plan_id": plan_id}
            )
            return
        
        plan = self.active_plans[plan_id]
        status_summary = {
            "plan_id": plan_id,
            "total_steps": len(plan.get("steps", [])),
            "completed_steps": sum(1 for step in plan.get("steps", []) 
                                 if step.get("status") == "completed"),
            "current_step": next((step for step in plan.get("steps", []) 
                                if step.get("status") == "executing"), None),
            "steps": plan.get("steps", [])
        }
        
        await self.send_message(
            [requester],
            "plan_status",
            status_summary
        )