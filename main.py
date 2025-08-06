import asyncio
from src.core.message_bus import MessageBus
from src.agents.conversation_agent import ConversationAgent
from src.agents.knowledge_agent import EplanKnowledgeAgent
from src.agents.codecraft_agent import CodeCraftAgent
from src.agents.execution_agent import ExecutionAgent
from src.agents.feedback_agent import FeedbackAgent

async def main():
    bus = MessageBus()
    
    # Todos los mini-agentes
    conversation = ConversationAgent(bus)
    knowledge = EplanKnowledgeAgent(bus)
    codecraft = CodeCraftAgent(bus)
    execution = ExecutionAgent(bus)
    feedback = FeedbackAgent(bus)
    
    await bus.register_agent("conversation", conversation)
    await bus.register_agent("knowledge", knowledge) 
    await bus.register_agent("codecraft", codecraft)
    await bus.register_agent("execution", execution)
    await bus.register_agent("feedback", feedback)
    
    print("🤖 EPLAN Agent System")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'quit':
            break
        
        response = await conversation.handle_user_input(user_input)
        print(f"System: {response}")

if __name__ == "__main__":
    asyncio.run(main())