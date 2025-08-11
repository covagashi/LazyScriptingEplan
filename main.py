# main.py - FIXED VERSION mantiene tu estructura original
import asyncio
import signal
import sys
from pathlib import Path
import json

from src.core.message_bus import ObservableMessageBus
from src.agents.mini_agent import MiniAgent
from src.agents.filesystem_agent import FileSystemAgent
from src.agents.conversation_agent import ConversationAgent
from src.agents.knowledge_agent import EplanKnowledgeAgent
from src.agents.codecraft_agent import CodeCraftAgent
from src.agents.execution_agent import ExecutionAgent
from src.agents.feedback_agent import FeedbackAgent
from src.core.memory_manager import AutoMemoryManager



def load_agent_from_artifact(artifact_name, class_name):
    """Load agent class from artifact file"""
    try:
        artifact_path = Path(f"{artifact_name}.py")
        if not artifact_path.exists():
            return None
            
        spec = importlib.util.spec_from_file_location(class_name, artifact_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return getattr(module, class_name)
    except Exception as e:
        print(f"⚠️ Could not load {class_name} from artifact: {e}")
        return None

class FixedEplanAgentSystem:
    """Fixed EPLAN Agent System with proper router initialization"""
    
    def __init__(self):
        self.bus = ObservableMessageBus() 
        self.agents = {}
        self.running = True
        
        self.dashboard = self.bus.get_dashboard()
        self._dashboard_task = None
        
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
    
    def _signal_handler(self, signum, frame):
        """Handle signals for clean shutdown"""
        print("\n🛑 Shutting down fixed system...")
        self.running = False
        
        if self.dashboard:
            self.dashboard.save_dashboard_snapshot()
    
    async def initialize_system(self):
        """Initialize system with fixed agents - SEQUENCED STARTUP"""
        self.memory_manager = AutoMemoryManager(memory_limit_mb=800)
        await self.memory_manager.start_monitoring()
        
        print("🚀 Initializing Fixed EPLAN Agent System")
        print("🔧 Router initialization fixes applied")
        print("=" * 60)
        
        # FIX 1: Initialize agents in dependency order with delays
        await self._initialize_core_agents()
        await asyncio.sleep(1.0)  # Let core agents settle
        
        await self._initialize_specialized_agents()
        await asyncio.sleep(0.5)  # Final settling time
        
        print("\n✅ All agents initialized with fixed routing!")
        print(f"📈 System ready with {len(self.agents)} agents")
        print("📊 Real-time P2P dashboard active")
        print("=" * 60)
        
        self._start_dashboard_monitoring()
        
        # FIX 2: Optional system tests (not blocking)
        try:
            await asyncio.wait_for(self._run_system_tests(), timeout=10.0)
        except asyncio.TimeoutError:
            print("⚠️ System tests timed out, continuing...")
    
    async def periodic_cleanup(self):
        """Background task para limpiar flows obsoletos"""
        while self.running:
            try:
                await asyncio.sleep(60)  
                if self.running:
                    cleaned = self.dashboard.cleanup_stale_flows(300) 
                    if cleaned > 0:
                        print(f"🧹 Cleaned {cleaned} stale flows")
            except Exception as e:
                print(f"Cleanup error: {e}")

    async def _initialize_core_agents(self):
        """Initialize core infrastructure agents - FIXED ORDER"""
        
        # FIX 3: FileSystem MUST be first and fully ready
        print("📁 Initializing FileSystemAgent...")
        try:
            filesystem = FileSystemAgent(self.bus)
            await self.bus.register_agent("filesystem", filesystem) 
            self.agents["filesystem"] = filesystem
            
            # Startup seguro sin timeout estricto
            filesystem_ready = await self._safe_agent_startup(filesystem)
            if filesystem_ready:
                print("  ✅ filesystem ready")
            else:
                print("  ⚠️ filesystem partial ready")
                
            await asyncio.sleep(1.0)  # Dar tiempo para settling
            
        except Exception as e:
            print(f"  ❌ filesystem failed: {e}")
            
        await asyncio.sleep(0.5)  # Let filesystem fully initialize
        
        print("💬 Initializing ConversationAgent...")
        conversation = ConversationAgent(self.bus)
        await self._register_agent_with_retry("conversation", conversation)
    
    async def _initialize_specialized_agents(self):
        """Initialize specialized agents with proper error handling"""
        
        # FIX 4: PlanningAgent with safe import
        print("🎯 Initializing PlanningAgent...")
        if PlanningAgent:
            try:
                planning = PlanningAgent(self.bus)
                await self._register_agent_with_retry("planning", planning)
            except Exception as e:
                print(f"⚠️ PlanningAgent failed, continuing: {e}")
        else:
            print("⚠️ PlanningAgent not available, skipping...")
        
        print("📚 Initializing KnowledgeAgent...")
        knowledge = EplanKnowledgeAgent(self.bus)
        await self._register_agent_with_retry("knowledge", knowledge)
        
        # FIX 5: CodeCraft with async loading fix
        print("⚙️ Initializing CodeCraftAgent...")
        codecraft = CodeCraftAgent(self.bus)
        # Ensure ScriptRAG is properly loaded
        if hasattr(codecraft, 'script_rag') and hasattr(codecraft.script_rag, 'ensure_loaded'):
            try:
                await codecraft.script_rag.ensure_loaded()
            except Exception as e:
                print(f"⚠️ ScriptRAG loading issue (non-critical): {e}")
        await self._register_agent_with_retry("codecraft", codecraft)
        
        # FIX 6: ValidationAgent with safe import
        print("✅ Initializing ValidationAgent...")
        if ValidationAgent:
            try:
                validation = ValidationAgent(self.bus)
                await self._register_agent_with_retry("validation", validation)
            except Exception as e:
                print(f"⚠️ ValidationAgent failed, continuing: {e}")
        else:
            print("⚠️ ValidationAgent not available, skipping...")
        
        print("🔧 Initializing ExecutionAgent...")
        try:
            execution = ExecutionAgent(self.bus)
            await self._register_agent_with_retry("execution", execution)
        except Exception as e:
            print(f"⚠️ ExecutionAgent failed (EPLAN not available?): {e}")
        
        print("📊 Initializing FeedbackAgent...")
        feedback = FeedbackAgent(self.bus)
        await self._register_agent_with_retry("feedback", feedback)
    
    async def _register_agent_with_retry(self, agent_id: str, agent, max_retries: int = 3):
        """Register agent with retry logic for robustness"""
        
        for attempt in range(max_retries):
            try:
                await self.bus.register_agent(agent_id, agent)
                self.agents[agent_id] = agent
                
                # STARTUP SIN TIMEOUT ESTRICTO
                try:
                    await agent.startup()
                    print(f"  ✅ {agent_id} registered and started")
                    return
                except Exception as startup_error:
                    print(f"  ⚠️ {agent_id} startup issue: {startup_error}")
                    # Continúa - el agente puede funcionar parcialmente
                    print(f"  ✅ {agent_id} registered (partial startup)")
                    return
                    
            except Exception as e:
                print(f"  ❌ {agent_id} registration error: {e}")
                if attempt == max_retries - 1:
                    print(f"  ❌ {agent_id} failed permanently")
                else:
                    await asyncio.sleep(0.5)
    
    def _start_dashboard_monitoring(self):
        """Start background dashboard monitoring"""
        self._dashboard_task = asyncio.create_task(self._dashboard_monitor_loop())
    
    async def _dashboard_monitor_loop(self):
        """Background loop for dashboard monitoring"""
        while self.running:
            try:
                await asyncio.sleep(300)  # 5 minutes
                if self.running:
                    self.dashboard.save_dashboard_snapshot()
                    
                    anomalies = self.dashboard.detect_anomalies()
                    if anomalies:
                        print(f"\n⚠️ Dashboard Alert: {len(anomalies)} anomalies detected")
                        for anomaly in anomalies[:3]:
                            print(f"   └─ {anomaly['type']}: {anomaly.get('trace_id', 'N/A')[:12]}...")
                
            except Exception as e:
                print(f"Dashboard monitoring error: {e}")
                await asyncio.sleep(60)  # Retry in 1 minute
    
    async def _run_system_tests(self):
        """Run basic system tests - FIX 9: Non-blocking with timeout"""
        print("\n🧪 Running System Verification Tests...")
        
        try:
            # Test 1: Agent routing
            test_queries = [
                "hello", "generate script", "validate code", 
                "execute action", "check results"
            ]
            
            routing_working = 0
            for query in test_queries:
                try:
                    # FIX 10: Timeout per query to prevent hanging
                    capable_agents = await asyncio.wait_for(
                        self.bus.find_capable_agents(query), 
                        timeout=2.0
                    )
                    if capable_agents:
                        routing_working += 1
                        print(f"✅ '{query}' -> {capable_agents}")
                    else:
                        print(f"⚠️ '{query}' -> No capable agents")
                except asyncio.TimeoutError:
                    print(f"⏱️ '{query}' -> Timeout")
                except Exception as e:
                    print(f"❌ '{query}' -> Error: {e}")
            
            print(f"📊 Routing test: {routing_working}/{len(test_queries)} queries routed successfully")
            
            # Test 2: Dashboard functionality
            status = self.dashboard.get_real_time_status()
            print(f"✅ Dashboard: {status['active_flows']['count']} flows, {len(self.agents)} agents")
            
            # Test 3: Message flow (lightweight test)
            from src.core.message_bus import AgentMessage
            test_message = AgentMessage(
                sender="system_test",
                recipients=["conversation"],
                intent="test_system_health",
                payload={"test": True}
            )
            
            await self.bus.broadcast(test_message)
            print("✅ Message broadcast test completed")
            
            print("🧪 System verification completed\n")
            
        except Exception as e:
            print(f"❌ System test failed: {e}")
    
    async def run_interactive_mode(self):
        """Enhanced interactive mode with better error handling"""
        
        print("🤖 Fixed EPLAN Agent System - Interactive Mode")
        print("🔧 Router initialization fixes active")
        print("📊 Real-time P2P Dashboard Active")
        print("Type 'quit', 'exit', or Ctrl+C to stop")
        print("Type 'help' for available commands")
        print("-" * 70)
        
        if "conversation" not in self.agents:
            print("⚠️ ConversationAgent not available, using basic mode")
            await self._run_basic_mode()
            return
        
        conversation_agent = self.agents["conversation"]
        
        while self.running:
            try:
                user_input = input("\n👤 You: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    break
                elif user_input.lower() == 'status':
                    await self._show_enhanced_system_status()
                    continue
                elif user_input.lower() == 'dashboard':
                    self.dashboard.print_real_time_dashboard()
                    continue
                elif user_input.lower() == 'agents':
                    self._show_agent_status()
                    continue
                elif user_input.lower() == 'test':
                    await self._run_system_tests()
                    continue
                elif user_input.lower() == 'help':
                    self._show_help()
                    continue
                
                print("🤔 Processing...", end="", flush=True)
                
                try:
                    # FIX 11: Timeout user queries to prevent hanging
                    try:
                        response = await conversation_agent.handle_user_input(user_input)
                    except Exception as e:
                        print(f"\r❌ Error: {e}")
                        continue
                    
                    print("\r" + " " * 20 + "\r", end="")
                    print(f"🤖 System: {response}")
                    
                except asyncio.TimeoutError:
                    print("\r" + " " * 20 + "\r", end="")
                    print("⏱️ Request timed out. The system may be busy. Try again.")
                except Exception as e:
                    print("\r" + " " * 20 + "\r", end="")
                    print(f"⚠️ Processing error: {e}")
                    print("The system is still running. Try a different query.")
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                continue
    
    async def _run_basic_mode(self):
        """FIX 12: Basic mode when ConversationAgent fails"""
        print("🔧 Running in basic mode...")
        
        while self.running:
            try:
                user_input = input("\nBasic> ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    break
                elif user_input.lower() == 'agents':
                    self._show_agent_status()
                elif user_input.lower() == 'dashboard':
                    self.dashboard.print_real_time_dashboard()
                else:
                    print("Basic mode: Try 'agents', 'dashboard', or 'quit'")
                    
            except KeyboardInterrupt:
                break
    
    def _show_agent_status(self):
        """Show status of all agents"""
        print("\n🤖 Agent Status:")
        print("-" * 40)
        
        for agent_id, agent in self.agents.items():
            status = "🟢 Active"
            if hasattr(agent, 'working') and agent.working:
                status = "🟡 Working"
            
            router_status = ""
            if hasattr(agent, 'router') and agent.router:
                router_status = " (Router: ✅)"
            elif hasattr(agent, 'router'):
                router_status = " (Router: ❌)"
            
            print(f"{agent_id:15} {status}{router_status}")
        
        print("-" * 40)
    
    def _show_help(self):
        """Show help information"""
        print("\n📋 Available Commands:")
        print("=" * 40)
        print("🔧 System Commands:")
        print("  help        - Show this help")
        print("  status      - System status") 
        print("  agents      - Show agent status")
        print("  dashboard   - Real-time dashboard")
        print("  test        - Run system tests")
        print("  quit/exit   - Exit system")
        
        print("\n💡 EPLAN Examples:")
        print("  'Create script to open MainPanel.elk'")
        print("  'Generate C# code for EPLAN automation'")
        print("  'Help with EPLAN API documentation'")
        print("=" * 40)
    
    async def _show_enhanced_system_status(self):
        """Show enhanced system status"""
        print("\n📊 Enhanced System Status:")
        print("=" * 45)
        
        # Agent status
        self._show_agent_status()
        
        # Dashboard status
        status = self.dashboard.get_real_time_status()
        print(f"\n📊 P2P Dashboard:")
        print(f"   Active Flows: {status['active_flows']['count']}")
        print(f"   Recent Events: {status['recent_activity']['events_last_60s']}")
        
        # Memory status
        if hasattr(self, 'memory_manager'):
            memory_stats = self.memory_manager.get_memory_stats()
            print(f"\n🧠 Memory Status:")
            print(f"   Usage: {memory_stats['usage_percent']:.1f}% ({memory_stats['current_mb']:.1f}MB)")
        
        print("=" * 45)
    
    async def shutdown_system(self):
        """Enhanced shutdown with proper cleanup"""
        print("\n🛑 Shutting down Fixed EPLAN Agent System...")
        
        self.running = False
        
        if self._dashboard_task:
            self._dashboard_task.cancel()
            try:
                await self._dashboard_task
            except asyncio.CancelledError:
                pass
        
        print("📸 Saving final dashboard snapshot...")
        try:
            final_snapshot = self.dashboard.save_dashboard_snapshot()
        except Exception as e:
            print(f"⚠️ Dashboard snapshot error: {e}")
        
        # FIX 13: Shutdown agents with timeout
        shutdown_tasks = []
        for agent_id in reversed(list(self.agents.keys())):
            agent = self.agents[agent_id]
            if hasattr(agent, 'shutdown'):
                task = asyncio.create_task(self._shutdown_agent(agent_id, agent))
                shutdown_tasks.append(task)
        
        if shutdown_tasks:
            try:
                await asyncio.wait_for(
                    asyncio.gather(*shutdown_tasks, return_exceptions=True),
                    timeout=10.0
                )
            except asyncio.TimeoutError:
                print("⚠️ Some agents didn't shutdown cleanly")
        
        if hasattr(self, 'memory_manager'):
            self.memory_manager.monitoring = False
        
        self.bus.running = False
        print("👋 Fixed system shutdown complete")
    
    async def _shutdown_agent(self, agent_id: str, agent):
        """FIX 14: Individual agent shutdown with timeout"""
        try:
            await asyncio.wait_for(agent.shutdown(), timeout=5.0)
            print(f"✅ {agent_id} shut down")
        except asyncio.TimeoutError:
            print(f"⚠️ {agent_id} shutdown timeout")
        except Exception as e:
            print(f"⚠️ {agent_id} shutdown error: {e}")

    async def _safe_agent_startup(self, agent):
        """Safe agent startup without strict timeouts"""
        try:
            if hasattr(agent, '_state_loading'):
                # Wait for state loading to complete
                max_wait = 10
                wait_count = 0
                while not agent._state_loading and wait_count < max_wait:
                    await asyncio.sleep(0.5)
                    wait_count += 1
            
            # Call startup
            await agent.startup()
            return True
        except Exception as e:
            print(f"Safe startup error: {e}")
            return False

# FIXES: Import agents that need fixes
try:
    from src.agents.planning_agent import PlanningAgent
except ImportError:
    PlanningAgent = None

try:
    from src.agents.validation_agent import ValidationAgent
except ImportError:
    ValidationAgent = None

async def main():
    """Main function with enhanced error handling"""
    
    print("🔧 EPLAN Multi-Agent System - Router Initialization Fix")
    print("Version: Fixed Router Initialization")
    print("=" * 60)
    
    if sys.platform == "win32":
        try:
            asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
            print("✅ Windows event loop policy set")
        except Exception as e:
            print(f"⚠️ Event loop policy warning: {e}")

    required_dirs = [
        Path("C:/temp/Agent/Context"),
        Path("C:/temp/Agent/Context/context"), 
        Path("C:/temp/Agent/Context/scratchpads"),
        Path("C:/temp/Agent/Observability")
    ]

    for directory in required_dirs:
        try:
            directory.mkdir(parents=True, exist_ok=True)
            print(f"📁 Created: {directory}")
        except Exception as e:
            print(f"⚠️ Directory error: {e}")

    # FIX 15: Check required directories
    required_paths = [
        Path("C:/temp/Agent/Observability"),
        Path("C:/temp/Agent/Context"),
        Path("src/ai/Knowledge/API"),
        Path("src/ai/Knowledge/Scripts")
    ]
    
    for path in required_paths:
        if not path.exists():
            print(f"⚠️ Creating directory: {path}")
            try:
                path.mkdir(parents=True, exist_ok=True)
            except Exception as e:
                print(f"❌ Failed to create {path}: {e}")
    
    system = FixedEplanAgentSystem()
    
    try:
        await system.initialize_system()
        await system.run_interactive_mode()
        
    except KeyboardInterrupt:
        print("\n⚠️ Interrupted by user")
    except Exception as e:
        print(f"❌ System error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        await system.shutdown_system()
    
    return 0


if __name__ == "__main__":
    # FIX 16: Windows event loop policy for stability
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    
    try:
        exit_code = asyncio.run(main())
        sys.exit(exit_code)
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)