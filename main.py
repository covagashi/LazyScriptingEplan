# main.py
import asyncio
import signal
import sys
from pathlib import Path
import json


# Import enhanced observability
from src.core.message_bus import ObservableMessageBus
from src.agents.mini_agent import MiniAgent
from src.agents.filesystem_agent import FileSystemAgent
from src.agents.conversation_agent import ConversationAgent
from src.agents.knowledge_agent import EplanKnowledgeAgent
from src.agents.codecraft_agent import CodeCraftAgent
from src.agents.execution_agent import ExecutionAgent
from src.agents.feedback_agent import FeedbackAgent
from src.agents.planning_agent import PlanningAgent
from src.agents.validation_agent import ValidationAgent

class EnhancedEplanAgentSystem:
    """Enhanced system with full P2P observability"""
    
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
        print("\n🛑 Shutting down enhanced system...")
        self.running = False
        
        if self.dashboard:
            self.dashboard.save_dashboard_snapshot()
    
    async def initialize_system(self):
        """Initialize enhanced system with full observability"""
        
        print("🚀 Initializing Enhanced EPLAN Agent System")
        print("📊 Full P2P Observability Dashboard Enabled")
        print("=" * 60)
        
        print("📁 Initializing FileSystemAgent...")
        filesystem = FileSystemAgent(self.bus)
        await self.bus.register_agent("filesystem", filesystem)
        self.agents["filesystem"] = filesystem
        await filesystem.startup()
        
        print("🎯 Initializing PlanningAgent...")
        planning = PlanningAgent(self.bus)
        await self.bus.register_agent("planning", planning)
        self.agents["planning"] = planning
        await planning.startup()
        
        print("💬 Initializing Enhanced ConversationAgent...")
        conversation = ConversationAgent(self.bus)
        await self.bus.register_agent("conversation", conversation)
        self.agents["conversation"] = conversation
        await conversation.startup()
        
        print("📚 Initializing KnowledgeAgent...")
        knowledge = EplanKnowledgeAgent(self.bus)
        await self.bus.register_agent("knowledge", knowledge)
        self.agents["knowledge"] = knowledge
        await knowledge.startup()
        
        print("⚙️ Initializing CodeCraftAgent...")
        codecraft = CodeCraftAgent(self.bus)
        await self.bus.register_agent("codecraft", codecraft)
        self.agents["codecraft"] = codecraft
        await codecraft.startup()
               
        print("✅ Initializing ValidationAgent...")
        validation = ValidationAgent(self.bus)
        await self.bus.register_agent("validation", validation)
        self.agents["validation"] = validation
        await validation.startup()
        
        print("🔧 Initializing ExecutionAgent...")
        execution = ExecutionAgent(self.bus)
        await self.bus.register_agent("execution", execution)
        self.agents["execution"] = execution
        await execution.startup()
        
        print("📊 Initializing FeedbackAgent...")
        feedback = FeedbackAgent(self.bus)
        await self.bus.register_agent("feedback", feedback)
        self.agents["feedback"] = feedback
        await feedback.startup()
        
        print("\n✅ All agents initialized with full observability!")
        print(f"📈 System ready with {len(self.agents)} agents")
        print("📊 Real-time P2P dashboard active")
        print("=" * 60)
        
        self._start_dashboard_monitoring()
        
        await self._run_enhanced_system_tests()
    
    def _start_dashboard_monitoring(self):
        """Start background dashboard monitoring"""
        self._dashboard_task = asyncio.create_task(self._dashboard_monitor_loop())
    
    async def _dashboard_monitor_loop(self):
        """Background loop for dashboard monitoring"""
        while self.running:
            try:
                await asyncio.sleep(300)
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
    
    async def _run_enhanced_system_tests(self):
        """Run tests for enhanced observability features"""
        print("\n🧪 Running Enhanced System Tests...")
        
        try:
            from src.core.message_bus import AgentMessage
            
            test_message = AgentMessage(
                sender="system_test",
                recipients=["conversation"],
                intent="test_observability",
                payload={"test": "observability_integration"}
            )
            
            self.dashboard.track_message_sent(test_message, "system_test")
            print("✅ Enhanced Message Tracking: Working")
            
            conv_agent = self.agents["conversation"]
            metrics = conv_agent.get_performance_metrics()
            print(f"✅ Performance Metrics: {len(metrics)} operation types tracked")
            
            status = self.dashboard.get_real_time_status()
            print(f"✅ Real-time Dashboard: {status['active_flows']['count']} flows tracked")
            
            interaction_map = self.dashboard.get_interaction_map()
            total_interactions = interaction_map.get('total_interactions', 0)
            print(f"✅ Interaction Mapping: {total_interactions} total interactions")
            
            print("🧪 Enhanced system tests completed\n")
            
        except Exception as e:
            print(f"❌ Enhanced system test failed: {e}")
    
    async def run_interactive_mode(self):
        """Enhanced interactive mode with observability commands"""
        
        print("🤖 Enhanced EPLAN Agent System - Observable Interactive Mode")
        print("📊 Real-time P2P Dashboard Active")
        print("🎯 PlanningAgent available for complex tasks")
        print("Type 'quit', 'exit', or Ctrl+C to stop")
        print("Type 'help' for available commands")
        print("-" * 70)
        
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
                elif user_input.lower() == 'flows':
                    await self._show_message_flows()
                    continue
                elif user_input.lower() == 'interactions':
                    self._show_interaction_map()
                    continue
                elif user_input.lower() == 'metrics':
                    await self._show_agent_metrics()
                    continue
                elif user_input.lower() == 'anomalies':
                    self._show_anomalies()
                    continue
                elif user_input.lower() == 'snapshot':
                    snapshot_file = self.dashboard.save_dashboard_snapshot()
                    print(f"📸 Dashboard snapshot saved: {snapshot_file}")
                    continue
                elif user_input.lower() == 'help':
                    self._show_enhanced_help()
                    continue
                elif user_input.lower() == 'reflection':
                    await self._show_reflection_status()
                    continue
                elif user_input.lower() == 'toggle-oar':
                    conv_agent = self.agents["conversation"]
                    conv_agent.reflection_enabled = not conv_agent.reflection_enabled
                    status = "enabled" if conv_agent.reflection_enabled else "disabled"
                    print(f"🧠 Observation-Action-Reflection loop {status}")
                    continue
                
                print("🤔 Processing...", end="", flush=True)
                
                response = await conversation_agent.handle_user_input(user_input)
                
                print("\r" + " " * 20 + "\r", end="")
                print(f"🤖 System: {response}")
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                continue
    
    async def _show_enhanced_system_status(self):
        """Show enhanced system status with observability"""
        print("\n📊 Enhanced System Status:")
        print("=" * 45)
        
        for agent_id, agent in self.agents.items():
            status = "🟢 Active"
            if hasattr(agent, 'working') and agent.working:
                status = "🟡 Working"
            
            metrics = ""
            if hasattr(agent, 'get_performance_metrics'):
                perf_metrics = agent.get_performance_metrics()
                if perf_metrics:
                    avg_times = [m['avg_time'] for m in perf_metrics.values()]
                    avg_overall = sum(avg_times) / len(avg_times) * 1000  # ms
                    metrics = f" ({avg_overall:.1f}ms avg)"
            
            print(f"{agent_id:15} {status}{metrics}")
        
        status = self.dashboard.get_real_time_status()
        print(f"\n📊 P2P Dashboard:")
        print(f"   Active Flows: {status['active_flows']['count']}")
        print(f"   Recent Events: {status['recent_activity']['events_last_60s']}")
        
        interaction_map = self.dashboard.get_interaction_map()
        print(f"   Total Interactions: {interaction_map['total_interactions']}")
        
        anomalies = self.dashboard.detect_anomalies()
        print(f"   Anomalies: {len(anomalies)}")
        
        print("=" * 45)
    
    async def _show_reflection_status(self):
        """Mostrar estado de reflexión"""
        conv_agent = self.agents["conversation"]
        
        print(f"\n🧠 Reflection Status:")
        print(f"Loop enabled: {conv_agent.reflection_enabled}")
        print(f"Reflection history: {len(conv_agent.reflection_history)} entries")
        
        if conv_agent.reflection_history:
            print("\nRecent reflections:")
            for reflection in conv_agent.reflection_history[-3:]:
                timestamp = time.strftime('%H:%M:%S', time.localtime(reflection['timestamp']))
                action_type = reflection['action'].get('type', 'unknown')
                print(f"  {timestamp}: {action_type}")

    async def _show_message_flows(self):
        """Show active message flows"""
        status = self.dashboard.get_real_time_status()
        flows = status['active_flows']['flows']
        
        if not flows:
            print("📭 No active message flows")
            return
        
        print(f"\n🔄 Active Message Flows ({len(flows)}):")
        print("-" * 50)
        
        for flow in flows:
            duration = flow['duration']
            agents = flow['agents_count']
            messages = flow['messages_count']
            trace_id = flow['trace_id']
            
            print(f"Flow {trace_id[:12]}...")
            print(f"  Duration: {duration:.1f}s")
            print(f"  Agents: {agents}, Messages: {messages}")
            if flow.get('conversation_id'):
                print(f"  Conversation: {flow['conversation_id']}")
            print()
    
    def _show_interaction_map(self):
        """Show P2P interaction map"""
        interaction_map = self.dashboard.get_interaction_map()
        
        print(f"\n🔗 P2P Interaction Map:")
        print(f"Total Interactions: {interaction_map['total_interactions']}")
        print("-" * 40)
        
        top_pairs = interaction_map['most_active_pairs']
        print("Top Agent Pairs:")
        for sender, receiver, count in top_pairs[:8]:
            percentage = (count / interaction_map['total_interactions']) * 100
            print(f"  {sender} → {receiver}: {count} ({percentage:.1f}%)")
        
        centrality = interaction_map['agent_centrality']
        if centrality:
            print(f"\nMost Active Agents:")
            sorted_agents = sorted(centrality.items(), key=lambda x: x[1], reverse=True)
            for agent, activity in sorted_agents[:5]:
                print(f"  {agent}: {activity} interactions")
        
        print("-" * 40)
    
    async def _show_agent_metrics(self):
        """Show detailed agent performance metrics"""
        print(f"\n⚡ Agent Performance Metrics:")
        print("-" * 50)
        
        for agent_id, agent in self.agents.items():
            if hasattr(agent, 'get_performance_metrics'):
                metrics = agent.get_performance_metrics()
                
                if metrics:
                    print(f"\n{agent_id.upper()}:")
                    for operation, stats in metrics.items():
                        avg_ms = stats['avg_time'] * 1000
                        count = stats['count']
                        recent_ms = stats['recent_avg'] * 1000
                        
                        print(f"  {operation:20}: {avg_ms:6.1f}ms avg ({count} ops) | Recent: {recent_ms:.1f}ms")
                else:
                    print(f"\n{agent_id.upper()}: No metrics available")
        
        print("-" * 50)
    
    def _show_anomalies(self):
        """Show detected anomalies"""
        anomalies = self.dashboard.detect_anomalies()
        
        if not anomalies:
            print("✅ No anomalies detected")
            return
        
        print(f"\n⚠️ Detected Anomalies ({len(anomalies)}):")
        print("-" * 40)
        
        for anomaly in anomalies:
            if anomaly['type'] == 'long_running_flow':
                print(f"🐌 Long Running Flow:")
                print(f"   Trace: {anomaly['trace_id'][:12]}...")
                print(f"   Duration: {anomaly['duration']:.1f}s")
                print(f"   Agents: {', '.join(anomaly['agents_involved'])}")
                
            elif anomaly['type'] == 'potential_circular_flow':
                print(f"🔄 Potential Circular Flow:")
                print(f"   Trace: {anomaly['trace_id'][:12]}...")
                print(f"   Messages: {anomaly['message_count']}")
                print(f"   Unique Agents: {anomaly['unique_agents']}")
            
            print()
        
        print("-" * 40)
    
    def _show_enhanced_help(self):
        """Show enhanced help with observability commands"""
        print("\n📋 Available Commands:")
        print("=" * 40)
        print("🔧 System Commands:")
        print("  help        - Show this help")
        print("  status      - Enhanced system status")
        print("  quit/exit   - Exit system")
        
        print("\n📊 Observability Commands:")
        print("  dashboard   - Real-time P2P dashboard")
        print("  flows       - Active message flows")
        print("  interactions - P2P interaction map")
        print("  metrics     - Agent performance metrics")
        print("  anomalies   - Detected anomalies")
        print("  snapshot    - Save dashboard snapshot")
        
        print("\n💡 EPLAN Examples:")
        print("  'Create script to open MainPanel.elk'")
        print("  'Research XAfActionSetting and generate code'")
        print("  'Execute generated script and validate'")
        
        print("\n🎯 Complex Tasks (Observed):")
        print("  'Create, test and validate EPLAN automation'")
        print("  'Research API, generate code, execute, analyze'")
        
        print("\n🧠 Reflection Commands:")
        print("  reflection  - Show reflection history")
        print("  toggle-oar  - Toggle observation loop")
                
        print("=" * 40)
    
    async def shutdown_system(self):
        """Enhanced shutdown with observability cleanup"""
        print("\n🛑 Shutting down Enhanced EPLAN Agent System...")
        
        if self._dashboard_task:
            self._dashboard_task.cancel()
        
        print("📸 Saving final dashboard snapshot...")
        final_snapshot = self.dashboard.save_dashboard_snapshot()
        
        status = self.dashboard.get_real_time_status()
        interaction_map = self.dashboard.get_interaction_map()
        print(f"📊 Final Statistics:")
        print(f"   Total Interactions: {interaction_map['total_interactions']}")
        print(f"   Completed Flows: {len(self.dashboard.completed_flows)}")
        
        for agent_id in reversed(list(self.agents.keys())):
            agent = self.agents[agent_id]
            try:
                if hasattr(agent, 'shutdown'):
                    await agent.shutdown()
                print(f"✅ {agent_id} shut down")
            except Exception as e:
                print(f"⚠️ {agent_id} shutdown error: {e}")
        
        self.bus.running = False
        print("👋 Enhanced system shutdown complete")


async def main():
    """Enhanced main with full observability"""
    
    try:
        import watchdog
    except ImportError:
        print("❌ Missing dependency: watchdog")
        return 1
    
    required_paths = [
        Path("C:/temp/Agent/Observability"),
        Path("C:/temp/Agent/Context"),
        Path("src/ai/Knowledge/API"),
        Path("src/ai/Knowledge/Scripts")
    ]
    
    for path in required_paths:
        if not path.exists():
            print(f"⚠️ Creating directory: {path}")
            path.mkdir(parents=True, exist_ok=True)
    
    system = EnhancedEplanAgentSystem()
    
    try:
        await system.initialize_system()
        await system.run_interactive_mode()
        
    except KeyboardInterrupt:
        print("\n⚠️ Interrupted by user")
    except Exception as e:
        print(f"❌ Enhanced system error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        await system.shutdown_system()
    
    return 0


if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    
    exit_code = asyncio.run(main())
    sys.exit(exit_code)