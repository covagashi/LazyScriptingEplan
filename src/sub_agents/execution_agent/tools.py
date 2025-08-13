# src/sub_agents/execution_agent/tools.py
import clr
import sys
import time
from System.Collections.Generic import List
from System.Diagnostics import ProcessStartInfo, Process

class EPLANConnectionManager:
   def __init__(self):
       self.client = None
       self.connected = False
       self._setup_eplan_api()
   
   def _setup_eplan_api(self):
       eplan_path = r"C:\Program Files\EPLAN\Platform\2023.0.3\Bin"
       sys.path.append(eplan_path)
       
       clr.AddReference("Eplan.EplApi.Starteru")
       clr.AddReference("Eplan.EplApi.RemoteClientu") 
       clr.AddReference("Eplan.EplApi.Remotingu")
   
   def start_eplan_and_connect(self) -> str:
       """Start EPLAN and establish connection"""
       try:
           from Eplan.EplApi.Starter import EplanFinder, EplanData
           from Eplan.EplApi.RemoteClient import EplanRemoteClient
           from Eplan.EplApi.Remoting import CallingContext
           import System
           
           # Find and start EPLAN
           eplan_finder = EplanFinder()
           eplan_versions = List[EplanData]()
           eplan_finder.GetInstalledEplanVersions(eplan_versions, True)
           
           eplan_2023 = None
           for version in eplan_versions:
               if (version.EplanVariant == "Electric P8" and 
                   version.EplanVersion.startswith("2023")):
                   eplan_2023 = version
                   break
           
           if eplan_2023 is None:
               return "❌ EPLAN 2023 Electric P8 not found"
           
           # Start EPLAN
           start_info = ProcessStartInfo()
           start_info.FileName = eplan_2023.EplanPath
           start_info.Arguments = f'/Variant:"{eplan_2023.EplanVariant}"'
           Process.Start(start_info)
           
           # Wait and connect
           time.sleep(15)
           self.client = EplanRemoteClient()
           self.client.Connect("localhost", "49152", System.TimeSpan.FromSeconds(5))
           
           if self.client.Ping():
               self.connected = True
               return "✅ EPLAN connected successfully"
           else:
               return "❌ EPLAN not responding"
               
       except Exception as e:
           return f"❌ Connection failed: {e}"
   
   def execute_action(self, action_name: str) -> str:
       """Execute EPLAN action"""
       if not self.connected:
           conn_result = self.start_eplan_and_connect()
           if "❌" in conn_result:
               return conn_result
       
       try:
           from Eplan.EplApi.Remoting import CallingContext
           context = CallingContext()
           self.client.ExecuteAction(action_name, context)
           return f"✅ Executed: {action_name}"
       except Exception as e:
           return f"❌ Execution failed: {e}"

# Global manager
eplan_manager = EPLANConnectionManager()

def check_eplan_connection() -> str:
   """Check EPLAN connection status"""
   if eplan_manager.connected:
       return "🟢 EPLAN connected and ready"
   else:
       return eplan_manager.start_eplan_and_connect()

def execute_eplan_action(action_name: str) -> str:
   """Execute EPLAN action via persistent connection"""
   return eplan_manager.execute_action(action_name)