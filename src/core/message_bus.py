# src/core/message_bus.py
import asyncio
import time
import json
from typing import Dict, List, Optional, Tuple, Set
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from .error_handling import ErrorHandler


@dataclass
class AgentMessage:
    sender: str
    recipients: List[str]
    intent: str
    payload: dict
    priority: int = 1
    timestamp: float = field(default_factory=time.time)
    correlation_id: str = field(default_factory=lambda: f"msg_{int(time.time() * 1000)}")
    parent_correlation_id: Optional[str] = None
    conversation_id: Optional[str] = None
    trace_id: str = field(default_factory=lambda: f"trace_{int(time.time() * 1000)}")
    
    def create_child_message(self, sender: str, recipients: List[str], intent: str, payload: dict):
        """Create child message maintaining correlation chain"""
        return AgentMessage(
            sender=sender,
            recipients=recipients,
            intent=intent,
            payload=payload,
            parent_correlation_id=self.correlation_id,
            conversation_id=self.conversation_id,
            trace_id=self.trace_id
        )

@dataclass
class MessageFlow:
    trace_id: str
    start_time: float
    conversation_id: Optional[str]
    messages: List[Dict] = field(default_factory=list)
    agents_involved: Set[str] = field(default_factory=set)
    current_status: str = "active"
    
    def add_message_event(self, message: AgentMessage, event_type: str, agent_id: str):
        event = {
            "timestamp": time.time(),
            "correlation_id": message.correlation_id,
            "parent_correlation_id": message.parent_correlation_id,
            "event_type": event_type,  # sent, received, processed, completed
            "agent_id": agent_id,
            "intent": message.intent,
            "recipients": message.recipients
        }
        self.messages.append(event)
        self.agents_involved.add(agent_id)

class ObservabilityDashboard:
    """Real-time P2P interaction dashboard"""
    
    def __init__(self, output_path: Path = None):
        self.output_path = output_path or Path("C:/temp/Agent/Observability")
        self.output_path.mkdir(exist_ok=True, parents=True)
        
        
        self.active_flows: Dict[str, MessageFlow] = {}
        self.completed_flows: List[MessageFlow] = []
        self.agent_metrics: Dict[str, Dict] = {}
        self.real_time_log = []
        
        # Performance tracking
        self.interaction_matrix = {}  # agent_a -> agent_b -> count
        self.latency_metrics = {}
        
        print("📊 ObservabilityDashboard initialized")
    
    def track_message_sent(self, message: AgentMessage, sender_agent: str):
        """Track when message is sent"""
        # Ensure flow exists
        if message.trace_id not in self.active_flows:
            self.active_flows[message.trace_id] = MessageFlow(
                trace_id=message.trace_id,
                start_time=message.timestamp,
                conversation_id=message.conversation_id
            )
        
        flow = self.active_flows[message.trace_id]
        flow.add_message_event(message, "sent", sender_agent)
        
        # Update interaction matrix
        for recipient in message.recipients:
            if sender_agent not in self.interaction_matrix:
                self.interaction_matrix[sender_agent] = {}
            self.interaction_matrix[sender_agent][recipient] = \
                self.interaction_matrix[sender_agent].get(recipient, 0) + 1
        
        # Real-time log
        self._add_real_time_event({
            "timestamp": datetime.now().isoformat(),
            "type": "message_sent",
            "trace_id": message.trace_id,
            "correlation_id": message.correlation_id,
            "sender": sender_agent,
            "recipients": message.recipients,
            "intent": message.intent
        })
    
    def track_message_received(self, message: AgentMessage, receiver_agent: str):
        """Track when message is received"""
        if message.trace_id in self.active_flows:
            flow = self.active_flows[message.trace_id]
            flow.add_message_event(message, "received", receiver_agent)
        
        self._add_real_time_event({
            "timestamp": datetime.now().isoformat(),
            "type": "message_received",
            "trace_id": message.trace_id,
            "correlation_id": message.correlation_id,
            "receiver": receiver_agent,
            "intent": message.intent
        })
    
    def track_message_processed(self, message: AgentMessage, processor_agent: str, 
                              processing_time: float):
        """Track when message processing completes"""
        if message.trace_id in self.active_flows:
            flow = self.active_flows[message.trace_id]
            flow.add_message_event(message, "processed", processor_agent)
        
        # Update latency metrics
        if processor_agent not in self.latency_metrics:
            self.latency_metrics[processor_agent] = []
        self.latency_metrics[processor_agent].append(processing_time)
        
        self._add_real_time_event({
            "timestamp": datetime.now().isoformat(),
            "type": "message_processed",
            "trace_id": message.trace_id,
            "correlation_id": message.correlation_id,
            "processor": processor_agent,
            "processing_time_ms": processing_time * 1000
        })
    
    def complete_flow(self, trace_id: str, success: bool = True):
        """Mark a message flow as completed"""
        if trace_id in self.active_flows:
            flow = self.active_flows[trace_id]
            flow.current_status = "completed" if success else "failed"
            
            self.completed_flows.append(flow)
            del self.active_flows[trace_id]
            
            # Keep only last 100 completed flows
            if len(self.completed_flows) > 100:
                self.completed_flows = self.completed_flows[-100:]
            
            self._add_real_time_event({
                "timestamp": datetime.now().isoformat(),
                "type": "flow_completed",
                "trace_id": trace_id,
                "success": success,
                "duration": time.time() - flow.start_time,
                "agents_involved": list(flow.agents_involved)
            })
    
    def _add_real_time_event(self, event: Dict):
        """Add event to real-time log"""
        self.real_time_log.append(event)
        
        # Keep only last 500 events
        if len(self.real_time_log) > 500:
            self.real_time_log = self.real_time_log[-500:]
    
    def get_interaction_map(self) -> Dict:
        """Generate P2P interaction map"""
        total_interactions = 0
        agent_centrality = {}
        
        # Calculate totals and centrality
        for sender, recipients in self.interaction_matrix.items():
            sent_count = sum(recipients.values())
            agent_centrality[sender] = agent_centrality.get(sender, 0) + sent_count
            total_interactions += sent_count
            
            for recipient, count in recipients.items():
                agent_centrality[recipient] = agent_centrality.get(recipient, 0) + count
        
        return {
            "interaction_matrix": self.interaction_matrix,
            "total_interactions": total_interactions,
            "agent_centrality": agent_centrality,
            "most_active_pairs": self._get_most_active_pairs()
        }
    
    def _get_most_active_pairs(self) -> List[Tuple[str, str, int]]:
        """Get most active agent pairs"""
        pairs = []
        for sender, recipients in self.interaction_matrix.items():
            for recipient, count in recipients.items():
                pairs.append((sender, recipient, count))
        
        return sorted(pairs, key=lambda x: x[2], reverse=True)[:10]
    
    def get_real_time_status(self) -> Dict:
        """Get current real-time status"""
        current_time = time.time()
        
        # Active flows analysis
        active_flows_summary = []
        for trace_id, flow in self.active_flows.items():
            duration = current_time - flow.start_time
            active_flows_summary.append({
                "trace_id": trace_id,
                "duration": duration,
                "agents_count": len(flow.agents_involved),
                "messages_count": len(flow.messages),
                "conversation_id": flow.conversation_id
            })
        
        # Recent activity (last 60 seconds)
        recent_cutoff = current_time - 60
        recent_events = [
            event for event in self.real_time_log 
            if datetime.fromisoformat(event["timestamp"]).timestamp() > recent_cutoff
        ]
        
        # Agent activity summary
        agent_activity = {}
        for event in recent_events:
            for agent_key in ["sender", "receiver", "processor"]:
                if agent_key in event:
                    agent_id = event[agent_key]
                    if agent_id not in agent_activity:
                        agent_activity[agent_id] = {"sent": 0, "received": 0, "processed": 0}
                    
                    if agent_key == "sender":
                        agent_activity[agent_id]["sent"] += 1
                    elif agent_key == "receiver":
                        agent_activity[agent_id]["received"] += 1
                    elif agent_key == "processor":
                        agent_activity[agent_id]["processed"] += 1
        
        return {
            "timestamp": datetime.now().isoformat(),
            "active_flows": {
                "count": len(self.active_flows),
                "flows": active_flows_summary
            },
            "recent_activity": {
                "events_last_60s": len(recent_events),
                "agent_activity": agent_activity
            },
            "system_metrics": {
                "total_completed_flows": len(self.completed_flows),
                "interaction_pairs": len(self._get_most_active_pairs())
            }
        }
    
    def detect_anomalies(self) -> List[Dict]:
        """Detect potential issues in message flows"""
        anomalies = []
        current_time = time.time()
        
        # Long-running flows
        for trace_id, flow in self.active_flows.items():
            duration = current_time - flow.start_time
            if duration > 300:  # 5 minutes
                anomalies.append({
                    "type": "long_running_flow",
                    "trace_id": trace_id,
                    "duration": duration,
                    "agents_involved": list(flow.agents_involved)
                })
        
        # Circular message patterns
        for trace_id, flow in self.active_flows.items():
            agents_in_flow = [msg["agent_id"] for msg in flow.messages]
            if len(agents_in_flow) > 10:  # Threshold for potential circular
                unique_agents = len(set(agents_in_flow))
                if len(agents_in_flow) / unique_agents > 3:  # Same agents repeated
                    anomalies.append({
                        "type": "potential_circular_flow",
                        "trace_id": trace_id,
                        "message_count": len(agents_in_flow),
                        "unique_agents": unique_agents
                    })
        
        return anomalies
    
    def save_dashboard_snapshot(self) -> str:
        """Save current dashboard state to file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        snapshot_file = self.output_path / f"dashboard_snapshot_{timestamp}.json"
        
        snapshot = {
            "timestamp": datetime.now().isoformat(),
            "active_flows": {
                trace_id: {
                    "start_time": flow.start_time,
                    "conversation_id": flow.conversation_id,
                    "agents_involved": list(flow.agents_involved),
                    "messages_count": len(flow.messages),
                    "status": flow.current_status
                }
                for trace_id, flow in self.active_flows.items()
            },
            "interaction_map": self.get_interaction_map(),
            "real_time_status": self.get_real_time_status(),
            "anomalies": self.detect_anomalies(),
            "recent_events": self.real_time_log[-50:]  # Last 50 events
        }
        
        try:
            with open(snapshot_file, 'w', encoding='utf-8') as f:
                json.dump(snapshot, f, indent=2, ensure_ascii=False)
            
            print(f"📊 Dashboard snapshot saved: {snapshot_file}")
            return str(snapshot_file)
        except Exception as e:
            print(f"⚠️ Failed to save dashboard snapshot: {e}")
            return None
    
    def print_real_time_dashboard(self):
        """Print real-time dashboard to console"""
        status = self.get_real_time_status()
        interaction_map = self.get_interaction_map()
        anomalies = self.detect_anomalies()
        
        print("\n" + "="*60)
        print("📊 REAL-TIME P2P OBSERVABILITY DASHBOARD")
        print("="*60)
        print(f"⏰ {status['timestamp']}")
        
        # Active flows
        active_count = status['active_flows']['count']
        print(f"\n🔄 Active Message Flows: {active_count}")
        if active_count > 0:
            for flow in status['active_flows']['flows'][:5]:  # Show top 5
                print(f"  └─ {flow['trace_id'][:12]}... ({flow['duration']:.1f}s, {flow['agents_count']} agents)")
        
        # Recent activity
        recent = status['recent_activity']
        print(f"\n⚡ Activity (last 60s): {recent['events_last_60s']} events")
        if recent['agent_activity']:
            print("   Agent Activity:")
            for agent_id, activity in list(recent['agent_activity'].items())[:5]:
                sent, received, processed = activity['sent'], activity['received'], activity['processed']
                print(f"   └─ {agent_id}: {sent}📤 {received}📥 {processed}⚙️")
        
        # Top interactions
        print(f"\n🔗 Top P2P Interactions:")
        top_pairs = interaction_map['most_active_pairs'][:5]
        for sender, receiver, count in top_pairs:
            print(f"   └─ {sender} → {receiver}: {count} messages")
        
        # Anomalies
        if anomalies:
            print(f"\n⚠️  Anomalies Detected: {len(anomalies)}")
            for anomaly in anomalies[:3]:
                if anomaly['type'] == 'long_running_flow':
                    print(f"   └─ Long flow: {anomaly['trace_id'][:12]}... ({anomaly['duration']:.1f}s)")
                elif anomaly['type'] == 'potential_circular_flow':
                    print(f"   └─ Circular: {anomaly['trace_id'][:12]}... ({anomaly['message_count']} msgs)")
        else:
            print("\n✅ No Anomalies Detected")
        
        print("\n" + "="*60)


class ObservableMessageBus:
    """Enhanced MessageBus with full observability"""
    
    def __init__(self):
        self.agents: Dict[str, 'MiniAgent'] = {}
        self.running = True
        self.error_handler = ErrorHandler()
        
        # Import batch_processor here to avoid circular import
        from .parallel_processor import batch_processor
        self.batch_processor = batch_processor
        
        # Observability
        self.dashboard = ObservabilityDashboard()
        
        # Message tracking
        self.pending_messages = {}
        
        print("📨 Observable MessageBus initialized")
    
    async def register_agent(self, agent_id: str, agent: 'MiniAgent'):
        """Register agent with observability setup"""
        self.agents[agent_id] = agent
        agent._set_observability_dashboard(self.dashboard)  # Inject dashboard
        print(f"✅ Agent {agent_id} registered with observability")
    
    async def broadcast(self, message: AgentMessage):
        """Broadcast message with tracking"""
        # Track sent
        self.dashboard.track_message_sent(message, message.sender)
        
        # Broadcast to recipients
        for recipient in message.recipients:
            if recipient in self.agents:
                success, result = await self.error_handler.safe_call(
                    self.batch_processor.add_message_to_batch,
                    f"broadcast_to_{recipient}",
                    recipient, 
                    message, 
                    self.agents[recipient].receive_message
                )
                
                if not success:
                    await self._handle_broadcast_error(recipient, message, result)
    
    async def _handle_broadcast_error(self, recipient: str, message: AgentMessage, error: str):
        """Handle broadcast errors without breaking the flow"""
        print(f"⚠️ Agent {recipient} failed to receive message: {error[:100]}")
        
        if message.sender != "conversation":
            await self.agents["conversation"].receive_message(
                AgentMessage(
                    sender="system",
                    recipients=["conversation"],
                    intent="agent_error",
                    payload={
                        "failed_agent": recipient,
                        "error": error,
                        "original_message": message.intent
                    }
                )
            )
    
    async def _deliver_with_tracking(self, recipient: str, message: AgentMessage):
        """Deliver message with observability tracking"""
        agent = self.agents[recipient]
        
        # Track received
        self.dashboard.track_message_received(message, recipient)
        
        # Deliver and track processing time
        start_time = time.time()
        try:
            await agent.receive_message(message)
            processing_time = time.time() - start_time
            
            # Track processed
            self.dashboard.track_message_processed(message, recipient, processing_time)
            
            return True
        except Exception as e:
            processing_time = time.time() - start_time
            self.dashboard.track_message_processed(message, recipient, processing_time)
            raise
    
    async def find_capable_agents(self, query: str) -> List[str]:
        """Find agents capable of handling a query"""
        capable_agents = []
        
        for agent_id, agent in self.agents.items():
            if hasattr(agent, 'can_handle'):
                try:
                    confidence = await agent.can_handle(query)
                    if confidence > 0.5:  # Threshold
                        capable_agents.append(agent_id)
                except Exception as e:
                    print(f"Error checking {agent_id} capability: {e}")
        
        return capable_agents
    
    def get_dashboard(self) -> ObservabilityDashboard:
        """Get observability dashboard"""
        return self.dashboard
    
    def print_dashboard(self):
        """Print real-time dashboard"""
        self.dashboard.print_real_time_dashboard()