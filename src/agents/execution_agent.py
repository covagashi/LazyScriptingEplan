# src/agents/execution_agent.py
import clr
import sys
import time
import asyncio
from typing import Dict, Any
from .mini_agent import MiniAgent
from ..core.message_bus import ObservableMessageBus, AgentMessage

class ExecutionAgent(MiniAgent):
    """Enhanced Execution Agent with observability integration"""
    
    def __init__(self, message_bus: ObservableMessageBus):
        super().__init__("execution", message_bus)
        
        self.execution_metrics = {
            "total_executions": 0,
            "successful_executions": 0,
            "failed_executions": 0,
            "connection_attempts": 0,
            "average_execution_time": 0
        }
        
        self._setup_eplan()
        self.client = None
        self._connect()
    
    def get_specialty(self) -> str:
        return "EPLAN Remoting execution, script running, EPLAN API operations"
    
    async def _get_current_capabilities(self) -> str:
        """Current capabilities with connection status"""
        connection_status = "connected" if self.client else "disconnected"
        success_rate = 0
        if self.execution_metrics["total_executions"] > 0:
            success_rate = (self.execution_metrics["successful_executions"] / 
                           self.execution_metrics["total_executions"]) * 100
        
        return f"EPLAN Remoting {connection_status}, success rate: {success_rate:.1f}%, executions: {self.execution_metrics['total_executions']}"
    
    async def _get_current_state(self) -> Dict:
        """Enhanced state with execution metrics"""
        base_state = await super()._get_current_state()
        base_state.update({
            "execution_metrics": self.execution_metrics,
            "connection_status": "connected" if self.client else "disconnected",
            "eplan_setup_status": hasattr(self, 'EplanRemoteClient')
        })
        return base_state
    
    async def _restore_from_state(self, state: Dict):
        """Restore with execution metrics"""
        if "execution_metrics" in state:
            self.execution_metrics = state["execution_metrics"]
        
        await self._log_structured_event({
            "event_type": "state_restored",
            "metrics_restored": self.execution_metrics
        })
    
    async def process_message_with_context(self, message: AgentMessage, contexts: Dict[str, Any]):
        """Enhanced processing with observability tracking"""
        
        async with await self.measure_performance("message_processing"):
            
            await self._log_structured_event({
                "event_type": "execution_request_start",
                "correlation_id": message.correlation_id,
                "intent": message.intent,
                "has_context": len(contexts) > 0
            })
            
            if message.intent == "execute_script":
                await self._handle_script_execution(message, contexts)                

                
            elif message.intent == "planned_task":
                await self._handle_planned_task(message, contexts)
                
            else:
                await self._log_structured_event({
                    "event_type": "unhandled_intent",
                    "intent": message.intent,
                    "correlation_id": message.correlation_id
                })
    
    async def _handle_script_execution(self, message: AgentMessage, contexts: Dict[str, Any]):
        """Handle direct script execution request"""
        
        script_path = message.payload.get("script_path")
        action_name = message.payload.get("action_name", "GeneratedScript")
        
        await self._log_structured_event({
            "event_type": "script_execution_start",
            "action_name": action_name,
            "script_path": script_path,
            "correlation_id": message.correlation_id
        })
        
        execution_start = time.time()
        success, result = await self._execute_script(action_name)
        execution_time = time.time() - execution_start
        
        self.execution_metrics["total_executions"] += 1
        if success:
            self.execution_metrics["successful_executions"] += 1
        else:
            self.execution_metrics["failed_executions"] += 1
        
        self._update_execution_metrics(execution_time)
        
        await self._log_structured_event({
            "event_type": "script_execution_complete",
            "action_name": action_name,
            "success": success,
            "execution_time": execution_time,
            "result": result[:100] if result else None,
            "correlation_id": message.correlation_id
        })
        
        await self.send_message(
            ["feedback"],
            "analyze_execution",
            {
                "success": success, 
                "result": result, 
                "action": action_name,
                "execution_time": execution_time
            },
            parent_message=message
        )
    
    
    async def _handle_planned_task(self, message: AgentMessage, contexts: Dict[str, Any]):
        """Handle planned task from PlanningAgent"""
        
        step_number = message.payload.get("step_number")
        action = message.payload.get("action")
        plan_id = message.payload.get("plan_id")
        
        await self._log_structured_event({
            "event_type": "planned_execution_task_received",
            "plan_id": plan_id,
            "step_number": step_number,
            "action": action,
            "correlation_id": message.correlation_id
        })
        
        action_name = "DefaultAction"
        for context_data in contexts.values():
            if "action_name" in context_data:
                action_name = context_data["action_name"]
                break
            
        
        if action in ["execute_script", "test_implementation", "run_code"]:
            success, result = await self._execute_script(action_name)
            
            await self.send_message(
                ["planning"],
                "planned_task_result",
                {
                    "plan_id": plan_id,
                    "step_number": step_number,
                    "success": success,
                    "result": result
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
    
    def _setup_eplan(self):
        """Setup EPLAN 2025 API with error logging"""
        try:
            eplan_path = r"C:\Program Files\EPLAN\Platform\2023.0.3\Bin"
            sys.path.append(eplan_path)
            clr.AddReference("Eplan.EplApi.RemoteClientu")
            from Eplan.EplApi.RemoteClient import EplanRemoteClient
            import System
            self.EplanRemoteClient = EplanRemoteClient
            self.TimeSpan = System.TimeSpan
            
            asyncio.create_task(self._log_structured_event({
                "event_type": "eplan_setup_success",
                "eplan_path": eplan_path
            }))
            
        except Exception as e:
            asyncio.create_task(self._log_structured_event({
                "event_type": "eplan_setup_error",
                "error": str(e)
            }))
            print(f"EPLAN setup failed: {e}")
    
    def _connect(self):
        """Connect to EPLAN with metrics tracking"""
        try:
            self.execution_metrics["connection_attempts"] += 1
            
            self.client = self.EplanRemoteClient()
            self.client.Connect("localhost", "49152", self.TimeSpan.FromSeconds(5))
            
            asyncio.create_task(self._log_structured_event({
                "event_type": "eplan_connection_success",
                "host": "localhost",
                "port": "49152"
            }))
            
        except Exception as e:
            asyncio.create_task(self._log_structured_event({
                "event_type": "eplan_connection_error",
                "error": str(e),
                "connection_attempts": self.execution_metrics["connection_attempts"]
            }))
            self.client = None
    
    async def _execute_script(self, action_name: str) -> tuple:
        """Execute script with enhanced logging and metrics"""
        
        if not self.client:
            await self._log_structured_event({
                "event_type": "execution_failed_no_connection",
                "action_name": action_name
            })
            return False, "Not connected to EPLAN"
        
        execution_start = time.time()
        
        try:
            await self._log_structured_event({
                "event_type": "eplan_action_executing",
                "action_name": action_name
            })
            
            self.client.ExecuteAction(action_name)
            execution_time = time.time() - execution_start
            
            await self._log_structured_event({
                "event_type": "eplan_action_success",
                "action_name": action_name,
                "execution_time": execution_time
            })
            
            return True, f"✓ Executed: {action_name} ({execution_time:.2f}s)"
            
        except Exception as e:
            execution_time = time.time() - execution_start
            
            await self._log_structured_event({
                "event_type": "eplan_action_error",
                "action_name": action_name,
                "error": str(e),
                "execution_time": execution_time
            })
            
            return False, f"✗ Failed: {e}"
    
   
    def _update_execution_metrics(self, execution_time: float):
        """Update average execution time metrics"""
        current_avg = self.execution_metrics["average_execution_time"]
        total_executions = self.execution_metrics["total_executions"]
        
        if total_executions == 1:
            self.execution_metrics["average_execution_time"] = execution_time
        else:
            self.execution_metrics["average_execution_time"] = (
                (current_avg * (total_executions - 1) + execution_time) / total_executions
            )
    
    async def _send_error_response(self, error_msg: str, original_message: AgentMessage):
        """Send error response with logging"""
        
        await self._log_structured_event({
            "event_type": "execution_error_response",
            "error": error_msg,
            "correlation_id": original_message.correlation_id
        })
        
        await self.send_message(
            ["conversation"],
            "response_to_user",
            {
                "content": f"❌ Execution error: {error_msg}",
                "source": "execution_agent",
                "status": "error"
            },
            parent_message=original_message
        )
    
    async def can_handle(self, intent: str) -> float:
        """Enhanced routing for execution tasks"""
        
        execution_patterns = [
            "execute", "run", "execute script", "run script",
            "eplan remoting", "execute action", "run code"
        ]
        
        intent_lower = intent.lower()
        for pattern in execution_patterns:
            if pattern in intent_lower:
                await self._log_structured_event({
                    "event_type": "routing_high_confidence",
                    "pattern": pattern,
                    "confidence": 0.9
                })
                return 0.9
        
        base_confidence, method = await self.hybrid_handler.can_handle(intent, self.get_specialty())
        
        execution_terms = ["action", "remoting", "eplan connection", "execute"]
        boost = sum(0.05 for term in execution_terms if term in intent_lower)
        
        final_confidence = min(1.0, base_confidence + boost)
        
        await self.log_to_scratchpad(
            f"Execution routing: {final_confidence:.2f} (base: {base_confidence:.2f}, boost: {boost:.2f})",
            "routing"
        )
        
        return final_confidence