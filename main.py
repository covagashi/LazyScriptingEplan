# main.py
import asyncio
import yaml
from src.orchestrator import EplanOrchestrator, AgentType
from src.agents import (
    ConversationAgent,
    CodeGeneratorAgent, 
    KnowledgeAgent,
    ExecutionAgent,
    FeedbackAgent,
    ProjectManagerAgent
)
from src.utils import setup_logging, Config

def load_config():
    """Load configuration from YAML files"""
    config = Config()
    
    try:
        with open('config/agents.yaml', 'r') as f:
            agents_config = yaml.safe_load(f)
        with open('config/eplan.yaml', 'r') as f:
            eplan_config = yaml.safe_load(f)
        
        return config, agents_config, eplan_config
    except FileNotFoundError:
        print("Warning: Config files not found, using defaults")
        return config, {}, {}

async def main():
    # Setup
    config, agents_config, eplan_config = load_config()
    logger = setup_logging()
    
    try:
        config.validate()
    except ValueError as e:
        print(f"Configuration error: {e}")
        return
    
    # Initialize orchestrator
    orchestrator = EplanOrchestrator()
    
    # Register agents
    orchestrator.register_agent(AgentType.CONVERSATION, ConversationAgent(orchestrator))
    orchestrator.register_agent(AgentType.CODE_GENERATOR, CodeGeneratorAgent(orchestrator))
    orchestrator.register_agent(AgentType.KNOWLEDGE, KnowledgeAgent(orchestrator))
    orchestrator.register_agent(AgentType.EXECUTION, ExecutionAgent(orchestrator))
    orchestrator.register_agent(AgentType.FEEDBACK, FeedbackAgent(orchestrator))
    orchestrator.register_agent(AgentType.PROJECT_MANAGER, ProjectManagerAgent(orchestrator))
    
    print("🤖 EPLAN Multi-Agent System")
    print("Workflows: Generation | Execution")

    # Force rebuild RAG cache to pick up latest JSON files
    #print("Rebuilding RAG cache...")
    from src.ai.rag import EplanRAG
    rag = EplanRAG()
    rag.rebuild_cache()
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'quit':
            break
        
        try:
            response = await orchestrator.process_user_input(user_input)
            #print(f"\nSystem:\n{response}")
        except Exception as e:
            logger.error(f"Processing error: {e}")
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())