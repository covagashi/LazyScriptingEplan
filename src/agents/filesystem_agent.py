# src/agents/filesystem_agent.py
import os
import json
from datetime import datetime
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
        elif intent == "get_agent_logs":
            agent_id = payload.get("agent_id", sender)
            limit = payload.get("limit", 100)
            logs = await self.get_agent_logs(agent_id, limit)            
            await self.send_message(
                [sender],
                "agent_logs",
                {"logs": logs, "agent_id": agent_id, "count": len(logs)}
            )
        elif intent == "generate_observability_report":
            time_range = payload.get("time_range_hours", 24)
            report = await self.generate_observability_report(time_range)          
            report_file = self.base_path / "reports" / f"observability_report_{int(time.time())}.json"
            report_file.parent.mkdir(exist_ok=True)
            with open(report_file, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            
            await self.send_message(
                [sender],
                "observability_report_ready",
                {"report_file": str(report_file), "report": report}
            )
    
    
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
    

   
    async def log_structured_event(self, event_data: Dict):
        """Log structured event for observability aggregation"""
        logs_path = self.base_path / "logs"
        logs_path.mkdir(exist_ok=True)
        
        # Create daily log file
        today = datetime.now().strftime("%Y%m%d")
        log_file = logs_path / f"structured_events_{today}.jsonl"
        
        try:
            # Append to JSONL file
            with open(log_file, 'a', encoding='utf-8') as f:
                json.dump(event_data, f, ensure_ascii=False)
                f.write('\n')
        except Exception as e:
            print(f"⚠️ Failed to log structured event: {e}")

    async def get_agent_logs(self, agent_id: str, limit: int = 100) -> List[Dict]:
        """Get recent structured logs for an agent"""
        logs_path = self.base_path / "logs"
        
        if not logs_path.exists():
            return []
        
        # Read from recent log files
        agent_events = []
        
        # Check last 3 days of logs
        for i in range(3):
            date_offset = datetime.now() - timedelta(days=i)
            date_str = date_offset.strftime("%Y%m%d")
            log_file = logs_path / f"structured_events_{date_str}.jsonl"
            
            if log_file.exists():
                try:
                    with open(log_file, 'r', encoding='utf-8') as f:
                        for line in f:
                            event = json.loads(line.strip())
                            if event.get("agent_id") == agent_id:
                                agent_events.append(event)
                except Exception as e:
                    continue
        
        # Sort by timestamp and return recent
        agent_events.sort(key=lambda x: x.get("timestamp", 0), reverse=True)
        return agent_events[:limit]

    async def generate_observability_report(self, time_range_hours: int = 24) -> Dict:
        """Generate observability report from structured logs"""
        logs_path = self.base_path / "logs"
        
        if not logs_path.exists():
            return {"error": "No logs directory found"}
        
        cutoff_time = time.time() - (time_range_hours * 3600)
        
        report = {
            "time_range_hours": time_range_hours,
            "generated_at": datetime.now().isoformat(),
            "agent_activity": {},
            "message_flows": {},
            "error_summary": [],
            "performance_summary": {}
        }
        
        # Read recent log files
        for log_file in logs_path.glob("structured_events_*.jsonl"):
            try:
                with open(log_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        event = json.loads(line.strip())
                        
                        if event.get("timestamp", 0) < cutoff_time:
                            continue
                        
                        agent_id = event.get("agent_id", "unknown")
                        event_type = event.get("event_type", "unknown")
                        
                        # Agent activity
                        if agent_id not in report["agent_activity"]:
                            report["agent_activity"][agent_id] = {
                                "events": 0,
                                "event_types": {},
                                "errors": 0
                            }
                        
                        report["agent_activity"][agent_id]["events"] += 1
                        report["agent_activity"][agent_id]["event_types"][event_type] = \
                            report["agent_activity"][agent_id]["event_types"].get(event_type, 0) + 1
                        
                        # Error tracking
                        if "error" in event or event_type.endswith("_error"):
                            report["agent_activity"][agent_id]["errors"] += 1
                            report["error_summary"].append({
                                "agent": agent_id,
                                "timestamp": event.get("timestamp"),
                                "error": event.get("error", "Unknown error")
                            })
                        
                        # Message flow tracking
                        correlation_id = event.get("correlation_id")
                        if correlation_id and event_type in ["message_sent", "message_received"]:
                            if correlation_id not in report["message_flows"]:
                                report["message_flows"][correlation_id] = {
                                    "events": [],
                                    "agents_involved": set()
                                }
                            
                            report["message_flows"][correlation_id]["events"].append(event)
                            report["message_flows"][correlation_id]["agents_involved"].add(agent_id)
                        
                        # Performance tracking
                        if "duration" in event:
                            operation = event.get("operation", "unknown")
                            if operation not in report["performance_summary"]:
                                report["performance_summary"][operation] = {
                                    "count": 0,
                                    "total_time": 0,
                                    "min_time": float('inf'),
                                    "max_time": 0
                                }
                            
                            duration = event["duration"]
                            perf = report["performance_summary"][operation]
                            perf["count"] += 1
                            perf["total_time"] += duration
                            perf["min_time"] = min(perf["min_time"], duration)
                            perf["max_time"] = max(perf["max_time"], duration)
            
            except Exception as e:
                continue
        
        # Convert sets to lists for JSON serialization
        for flow in report["message_flows"].values():
            flow["agents_involved"] = list(flow["agents_involved"])
        
        # Calculate averages
        for operation, stats in report["performance_summary"].items():
            if stats["count"] > 0:
                stats["avg_time"] = stats["total_time"] / stats["count"]
        
        return report

   


        

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