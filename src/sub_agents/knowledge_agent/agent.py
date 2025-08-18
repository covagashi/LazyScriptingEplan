# src/sub_agents/knowledge_agent/agent.py
from google.adk import Agent
from google.adk.tools import FunctionTool
from .tools import search_eplan_docs, find_action_docs
from . import prompt

knowledge_agent = Agent(
    model="gemini-2.0-flash-lite",
    name="knowledge_agent",
    instruction=prompt.KNOWLEDGE_AGENT_PROMPT,
    output_key="knowledge_output",
    tools=[
        FunctionTool(search_eplan_docs),
        FunctionTool(find_action_docs)
    ],
)