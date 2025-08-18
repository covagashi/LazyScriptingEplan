# src/sub_agents/validation_agent/agent.py
from google.adk import Agent
from google.adk.tools import FunctionTool
from .tools import validate_csharp_syntax, security_audit, check_eplan_best_practices
from . import prompt

validation_agent = Agent(
    model="gemini-2.5-flash-lite",
    name="validation_agent",
    instruction=prompt.VALIDATION_AGENT_PROMPT,
    output_key="validation_output",
    tools=[
        FunctionTool(validate_csharp_syntax),
        FunctionTool(security_audit),
        FunctionTool(check_eplan_best_practices)
    ],
)