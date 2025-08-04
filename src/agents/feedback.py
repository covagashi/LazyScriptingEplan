# src/agents/feedback.py
import os
import csv
from datetime import datetime, timedelta
from .base import BaseAgent
from ..orchestrator.types import AgentMessage, TaskContext, AgentType

class FeedbackAgent(BaseAgent):
    """Analyzes EPLAN execution logs and reports to ProjectManager"""
    
    def __init__(self, orchestrator):
        super().__init__(orchestrator)
        self.log_path = r"C:\temp\Agent\EplanLog\Events.csv"
    
    async def process(self, context: TaskContext) -> AgentMessage:
        execution_result = await self.get_peer_result(AgentType.EXECUTION)
        
        # Wait briefly for logs to be written
        import asyncio
        await asyncio.sleep(2)
        
        log_analysis = self._read_recent_logs()
        success = self._determine_success(log_analysis, execution_result)
        
        report = self._create_report(log_analysis, success)
        
        return AgentMessage(
            agent_type=AgentType.FEEDBACK,
            content=report,
            metadata={
                'success': success,
                'log_errors': log_analysis['errors'],
                'completion_detected': log_analysis['completion_found']
            }
        )
    
    def _read_recent_logs(self) -> dict:
        analysis = {
            'errors': [],
            'warnings': [],
            'messages': [],
            'completion_found': False
        }
        
        if not os.path.exists(self.log_path):
            return analysis
        
        # Read last 10 lines for recent activity
        try:
            with open(self.log_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                recent_lines = lines[-10:] if len(lines) > 10 else lines
                
                reader = csv.DictReader(recent_lines)
                for row in reader:
                    message = row.get('Mensaje', '')
                    level = row.get('Nivel', '').lower()
                    
                    analysis['messages'].append(message)
                    
                    if 'agent final task' in message.lower():
                        analysis['completion_found'] = True
                    
                    if 'error' in level:
                        analysis['errors'].append(message)
                    elif 'warning' in level:
                        analysis['warnings'].append(message)
        
        except Exception:
            pass
        
        return analysis
    
    def _determine_success(self, log_analysis: dict, execution_result: str) -> bool:
        # Check execution result and log completion
        execution_ok = '✓' in execution_result
        no_errors = len(log_analysis['errors']) == 0
        completion_found = log_analysis['completion_found']
        
        return execution_ok and no_errors and completion_found
    
    def _create_report(self, log_analysis: dict, success: bool) -> str:
        if success:
            return "✅ Task completed successfully"
        
        issues = []
        if log_analysis['errors']:
            issues.extend([f"Error: {error}" for error in log_analysis['errors']])
        
        if not log_analysis['completion_found']:
            issues.append("Script completion not detected")
        
        return f"❌ Issues found:\n" + "\n".join(issues)