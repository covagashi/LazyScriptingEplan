# src/utils/config.py
import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class EplanConfig:
    """EPLAN configuration settings"""
    eplan_path: str = r"C:\Program Files\EPLAN\Platform\2023.0.3\Bin"
    remoting_host: str = "localhost"
    remoting_port: str = "49152"
    connection_timeout: int = 5

@dataclass
class AgentConfig:
    """Agent system configuration"""
    output_dir: str = r"C:\temp\Agent"
    log_dir: str = r"C:\temp\Agent\EplanLog"
    script_filename: str = "eplan_script.cs"
    log_filename: str = "Events.csv"

@dataclass
class AIConfig:
    """AI configuration"""
    gemini_api_key: str = os.getenv('GEMINI_API_KEY', '')
    model_name: str = 'gemini-1.5-flash'
    max_tokens: int = 4096

class Config:
    """Main configuration class"""
    
    def __init__(self):
        self.eplan = EplanConfig()
        self.agents = AgentConfig()
        self.ai = AIConfig()
    
    def validate(self) -> bool:
        """Validate configuration"""
        if not self.ai.gemini_api_key:
            raise ValueError("GEMINI_API_KEY not found")
        
        if not os.path.exists(self.eplan.eplan_path):
            raise ValueError(f"EPLAN path not found: {self.eplan.eplan_path}")
        
        return True