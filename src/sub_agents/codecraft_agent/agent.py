# src/sub_agents/codecraft_agent/agent.py
from google.adk import Agent
from google.adk.tools import FunctionTool
from .tools import generate_eplan_script, save_script_to_file, enhance_script_with_context
from . import prompt

codecraft_agent = Agent(
    model="gemini-2.5-flash-lite",
    name="codecraft_agent",
    instruction=prompt.CODECRAFT_AGENT_PROMPT,
    output_key="script_output",
    tools=[
        FunctionTool(generate_eplan_script),
        FunctionTool(save_script_to_file),
        FunctionTool(enhance_script_with_context)
    ],
)