# src/agents/feedback_agent.py
import os
import csv
import asyncio
from .mini_agent import MiniAgent
from ..core.message_bus import AgentMessage

class FeedbackAgent(MiniAgent):
    def __init__(self, message_bus):
        super().__init__("feedback", message_bus)
        self.log_path = r"C:\temp\Agent\EplanLog\Events.csv"
    
    def get_specialty(self) -> str:
        return "EPLAN software log analysis, execution validation"
    
    async def process_message(self, message: AgentMessage):
        if message.intent == "analyze_execution":
            success = message.payload.get("success", False)
            result = message.payload.get("result", "")
            action = message.payload.get("action", "Unknown")
            
            # Esperar logs
            await asyncio.sleep(2)
            
            log_analysis = self._analyze_logs()
            final_success = success and len(log_analysis['errors']) == 0
            
            report = f"✅ Success" if final_success else f"❌ Issues: {log_analysis['errors']}"
            
            # Responder directamente al usuario
            await self.send_message(
                ["conversation"],
                "response_to_user",
                {"content": f"⚡ Execution: {result}\n📊 Feedback: {report}"}
            )
    
    def _analyze_logs(self) -> dict:
        analysis = {'errors': [], 'warnings': []}
        
        if not os.path.exists(self.log_path):
            return analysis
        
        try:
            with open(self.log_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()[-5:]  # Últimas 5 líneas
                
                for line in lines:
                    if 'error' in line.lower():
                        analysis['errors'].append(line.strip())
        except:
            pass
        
        return analysis