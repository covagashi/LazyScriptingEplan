# src/agents/validation_agent.py
import re
import time
import subprocess
import tempfile
from pathlib import Path
from typing import Dict, List, Any, Tuple
from .mini_agent import MiniAgent
from ..core.message_bus import ObservableMessageBus, AgentMessage

class ValidationAgent(MiniAgent):
    """C# Validation Agent with observability integration"""
    
    def __init__(self, message_bus: ObservableMessageBus):
        super().__init__("validation", message_bus)
        
        self.validation_metrics = {
            "scripts_validated": 0,
            "syntax_errors_found": 0,
            "warnings_found": 0,
            "successful_validations": 0,
            "context_injections": 0
        }
        
        self.eplan_usings = [
            "using Eplan.EplApi.Base;",
            "using Eplan.EplApi.Scripting;",
            "using Eplan.EplApi.ApplicationFramework;",
            "using Eplan.EplApi.DataModel;",
            "using System;"
        ]
        
        # Setup custom routing after parent initialization
        self._setup_custom_routing()
    
    def _setup_custom_routing(self):
        """Configure routing for validation tasks"""
        custom_keywords = {
            "high_confidence": [
                "validate", "check syntax", "verify code", "compile check",
                "syntax validation", "code validation", "pre-execution check"
            ],
            "medium_confidence": [
                "validate", "check", "verify", "syntax", "compile",
                "before execute", "pre-check"
            ],
            "low_confidence": [
                "execute", "run", "just generate", "skip validation"
            ]
        }
        
        # Safely set routing keywords if router is available
        if self.router and hasattr(self.router, 'agent_keywords'):
            self.router.agent_keywords["validation"] = custom_keywords
    
    def get_specialty(self) -> str:
        return "C# syntax validation, EPLAN script enrichment, pre-execution verification"
    
    async def _get_current_capabilities(self) -> str:
        """Current capabilities with validation metrics"""
        success_rate = 0
        if self.validation_metrics["scripts_validated"] > 0:
            success_rate = (self.validation_metrics["successful_validations"] / 
                           self.validation_metrics["scripts_validated"]) * 100
        
        return f"C# validation, success rate: {success_rate:.1f}%, injections: {self.validation_metrics['context_injections']}"
    
    async def _get_current_state(self) -> Dict:
        """Enhanced state with validation metrics"""
        base_state = await super()._get_current_state()
        base_state.update({
            "validation_metrics": self.validation_metrics
        })
        return base_state
    
    async def _restore_from_state(self, state: Dict):
        """Restore with validation metrics"""
        if "validation_metrics" in state:
            self.validation_metrics = state["validation_metrics"]
        
        await self._log_structured_event({
            "event_type": "state_restored",
            "metrics_restored": self.validation_metrics
        })
    
    async def process_message_with_context(self, message: AgentMessage, contexts: Dict[str, Any]):
        """Enhanced processing with observability tracking"""
        
        async with await self.measure_performance("message_processing"):
            
            await self._log_structured_event({
                "event_type": "validation_request_start",
                "correlation_id": message.correlation_id,
                "intent": message.intent,
                "has_context": len(contexts) > 0
            })
            
            if message.intent == "validate_script":
                await self._handle_script_validation(message, contexts)
                
            elif message.intent == "planned_task":
                await self._handle_planned_task(message, contexts)
                
            else:
                await self._log_structured_event({
                    "event_type": "unhandled_intent",
                    "intent": message.intent,
                    "correlation_id": message.correlation_id
                })
    
    async def _handle_script_validation(self, message: AgentMessage, contexts: Dict[str, Any]):
        """Handle script validation request"""
        
        script_content = message.payload.get("script_content", "")
        script_purpose = message.payload.get("script_purpose", "EPLAN Operation")
        
        validation_start = time.time()
        
        await self._log_structured_event({
            "event_type": "script_validation_start",
            "script_lines": len(script_content.split('\n')),
            "script_purpose": script_purpose,
            "correlation_id": message.correlation_id
        })
        
        self.validation_metrics["scripts_validated"] += 1
        
        # Step 1: Syntax validation
        async with await self.measure_performance("syntax_validation"):
            syntax_valid, syntax_errors = await self._validate_syntax(script_content)
        
        if not syntax_valid:
            self.validation_metrics["syntax_errors_found"] += len(syntax_errors)
            await self._send_validation_error(syntax_errors, message)
            return
        
        # Step 2: Inject context messages
        async with await self.measure_performance("context_injection"):
            enriched_script = await self._inject_context_messages(script_content, script_purpose)
        
        if enriched_script:
            self.validation_metrics["successful_validations"] += 1
            self.validation_metrics["context_injections"] += 1
            
            validation_time = time.time() - validation_start
            
            await self._log_structured_event({
                "event_type": "script_validation_complete",
                "validation_time": validation_time,
                "enriched_lines": len(enriched_script.split('\n')),
                "correlation_id": message.correlation_id
            })
            
            # Store enriched script and send to execution
            script_ref = await self.store_heavy_context(
                {
                    "enriched_script": enriched_script,
                    "original_script": script_content,
                    "validation_metadata": {
                        "purpose": script_purpose,
                        "validation_time": validation_time,
                        "injected_messages": True
                    }
                },
                metadata={"type": "validated_script"}
            )
            
            await self.send_message(
                ["execution"],
                "execute_validated_script",
                {
                    "script_ready": True,
                    "validation_success": True,
                    "script_purpose": script_purpose
                },
                heavy_context={
                    "validated_script": enriched_script,
                    "validation_report": {
                        "syntax_valid": True,
                        "context_injected": True,
                        "validation_time": validation_time
                    }
                },
                parent_message=message
            )
        else:
            await self._send_validation_error(["Context injection failed"], message)
    
    async def _handle_planned_task(self, message: AgentMessage, contexts: Dict[str, Any]):
        """Handle planned task from PlanningAgent"""
        
        step_number = message.payload.get("step_number")
        action = message.payload.get("action")
        plan_id = message.payload.get("plan_id")
        
        await self._log_structured_event({
            "event_type": "planned_validation_task_received",
            "plan_id": plan_id,
            "step_number": step_number,
            "action": action,
            "correlation_id": message.correlation_id
        })
        
        if action in ["validate_script", "pre_execution_check", "syntax_check"]:
            # Look for script in contexts
            script_content = None
            script_purpose = "Planned Task Execution"
            
            for context_data in contexts.values():
                if "script_content" in context_data:
                    script_content = context_data["script_content"]
                    script_purpose = context_data.get("script_purpose", script_purpose)
                    break
            
            if script_content:
                await self._handle_script_validation(
                    AgentMessage(
                        sender=message.sender,
                        recipients=["validation"],
                        intent="validate_script",
                        payload={
                            "script_content": script_content,
                            "script_purpose": script_purpose
                        }
                    ),
                    contexts
                )
            else:
                await self._log_structured_event({
                    "event_type": "planned_task_no_script",
                    "plan_id": plan_id,
                    "step_number": step_number
                })
        
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
    
    async def _validate_syntax(self, script_content: str) -> Tuple[bool, List[str]]:
        """Validate C# syntax using basic checks and optional compilation"""
        
        errors = []
        
        # Basic syntax checks
        if not self._has_required_structure(script_content):
            errors.append("Missing required EPLAN script structure (class or [Start] method)")
        
        # Check for balanced braces
        if not self._check_balanced_braces(script_content):
            errors.append("Unbalanced braces in script")
        
        # Check for missing semicolons (basic)
        missing_semicolons = self._check_semicolons(script_content)
        if missing_semicolons:
            errors.extend(missing_semicolons)
        
        # Try compilation check if available
        compilation_errors = await self._try_compilation_check(script_content)
        if compilation_errors:
            errors.extend(compilation_errors)
        
        await self._log_structured_event({
            "event_type": "syntax_validation_complete",
            "errors_found": len(errors),
            "validation_methods": ["structure", "braces", "semicolons", "compilation"]
        })
        
        return len(errors) == 0, errors
    
    def _has_required_structure(self, script: str) -> bool:
        """Check for EPLAN script structure"""
        has_start_attribute = "[Start]" in script or "[DeclareAction" in script
        has_class = "class " in script and "{" in script
        has_method = "public " in script and "(" in script and ")" in script
        
        return has_start_attribute or (has_class and has_method)
    
    def _check_balanced_braces(self, script: str) -> bool:
        """Check for balanced braces"""
        count = 0
        in_string = False
        in_comment = False
        
        i = 0
        while i < len(script):
            char = script[i]
            
            # Handle string literals
            if char == '"' and not in_comment:
                if i == 0 or script[i-1] != '\\':
                    in_string = not in_string
            
            # Handle comments
            elif char == '/' and i + 1 < len(script) and not in_string:
                if script[i + 1] == '/':
                    in_comment = True
                elif script[i + 1] == '*':
                    # Multi-line comment start
                    i += 1
            
            elif char == '\n':
                in_comment = False
            
            # Count braces
            elif not in_string and not in_comment:
                if char == '{':
                    count += 1
                elif char == '}':
                    count -= 1
                    if count < 0:
                        return False
            
            i += 1
        
        return count == 0
    
    def _check_semicolons(self, script: str) -> List[str]:
        """Basic semicolon checking"""
        errors = []
        lines = script.split('\n')
        
        for i, line in enumerate(lines, 1):
            line = line.strip()
            if not line or line.startswith('//') or line.startswith('/*'):
                continue
            
            # Lines that should end with semicolon
            if (any(line.strip().startswith(keyword) for keyword in 
                   ['new ', 'return ', 'throw ', 'var ', 'string ', 'int ', 'bool ']) and
                not line.endswith(';') and not line.endswith('{') and not line.endswith('}')):
                errors.append(f"Line {i}: Missing semicolon")
        
        return errors[:5]  # Limit to first 5 errors
    
    async def _try_compilation_check(self, script: str) -> List[str]:
        """Try compilation check using csc if available"""
        try:
            # Add EPLAN usings
            full_script = '\n'.join(self.eplan_usings) + '\n\n' + script
            
            # Create temporary file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.cs', delete=False) as temp_file:
                temp_file.write(full_script)
                temp_path = temp_file.name
            
            try:
                # Try to compile (this requires .NET SDK)
                result = subprocess.run(
                    ['csc', '/nologo', '/t:library', temp_path],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                if result.returncode != 0:
                    # Parse compilation errors
                    error_lines = result.stdout.split('\n')
                    compilation_errors = []
                    for line in error_lines:
                        if 'error CS' in line:
                            # Extract meaningful error message
                            error_msg = line.split('error CS')[1]
                            compilation_errors.append(f"Compilation error: CS{error_msg}")
                    
                    return compilation_errors[:3]  # Limit to first 3
                
            finally:
                # Cleanup
                Path(temp_path).unlink(missing_ok=True)
                Path(temp_path.replace('.cs', '.dll')).unlink(missing_ok=True)
            
        except Exception as e:
            await self._log_structured_event({
                "event_type": "compilation_check_error",
                "error": str(e)
            })
        
        return []
    
    async def _inject_context_messages(self, script_content: str, script_purpose: str) -> str:
        """Inject contextual logging messages into script"""
        
        lines = script_content.split('\n')
        enriched_lines = []
        
        # Add usings if not present
        has_eplan_base = any("Eplan.EplApi.Base" in line for line in lines)
        if not has_eplan_base:
            enriched_lines.extend(self.eplan_usings)
            enriched_lines.append("")
        
        method_started = False
        brace_count = 0
        
        for line in lines:
            enriched_lines.append(line)
            
            # Detect method start
            if ("[Start]" in line or "[DeclareAction" in line) and not method_started:
                method_started = True
                continue
            
            # Inject start message after first opening brace of method
            if method_started and "{" in line and not method_started == "injected":
                brace_count += line.count("{")
                if brace_count > 0:
                    indent = "    " * (brace_count)
                    start_msg = f'{indent}new BaseException("Script START: {script_purpose}", MessageLevel.Message).FixMessage();'
                    enriched_lines.append(start_msg)
                    method_started = "injected"
            
            # Track brace count for proper indentation
            if method_started == "injected":
                brace_count += line.count("{") - line.count("}")
        
        # Add completion message before final brace
        if enriched_lines and method_started == "injected":
            # Find last meaningful line before final brace
            for i in range(len(enriched_lines) - 1, -1, -1):
                if enriched_lines[i].strip() and not enriched_lines[i].strip() == "}":
                    indent = "    "
                    complete_msg = f'{indent}new BaseException("Script COMPLETE: {script_purpose} finished", MessageLevel.Message).FixMessage();'
                    enriched_lines.insert(i + 1, complete_msg)
                    break
        
        await self._log_structured_event({
            "event_type": "context_injection_complete",
            "original_lines": len(lines),
            "enriched_lines": len(enriched_lines),
            "script_purpose": script_purpose
        })
        
        return '\n'.join(enriched_lines)
    
    async def _send_validation_error(self, errors: List[str], original_message: AgentMessage):
        """Send validation error response"""
        
        error_summary = f"❌ **Script Validation Failed**\n\n"
        error_summary += f"**Errors found ({len(errors)}):**\n"
        for i, error in enumerate(errors[:5], 1):
            error_summary += f"{i}. {error}\n"
        
        if len(errors) > 5:
            error_summary += f"... and {len(errors) - 5} more errors\n"
        
        error_summary += "\n*Please fix these issues before execution.*"
        
        await self._log_structured_event({
            "event_type": "validation_error_response",
            "errors_count": len(errors),
            "correlation_id": original_message.correlation_id
        })
        
        await self.send_message(
            ["conversation"],
            "response_to_user",
            {
                "content": error_summary,
                "source": "validation_agent",
                "validation_status": "failed",
                "errors": errors
            },
            parent_message=original_message
        )
    
    async def can_handle(self, intent: str) -> float:
        """Enhanced routing for validation tasks"""
        
        validation_patterns = [
            "validate", "check syntax", "verify code", "compile check",
            "pre-execution", "syntax validation"
        ]
        
        intent_lower = intent.lower()
        for pattern in validation_patterns:
            if pattern in intent_lower:
                await self._log_structured_event({
                    "event_type": "routing_high_confidence",
                    "pattern": pattern,
                    "confidence": 0.9
                })
                return 0.9
        
        # Use parent's enhanced can_handle method
        return await super().can_handle(intent)