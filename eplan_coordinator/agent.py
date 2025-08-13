# eplan_coordinator/agent.py
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.agents.callback_context import CallbackContext
from .eplan_startup import initialize_eplan
from .prompt import EPLAN_COORDINATOR_PROMPT
from src.sub_agents.knowledge_agent import knowledge_agent
from src.sub_agents.examples_agent import examples_agent
from src.sub_agents.codecraft_agent import codecraft_agent
from src.sub_agents.validation_agent import validation_agent
from src.sub_agents.execution_agent import execution_agent

def setup_eplan_on_startup(callback_context: CallbackContext):
    """Initialize EPLAN before any agent calls"""
    if "eplan_initialized" not in callback_context.state:
        initialize_eplan()
        callback_context.state["eplan_initialized"] = True

root_agent = Agent(  
    model="gemini-2.5-pro",
    name="eplan_coordinator", 
    instruction=EPLAN_COORDINATOR_PROMPT,
    tools=[
        AgentTool(agent=knowledge_agent),
        AgentTool(agent=examples_agent),
        AgentTool(agent=codecraft_agent),
        AgentTool(agent=validation_agent),
        AgentTool(agent=execution_agent),
    ],
    before_agent_callback=setup_eplan_on_startup,
)