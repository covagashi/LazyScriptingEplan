# main_enhanced.py
import asyncio
import signal
import sys
from pathlib import Path
import watchdog.observers
import watchdog.events

from src.core.message_bus import MessageBus
from src.agents.filesystem_agent import FileSystemAgent
from src.agents.conversation_agent import EnhancedConversationAgent
from src.agents.knowledge_agent import EplanKnowledgeAgent
from src.agents.codecraft_agent import CodeCraftAgent
from src.agents.execution_agent import ExecutionAgent
from src.agents.feedback_agent import FeedbackAgent

class EplanAgentSystem:
    """Sistema principal mejorado con FileSystemAgent"""
    
    def __init__(self):
        self.bus = MessageBus()
        self.agents = {}
        self.running = True
        
        # Señales para cierre limpio
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
    
    def _signal_handler(self, signum, frame):
        """Manejo de señales para cierre limpio"""
        print("\n🛑 Shutting down system...")
        self.running = False
    
    async def initialize_system(self):
        """Inicializar sistema con todos los agentes"""
        
        print("🚀 Initializing Enhanced EPLAN Agent System")
        print("=" * 50)
        
        # 1. FileSystemAgent PRIMERO (otros dependen de él)
        print("📁 Initializing FileSystemAgent...")
        filesystem = FileSystemAgent(self.bus)
        await self.bus.register_agent("filesystem", filesystem)
        self.agents["filesystem"] = filesystem
        await filesystem.startup()
        
        # 2. ConversationAgent mejorado
        print("💬 Initializing Enhanced ConversationAgent...")
        conversation = EnhancedConversationAgent(self.bus)
        await self.bus.register_agent("conversation", conversation)
        self.agents["conversation"] = conversation
        await conversation.startup()
        
        # 3. Agentes especializados existentes
        print("📚 Initializing KnowledgeAgent...")
        knowledge = EplanKnowledgeAgent(self.bus)
        await self.bus.register_agent("knowledge", knowledge)
        self.agents["knowledge"] = knowledge
        
        print("⚙️ Initializing CodeCraftAgent...")
        codecraft = CodeCraftAgent(self.bus)
        await self.bus.register_agent("codecraft", codecraft)
        self.agents["codecraft"] = codecraft
        
        print("🔧 Initializing ExecutionAgent...")
        execution = ExecutionAgent(self.bus)
        await self.bus.register_agent("execution", execution)
        self.agents["execution"] = execution
        
        print("📊 Initializing FeedbackAgent...")
        feedback = FeedbackAgent(self.bus)
        await self.bus.register_agent("feedback", feedback)
        self.agents["feedback"] = feedback
        
        print("\n✅ All agents initialized successfully!")
        print(f"📈 System ready with {len(self.agents)} agents")
        print("=" * 50)
        
        # Test del sistema
        await self._run_system_tests()
    
    async def _run_system_tests(self):
        """Ejecutar tests básicos del sistema"""
        print("\n🧪 Running system tests...")
        
        try:
            # Test FileSystemAgent
            test_context = {"test": "data", "timestamp": "now"}
            context_ref = await self.agents["conversation"].store_heavy_context(
                test_context, 
                "system_test", 
                {"purpose": "initialization_test"}
            )
            
            if context_ref:
                print("✅ FileSystemAgent: Context storage working")
                
                # Test recovery
                recovered = await context_ref.load()
                if recovered and recovered.get("data", {}).get("test") == "data":
                    print("✅ FileSystemAgent: Context recovery working")
                else:
                    print("⚠️ FileSystemAgent: Context recovery issue")
            else:
                print("⚠️ FileSystemAgent: Context storage issue")
            
            # Test agent communication
            capable_agents = await self.bus.find_capable_agents("hello test")
            if capable_agents:
                print(f"✅ Agent Discovery: Found {len(capable_agents)} capable agents")
            else:
                print("⚠️ Agent Discovery: No agents found")
            
            print("🧪 System tests completed\n")
            
        except Exception as e:
            print(f"❌ System test failed: {e}")
    
    async def run_interactive_mode(self):
        """Modo interactivo principal"""
        
        print("🤖 Enhanced EPLAN Agent System - Interactive Mode")
        print("Type 'quit', 'exit', or Ctrl+C to stop")
        print("Type 'status' for system status")
        print("Type 'help' for available commands")
        print("-" * 50)
        
        conversation_agent = self.agents["conversation"]
        
        while self.running:
            try:
                user_input = input("\n👤 You: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    break
                elif user_input.lower() == 'status':
                    await self._show_system_status()
                    continue
                elif user_input.lower() == 'help':
                    self._show_help()
                    continue
                elif user_input.lower() == 'debug':
                    await self._debug_mode()
                    continue
                
                print("🤔 Processing...", end="", flush=True)
                
                # Procesar con ConversationAgent mejorado
                response = await conversation_agent.handle_user_input(user_input)
                
                print("\r" + " " * 20 + "\r", end="")  # Clear processing message
                print(f"🤖 System: {response}")
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                continue
    
    async def _show_system_status(self):
        """Mostrar estado del sistema"""
        print("\n📊 System Status:")
        print("=" * 30)
        
        # Estado de agentes
        for agent_id, agent in self.agents.items():
            status = "🟢 Active"
            if hasattr(agent, 'working') and agent.working:
                status = "🟡 Working"
            print(f"{agent_id:15} {status}")
        
        # Estado del FileSystem
        fs_agent = self.agents.get("filesystem")
        if fs_agent:
            cache_size = len(fs_agent.memory_cache)
            refs_size = len(fs_agent.context_refs)
            print(f"\n📁 FileSystem: {cache_size} cached, {refs_size} refs")
        
        # Estado de conversación
        conv_agent = self.agents.get("conversation")
        if conv_agent:
            history_len = len(conv_agent.conversation_history)
            active_reqs = len(conv_agent.active_requests)
            print(f"💬 Conversation: {history_len} history, {active_reqs} active requests")
        
        print("=" * 30)
    
    def _show_help(self):
        """Mostrar ayuda de comandos"""
        print("\n📋 Available Commands:")
        print("=" * 30)
        print("help     - Show this help")
        print("status   - Show system status")
        print("debug    - Enter debug mode")
        print("quit/exit - Exit system")
        print("\n💡 EPLAN Examples:")
        print("- 'Create a script to open project MainPanel.elk'")
        print("- 'How do I use XAfActionSetting?'")
        print("- 'Generate code for progress dialog'")
        print("- 'Execute the generated script'")
        print("=" * 30)
    
    async def _debug_mode(self):
        """Modo debug interactivo"""
        print("\n🔍 Debug Mode (type 'back' to return)")
        print("-" * 30)
        
        while True:
            debug_cmd = input("Debug> ").strip().lower()
            
            if debug_cmd == 'back':
                break
            elif debug_cmd == 'agents':
                print("Registered agents:")
                for agent_id, agent in self.agents.items():
                    specialty = agent.get_specialty() if hasattr(agent, 'get_specialty') else "Unknown"
                    print(f"  {agent_id}: {specialty}")
            elif debug_cmd == 'cache':
                fs_agent = self.agents.get("filesystem")
                if fs_agent:
                    print(f"Memory cache: {list(fs_agent.memory_cache.keys())}")
                    print(f"Context refs: {list(fs_agent.context_refs.keys())}")
            elif debug_cmd == 'conversation':
                conv_agent = self.agents.get("conversation")
                if conv_agent and conv_agent.conversation_history:
                    print("Recent conversation:")
                    for entry in conv_agent.conversation_history[-3:]:
                        print(f"  {entry.get('type')}: {entry.get('content', '')[:50]}...")
            elif debug_cmd == 'test':
                await self._run_debug_test()
            else:
                print("Debug commands: agents, cache, conversation, test, back")
    
    async def _run_debug_test(self):
        """Test rápido en modo debug"""
        print("Running debug test...")
        try:
            # Test simple
            conv_agent = self.agents["conversation"]
            response = await conv_agent.handle_user_input("hello debug test")
            print(f"Test response: {response[:100]}...")
        except Exception as e:
            print(f"Debug test failed: {e}")
    
    async def shutdown_system(self):
        """Cierre limpio del sistema"""
        print("\n🛑 Shutting down Enhanced EPLAN Agent System...")
        
        # Cerrar agentes en orden inverso
        for agent_id in reversed(list(self.agents.keys())):
            agent = self.agents[agent_id]
            try:
                if hasattr(agent, 'shutdown'):
                    await agent.shutdown()
                print(f"✅ {agent_id} shut down")
            except Exception as e:
                print(f"⚠️ {agent_id} shutdown error: {e}")
        
        # Parar MessageBus
        self.bus.running = False
        
        print("👋 System shutdown complete")


async def main():
    """Función principal"""
    
    # Verificar dependencias
    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
    except ImportError:
        print("❌ Missing dependency: watchdog")
        print("Install with: pip install watchdog")
        return 1
    
    # Verificar directorios necesarios
    required_paths = [
        Path("src/ai/Knowledge/API"),
        Path("src/ai/Knowledge/Scripts"),
        Path("C:/temp/Agent")
    ]
    
    for path in required_paths:
        if not path.exists():
            print(f"⚠️ Creating missing directory: {path}")
            path.mkdir(parents=True, exist_ok=True)
    
    # Inicializar sistema
    system = EplanAgentSystem()
    
    try:
        # Inicializar todos los agentes
        await system.initialize_system()
        
        # Ejecutar modo interactivo
        await system.run_interactive_mode()
        
    except KeyboardInterrupt:
        print("\n⚠️ Interrupted by user")
    except Exception as e:
        print(f"❌ System error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        # Cierre limpio
        await system.shutdown_system()
    
    return 0


if __name__ == "__main__":
    # Configurar event loop para Windows si es necesario
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    
    exit_code = asyncio.run(main())
    sys.exit(exit_code)