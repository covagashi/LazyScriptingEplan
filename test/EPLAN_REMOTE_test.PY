import clr
import sys
import os
from System.Collections.Generic import List
from System.Diagnostics import ProcessStartInfo, Process

# EPLAN API path
eplan_path = r"C:\Program Files\EPLAN\Platform\2023.0.3\Bin"
sys.path.append(eplan_path)

try:   
   clr.AddReference("Eplan.EplApi.Starteru")
   clr.AddReference("Eplan.EplApi.RemoteClientu") 
   clr.AddReference("Eplan.EplApi.Remotingu")
   
   from Eplan.EplApi.Starter import EplanFinder, EplanData
   from Eplan.EplApi.RemoteClient import EplanRemoteClient
   from Eplan.EplApi.Remoting import CallingContext
   import System
   
   def start_eplan_server():
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
           print("EPLAN 2023 Electric P8 not found")
           return False
           
       print(f"Starting EPLAN: {eplan_2023.EplanVersion}")
       
       start_info = ProcessStartInfo()
       start_info.FileName = eplan_2023.EplanPath
       start_info.Arguments = f'/Variant:"{eplan_2023.EplanVariant}"'
       
       try:
           Process.Start(start_info)
           print("EPLAN started successfully")
           return True
       except Exception as e:
           print(f"Error starting EPLAN: {e}")
           return False
   
   def test_connection():
       import time
       
       print("Waiting for EPLAN to initialize...")
       time.sleep(15)
       
       client = EplanRemoteClient()
       try:
           client.Connect("localhost", "49152", System.TimeSpan.FromSeconds(5))
           
           if client.Ping():
               print("✓ Connected to EPLAN server!")
               
               # Test XPrjActionProjectClose
               context = CallingContext()
               client.ExecuteAction("XPrjActionProjectClose", context)
               print("✓ XPrjActionProjectClose executed successfully")
               
           else:
               print("✗ EPLAN not responding")
               
       except Exception as e:
           print(f"Connection error: {e}")
       finally:
           try:
               client.Disconnect()
           except:
               pass
   
   if start_eplan_server():
       test_connection()
   
except Exception as e:
   print(f"Error: {e}")