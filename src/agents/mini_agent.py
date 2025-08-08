# src/agents/mini_agent.py
import asyncio
import time
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from ..ai import GeminiClient
from ..core.message_bus import ObservableMessageBus, AgentMessage, ObservabilityDashboard
from ..core.filesystem_helpers import FileSystemHelper, ContextReference
from ..core.error_handling import ErrorHandler
from ..core.intelligent_cache import cache_manager
from ..core.parallel_processor import parallel_processor, batch_processor


class MiniAgent(ABC):
    """Enhanced mini-agent with full observability support"""
    
    def __init__(self, agent_id: str, message_bus: ObservableMessageBus):
        self.id = agent_id
        self.bus = message_bus
        self.ai_client = GeminiClient()
        self.error_handler = ErrorHandler()
        self.agent_cache = cache_manager.get_cache(agent_id)
        self.parallel_processor = parallel_processor
        self.working = False
        self.message_queue = asyncio.Queue()
        
        self.fs_helper = FileSystemHelper(agent_id, message_bus)
        self.context_cache = {}
        self.state_loaded = False
        
        self.dashboard = None  
        self.current_conversation_id = None
        self.processing_metrics = {}
        
        asyncio.create_task(self._load_persistent_state())
        print(f"🤖 {agent_id} initialized with observability support")
    
    def _set_observability_dashboard(self, dashboard: ObservabilityDashboard):
        """Inject observability dashboard (called by MessageBus)"""
        self.dashboard = dashboard
    
    # === Enhanced Message Handling ===
    async def receive_message(self, message: AgentMessage):
        """Enhanced receive with observability tracking"""
        await self.message_queue.put(message)
        
        if message.conversation_id:
            self.current_conversation_id = message.conversation_id
        
        if not self.working:
            asyncio.create_task(self._process_queue())
    
    async def _process_queue(self):
        """Process message queue with robust error handling"""
        self.working = True
        try:
            while not self.message_queue.empty():
                message = await self.message_queue.get()
                
                success, result = await self.error_handler.safe_call(
                    self._process_single_message,
                    f"{self.id}_message_processing",
                    message
                )
                
                if not success:
                    await self._handle_processing_error(message, result)
        finally:
            self.working = False

    async def _process_single_message(self, message: AgentMessage):
        """Process single message with error tracking"""
        start_time = time.time()
        
        await self._log_structured_event({
            "event_type": "message_processing_start",
            "correlation_id": message.correlation_id,
            "intent": message.intent,
            "sender": message.sender
        })
        
        resolved_contexts = await self.resolve_context_refs(message)
        await self.process_message_with_context(message, resolved_contexts)
        
        if self._should_complete_flow(message):
            self.dashboard.complete_flow(message.trace_id, True)
        
        processing_time = time.time() - start_time
        self._update_processing_metrics(message.intent, processing_time)

    async def _handle_processing_error(self, message: AgentMessage, error: str):
        """Handle processing errors gracefully"""
        await self._log_structured_event({
            "event_type": "message_processing_error",
            "correlation_id": message.correlation_id,
            "error": error,
            "fallback_triggered": True
        })
        
        # Graceful fallback
        await self.send_message(
            ["conversation"],
            "response_to_user",
            {
                "content": f"I encountered an issue processing your request: {error[:100]}... Please try again.",
                "source": self.id,
                "status": "error_fallback"
            },
            parent_message=message
        )
    
    def _should_complete_flow(self, message: AgentMessage) -> bool:
        """Determine if this message completes a flow"""
        return message.intent in ["response_to_user", "final_result", "task_completed"]
    
    def _update_processing_metrics(self, intent: str, processing_time: float):
        """Update processing time metrics"""
        if intent not in self.processing_metrics:
            self.processing_metrics[intent] = []
        
        self.processing_metrics[intent].append(processing_time)
        
        if len(self.processing_metrics[intent]) > 100:
            self.processing_metrics[intent] = self.processing_metrics[intent][-100:]
    
    # === Enhanced Message Sending ===
    async def send_message(self, recipients: List[str], intent: str, payload: dict, 
                          heavy_context: Any = None, context_metadata: Dict = None,
                          parent_message: AgentMessage = None):
        """Enhanced send with correlation chain tracking"""
        
        context_refs = []
        if heavy_context is not None:
            context_ref = await self.store_heavy_context(
                heavy_context, 
                metadata=context_metadata
            )
            if context_ref:
                context_refs.append(context_ref.get_id())
        
        if parent_message:
            message = parent_message.create_child_message(self.id, recipients, intent, payload)
        else:
            message = AgentMessage(
                sender=self.id,
                recipients=recipients,
                intent=intent,
                payload=payload,
                conversation_id=self.current_conversation_id
            )
        
        if context_refs:
            message.payload["context_refs"] = context_refs
            message.payload["has_heavy_context"] = True
        
        await self.bus.broadcast(message)
        
        await self._log_structured_event({
            "event_type": "message_sent",
            "correlation_id": message.correlation_id,
            "parent_correlation_id": message.parent_correlation_id,
            "intent": intent,
            "recipients": recipients
        })
    
    # === Structured Logging ===
    async def _log_structured_event(self, event_data: Dict):
        """Log structured event with standard format"""
        structured_event = {
            "timestamp": time.time(),
            "iso_timestamp": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()),
            "agent_id": self.id,
            "conversation_id": self.current_conversation_id,
            **event_data
        }
        
        await self.log_to_scratchpad(structured_event, "structured_event")
        
        if hasattr(self.fs_helper, 'log_structured_event'):
            await self.fs_helper.log_structured_event(structured_event)
    
    async def log_to_scratchpad(self, message: Any, category: str = "general"):
        """Enhanced logging with structured format"""
        log_entry = {
            "timestamp": time.time(),
            "iso_timestamp": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()),
            "category": category,
            "agent_id": self.id,
            "conversation_id": self.current_conversation_id,
            "message": message if isinstance(message, (str, dict)) else str(message)
        }
        
        await self.fs_helper.update_scratchpad({"logs": [log_entry]}, "append")
    
    # === Performance Monitoring ===
    def get_performance_metrics(self) -> Dict:
        """Get current performance metrics"""
        metrics = {}
        
        for intent, times in self.processing_metrics.items():
            if times:
                metrics[intent] = {
                    "count": len(times),
                    "avg_time": sum(times) / len(times),
                    "min_time": min(times),
                    "max_time": max(times),
                    "recent_avg": sum(times[-10:]) / len(times[-10:]) if len(times) >= 10 else sum(times) / len(times)
                }
        
        return metrics
    
    async def measure_performance(self, operation_name: str):
        """Enhanced performance monitoring context manager"""
        return PerformanceMonitor(self, operation_name)
    
    # === Collaboration with Observability ===
    async def collaborate_with_agent(self, agent_id: str, task: str, context_data: Any = None,
                                   parent_message: AgentMessage = None) -> bool:
        """Enhanced collaboration with correlation tracking"""
        await self.send_message(
            [agent_id],
            "collaboration_request",
            {"task": task, "requester": self.id},
            heavy_context=context_data,
            parent_message=parent_message
        )
        
        await self._log_structured_event({
            "event_type": "collaboration_started",
            "collaborator": agent_id,
            "task": task
        })
        
        return True
    
    # === Abstract Methods ===
    @abstractmethod
    async def process_message_with_context(self, message: AgentMessage, contexts: Dict[str, Any]):
        """Process message with resolved contexts"""
        pass
    
    @abstractmethod
    def get_specialty(self) -> str:
        """Get agent specialty"""
        pass
    
    # === Compatibility Methods ===
    async def process_message(self, message):
        """Compatibility method for old message format"""
        if isinstance(message, AgentMessage):
            await self.process_message_with_context(message, {})
        else:
            enhanced_message = AgentMessage(
                sender=getattr(message, 'sender', 'unknown'),
                recipients=getattr(message, 'recipients', []),
                intent=getattr(message, 'intent', 'unknown'),
                payload=getattr(message, 'payload', {})
            )
            await self.process_message_with_context(enhanced_message, {})
    
    # === State Management (unchanged) ===
    async def _load_persistent_state(self):
        """Load persistent state at startup"""
        try:
            state = await self.fs_helper.load_agent_state()
            if state:
                await self._restore_from_state(state)
                print(f"📂 {self.id} restored from persistent state")
            self.state_loaded = True
        except Exception as e:
            print(f"⚠️ {self.id} couldn't load state: {e}")
            self.state_loaded = True
    
    async def _restore_from_state(self, state: Dict):
        """Restore agent from saved state"""
        pass
    
    async def _get_current_state(self) -> Dict:
        """Get current state to persist"""
        return {
            "agent_id": self.id,
            "last_save": time.time(),
            "processing_metrics": self.processing_metrics
        }
    
    async def save_state(self) -> bool:
        """Save current state to filesystem"""
        current_state = await self._get_current_state()
        return await self.fs_helper.save_agent_state(current_state)
    
    # === Context Management (unchanged) ===
    async def store_heavy_context(self, data: Any, context_id: str = None, metadata: Dict = None) -> ContextReference:
        """Store heavy context and get light reference"""
        result = await self.fs_helper.store_context(data, context_id, metadata)
        if result.get("success"):
            ref = result.get("reference", {})
            context_id = ref.get("context_id")
            if context_id:
                context_ref = ContextReference(self.fs_helper, context_id)
                self.context_cache[context_id] = context_ref
                return context_ref
        return None
    
    async def get_context_data(self, context_ref: ContextReference) -> Optional[Dict]:
        """Getting full data from a context reference"""
        return await context_ref.load()
    
    async def resolve_context_refs(self, message: AgentMessage) -> Dict[str, Any]:
        """Resolving context references in a received message"""
        resolved_contexts = {}
        
        if message.payload.get("has_heavy_context"):
            context_refs = message.payload.get("context_refs", [])
            
            for ref_id in context_refs:
                if ref_id in self.context_cache:
                    context_ref = self.context_cache[ref_id]
                else:
                    context_ref = ContextReference(self.fs_helper, ref_id)
                    self.context_cache[ref_id] = context_ref
                
                context_data = await context_ref.load()
                if context_data:
                    resolved_contexts[ref_id] = context_data
        
        return resolved_contexts
    
    # === Lifecycle Management ===
    async def startup(self):
        """Agent initialization with observability"""
        while not self.state_loaded:
            await asyncio.sleep(0.1)
        
        await self.init_scratchpad({
            "agent_id": self.id,
            "startup_time": time.time(),
            "specialty": self.get_specialty()
        })
        
        await self._log_structured_event({
            "event_type": "agent_started",
            "specialty": self.get_specialty()
        })
        await self.start_observation_loop()
    
    async def shutdown(self):
        """Clean closing with observability"""
        await self._log_structured_event({
            "event_type": "agent_shutdown",
            "final_metrics": self.get_performance_metrics()
        })
        
        await self.save_state()
    
    async def start_observation_loop(self):
        """Default empty observation loop - can be overridden by agents"""
        # Default implementation does nothing
        # ConversationAgent will override this with actual O-A-R loop
        pass

    # === Scratchpad Operations (unchanged) ===
    async def init_scratchpad(self, initial_data: Dict = None):
        """Initialize personal scratchpad"""
        await self.fs_helper.create_scratchpad(initial_data)
    
    async def update_scratchpad(self, key: str, value: Any):
        """Update a value in scratchpad"""
        await self.fs_helper.update_scratchpad({key: value}, "merge")


class PerformanceMonitor:
    """Enhanced context manager for performance monitoring with observability"""
    
    def __init__(self, agent: MiniAgent, operation: str):
        self.agent = agent
        self.operation = operation
        self.start_time = None
    
    async def __aenter__(self):
        self.start_time = time.time()
        
        await self.agent._log_structured_event({
            "event_type": "operation_start",
            "operation": self.operation
        })
        
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        duration = time.time() - self.start_time
        success = exc_type is None
        
        self.agent._update_processing_metrics(f"operation_{self.operation}", duration)
        
        await self.agent._log_structured_event({
            "event_type": "operation_complete",
            "operation": self.operation,
            "duration": duration,
            "success": success,
            "error": str(exc_val) if exc_val else None
        })
        
        await self.agent.update_scratchpad("performance_metrics", {
            self.operation: {
                "duration": duration,
                "timestamp": time.time(),
                "success": success
            }
        })