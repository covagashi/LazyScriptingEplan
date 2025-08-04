# src/orchestrator/types.py
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from enum import Enum

class AgentType(Enum):
    CONVERSATION = "conversation"
    CODE_GENERATOR = "code_generator"
    PROJECT_MANAGER = "project_manager"
    KNOWLEDGE = "knowledge"
    EXECUTION = "execution"
    FEEDBACK = "feedback"

class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass
class AgentMessage:
    agent_type: AgentType
    content: str
    metadata: Optional[Dict[str, Any]] = field(default_factory=dict)
    status: TaskStatus = TaskStatus.COMPLETED

@dataclass
class TaskContext:
    user_query: str
    current_project: Optional[str] = None
    session_history: List[str] = field(default_factory=list)
    eplan_state: Dict[str, Any] = field(default_factory=dict)
    agent_results: Dict[AgentType, AgentMessage] = field(default_factory=dict)

@dataclass
class EplanAction:
    action_name: str
    parameters: Dict[str, str] = field(default_factory=dict)
    description: str = ""

@dataclass
class ExecutionResult:
    success: bool
    message: str
    action_executed: Optional[str] = None
    error_details: Optional[str] = None