# src/core/filesystem_helpers.py
import json
import asyncio
from pathlib import Path
from typing import Dict, Any, Optional

class ContextReference:
    """Referencia ligera a contexto almacenado en filesystem"""
    
    def __init__(self, fs_helper: 'FileSystemHelper', context_id: str):
        self.fs_helper = fs_helper
        self.context_id = context_id
    
    def get_id(self) -> str:
        return self.context_id
    
    async def load(self) -> Optional[Dict]:
        """Load full context data"""
        return await self.fs_helper.get_context(self.context_id)


class FileSystemHelper:
    """Helper for integration with FileSystemAgent"""
    
    def __init__(self, agent_id: str, message_bus):
        self.agent_id = agent_id
        self.bus = message_bus
        self.pending_requests = {}
    
    async def store_context(self, data: Any, context_id: str = None, metadata: Dict = None) -> Dict:
        """Store context and get reference - INCREASED TIMEOUT"""
        if context_id is None:
            import time
            context_id = f"{self.agent_id}_{int(time.time() * 1000)}"
        
        request_id = f"store_{context_id}"
        self.pending_requests[request_id] = asyncio.Future()
        
        from ..core.message_bus import AgentMessage
        message = AgentMessage(
            sender=self.agent_id,
            recipients=["filesystem"],
            intent="store_context",
            payload={
                "context_id": context_id,
                "data": data,
                "metadata": metadata or {},
                "request_id": request_id
            }
        )
        await self.bus.broadcast(message)
        
        try:
            result = await asyncio.wait_for(self.pending_requests[request_id], timeout=30.0)
            return result
        except asyncio.TimeoutError:
            return {"success": False, "error": "Timeout"}
        finally:
            if request_id in self.pending_requests:
                del self.pending_requests[request_id]
    
    async def get_context(self, context_id: str) -> Optional[Dict]:
        """Get context by ID"""
        request_id = f"get_{context_id}"
        self.pending_requests[request_id] = asyncio.Future()
        
        from ..core.message_bus import AgentMessage
        message = AgentMessage(
            sender=self.agent_id,
            recipients=["filesystem"],
            intent="get_context",
            payload={
                "context_id": context_id,
                "request_id": request_id
            }
        )
        await self.bus.broadcast(message)
        
        try:
            result = await asyncio.wait_for(self.pending_requests[request_id], timeout=30.0)
            return result.get("context", {}).get("data") if result else None
        except asyncio.TimeoutError:
            return None
        finally:
            if request_id in self.pending_requests:
                del self.pending_requests[request_id]
    
    
    async def create_scratchpad(self, initial_data: Dict = None):
        """Create scratchpad for agent"""
        pass
    
    async def update_scratchpad(self, data: Dict, operation: str = "merge"):
        """Update scratchpad data"""
        pass
    
    async def load_agent_state(self) -> Optional[Dict]:
        """Load agent state from filesystem"""
        request_id = f"load_state_{self.agent_id}"
        self.pending_requests[request_id] = asyncio.Future()
        
        from ..core.message_bus import AgentMessage
        message = AgentMessage(
            sender=self.agent_id,
            recipients=["filesystem"],
            intent="get_state",
            payload={
                "state_id": f"{self.agent_id}_state",
                "request_id": request_id
            }
        )
        await self.bus.broadcast(message)
        
        try:
            result = await asyncio.wait_for(self.pending_requests[request_id], timeout=30.0)
            return result.get("state", {}).get("data") if result else None
        except asyncio.TimeoutError:
            return None
        finally:
            if request_id in self.pending_requests:
                del self.pending_requests[request_id]
    
    async def save_agent_state(self, state: Dict) -> bool:
        """Save agent state to filesystem"""
        request_id = f"save_state_{self.agent_id}"
        self.pending_requests[request_id] = asyncio.Future()
        
        from ..core.message_bus import AgentMessage
        message = AgentMessage(
            sender=self.agent_id,
            recipients=["filesystem"],
            intent="save_state",
            payload={
                "state_id": f"{self.agent_id}_state",
                "state": state,
                "request_id": request_id
            }
        )
        await self.bus.broadcast(message)
        
        try:
            result = await asyncio.wait_for(self.pending_requests[request_id], timeout=30.0)
            return result.get("success", False)
        except asyncio.TimeoutError:
            return False
        finally:
            if request_id in self.pending_requests:
                del self.pending_requests[request_id]
    
    async def log_structured_event(self, event_data: Dict):
        """Log structured event via filesystem agent"""
        # Send to filesystem agent for logging
        from ..core.message_bus import AgentMessage
        message = AgentMessage(
            sender=self.agent_id,
            recipients=["filesystem"],
            intent="log_event",
            payload=event_data
        )
        await self.bus.broadcast(message)
    
    def handle_filesystem_response(self, message):
        """Handling FileSystemAgent responses"""
        request_id = message.payload.get("request_id")
        if request_id in self.pending_requests and not self.pending_requests[request_id].done():
            if message.intent == "context_stored":
                self.pending_requests[request_id].set_result(message.payload)
            elif message.intent == "context_retrieved":
                self.pending_requests[request_id].set_result(message.payload)
            elif message.intent == "scratchpad_created":
                self.pending_requests[request_id].set_result({"success": True})
            elif message.intent == "scratchpad_updated":
                self.pending_requests[request_id].set_result({"success": True})
            elif message.intent == "state_retrieved":
                self.pending_requests[request_id].set_result(message.payload)
            elif message.intent == "state_saved":
                self.pending_requests[request_id].set_result(message.payload)
            elif message.intent in ["context_error", "context_not_found", "scratchpad_error", "state_error", "state_not_found"]:
                self.pending_requests[request_id].set_result({"success": False, "error": message.payload.get("error")})