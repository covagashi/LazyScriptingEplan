# main.py
import asyncio
import signal
import sys
from pathlib import Path
import json
import time

from src.core.message_bus import ObservableMessageBus
from src.agents.mini_agent import MiniAgent
from src.agents.filesystem_agent import FileSystemAgent
from src.agents.conversation_agent import ConversationAgent
from src.agents.knowledge_agent import EplanKnowledgeAgent
from src.agents.codecraft_agent import CodeCraftAgent
from src.agents.execution_agent import ExecutionAgent
from src.agents.feedback_agent import FeedbackAgent
from src.core.memory_manager import AutoMemoryManager

# Safe imports with fallbacks
try:
    from src.agents.planning_agent import PlanningAgent
except ImportError:
    PlanningAgent = None

try:
    from src.agents.validation_agent import ValidationAgent
except ImportError:
    ValidationAgent = None


class NonHangingEplanSystem:
    """EPLAN Agent System with anti-hanging fixes"""
    
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
        print("\n🛑 Emergency shutdown triggered...")
        self.running = False
        sys.exit(0) 
    
    async def initialize_system(self):
        """Initialize system with timeout protection"""
        print("🚀 Initializing Non-Hanging EPLAN System")
        print("🔧 Anti-hanging protection active")
        print("=" * 60)        
        
        try:
            self.memory_manager = AutoMemoryManager(memory_limit_mb=600)
            await asyncio.wait_for(
                self.memory_manager.start_monitoring(), 
                timeout=5.0
            )
        except asyncio.TimeoutError:
            print("⚠️ Memory manager timeout, continuing...")
                
        await self._initialize_core_agents_safe()
        await self._initialize_specialized_agents_safe()
        
        print("\n✅ System initialization complete!")
        print(f"📈 {len(self.agents)} agents active")
        print("=" * 60)
        
        self._start_dashboard_monitoring()
    
    async def _initialize_core_agents_safe(self):
        """Initialize core agents with timeout protection"""
                
        print("📁 Initializing FileSystemAgent...")
        try:
            filesystem = FileSystemAgent(self.bus)
            await asyncio.wait_for(
                self._register_agent_with_timeout("filesystem", filesystem),
                timeout=15.0
            )
        except asyncio.TimeoutError:
            print("⚠️ FileSystemAgent timeout - using minimal mode")            
        except Exception as e:
            print(f"⚠️ FileSystemAgent error: {e}")
         
        print("💬 Initializing ConversationAgent...")
        try:
            conversation = ConversationAgent(self.bus)
            await asyncio.wait_for(
                self._register_agent_with_timeout("conversation", conversation),
                timeout=10.0
            )
        except asyncio.TimeoutError:
            print("⚠️ ConversationAgent timeout")
        except Exception as e:
            print(f"⚠️ ConversationAgent error: {e}")
    
    async def _initialize_specialized_agents_safe(self):
        """Initialize specialized agents with individual timeouts"""
        
        agents_to_init = [
            ("planning", PlanningAgent, 8.0),
            ("knowledge", EplanKnowledgeAgent, 20.0),  
            ("codecraft", CodeCraftAgent, 20.0),       
            ("validation", ValidationAgent, 5.0),
            ("execution", ExecutionAgent, 10.0),
            ("feedback", FeedbackAgent, 5.0),
        ]
        
        for agent_id, agent_class, timeout in agents_to_init:
            if agent_class is None:
                print(f"⚠️ {agent_id} not available, skipping...")
                continue
                
            print(f"🔧 Initializing {agent_id}Agent...")
            try:
                agent = agent_class(self.bus)
                
                if agent_id == "codecraft":
                    await self._init_codecraft_safe(agent, timeout)
                else:
                    await asyncio.wait_for(
                        self._register_agent_with_timeout(agent_id, agent),
                        timeout=timeout
                    )
                    
            except asyncio.TimeoutError:
                print(f"⏱️ {agent_id}Agent initialization timeout - skipping")
            except Exception as e:
                print(f"⚠️ {agent_id}Agent error: {e}")
    
    async def _init_codecraft_safe(self, agent, timeout):
        """Special safe initialization for CodeCraftAgent"""
        try:
            await self.bus.register_agent("codecraft", agent)
            self.agents["codecraft"] = agent
            print("  ✅ codecraft registered")
            
            if hasattr(agent, 'script_rag'):
                try:
                    await asyncio.wait_for(
                        agent.script_rag.ensure_loaded(),
                        timeout=10.0
                    )
                    print("  ✅ ScriptRAG loaded")
                except asyncio.TimeoutError:
                    print("  ⚠️ ScriptRAG loading timeout, will load lazily")
                except Exception as e:
                    print(f"  ⚠️ ScriptRAG error: {e}")
            
            try:
                await asyncio.wait_for(agent.startup(), timeout=5.0)
                print("  ✅ codecraft started")
            except asyncio.TimeoutError:
                print("  ⚠️ codecraft startup timeout")
                
        except Exception as e:
            print(f"  ❌ codecraft failed: {e}")
    
    async def _register_agent_with_timeout(self, agent_id: str, agent):
        """Register agent with timeout protection"""
        await self.bus.register_agent(agent_id, agent)
        self.agents[agent_id] = agent
        try:
            await asyncio.wait_for(agent.startup(), timeout=5.0)
            print(f"  ✅ {agent_id} ready")
        except asyncio.TimeoutError:
            print(f"  ⚠️ {agent_id} startup timeout")
        except Exception as e:
            print(f"  ⚠️ {agent_id} startup error: {e}")
    
    def _start_dashboard_monitoring(self):
        """Start lightweight dashboard monitoring"""
        self._dashboard_task = asyncio.create_task(self._dashboard_monitor_loop())
    
    async def _dashboard_monitor_loop(self):
        """Lightweight dashboard monitoring"""
        while self.running:
            try:
                await asyncio.sleep(600)  
                if self.running:
                    self.dashboard.save_dashboard_snapshot()
            except Exception:
                pass  
    
    async def run_interactive_mode(self):
        """Non-hanging interactive mode"""
        
        print("\n🤖 Non-Hanging EPLAN Agent System Ready")
        print("Type 'quit' to exit, 'help' for commands")
        print("-" * 50)
        
        if "conversation" not in self.agents:
            print("⚠️ Running in basic mode (no conversation agent)")
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
                    self._show_system_status()
                    continue
                elif user_input.lower() == 'agents':
                    self._show_agent_status()
                    continue
                elif user_input.lower() == 'help':
                    self._show_help()
                    continue
                elif user_input.lower() == 'dashboard':
                    try:
                        self.dashboard.print_real_time_dashboard()
                    except Exception as e:
                        print(f"Dashboard error: {e}")
                    continue

                print("🤔 Processing...", end="", flush=True)
                
                try:
                    response = await asyncio.wait_for(
                        conversation_agent.handle_user_input(user_input),
                        timeout=30.0 
                    )
                    
                    print("\r" + " " * 20 + "\r", end="")
                    print(f"🤖 System: {response}")
                    
                except asyncio.TimeoutError:
                    print("\r⏱️ Request timed out. Try a simpler query.")
                except Exception as e:
                    print(f"\r⚠️ Error: {e}")
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                continue
    
    async def _run_basic_mode(self):
        """Basic mode without conversation agent"""
        print("🔧 Basic mode active")
        
        while self.running:
            try:
                user_input = input("\nBasic> ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    break
                elif user_input.lower() == 'agents':
                    self._show_agent_status()
                elif user_input.lower() == 'status':
                    self._show_system_status()
                elif user_input.lower() == 'help':
                    self._show_basic_help()
                else:
                    print("Basic mode: Limited commands available")
                    
            except KeyboardInterrupt:
                break
    
    def _show_agent_status(self):
        """Show agent status"""
        print("\n🤖 Agent Status:")
        print("-" * 30)
        
        for agent_id, agent in self.agents.items():
            status = "🟢 Ready"
            if hasattr(agent, 'working') and agent.working:
                status = "🟡 Working"
            
            print(f"{agent_id:12} {status}")
        
        print(f"\nTotal: {len(self.agents)} agents")
        print("-" * 30)
    
    def _show_system_status(self):
        """Show system status"""
        print("\n📊 System Status:")
        print("=" * 30)

        print(f"Agents: {len(self.agents)} active")

        try:
            status = self.dashboard.get_real_time_status()
            print(f"Active flows: {status['active_flows']['count']}")
            print(f"Recent events: {status['recent_activity']['events_last_60s']}")
        except Exception:
            print("Dashboard: Error")

        if hasattr(self, 'memory_manager'):
            try:
                memory_stats = self.memory_manager.get_memory_stats()
                print(f"Memory: {memory_stats['current_mb']:.1f}MB")
            except Exception:
                print("Memory: Error")
        
        print("=" * 30)
    
    def _show_help(self):
        """Show help"""
        print("\n📋 Commands:")
        print("-" * 20)
        print("status  - System status")
        print("agents  - Agent list")
        print("help    - This help")
        print("quit    - Exit")
        print("\n💡 Try:")
        print("'Generate EPLAN script'")
        print("'Help with EPLAN API'")
        print("-" * 20)
    
    def _show_basic_help(self):
        """Show basic help"""
        print("\n📋 Basic Commands:")
        print("status, agents, help, quit")
    
    async def shutdown_system(self):
        """Quick shutdown"""
        print("\n🛑 Shutting down...")
        
        self.running = False

        if self._dashboard_task:
            self._dashboard_task.cancel()

        for agent_id in list(self.agents.keys()):
            try:
                agent = self.agents[agent_id]
                if hasattr(agent, 'shutdown'):
                    await asyncio.wait_for(agent.shutdown(), timeout=2.0)
            except:
                pass 
        
        print("👋 Shutdown complete")


async def main():
    """Main with timeout protection"""
    
    print("🔧 Non-Hanging EPLAN Multi-Agent System")
    print("Version: Anti-Hang Protection")
    print("=" * 50)

    if sys.platform == "win32":
        try:
            asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
        except Exception:
            pass

    required_dirs = [
        Path("C:/temp/Agent/Context"),
        Path("C:/temp/Agent/Observability"),
        Path("src/ai/Knowledge/API"),
        Path("src/ai/Knowledge/Scripts")
    ]
    
    for directory in required_dirs:
        try:
            directory.mkdir(parents=True, exist_ok=True)
        except Exception:
            pass
    
    system = NonHangingEplanSystem()
    
    try:
        await asyncio.wait_for(
            system.initialize_system(),
            timeout=120.0  
        )
        
        await system.run_interactive_mode()
        
    except asyncio.TimeoutError:
        print("❌ System initialization timeout")
        return 1
    except KeyboardInterrupt:
        print("\n⚠️ Interrupted")
    except Exception as e:
        print(f"❌ System error: {e}")
        return 1
    finally:
        try:
            await asyncio.wait_for(
                system.shutdown_system(),
                timeout=10.0
            )
        except:
            pass
    
    return 0


if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    
    try:
        exit_code = asyncio.run(main())
        sys.exit(exit_code)
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)