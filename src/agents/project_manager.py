# src/agents/project_manager.py
import re
import os
from .base import BaseAgent
from ..orchestrator.types import AgentMessage, TaskContext, AgentType

class ProjectManagerAgent(BaseAgent):
    """Orchestrates execution workflow and validates scripts"""
    
    def __init__(self, orchestrator):
        super().__init__(orchestrator)
        self.execution_context = {}
    
    async def process(self, context: TaskContext) -> AgentMessage:
        # Step 1: Check if parameters are complete
        knowledge_result = await self.get_peer_result(AgentType.KNOWLEDGE)
        knowledge_metadata = getattr(knowledge_result, 'metadata', {})
        
        if knowledge_metadata.get('needs_clarification'):
            return AgentMessage(
                agent_type=AgentType.PROJECT_MANAGER,
                content="❌ Cannot proceed - missing required parameters",
                metadata={'script_ready': False, 'needs_clarification': True}
            )
        
        # Step 2: Create execution context
        self.execution_context = {
            'user_query': context.user_query,
            'purpose': self._extract_purpose(context.user_query),
            'required_params': knowledge_metadata.get('required_params', [])
        }
        
        # Step 3: Report context
        context_info = f"📋 Execution Context:\nPurpose: {self.execution_context['purpose']}\nRequired params: {self.execution_context['required_params']}"
        
        # Step 4: Get and validate script
        code_result = await self.get_peer_result(AgentType.CODE_GENERATOR)
        
        validation = self._validate_script(code_result)
        if not validation['valid']:
            return AgentMessage(
                agent_type=AgentType.PROJECT_MANAGER,
                content=f"❌ Script validation failed: {validation['errors']}",
                metadata={'script_ready': False}
            )
        
        # Step 5: Validate parameters are not invented
        param_validation = self._validate_parameters(code_result, self.execution_context['required_params'])
        if not param_validation['valid']:
            return AgentMessage(
                agent_type=AgentType.PROJECT_MANAGER,
                content=f"❌ Parameter validation failed: {param_validation['errors']}",
                metadata={'script_ready': False}
            )
        
        # Step 6: Enhance script
        enhanced_script = self._inject_logs(code_result)
        self._save_script(enhanced_script)
        action_name = self._extract_action(enhanced_script)
        
        return AgentMessage(
            agent_type=AgentType.PROJECT_MANAGER,
            content=f"{context_info}\n\n✅ Script validated and ready\nAction: {action_name}",
            metadata={
                'script_ready': True,
                'action_name': action_name,
                'execution_context': self.execution_context
            }
        )
    
    def _validate_parameters(self, script: str, required_params: list) -> dict:
        """Validate that script doesn't use invented parameters"""
        errors = []
        
        # Check for hardcoded values that should be parameters
        lines = script.split('\n')
        for i, line in enumerate(lines, 1):
            if 'AddParameter' in line:
                # Extract parameter value
                if '"' in line:
                    parts = line.split('"')
                    if len(parts) >= 4:
                        param_name = parts[1]
                        param_value = parts[3]
                        
                        # Check if using placeholder values
                        if any(placeholder in param_value.lower() for placeholder in ['example', 'test', 'default', 'placeholder']):
                            errors.append(f"Line {i}: Parameter '{param_name}' uses placeholder value '{param_value}'")
        
        return {'valid': len(errors) == 0, 'errors': errors}
    
    def _extract_purpose(self, user_query: str) -> str:
        return user_query.replace('"', "'")
    
    def _validate_script(self, script: str) -> dict:
        errors = []
        
        # Check for $ usage
        lines = script.split('\n')
        for i, line in enumerate(lines, 1):
            if '$(' in line and 'PathMap.SubstitutePath' not in line:
                errors.append(f"Line {i}: Use PathMap.SubstitutePath for path variables")
            
            if re.search(r'\$[^("]', line):  # $ not followed by ( or "
                errors.append(f"Line {i}: Invalid $ usage")
        
        # Check for [Start] attribute
        if '[Start]' not in script:
            errors.append("Missing [Start] attribute")
        
        # Check basic C# syntax
        if script.count('{') != script.count('}'):
            errors.append("Unmatched braces")
        
        return {'valid': len(errors) == 0, 'errors': errors}
    
    def _inject_logs(self, script: str) -> str:
        purpose = self.execution_context['purpose']
        
        start_log = f'new BaseException("Agent START: {purpose}", MessageLevel.Message).FixMessage();'
        end_log = f'new BaseException("Agent final task", MessageLevel.Message).FixMessage();'
        
        # Find insertion points
        lines = script.split('\n')
        enhanced_lines = []
        
        for line in lines:
            enhanced_lines.append(line)
            
            # Insert start log after [Start]
            if '[Start]' in line:
                enhanced_lines.append(f'        {start_log}')
        
        # Add end log before last brace
        enhanced_lines.insert(-1, f'        {end_log}')
        
        return '\n'.join(enhanced_lines)
    
    def _save_script(self, script: str):
        filepath = r"C:\temp\Agent\eplan_script.cs"
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(script)
    
    def _extract_action(self, script: str) -> str:
        lines = script.split('\n')
        for line in lines:
            if 'ExecuteAction' in line and '"' in line:
                start = line.find('"') + 1
                end = line.find('"', start)
                if end > start:
                    return line[start:end]
        return "UnknownAction"
    
    async def process_feedback(self, feedback_result) -> str:
        """Process feedback and determine completion"""
        if feedback_result.metadata.get('success', False):
            return "🎉 Execution completed successfully. Returning control to conversation."
        else:
            errors = feedback_result.metadata.get('log_errors', [])
            return f"⚠️ Execution issues: {errors}. Returning control to conversation."