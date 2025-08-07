# src/agents/mini_agent.py
import asyncio
import time
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from ..ai import GeminiClient
from ..core.message_bus import MessageBus, AgentMessage
from ..core.filesystem_helpers import FileSystemHelper, ContextReference

class EnhancedMiniAgent(ABC):
    """Improved mini-agent with filesystem integration and persistent context"""
    
    def __init__(self, agent_id: str, message_bus: MessageBus):
        self.id = agent_id
        self.bus = message_bus
        self.ai_client = GeminiClient()
        self.working = False
        self.message_queue = asyncio.Queue()
        
        # FileSystem integration
        self.fs_helper = FileSystemHelper(agent_id, message_bus)
        self.context_cache = {}  # Cache local de referencias
        self.state_loaded = False
        
        # Inicializar estado persistente
        asyncio.create_task(self._load_persistent_state())
        
        print(f"🤖 {agent_id} initialized with filesystem support")
    
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
        """Restore agent from saved state - implement in subclasses"""
        pass
    
    async def _get_current_state(self) -> Dict:
        """Get current state to persist - implement in subclasses"""
        return {
            "agent_id": self.id,
            "last_save": time.time()
        }
    
    async def save_state(self) -> bool:
        """Save current state to filesystem"""
        current_state = await self._get_current_state()
        return await self.fs_helper.save_agent_state(current_state)
    
    # === Context Management ===
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
    
    def create_lightweight_message(self, recipients: List[str], intent: str, 
                                 context_refs: List[str] = None, 
                                 light_payload: Dict = None) -> AgentMessage:
        """Create a lightweight message with heavy context references"""
        payload = light_payload or {}
        
        if context_refs:
            payload["context_refs"] = context_refs
            payload["has_heavy_context"] = True
        
        return AgentMessage(
            sender=self.id,
            recipients=recipients,
            intent=intent,
            payload=payload
        )
    
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
    
    # === Scratchpad Operations ===
    async def init_scratchpad(self, initial_data: Dict = None):
        """Initialize personal scratchpad"""
        await self.fs_helper.create_scratchpad(initial_data)
    
    async def update_scratchpad(self, key: str, value: Any):
        """Update a value in scratchpad"""
        await self.fs_helper.update_scratchpad({key: value}, "merge")
    
    async def append_to_scratchpad(self, key: str, item: Any):
        """Add item to list in scratchpad"""
        current_scratch = await self.fs_helper.update_scratchpad({key: [item]}, "append")
    
    async def log_to_scratchpad(self, message: str, category: str = "general"):
        """Add log entry to scratchpad"""
        log_entry = {
            "timestamp": time.time(),
            "category": category,
            "message": message
        }
        await self.fs_helper.update_scratchpad({"logs": [log_entry]}, "append")
    
    # === Output Management ===
    async def save_output(self, content: Any, output_type: str = "text", filename: str = None) -> str:
        """Save output to filesystem"""
        return await self.fs_helper.store_output(content, output_type, filename)
    
    async def save_script(self, script_content: str, script_name: str = None) -> str:
        """Save generated C# script"""
        if script_name is None:
            script_name = f"{self.id}_generated_{int(time.time())}"
        
        return await self.save_output(script_content, "script", script_name)
    
    # === Enhanced Message Processing ===
    async def can_handle(self, intent: str) -> float:
        """Improved method with cache and context"""
        # Cache de decisiones can_handle para evitar LLM repetido
        cache_key = f"can_handle_{intent.lower()}"
        
        # Intentar desde scratchpad cache primero
        # (En implementación real, cargarías esto desde scratchpad) - claude arregla esto
        
        # Usar LLM con contexto de especialidad
        prompt = f"""Can I help with: "{intent}"?
        
My specialty: {self.get_specialty()}
My current capabilities: {await self._get_current_capabilities()}
        
Return confidence 0.0-1.0:"""
        
        try:
            response = await self.ai_client.generate(prompt)
            confidence = float(response.strip())
            
            await self.update_scratchpad(cache_key, {
                "confidence": confidence,
                "timestamp": time.time()
            })
            
            return confidence
        except Exception as e:
            await self.log_to_scratchpad(f"can_handle error: {e}", "error")
            return 0.0
    
    async def _get_current_capabilities(self) -> str:
        """Get description of current capabilities - implement in subclasses"""
        return "Basic agent capabilities"
    
    async def receive_message(self, message: AgentMessage):
        """Improved reception with persistent context"""
        await self.message_queue.put(message)
        if not self.working:
            asyncio.create_task(self._process_queue())
    
    async def _process_queue(self):
        """Improved message queue processing"""
        self.working = True
        try:
            while not self.message_queue.empty():
                message = await self.message_queue.get()
                
                await self.log_to_scratchpad(
                    f"Received message: {message.intent} from {message.sender}",
                    "message_flow"
                )
                
                resolved_contexts = await self.resolve_context_refs(message)
                
                await self.process_message_with_context(message, resolved_contexts)
                
        except Exception as e:
            await self.log_to_scratchpad(f"Queue processing error: {e}", "error")
        finally:
            self.working = False
    
    async def process_message_with_context(self, message: AgentMessage, contexts: Dict[str, Any]):
        """Process message with resolved contexts"""
        await self.process_message(message)
    
    async def send_message(self, recipients: List[str], intent: str, payload: dict, 
                          heavy_context: Any = None, context_metadata: Dict = None):
        """Improved shipping with automatic heavy context handling"""
        
        context_refs = []
        if heavy_context is not None:
            context_ref = await self.store_heavy_context(
                heavy_context, 
                metadata=context_metadata
            )
            if context_ref:
                context_refs.append(context_ref.get_id())
        
        if context_refs:
            message = self.create_lightweight_message(recipients, intent, context_refs, payload)
        else:
            message = AgentMessage(
                sender=self.id,
                recipients=recipients,
                intent=intent,
                payload=payload
            )
        
        await self.bus.broadcast(message)
        
        await self.log_to_scratchpad(
            f"Sent message: {intent} to {recipients}",
            "message_flow"
        )
    
    # === Collaboration Helpers ===
    async def collaborate_with_agent(self, agent_id: str, task: str, context_data: Any = None) -> bool:
        """Helper para colaboración directa con otro agente"""
        await self.send_message(
            [agent_id],
            "collaboration_request",
            {"task": task, "requester": self.id},
            heavy_context=context_data
        )
        return True
    
    async def request_knowledge(self, query: str, knowledge_type: str = "general") -> bool:
        """Request specific knowledge"""
        await self.send_message(
            ["knowledge"],
            "knowledge_request",
            {
                "query": query,
                "type": knowledge_type,
                "requester": self.id
            }
        )
        return True
    
    async def request_code_generation(self, specification: str, examples: List = None) -> bool:
        """Request code generation"""
        await self.send_message(
            ["codecraft"],
            "code_request",
            {
                "specification": specification,
                "requester": self.id
            },
            heavy_context={"examples": examples} if examples else None
        )
        return True
    
    # === Lifecycle Management ===
    async def startup(self):
        """Agent initialization - call after constructor"""
        while not self.state_loaded:
            await asyncio.sleep(0.1)
        
        await self.init_scratchpad({
            "agent_id": self.id,
            "startup_time": time.time(),
            "specialty": self.get_specialty()
        })
        
        await self.log_to_scratchpad("Agent started successfully", "lifecycle")
    
    async def shutdown(self):
        """Clean closing of the agent"""
        await self.log_to_scratchpad("Agent shutting down", "lifecycle")
        await self.save_state()
    
    # === Performance Monitoring ===
    async def measure_performance(self, operation_name: str):
        """Context manager to measure operations performance"""
        return PerformanceMonitor(self, operation_name)
    
    # === Abstract Methods ===
    @abstractmethod
    async def process_message(self, message: AgentMessage):
        """Process message - implement in subclasses"""
        pass
    
    @abstractmethod
    def get_specialty(self) -> str:
        """Get agent specialty - implement in subclasses"""
        pass


class PerformanceMonitor:
    """Context manager para medir performance"""
    
    def __init__(self, agent: EnhancedMiniAgent, operation: str):
        self.agent = agent
        self.operation = operation
        self.start_time = None
    
    async def __aenter__(self):
        self.start_time = time.time()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        duration = time.time() - self.start_time
        
        await self.agent.update_scratchpad("performance_metrics", {
            self.operation: {
                "duration": duration,
                "timestamp": time.time(),
                "success": exc_type is None
            }
        })
        
        if exc_type:
            await self.agent.log_to_scratchpad(
                f"Operation {self.operation} failed: {exc_val}",
                "performance"
            )
        else:
            await self.agent.log_to_scratchpad(
                f"Operation {self.operation} completed in {duration:.2f}s",
                "performance"
            )

