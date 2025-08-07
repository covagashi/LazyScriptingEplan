# src/agents/feedback_agent.py
import os
import csv
import asyncio
import time
from typing import Dict, Any, List
from pathlib import Path
from .mini_agent import MiniAgent
from ..core.message_bus import ObservableMessageBus, AgentMessage

class FeedbackAgent(MiniAgent):
    """Enhanced Feedback Agent with observability integration"""
    
    def __init__(self, message_bus: ObservableMessageBus):
        super().__init__("feedback", message_bus)
        self.log_path = Path(r"C:\temp\Agent\EplanLog\Events.csv")
        
        self.analysis_metrics = {
            "total_analyses": 0,
            "errors_detected": 0,
            "warnings_detected": 0,
            "successful_validations": 0,
            "log_parsing_errors": 0
        }
    
    def get_specialty(self) -> str:
        return "EPLAN software log analysis, execution validation, result verification"
    
    async def _get_current_capabilities(self) -> str:
        """Current capabilities with analysis metrics"""
        log_status = "available" if self.log_path.exists() else "not_found"
        error_rate = 0
        if self.analysis_metrics["total_analyses"] > 0:
            error_rate = (self.analysis_metrics["errors_detected"] / 
                         self.analysis_metrics["total_analyses"]) * 100
        
        return f"EPLAN log {log_status}, analyses: {self.analysis_metrics['total_analyses']}, error detection rate: {error_rate:.1f}%"
    
    async def _get_current_state(self) -> Dict:
        """Enhanced state with analysis metrics"""
        base_state = await super()._get_current_state()
        base_state.update({
            "analysis_metrics": self.analysis_metrics,
            "log_path_exists": self.log_path.exists(),
            "log_path": str(self.log_path)
        })
        return base_state
    
    async def _restore_from_state(self, state: Dict):
        """Restore with analysis metrics"""
        if "analysis_metrics" in state:
            self.analysis_metrics = state["analysis_metrics"]
        
        await self._log_structured_event({
            "event_type": "state_restored",
            "metrics_restored": self.analysis_metrics
        })
    
    async def process_message_with_context(self, message: AgentMessage, contexts: Dict[str, Any]):
        """Enhanced processing with observability tracking"""
        
        async with await self.measure_performance("message_processing"):
            
            await self._log_structured_event({
                "event_type": "feedback_analysis_start",
                "correlation_id": message.correlation_id,
                "intent": message.intent,
                "has_context": len(contexts) > 0
            })
            
            if message.intent == "analyze_execution":
                await self._handle_execution_analysis(message, contexts)
                
            elif message.intent in ["enhanced_user_request", "validation_request"]:
                await self._handle_validation_request(message, contexts)
                
            elif message.intent == "planned_task":
                await self._handle_planned_task(message, contexts)
                
            else:
                await self._log_structured_event({
                    "event_type": "unhandled_intent",
                    "intent": message.intent,
                    "correlation_id": message.correlation_id
                })
    
    async def _handle_execution_analysis(self, message: AgentMessage, contexts: Dict[str, Any]):
        """Handle execution analysis with enhanced logging"""
        
        success = message.payload.get("success", False)
        result = message.payload.get("result", "")
        action = message.payload.get("action", "Unknown")
        execution_time = message.payload.get("execution_time", 0)
        
        await self._log_structured_event({
            "event_type": "execution_analysis_start",
            "action": action,
            "initial_success": success,
            "execution_time": execution_time,
            "correlation_id": message.correlation_id
        })
        
        await asyncio.sleep(2)
        
        analysis_start = time.time()
        
        async with await self.measure_performance("log_analysis"):
            log_analysis = await self._analyze_logs_enhanced()
        
        analysis_time = time.time() - analysis_start
        
        self.analysis_metrics["total_analyses"] += 1
        if log_analysis['errors']:
            self.analysis_metrics["errors_detected"] += len(log_analysis['errors'])
        if log_analysis['warnings']:
            self.analysis_metrics["warnings_detected"] += len(log_analysis['warnings'])
        if success and not log_analysis['errors']:
            self.analysis_metrics["successful_validations"] += 1
        
        final_success = success and len(log_analysis['errors']) == 0
        
        report = await self._create_analysis_report(success, result, log_analysis, execution_time)
        
        await self._log_structured_event({
            "event_type": "execution_analysis_complete",
            "action": action,
            "final_success": final_success,
            "errors_found": len(log_analysis['errors']),
            "warnings_found": len(log_analysis['warnings']),
            "analysis_time": analysis_time,
            "correlation_id": message.correlation_id
        })
        
        await self.send_message(
            ["conversation"],
            "response_to_user",
            {
                "content": report,
                "source": "feedback_agent",
                "final_success": final_success,
                "analysis_metrics": {
                    "errors": len(log_analysis['errors']),
                    "warnings": len(log_analysis['warnings']),
                    "analysis_time": analysis_time
                }
            },
            parent_message=message
        )
    
    async def _handle_validation_request(self, message: AgentMessage, contexts: Dict[str, Any]):
        """Handle validation request from user"""
        
        query = message.payload.get("query", "")
        for context_data in contexts.values():
            if "user_query" in context_data:
                query = context_data["user_query"]
                break
        
        log_analysis = await self._analyze_logs_enhanced()
        
        report = f"📊 **EPLAN System Status Analysis**\n\n"
        report += f"**Recent Activity:**\n"
        report += f"- Errors: {len(log_analysis['errors'])}\n"
        report += f"- Warnings: {len(log_analysis['warnings'])}\n"
        report += f"- Log entries analyzed: {log_analysis.get('total_entries', 0)}\n\n"
        
        if log_analysis['errors']:
            report += f"**Recent Errors:**\n"
            for error in log_analysis['errors'][:3]:
                report += f"- {error[:100]}...\n"
        
        await self.send_message(
            ["conversation"],
            "response_to_user",
            {
                "content": report,
                "source": "feedback_agent",
                "analysis_type": "system_status"
            },
            parent_message=message
        )
    
    async def _handle_planned_task(self, message: AgentMessage, contexts: Dict[str, Any]):
        """Handle planned task from PlanningAgent"""
        
        step_number = message.payload.get("step_number")
        action = message.payload.get("action")
        plan_id = message.payload.get("plan_id")
        
        await self._log_structured_event({
            "event_type": "planned_feedback_task_received",
            "plan_id": plan_id,
            "step_number": step_number,
            "action": action,
            "correlation_id": message.correlation_id
        })
        
        if action in ["validate_results", "evaluate_success", "analyze_execution"]:
            log_analysis = await self._analyze_logs_enhanced()
            validation_report = await self._create_validation_report(log_analysis)
            
            await self.send_message(
                ["planning"],
                "planned_task_result",
                {
                    "plan_id": plan_id,
                    "step_number": step_number,
                    "validation_success": len(log_analysis['errors']) == 0,
                    "content": validation_report
                },
                heavy_context={
                    "detailed_analysis": log_analysis,
                    "validation_metrics": self.analysis_metrics
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
    
    async def _analyze_logs_enhanced(self) -> Dict[str, Any]:
        """Enhanced log analysis with detailed tracking"""
        analysis = {
            'errors': [], 
            'warnings': [], 
            'info_messages': [],
            'total_entries': 0,
            'analysis_timestamp': time.time()
        }
        
        if not self.log_path.exists():
            await self._log_structured_event({
                "event_type": "log_file_not_found",
                "log_path": str(self.log_path)
            })
            return analysis
        
        try:
            with open(self.log_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                analysis['total_entries'] = len(lines)
                                
                recent_lines = lines[-15:] # Analyze recent entries (last 15)
                
                for line in recent_lines:
                    line = line.strip()
                    if not line:
                        continue
                    
                    line_lower = line.lower()
                    
                    if any(error_term in line_lower for error_term in ['error', 'exception', 'failed']):
                        analysis['errors'].append(line)
                    elif any(warn_term in line_lower for warn_term in ['warning', 'warn', 'caution']):
                        analysis['warnings'].append(line)
                    elif any(info_term in line_lower for info_term in ['info', 'success', 'completed']):
                        analysis['info_messages'].append(line)
            
            await self._log_structured_event({
                "event_type": "log_analysis_success",
                "total_entries": analysis['total_entries'],
                "errors_found": len(analysis['errors']),
                "warnings_found": len(analysis['warnings']),
                "info_messages": len(analysis['info_messages'])
            })
            
        except Exception as e:
            self.analysis_metrics["log_parsing_errors"] += 1
            
            await self._log_structured_event({
                "event_type": "log_analysis_error",
                "error": str(e),
                "log_path": str(self.log_path)
            })
        
        return analysis
    
    async def _create_analysis_report(self, initial_success: bool, result: str, 
                                     log_analysis: Dict, execution_time: float) -> str:
        """Create comprehensive analysis report"""
        
        report = f"⚡ **Execution Analysis Report**\n\n"
        report += f"**Initial Result:** {'✅ Success' if initial_success else '❌ Failed'}\n"
        report += f"**Execution Time:** {execution_time:.2f}s\n"
        report += f"**Result:** {result}\n\n"
        
        report += f"📊 **Log Analysis:**\n"
        report += f"- Total log entries: {log_analysis.get('total_entries', 0)}\n"
        report += f"- Errors detected: {len(log_analysis['errors'])}\n"
        report += f"- Warnings detected: {len(log_analysis['warnings'])}\n"
        report += f"- Info messages: {len(log_analysis.get('info_messages', []))}\n\n"
        
        if log_analysis['errors']:
            report += f"🔴 **Errors Found:**\n"
            for i, error in enumerate(log_analysis['errors'][:3], 1):
                report += f"{i}. {error[:100]}{'...' if len(error) > 100 else ''}\n"
            if len(log_analysis['errors']) > 3:
                report += f"... and {len(log_analysis['errors']) - 3} more errors\n"
            report += "\n"
        
        if log_analysis['warnings']:
            report += f"🟡 **Warnings:**\n"
            for i, warning in enumerate(log_analysis['warnings'][:2], 1):
                report += f"{i}. {warning[:100]}{'...' if len(warning) > 100 else ''}\n"
            report += "\n"
        
        final_success = initial_success and len(log_analysis['errors']) == 0
        if final_success:
            report += f"✅ **Final Status:** Success - No errors detected in logs"
        else:
            report += f"❌ **Final Status:** Issues detected - Check errors above"
        
        return report
    
    async def _create_validation_report(self, log_analysis: Dict) -> str:
        """Create validation report for planned tasks"""
        
        report = f"📋 **System Validation Report**\n\n"
        report += f"**Analysis Timestamp:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        report += f"**Log Entries Analyzed:** {log_analysis.get('total_entries', 0)}\n\n"
        
        if log_analysis['errors']:
            report += f"❌ **Critical Issues ({len(log_analysis['errors'])}):**\n"
            for error in log_analysis['errors']:
                report += f"- {error[:80]}...\n"
        else:
            report += f"✅ **No Critical Errors Detected**\n"
        
        if log_analysis['warnings']:
            report += f"\n⚠️ **Warnings ({len(log_analysis['warnings'])}):**\n"
            for warning in log_analysis['warnings']:
                report += f"- {warning[:80]}...\n"
        
        health_score = self._calculate_health_score(log_analysis)
        report += f"\n📊 **System Health Score:** {health_score}/100\n"
        
        return report
    
    def _calculate_health_score(self, log_analysis: Dict) -> int:
        """Calculate system health score based on log analysis"""
        
        base_score = 100
        
        errors = len(log_analysis['errors'])
        warnings = len(log_analysis['warnings'])
        
        score_deduction = (errors * 15) + (warnings * 5)
        
        health_score = max(0, base_score - score_deduction)
        
        return health_score
    
    async def can_handle(self, intent: str) -> float:
        """Enhanced routing for feedback and validation tasks"""
        
        feedback_patterns = [
            "analyze", "check results", "validate execution", "feedback",
            "log analysis", "error check", "verify results"
        ]
        
        intent_lower = intent.lower()
        for pattern in feedback_patterns:
            if pattern in intent_lower:
                await self._log_structured_event({
                    "event_type": "routing_high_confidence",
                    "pattern": pattern,
                    "confidence": 0.9
                })
                return 0.9
        
        base_confidence, method = await self.hybrid_handler.can_handle(intent, self.get_specialty())
        
        feedback_terms = ["validate", "check", "logs", "results", "analysis"]
        boost = sum(0.05 for term in feedback_terms if term in intent_lower)
        
        final_confidence = min(1.0, base_confidence + boost)
        
        await self.log_to_scratchpad(
            f"Feedback routing: {final_confidence:.2f} (base: {base_confidence:.2f}, boost: {boost:.2f})",
            "routing"
        )
        
        return final_confidence