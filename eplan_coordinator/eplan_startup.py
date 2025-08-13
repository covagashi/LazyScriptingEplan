# eplan_coordinator/eplan_startup.py
from src.sub_agents.execution_agent.tools import eplan_manager

def initialize_eplan():
    """Auto-connect EPLAN on system startup"""
    print("🚀 Starting EPLAN connection...")
    result = eplan_manager.start_eplan_and_connect()
    print(result)
    return eplan_manager.connected

