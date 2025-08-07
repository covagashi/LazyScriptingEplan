# src/agents/filesystem_agent.py
import os
import json
import time
import asyncio
from pathlib import Path
from typing import Dict, Any, List, Optional
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from .mini_agent import MiniAgent
from ..core.message_bus import AgentMessage

class FileSystemAgent(MiniAgent):
    """Agent that handles persistent context and reactive filesystem"""
    
    def __init__(self, message_bus):
        super().__init__("filesystem", message_bus)
        self.base_path = Path(r"C:\temp\Agent\Context")
        self.base_path.mkdir(exist_ok=True, parents=True)
        
        self.scratchpads_path = self.base_path / "scratchpads"
        self.context_path = self.base_path / "context"
        self.outputs_path = self.base_path / "outputs"
        self.state_path = self.base_path / "state"
        
        for path in [self.scratchpads_path, self.context_path, self.outputs_path, self.state_path]:
            path.mkdir(exist_ok=True)
        
        self.observer = Observer()
        self.file_handler = FileSystemWatcher(self)
        self.observer.schedule(self.file_handler, str(self.base_path), recursive=True)
        self.observer.start()
        
        self.memory_cache = {}
        self.context_refs = {}
        
        print(f"📁 FileSystemAgent initialized at {self.base_path}")
    
    def get_specialty(self) -> str:
        return "Persistent context storage, filesystem operations, agent scratchpads"
    
    async def process_message(self, message: AgentMessage):
        intent = message.intent
        payload = message.payload
        sender = message.sender
        
        if intent == "store_context":
            await self._store_context(sender, payload)
        elif intent == "get_context":
            await self._get_context(sender, payload)
        elif intent == "create_scratchpad":
            await self._create_scratchpad(sender, payload)
        elif intent == "update_scratchpad":
            await self._update_scratchpad(sender, payload)
        elif intent == "store_output":
            await self._store_output(sender, payload)
        elif intent == "get_state":
            await self._get_state(sender, payload)
        elif intent == "save_state":
            await self._save_state(sender, payload)
        elif intent == "cleanup":
            await self._cleanup_old_files()
    
    # === Context Management ===
    async def _store_context(self, sender: str, payload: Dict[str, Any]):
        """Storing heavy context in filesystem"""
        context_id = payload.get("context_id", f"{sender}_{int(time.time())}")
        data = payload.get("data")
        metadata = payload.get("metadata", {})
        
        context_file = self.context_path / f"{context_id}.json"
        
        context_data = {
            "id": context_id,
            "sender": sender,
            "timestamp": time.time(),
            "metadata": metadata,
            "data": data
        }
        
        try:
            with open(context_file, 'w', encoding='utf-8') as f:
                json.dump(context_data, f, indent=2, ensure_ascii=False)
            
            self.memory_cache[context_id] = context_data
            a
            ref = {
                "context_id": context_id,
                "file_path": str(context_file),
                "size": context_file.stat().st_size,
                "timestamp": time.time()
            }
            self.context_refs[context_id] = ref
            
            await self.send_message(
                [sender],
                "context_stored",
                {"reference": ref, "success": True}
            )
            
        except Exception as e:
            await self.send_message(
                [sender],
                "context_error",
                {"error": str(e), "context_id": context_id}
            )
    
    async def _get_context(self, sender: str, payload: Dict[str, Any]):
        """Retrieve context by ID"""
        context_id = payload.get("context_id")
        
        if context_id in self.memory_cache:
            context_data = self.memory_cache[context_id]
        else:
            context_file = self.context_path / f"{context_id}.json"
            if not context_file.exists():
                await self.send_message(
                    [sender],
                    "context_not_found",
                    {"context_id": context_id}
                )
                return
            
            try:
                with open(context_file, 'r', encoding='utf-8') as f:
                    context_data = json.load(f)
                self.memory_cache[context_id] = context_data
            except Exception as e:
                await self.send_message(
                    [sender],
                    "context_error", 
                    {"error": str(e), "context_id": context_id}
                )
                return
        
        await self.send_message(
            [sender],
            "context_retrieved",
            {"context": context_data, "context_id": context_id}
        )
    
    # === Scratchpad Management ===
    async def _create_scratchpad(self, sender: str, payload: Dict[str, Any]):
        """Create individual scratchpad for an agent"""
        agent_id = payload.get("agent_id", sender)
        initial_data = payload.get("data", {})
        
        scratchpad_file = self.scratchpads_path / f"{agent_id}_scratch.json"
        
        scratchpad_data = {
            "agent_id": agent_id,
            "created": time.time(),
            "updated": time.time(),
            "data": initial_data,
            "history": []
        }
        
        try:
            with open(scratchpad_file, 'w', encoding='utf-8') as f:
                json.dump(scratchpad_data, f, indent=2)
            
            await self.send_message(
                [sender],
                "scratchpad_created",
                {"scratchpad_path": str(scratchpad_file), "agent_id": agent_id}
            )
            
        except Exception as e:
            await self.send_message(
                [sender],
                "scratchpad_error",
                {"error": str(e), "agent_id": agent_id}
            )
    
    async def _update_scratchpad(self, sender: str, payload: Dict[str, Any]):
        """Update agent scratchpad"""
        agent_id = payload.get("agent_id", sender)
        update_data = payload.get("data")
        operation = payload.get("operation", "merge")  # merge, replace, append
        
        scratchpad_file = self.scratchpads_path / f"{agent_id}_scratch.json"
        
        if not scratchpad_file.exists():
            # Create if doesn't exist
            await self._create_scratchpad(sender, {"agent_id": agent_id, "data": update_data})
            return
        
        try:
            with open(scratchpad_file, 'r', encoding='utf-8') as f:
                scratchpad_data = json.load(f)
            
            scratchpad_data["history"].append({
                "timestamp": time.time(),
                "operation": operation,
                "data": scratchpad_data["data"].copy()
            })
            
            if operation == "replace":
                scratchpad_data["data"] = update_data
            elif operation == "merge":
                if isinstance(scratchpad_data["data"], dict) and isinstance(update_data, dict):
                    scratchpad_data["data"].update(update_data)
                else:
                    scratchpad_data["data"] = update_data
            elif operation == "append":
                if isinstance(scratchpad_data["data"], list):
                    scratchpad_data["data"].extend(update_data if isinstance(update_data, list) else [update_data])
                else:
                    scratchpad_data["data"] = [scratchpad_data["data"], update_data]
            
            scratchpad_data["updated"] = time.time()
            
            with open(scratchpad_file, 'w', encoding='utf-8') as f:
                json.dump(scratchpad_data, f, indent=2)
            
            await self.send_message(
                [sender],
                "scratchpad_updated",
                {"success": True, "agent_id": agent_id}
            )
            
        except Exception as e:
            await self.send_message(
                [sender],
                "scratchpad_error",
                {"error": str(e), "agent_id": agent_id}
            )
    
    # === Output Management ===
    async def _store_output(self, sender: str, payload: Dict[str, Any]):
        """Store agent outputs (scripts, results, etc.)"""
        output_type = payload.get("type", "general")
        content = payload.get("content")
        filename = payload.get("filename")
        
        if not filename:
            timestamp = int(time.time())
            filename = f"{sender}_{output_type}_{timestamp}"
        
        extensions = {
            "script": ".cs",
            "text": ".txt", 
            "json": ".json",
            "log": ".log"
        }
        ext = extensions.get(output_type, ".txt")
        
        output_file = self.outputs_path / f"{filename}{ext}"
        
        try:
            if output_type == "json":
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(content, f, indent=2, ensure_ascii=False)
            else:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(str(content))
            
            await self.send_message(
                [sender],
                "output_stored",
                {
                    "file_path": str(output_file),
                    "type": output_type,
                    "size": output_file.stat().st_size
                }
            )
            
        except Exception as e:
            await self.send_message(
                [sender],
                "output_error",
                {"error": str(e), "filename": filename}
            )
    
    # === State Management ===
    async def _save_state(self, sender: str, payload: Dict[str, Any]):
        """Save persistent system state"""
        state_data = payload.get("state")
        state_id = payload.get("state_id", "system_state")
        
        state_file = self.state_path / f"{state_id}.json"
        
        full_state = {
            "state_id": state_id,
            "timestamp": time.time(),
            "saved_by": sender,
            "data": state_data
        }
        
        try:
            with open(state_file, 'w', encoding='utf-8') as f:
                json.dump(full_state, f, indent=2)
            
            await self.send_message(
                [sender],
                "state_saved",
                {"state_id": state_id, "success": True}
            )
            
        except Exception as e:
            await self.send_message(
                [sender],
                "state_error",
                {"error": str(e), "state_id": state_id}
            )
    
    async def _get_state(self, sender: str, payload: Dict[str, Any]):
        """Recover persistent state"""
        state_id = payload.get("state_id", "system_state")
        state_file = self.state_path / f"{state_id}.json"
        
        if not state_file.exists():
            await self.send_message(
                [sender],
                "state_not_found", 
                {"state_id": state_id}
            )
            return
        
        try:
            with open(state_file, 'r', encoding='utf-8') as f:
                state_data = json.load(f)
            
            await self.send_message(
                [sender],
                "state_retrieved",
                {"state": state_data, "state_id": state_id}
            )
            
        except Exception as e:
            await self.send_message(
                [sender],
                "state_error",
                {"error": str(e), "state_id": state_id}
            )
    
    # === Utilities ===
    async def _cleanup_old_files(self):
        """Clean up old files (>7 days)"""
        cutoff = time.time() - (7 * 24 * 3600)  # 7 días
        cleaned = 0
        
        for folder in [self.context_path, self.outputs_path]:
            for file in folder.glob("*.json"):
                if file.stat().st_mtime < cutoff:
                    try:
                        file.unlink()
                        cleaned += 1
                    except:
                        pass
        
        print(f"🧹 Cleaned {cleaned} old files")
    
    def get_context_reference(self, context_id: str) -> Optional[Dict]:
        """Get lightweight reference for MessageBus"""
        return self.context_refs.get(context_id)
    
    def __del__(self):
        """Cleanup al destruir el agente"""
        if hasattr(self, 'observer'):
            self.observer.stop()
            self.observer.join()


class FileSystemWatcher(FileSystemEventHandler):
    """Reactive monitor of filesystem changes"""
    
    def __init__(self, fs_agent):
        self.fs_agent = fs_agent
        super().__init__()
    
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith('.json'):            
            asyncio.create_task(self._notify_file_created(event.src_path))
    
    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith('.json'):           
            file_path = Path(event.src_path)
            for context_id, cached_data in list(self.fs_agent.memory_cache.items()):
                if file_path.name == f"{context_id}.json":
                    del self.fs_agent.memory_cache[context_id]
                    break
    
    async def _notify_file_created(self, file_path: str):
        """Notify interested agents about new files"""
        await self.fs_agent.send_message(
            ["conversation", "feedback"],  
            "file_created",
            {"file_path": file_path, "timestamp": time.time()}
        )