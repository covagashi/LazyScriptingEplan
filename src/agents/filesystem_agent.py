# src/agents/filesystem_agent.py
import os
import json
from datetime import datetime, timedelta
import time
import asyncio
from pathlib import Path
from typing import Dict, Any, List, Optional
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from .mini_agent import MiniAgent
from ..core.message_bus import ObservableMessageBus, AgentMessage

class FileSystemAgent(MiniAgent):
    """Enhanced FileSystem Agent with observability integration"""
    
    def __init__(self, message_bus: ObservableMessageBus):
        super().__init__("filesystem", message_bus)
        self.base_path = Path(r"C:\temp\Agent\Context")
        self.base_path.mkdir(exist_ok=True, parents=True)
        
        self.scratchpads_path = self.base_path / "scratchpads"
        self.context_path = self.base_path / "context"
        self.outputs_path = self.base_path / "outputs"
        self.state_path = self.base_path / "state"
        
        # File operation metrics
        self.fs_metrics = {
            "contexts_stored": 0,
            "contexts_retrieved": 0,
            "scratchpads_created": 0,
            "outputs_saved": 0,
            "cleanup_operations": 0
        }
        
        for path in [self.scratchpads_path, self.context_path, self.outputs_path, self.state_path]:
            path.mkdir(exist_ok=True)
        
        self.observer = Observer()
        self.file_handler = FileSystemWatcher(self)
        self.observer.schedule(self.file_handler, str(self.base_path), recursive=True)
        self.observer.start()
        
        self.memory_cache = {}
        self.context_refs = {}
        
        print(f"📁 Enhanced FileSystemAgent initialized at {self.base_path}")
    
    def get_specialty(self) -> str:
        return "Persistent context storage, filesystem operations, agent scratchpads, observability logging"
    
    async def _get_current_capabilities(self) -> str:
        """Current capabilities with filesystem metrics"""
        total_contexts = len(self.context_refs)
        cached_contexts = len(self.memory_cache)
        
        return f"Contexts: {total_contexts} stored, {cached_contexts} cached, Operations: {self.fs_metrics['contexts_stored']} stored"
    
    async def _get_current_state(self) -> Dict:
        """Enhanced state with filesystem metrics"""
        base_state = await super()._get_current_state()
        base_state.update({
            "fs_metrics": self.fs_metrics,
            "active_contexts": len(self.context_refs),
            "cached_contexts": len(self.memory_cache),
            "base_path": str(self.base_path)
        })
        return base_state
    
    async def _restore_from_state(self, state: Dict):
        """Restore with filesystem metrics"""
        if "fs_metrics" in state:
            self.fs_metrics = state["fs_metrics"]
        
        await self._log_structured_event({
            "event_type": "state_restored",
            "metrics_restored": self.fs_metrics
        })
    
    async def process_message_with_context(self, message: AgentMessage, contexts: Dict[str, Any]):
        """Enhanced processing with observability tracking"""
        
        async with await self.measure_performance("message_processing"):
            
            await self._log_structured_event({
                "event_type": "filesystem_operation_start",
                "correlation_id": message.correlation_id,
                "intent": message.intent,
                "sender": message.sender
            })
            
            intent = message.intent
            payload = message.payload
            sender = message.sender
            
            try:
                if intent == "store_context":
                    await self._store_context(sender, payload, message)
                elif intent == "get_context":
                    await self._get_context(sender, payload, message)
                elif intent == "create_scratchpad":
                    await self._create_scratchpad(sender, payload, message)
                elif intent == "update_scratchpad":
                    await self._update_scratchpad(sender, payload, message)
                elif intent == "store_output":
                    await self._store_output(sender, payload, message)
                elif intent == "get_state":
                    await self._get_state(sender, payload, message)
                elif intent == "save_state":
                    await self._save_state(sender, payload, message)
                elif intent == "cleanup":
                    await self._cleanup_old_files(message)
                elif intent == "get_agent_logs":
                    await self._handle_agent_logs_request(sender, payload, message)
                elif intent == "generate_observability_report":
                    await self._handle_observability_report_request(sender, payload, message)
                else:
                    await self._log_structured_event({
                        "event_type": "unhandled_filesystem_intent",
                        "intent": intent,
                        "correlation_id": message.correlation_id
                    })
                    
            except Exception as e:
                await self._log_structured_event({
                    "event_type": "filesystem_operation_error",
                    "intent": intent,
                    "error": str(e),
                    "correlation_id": message.correlation_id
                })
                raise
    
    # === Context Management ===
    async def _store_context(self, sender: str, payload: Dict[str, Any], original_message: AgentMessage):
        """Store heavy context in filesystem with observability"""
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
        
        storage_start = time.time()
        
        try:
            with open(context_file, 'w', encoding='utf-8') as f:
                json.dump(context_data, f, indent=2, ensure_ascii=False)
            
            self.memory_cache[context_id] = context_data
            
            ref = {
                "context_id": context_id,
                "file_path": str(context_file),
                "size": context_file.stat().st_size,
                "timestamp": time.time()
            }
            self.context_refs[context_id] = ref
            
            self.fs_metrics["contexts_stored"] += 1
            
            storage_time = time.time() - storage_start
            
            await self._log_structured_event({
                "event_type": "context_stored_success",
                "context_id": context_id,
                "file_size": ref["size"],
                "storage_time": storage_time,
                "correlation_id": original_message.correlation_id
            })
            
            await self.send_message(
                [sender],
                "context_stored",
                {"reference": ref, "success": True},
                parent_message=original_message
            )
            
        except Exception as e:
            await self._log_structured_event({
                "event_type": "context_storage_error",
                "error": str(e),
                "context_id": context_id,
                "correlation_id": original_message.correlation_id
            })
            
            await self.send_message(
                [sender],
                "context_error",
                {"error": str(e), "context_id": context_id},
                parent_message=original_message
            )
    
    async def _get_context(self, sender: str, payload: Dict[str, Any], original_message: AgentMessage):
        """Retrieve context by ID with observability"""
        context_id = payload.get("context_id")
        
        retrieval_start = time.time()
        
        if context_id in self.memory_cache:
            context_data = self.memory_cache[context_id]
            retrieval_time = time.time() - retrieval_start
            
            await self._log_structured_event({
                "event_type": "context_retrieved_from_cache",
                "context_id": context_id,
                "retrieval_time": retrieval_time
            })
        else:
            context_file = self.context_path / f"{context_id}.json"
            if not context_file.exists():
                await self._log_structured_event({
                    "event_type": "context_not_found",
                    "context_id": context_id,
                    "correlation_id": original_message.correlation_id
                })
                
                await self.send_message(
                    [sender],
                    "context_not_found",
                    {"context_id": context_id},
                    parent_message=original_message
                )
                return
            
            try:
                with open(context_file, 'r', encoding='utf-8') as f:
                    context_data = json.load(f)
                self.memory_cache[context_id] = context_data
                
                retrieval_time = time.time() - retrieval_start
                
                await self._log_structured_event({
                    "event_type": "context_retrieved_from_disk",
                    "context_id": context_id,
                    "retrieval_time": retrieval_time,
                    "file_size": context_file.stat().st_size
                })
                
            except Exception as e:
                await self._log_structured_event({
                    "event_type": "context_retrieval_error",
                    "error": str(e),
                    "context_id": context_id
                })
                
                await self.send_message(
                    [sender],
                    "context_error", 
                    {"error": str(e), "context_id": context_id},
                    parent_message=original_message
                )
                return
        
        self.fs_metrics["contexts_retrieved"] += 1
        
        await self.send_message(
            [sender],
            "context_retrieved",
            {"context": context_data, "context_id": context_id},
            parent_message=original_message
        )
    
    # === Scratchpad Management ===
    async def _create_scratchpad(self, sender: str, payload: Dict[str, Any], original_message: AgentMessage):
        """Create scratchpad with observability"""
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
            
            self.fs_metrics["scratchpads_created"] += 1
            
            await self._log_structured_event({
                "event_type": "scratchpad_created",
                "agent_id": agent_id,
                "file_path": str(scratchpad_file)
            })
            
            await self.send_message(
                [sender],
                "scratchpad_created",
                {"scratchpad_path": str(scratchpad_file), "agent_id": agent_id},
                parent_message=original_message
            )
            
        except Exception as e:
            await self._log_structured_event({
                "event_type": "scratchpad_creation_error",
                "error": str(e),
                "agent_id": agent_id
            })
            
            await self.send_message(
                [sender],
                "scratchpad_error",
                {"error": str(e), "agent_id": agent_id},
                parent_message=original_message
            )
    
    async def _update_scratchpad(self, sender: str, payload: Dict[str, Any], original_message: AgentMessage):
        """Update scratchpad with observability"""
        agent_id = payload.get("agent_id", sender)
        update_data = payload.get("data")
        operation = payload.get("operation", "merge")
        
        scratchpad_file = self.scratchpads_path / f"{agent_id}_scratch.json"
        
        if not scratchpad_file.exists():
            await self._create_scratchpad(sender, {"agent_id": agent_id, "data": update_data}, original_message)
            return
        
        try:
            with open(scratchpad_file, 'r', encoding='utf-8') as f:
                scratchpad_data = json.load(f)
            
            scratchpad_data["history"].append({
                "timestamp": time.time(),
                "operation": operation,
                "data": scratchpad_data["data"].copy() if isinstance(scratchpad_data["data"], dict) else str(scratchpad_data["data"])
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
            
            await self._log_structured_event({
                "event_type": "scratchpad_updated",
                "agent_id": agent_id,
                "operation": operation
            })
            
            await self.send_message(
                [sender],
                "scratchpad_updated",
                {"success": True, "agent_id": agent_id},
                parent_message=original_message
            )
            
        except Exception as e:
            await self._log_structured_event({
                "event_type": "scratchpad_update_error",
                "error": str(e),
                "agent_id": agent_id
            })
            
            await self.send_message(
                [sender],
                "scratchpad_error",
                {"error": str(e), "agent_id": agent_id},
                parent_message=original_message
            )
    
    # === Output Management ===
    async def _store_output(self, sender: str, payload: Dict[str, Any], original_message: AgentMessage):
        """Store outputs with observability"""
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
            
            self.fs_metrics["outputs_saved"] += 1
            
            await self._log_structured_event({
                "event_type": "output_stored",
                "output_type": output_type,
                "file_path": str(output_file),
                "file_size": output_file.stat().st_size
            })
            
            await self.send_message(
                [sender],
                "output_stored",
                {
                    "file_path": str(output_file),
                    "type": output_type,
                    "size": output_file.stat().st_size
                },
                parent_message=original_message
            )
            
        except Exception as e:
            await self.send_message(
                [sender],
                "output_error",
                {"error": str(e), "filename": filename},
                parent_message=original_message
            )
    
    # === State Management ===
    async def _save_state(self, sender: str, payload: Dict[str, Any], original_message: AgentMessage):
        """Save state with observability"""
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
                {"state_id": state_id, "success": True},
                parent_message=original_message
            )
            
        except Exception as e:
            await self.send_message(
                [sender],
                "state_error",
                {"error": str(e), "state_id": state_id},
                parent_message=original_message
            )
    
    async def _get_state(self, sender: str, payload: Dict[str, Any], original_message: AgentMessage):
        """Get state with observability"""
        state_id = payload.get("state_id", "system_state")
        state_file = self.state_path / f"{state_id}.json"
        
        if not state_file.exists():
            await self.send_message(
                [sender],
                "state_not_found", 
                {"state_id": state_id},
                parent_message=original_message
            )
            return
        
        try:
            with open(state_file, 'r', encoding='utf-8') as f:
                state_data = json.load(f)
            
            await self.send_message(
                [sender],
                "state_retrieved",
                {"state": state_data, "state_id": state_id},
                parent_message=original_message
            )
            
        except Exception as e:
            await self.send_message(
                [sender],
                "state_error",
                {"error": str(e), "state_id": state_id},
                parent_message=original_message
            )
    
    # === Observability Support ===
    async def log_structured_event(self, event_data: Dict):
        """Log structured event for observability"""
        logs_path = self.base_path / "logs"
        logs_path.mkdir(exist_ok=True)
        
        today = datetime.now().strftime("%Y%m%d")
        log_file = logs_path / f"structured_events_{today}.jsonl"
        
        try:
            with open(log_file, 'a', encoding='utf-8') as f:
                json.dump(event_data, f, ensure_ascii=False)
                f.write('\n')
        except Exception as e:
            print(f"⚠️ Failed to log structured event: {e}")

    async def get_agent_logs(self, agent_id: str, limit: int = 100) -> List[Dict]:
        """Get recent logs for agent"""
        logs_path = self.base_path / "logs"
        
        if not logs_path.exists():
            return []
        
        agent_events = []
        
        for i in range(3):  # Last 3 days
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
                except Exception:
                    continue
        
        agent_events.sort(key=lambda x: x.get("timestamp", 0), reverse=True)
        return agent_events[:limit]

    async def generate_observability_report(self, time_range_hours: int = 24) -> Dict:
        """Generate observability report"""
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
            "performance_summary": {},
            "filesystem_metrics": self.fs_metrics.copy()
        }
        
        for log_file in logs_path.glob("structured_events_*.jsonl"):
            try:
                with open(log_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        event = json.loads(line.strip())
                        
                        if event.get("timestamp", 0) < cutoff_time:
                            continue
                        
                        agent_id = event.get("agent_id", "unknown")
                        event_type = event.get("event_type", "unknown")
                        
                        if agent_id not in report["agent_activity"]:
                            report["agent_activity"][agent_id] = {
                                "events": 0,
                                "event_types": {},
                                "errors": 0
                            }
                        
                        report["agent_activity"][agent_id]["events"] += 1
                        report["agent_activity"][agent_id]["event_types"][event_type] = \
                            report["agent_activity"][agent_id]["event_types"].get(event_type, 0) + 1
                        
                        if "error" in event or event_type.endswith("_error"):
                            report["agent_activity"][agent_id]["errors"] += 1
                            report["error_summary"].append({
                                "agent": agent_id,
                                "timestamp": event.get("timestamp"),
                                "error": event.get("error", "Unknown error")
                            })
                        
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
            
            except Exception:
                continue
        
        for operation, stats in report["performance_summary"].items():
            if stats["count"] > 0:
                stats["avg_time"] = stats["total_time"] / stats["count"]
        
        return report

    async def _handle_agent_logs_request(self, sender: str, payload: Dict[str, Any], original_message: AgentMessage):
        """Handle agent logs request"""
        agent_id = payload.get("agent_id", sender)
        limit = payload.get("limit", 100)
        
        logs = await self.get_agent_logs(agent_id, limit)
        
        await self.send_message(
            [sender],
            "agent_logs",
            {"logs": logs, "agent_id": agent_id, "count": len(logs)},
            parent_message=original_message
        )

    async def _handle_observability_report_request(self, sender: str, payload: Dict[str, Any], original_message: AgentMessage):
        """Handle observability report request"""
        time_range = payload.get("time_range_hours", 24)
        report = await self.generate_observability_report(time_range)
        
        report_file = self.base_path / "reports" / f"observability_report_{int(time.time())}.json"
        report_file.parent.mkdir(exist_ok=True)
        
        try:
            with open(report_file, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            
            await self.send_message(
                [sender],
                "observability_report_ready",
                {"report_file": str(report_file), "report": report},
                parent_message=original_message
            )
        except Exception as e:
            await self.send_message(
                [sender],
                "report_generation_error",
                {"error": str(e)},
                parent_message=original_message
            )
    
    # === Cleanup ===
    async def _cleanup_old_files(self, original_message: AgentMessage):
        """Cleanup old files with observability"""
        cutoff = time.time() - (7 * 24 * 3600)  # 7 days
        cleaned = 0
        
        cleanup_start = time.time()
        
        for folder in [self.context_path, self.outputs_path]:
            for file in folder.glob("*.json"):
                if file.stat().st_mtime < cutoff:
                    try:
                        file.unlink()
                        cleaned += 1
                    except:
                        pass
        
        cleanup_time = time.time() - cleanup_start
        
        self.fs_metrics["cleanup_operations"] += 1
        
        await self._log_structured_event({
            "event_type": "cleanup_completed",
            "files_cleaned": cleaned,
            "cleanup_time": cleanup_time
        })
        
        print(f"🧹 Cleaned {cleaned} old files")
    
    def get_context_reference(self, context_id: str) -> Optional[Dict]:
        """Get lightweight reference for MessageBus"""
        return self.context_refs.get(context_id)
    
    async def can_handle(self, intent: str) -> float:
        """Enhanced routing for filesystem operations"""
        filesystem_patterns = [
            "store", "save", "retrieve", "get context", "scratchpad",
            "file", "output", "state", "logs", "cleanup"
        ]
        
        intent_lower = intent.lower()
        for pattern in filesystem_patterns:
            if pattern in intent_lower:
                return 0.95
        
        base_confidence, method = await self.hybrid_handler.can_handle(intent, self.get_specialty())
        
        return base_confidence
    
    def __del__(self):
        """Cleanup on destroy"""
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
        """Notify agents about new files"""
        await self.fs_agent.send_message(
            ["conversation", "feedback"],  
            "file_created",
            {"file_path": file_path, "timestamp": time.time()}
        )