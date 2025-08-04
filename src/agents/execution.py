# src/agents/execution.py
from .base import BaseAgent
from ..orchestrator.types import AgentMessage, TaskContext, AgentType

class ExecutionAgent(BaseAgent):
    """Executes EPLAN actions via Remoting API"""
    
    def __init__(self, orchestrator):
        super().__init__(orchestrator)
        self.client = None
        self._setup_eplan()
        self._connect()
    
    def _setup_eplan(self):
        try:
            import clr
            import sys
            
            eplan_path = r"C:\Program Files\EPLAN\Platform\2023.0.3\Bin"
            sys.path.append(eplan_path)
            
            clr.AddReference("Eplan.EplApi.RemoteClientu")
            
            from Eplan.EplApi.RemoteClient import EplanRemoteClient
            import System
            
            self.EplanRemoteClient = EplanRemoteClient
            self.TimeSpan = System.TimeSpan
            
        except Exception as e:
            self.eplan_available = False
    
    def _connect(self):
        try:
            self.client = self.EplanRemoteClient()
            self.client.SynchronousMode = True
            self.client.Connect("localhost", "49152", self.TimeSpan(0, 0, 0, 5))
        except Exception as e:
            self.client = None
    
    async def process(self, context: TaskContext) -> AgentMessage:
        if not self.client:
            return AgentMessage(
                agent_type=AgentType.EXECUTION,
                content="✗ EPLAN not connected",
                metadata={'success': False}
            )
        
        # Get action name from ProjectManager
        pm_result = await self.get_peer_result(AgentType.PROJECT_MANAGER)
        pm_metadata = getattr(pm_result, 'metadata', {})
        action_name = pm_metadata.get('action_name')
        
        if not action_name or not pm_metadata.get('script_ready'):
            return AgentMessage(
                agent_type=AgentType.EXECUTION,
                content="✗ No action ready for execution",
                metadata={'success': False}
            )
        
        try:
            # Execute the action that triggers the script
            self.client.ExecuteAction(action_name)
            
            return AgentMessage(
                agent_type=AgentType.EXECUTION,
                content=f"✓ Executed: {action_name}",
                metadata={'success': True, 'action': action_name}
            )
            
        except Exception as e:
            return AgentMessage(
                agent_type=AgentType.EXECUTION,
                content=f"✗ Execution failed: {e}",
                metadata={'success': False, 'error': str(e)}
            )