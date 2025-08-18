#!/usr/bin/env python3
"""
EPLAN Multi-Agent Coordinator - Main Entry Point
Run this file to start the agent system
"""

import sys
from pathlib import Path


project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from eplan_coordinator import root_agent

def main():
    """Main entry point for EPLAN agent system"""
    print("🚀 Starting EPLAN Agent System...")    

    print(f"✅ Agent '{root_agent.name}' initialized successfully")
    print("💬 Ready to process EPLAN automation requests")
    
if __name__ == "__main__":
    main()