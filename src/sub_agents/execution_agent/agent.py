# src/sub_agents/execution_agent/agent.py
from google.adk import Agent
from google.adk.tools import FunctionTool
from .tools import check_eplan_connection, execute_eplan_action
from . import prompt

execution_agent = Agent(
    model="gemini-2.5-pro",
    name="execution_agent",
    instruction=prompt.EXECUTION_AGENT_PROMPT,
    output_key="execution_output",
    tools=[
        FunctionTool(check_eplan_connection),
        FunctionTool(execute_eplan_action)
    ],
)


