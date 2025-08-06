# src/agents/execution_agent.py
import clr
import sys
from .mini_agent import MiniAgent
from ..core.message_bus import AgentMessage

class ExecutionAgent(MiniAgent):
    def __init__(self, message_bus):
        super().__init__("execution", message_bus)
        self._setup_eplan()
        self.client = None
        self._connect()
    
    def get_specialty(self) -> str:
        return "EPLAN Remoting execution, script running"
    
    async def process_message(self, message: AgentMessage):
        if message.intent == "execute_script":
            script_path = message.payload.get("script_path")
            action_name = message.payload.get("action_name", "GeneratedScript")
            
            success, result = await self._execute_script(action_name)
            
            # Auto-colaboración: pedir feedback automáticamente
            await self.send_message(
                ["feedback"],
                "analyze_execution",
                {"success": success, "result": result, "action": action_name}
            )
    
    def _setup_eplan(self):
        try:
            eplan_path = r"C:\Program Files\EPLAN\Platform\2023.0.3\Bin"
            sys.path.append(eplan_path)
            clr.AddReference("Eplan.EplApi.RemoteClientu")
            from Eplan.EplApi.RemoteClient import EplanRemoteClient
            import System
            self.EplanRemoteClient = EplanRemoteClient
            self.TimeSpan = System.TimeSpan
        except Exception as e:
            print(f"EPLAN setup failed: {e}")
    
    def _connect(self):
        try:
            self.client = self.EplanRemoteClient()
            self.client.Connect("localhost", "49152", self.TimeSpan.FromSeconds(5))
        except:
            self.client = None
    
    async def _execute_script(self, action_name: str) -> tuple:
        if not self.client:
            return False, "Not connected to EPLAN"
        
        try:
            self.client.ExecuteAction(action_name)
            return True, f"✓ Executed: {action_name}"
        except Exception as e:
            return False, f"✗ Failed: {e}"