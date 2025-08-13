# src/sub_agents/examples_agent/agent.py
from google.adk import Agent
from google.adk.tools import FunctionTool
from .tools import search_script_examples, find_pattern_examples
from . import prompt

examples_agent = Agent(
    model="gemini-2.5-pro",
    name="examples_agent",
    instruction=prompt.EXAMPLES_AGENT_PROMPT,
    output_key="examples_output",
    tools=[
        FunctionTool(search_script_examples),
        FunctionTool(find_pattern_examples)
    ],
)