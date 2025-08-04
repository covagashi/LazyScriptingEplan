# src/utils/logging.py
import logging
import os
from datetime import datetime

def setup_logging(log_dir: str = r"C:\temp\Agent\EplanLog"):
    """Setup logging configuration"""
    os.makedirs(log_dir, exist_ok=True)
    
    log_file = os.path.join(log_dir, "agent_system.log")
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger(__name__)

def log_agent_execution(agent_type: str, user_query: str, result: str, success: bool):
    """Log agent execution details"""
    logger = logging.getLogger('agents')
    
    status = "SUCCESS" if success else "FAILED"
    logger.info(f"[{agent_type}] {status} - Query: '{user_query}' - Result: {result[:100]}...")

def log_eplan_action(action: str, success: bool, error: str = None):
    """Log EPLAN action execution"""
    logger = logging.getLogger('eplan')
    
    if success:
        logger.info(f"EPLAN Action executed: {action}")
    else:
        logger.error(f"EPLAN Action failed: {action} - Error: {error}")