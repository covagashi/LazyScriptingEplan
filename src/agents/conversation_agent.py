# src/agents/conversation_agent.py
import time
import asyncio
from typing import Dict, Any, List, Optional 
from .mini_agent import MiniAgent
from ..core.message_bus import ObservableMessageBus, AgentMessage


class ConversationAgent(MiniAgent):
    """Enhanced ConversationAgent with persistent context and conversation management"""
    
    def __init__(self, message_bus: ObservableMessageBus):
        super().__init__("conversation", message_bus)
        
        self.current_conversation = None
        self.user_response = None
        self.conversation_history = []
        self.active_requests = {} 
        self.reflection_enabled = True
        self.observation_interval = 30  
        self.reflection_history = []
        self._observation_task = None 
        
    async def _restore_from_state(self, state: Dict):
        """Restore conversation status"""
        self.conversation_history = state.get("conversation_history", [])
        active_conv = state.get("current_conversation")
        if active_conv:
            self.current_conversation = active_conv
        self.reflection_history = state.get("reflection_history", [])
        self.reflection_enabled = state.get("reflection_enabled", True)
        
        await self.log_to_scratchpad(
            f"Restored {len(self.conversation_history)} conversation entries",
            "restoration"
        )
    
    async def _get_current_state(self) -> Dict:
        """Current state to persist"""
        base_state = await super()._get_current_state()
        base_state.update({
            "conversation_history": self.conversation_history[-50:],  # last 50 entries
            "current_conversation": self.current_conversation,
            "active_requests_count": len(self.active_requests),
            "reflection_history": self.reflection_history[-20:],  
            "reflection_enabled": self.reflection_enabled  
        })
        return base_state
    
    async def _get_current_capabilities(self) -> str:
        """Current capabilities of the conversational agent"""
        return f"Natural conversation, user intent detection, {len(self.active_requests)} active requests"
    
    def get_specialty(self) -> str:
        return "Natural conversation, user intent detection, conversation flow management"
    
    async def handle_user_input(self, user_query: str) -> str:
        """Improved user input handling with persistent context"""
                
        conversation_entry = {
            "timestamp": time.time(),
            "type": "user_input",
            "content": user_query,
            "conversation_id": self._get_conversation_id()
        }
        
        if len(user_query) > 200:
            context_ref = await self.store_heavy_context(
                {"user_query": user_query, "metadata": conversation_entry},
                metadata={"type": "user_input", "complexity": "high"}
            )
            conversation_entry["context_ref"] = context_ref.get_id() if context_ref else None
        
        self.conversation_history.append(conversation_entry)
        
        async with await self.measure_performance("handle_user_input"):
            
            direct_response = await self._try_direct_response(user_query)
            if direct_response:
                await self._record_response(direct_response, "direct")
                return direct_response
            
            
            intent_analysis = await self._analyze_user_intent(user_query)
            
            
            capable_agents = await self._find_capable_agents_with_context(user_query, intent_analysis)
            
            if not capable_agents:
                response = "I can help you with EPLAN electrical software. What would you like to know?"
                await self._record_response(response, "fallback")
                return response
            
            
            request_id = await self._delegate_to_agents(capable_agents, user_query, intent_analysis)
            
           
            response = await self._wait_for_agent_response(request_id)
            
            await self._record_response(response, "delegated")
            return response
    
    async def _analyze_user_intent(self, query: str) -> Dict[str, Any]:
        """Improved intent analysis with historical context"""
                
        recent_context = self._get_recent_conversation_context()
        
        prompt = f"""Analyze user intent with conversation context:
        
Current query: "{query}"

Recent conversation context:
{recent_context}

Determine:
1. Primary intent (technical_help, code_generation, documentation, general_chat)
2. Complexity level (simple, moderate, complex)
3. Required agents (knowledge, codecraft, execution, etc.)
4. Context dependencies (needs previous conversation context?)

Return JSON:"""
        
        try:
            response = await self.ai_client.generate(prompt)
            import json
            intent_data = json.loads(response.strip())
            
            await self.update_scratchpad("last_intent_analysis", {
                "query": query,
                "analysis": intent_data,
                "timestamp": time.time()
            })
            
            return intent_data
        except Exception as e:
            await self.log_to_scratchpad(f"Intent analysis error: {e}", "error")
            return {
                "primary_intent": "general_help",
                "complexity": "simple",
                "required_agents": ["knowledge"],
                "context_dependencies": False
            }
    
    async def _find_capable_agents_with_context(self, query: str, intent_analysis: Dict) -> List[str]:
        """Search for capable agents considering intent analysis"""
                
        suggested_agents = intent_analysis.get("required_agents", [])
        
        if suggested_agents:            
            available_agents = []
            for agent_id in suggested_agents:
                if agent_id in self.bus.agents:
                    confidence = await self.bus.agents[agent_id].can_handle(query)
                    if confidence > 0.5:
                        available_agents.append(agent_id)
            
            if available_agents:
                await self.log_to_scratchpad(
                    f"Found capable agents via intent analysis: {available_agents}",
                    "agent_selection"
                )
                return available_agents
                
        return await self.bus.find_capable_agents(query)
    
    async def _delegate_to_agents(self, agents: List[str], query: str, intent_analysis: Dict) -> str:
        """Enhanced delegation with rich context"""
        
        request_id = f"req_{int(time.time() * 1000)}"
        
        enriched_context = {
            "user_query": query,
            "intent_analysis": intent_analysis,
            "conversation_context": self._get_recent_conversation_context(),
            "request_id": request_id,
            "requester": "user_via_conversation"
        }
        
        context_ref = await self.store_heavy_context(
            enriched_context,
            metadata={"type": "delegation_context", "agents": agents}
        )
        
        await self.send_message(
            agents,
            "enhanced_user_request",
            {
                "query": query[:100],  
                "complexity": intent_analysis.get("complexity"),
                "request_id": request_id
            },
            heavy_context=enriched_context
        )
        
        self.active_requests[request_id] = {
            "timestamp": time.time(),
            "agents": agents,
            "query": query,
            "status": "pending"
        }
        
        return request_id
    
    async def _wait_for_agent_response(self, request_id: str, timeout: float = 15.0) -> str:
        """Wait for agent response with enhanced timeout"""
        
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            if self.user_response:
                response = self.user_response
                self.user_response = None

                if request_id in self.active_requests:
                    self.active_requests[request_id]["status"] = "completed"
                    self.active_requests[request_id]["completed_at"] = time.time()
                
                return response
            
            await asyncio.sleep(0.1)
        
        if request_id in self.active_requests:
            self.active_requests[request_id]["status"] = "timeout"
            agents = self.active_requests[request_id]["agents"]
            
            await self.log_to_scratchpad(
                f"Request {request_id} timed out waiting for agents: {agents}",
                "timeout"
            )
        
        return "I'm still processing your request. This is taking longer than expected. Could you try rephrasing your question?"
    
    async def _try_direct_response(self, query: str) -> str:
        """Enhanced direct response with historical context"""
        
        conversation_context = self._get_recent_conversation_context()
        
        prompt = f"""User query: "{query}"

Conversation context:
{conversation_context}

If this is about:
- Complex EPLAN 2025 technical actions
- EPLAN 2025 script generation  
- EPLAN 2025 API documentation lookup
Return: "DELEGATE"

If this is:
- Simple greeting/chat
- Basic EPLAN 2025 questions I can answer directly
- Follow-up to previous conversation

Respond naturally considering the conversation context."""
        
        response = await self.ai_client.generate(prompt)
        
        if "DELEGATE" in response:
            return None
        
        return response
    
    def _get_recent_conversation_context(self, limit: int = 5) -> str:
        """Get context of recent conversation"""
        if not self.conversation_history:
            return "No previous conversation"
        
        recent_entries = self.conversation_history[-limit:]
        context_lines = []
        
        for entry in recent_entries:
            timestamp = entry.get("timestamp", 0)
            entry_type = entry.get("type", "unknown")
            content = entry.get("content", "")[:100]  # Limit content
            
            context_lines.append(f"[{entry_type}] {content}")
        
        return "\n".join(context_lines)
    
    def _get_conversation_id(self) -> str:
        """Generate/Get Current Conversation ID"""
        if not self.current_conversation:
            self.current_conversation = f"conv_{int(time.time())}"
        return self.current_conversation
    
    async def _record_response(self, response: str, response_type: str):
        """Record response in history"""
        response_entry = {
            "timestamp": time.time(),
            "type": "agent_response",
            "response_type": response_type,
            "content": response,
            "conversation_id": self._get_conversation_id()
        }
        
        self.conversation_history.append(response_entry)
        
        if len(self.conversation_history) % 10 == 0:
            await self.save_state()
    
    # === Message Processing ===
    async def process_message_with_context(self, message: AgentMessage, contexts: Dict[str, Any]):
        """Improved processing with resolved context"""
        
        if message.intent == "response_to_user":
            content = message.payload.get("content", "No response available")
            
            if contexts:
                for context_id, context_data in contexts.items():
                    if "enriched_response" in context_data:
                        content = context_data["enriched_response"]
                        break
            
            self.user_response = content
            
            await self.log_to_scratchpad(
                f"Received response from {message.sender}: {content[:100]}",
                "response_received"
            )
        
        else:
            await self.process_message(message)
    
    async def startup(self):
        """Enhanced startup with O-A-R loop"""
        await super().startup()  
        await self.start_observation_loop()

    async def shutdown(self):
        """Enhanced shutdown with O-A-R cleanup"""
        self.reflection_enabled = False
        if self._observation_task:
            self._observation_task.cancel()
        await super().shutdown() 


    async def process_message(self, message: AgentMessage):
        """Basic message processing"""
        if message.sender == "filesystem":
            await self.fs_helper.handle_filesystem_response(message)
            return
        
        await self.log_to_scratchpad(
            f"Processed message: {message.intent} from {message.sender}",
            "message_processing"
        )
    
    async def start_observation_loop(self):
        """Start proactive loop"""
        self._observation_task = asyncio.create_task(self._observation_action_reflection_loop())

    async def _observation_action_reflection_loop(self):
        """Main loop O-A-R"""
        while self.reflection_enabled:
            try:
                # Observar
                observations = await self._observe_system_state()
                
                # Decidir acción proactiva
                if observations.get("needs_proactive_action"):
                    action = await self._decide_proactive_action(observations)
                    if action:
                        await self._execute_proactive_action(action)
                        await self._reflect_on_action(action, observations)
                
                await asyncio.sleep(self.observation_interval)
            except Exception as e:
                await self.log_to_scratchpad(f"O-A-R loop error: {e}", "error")

    async def _observe_system_state(self) -> Dict:
        """Observe system status"""
        observations = {
            "recent_conversations": len(self.conversation_history[-10:]),
            "active_requests": len(self.active_requests),
            "last_interaction_time": self.conversation_history[-1]["timestamp"] if self.conversation_history else 0,
            "needs_proactive_action": False
        }
        
        if time.time() - observations["last_interaction_time"] > 300:  # 5 min
            observations["needs_proactive_action"] = True
            observations["suggested_action"] = "offer_help"
        
        return observations

    async def _decide_proactive_action(self, observations: Dict) -> Optional[Dict]:
        """Decide on proactive action based on observations"""
        if observations.get("suggested_action") == "offer_help":
            return {
                "type": "proactive_help",
                "message": "I notice you haven't interacted in a while. Do you need help with EPLAN tasks?"
            }
        return None

    async def _execute_proactive_action(self, action: Dict):
        """Take proactive action"""
        if action["type"] == "proactive_help":
            print(f"\n🤖 {action['message']}")

    async def _reflect_on_action(self, action: Dict, observations: Dict):
        """Reflect on the results of the action"""
        reflection = {
            "timestamp": time.time(),
            "action": action,
            "observations": observations,
            "outcome": "executed"  # Simplified
        }
        
        self.reflection_history.append(reflection)
        if len(self.reflection_history) > 50:
            self.reflection_history.pop(0)

    async def can_handle(self, intent: str) -> float:
        """Enhanced capacity with conversational context"""
        
        conversational_keywords = [
            "hello", "hi", "help", "what", "how", "explain", 
            "greet", "chat", "conversation"
        ]
        
        if any(keyword in intent.lower() for keyword in conversational_keywords):
            return 0.8

        eplan_conversational = [
            "eplan questions", "eplan help", "basic eplan", "eplan software"
        ]
        
        if any(phrase in intent.lower() for phrase in eplan_conversational):
            return 0.6

        technical_keywords = [
            "script", "code", "api", "action", "execute", "generate"
        ]
        
        if any(keyword in intent.lower() for keyword in technical_keywords):
            return 0.2 
        
        return 0.3