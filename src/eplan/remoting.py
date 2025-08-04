# src/eplan/remoting.py
import clr
import sys
from typing import Dict, Optional, Tuple

class EplanRemoting:
    """EPLAN Remoting API wrapper"""
    
    def __init__(self, eplan_path: str = r"C:\Program Files\EPLAN\Platform\2023.0.3\Bin"):
        self.eplan_path = eplan_path
        self.client = None
        self._setup_clr()
    
    def _setup_clr(self):
        try:
            sys.path.append(self.eplan_path)
            clr.AddReference("Eplan.EplApi.RemoteClientu")
            clr.AddReference("Eplan.EplApi.Remotingu")
            
            from Eplan.EplApi.RemoteClient import EplanRemoteClient
            from Eplan.EplApi.Remoting import CallingContext
            import System
            
            self.EplanRemoteClient = EplanRemoteClient
            self.CallingContext = CallingContext
            self.TimeSpan = System.TimeSpan
            
        except Exception as e:
            raise ImportError(f"Failed to load EPLAN assemblies: {e}")
    
    def connect(self, host: str = "localhost", port: str = "49152", timeout: int = 5) -> bool:
        try:
            self.client = self.EplanRemoteClient()
            self.client.Connect(host, port, self.TimeSpan.FromSeconds(timeout))
            return self.client.Ping()
        except Exception:
            return False
    
    def disconnect(self):
        if self.client:
            try:
                self.client.Disconnect()
            except:
                pass
            finally:
                self.client = None
    
    def execute_action(self, action: str, parameters: Dict[str, str] = None) -> Tuple[bool, str]:
        if not self.client:
            return False, "Not connected to EPLAN"
        
        try:
            ctx = self.CallingContext()
            
            if parameters:
                for key, value in parameters.items():
                    ctx.AddParameter(key, value)
            
            self.client.ExecuteAction(action, ctx)
            return True, f"Action '{action}' executed successfully"
            
        except Exception as e:
            return False, str(e)
    
    def is_connected(self) -> bool:
        return self.client and self.client.Ping()