# src/core/mesage_bus.py
import asyncio
import time
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from .agent_routing import DeterministicRouter, RoutingMonitor

@dataclass
class AgentMessage:
    sender: str
    recipients: List[str]
    intent: str
    payload: dict
    priority: int = 1
    timestamp: float = None
    correlation_id: str = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = time.time()
        if self.correlation_id is None:
            self.correlation_id = f"{self.sender}_{int(time.time() * 1000)}"

class EnhancedMessageBus:
    """MessageBus optimized with deterministic routing and monitoring"""
    
    def __init__(self):
        self.agents: Dict[str, 'EnhancedMiniAgent'] = {}
        self.running = True
        
        # Routing system
        self.router = DeterministicRouter()
        self.routing_monitor = RoutingMonitor()
        
        # Message tracking
        self.message_history = []
        self.pending_messages = {}
        
        # Performance optimization
        self.agent_capability_cache = {}
        self.cache_ttl = 300  # 5 minutes
        
        print("📨 Enhanced MessageBus initialized with deterministic routing")
    
    async def register_agent(self, agent_id: str, agent: 'EnhancedMiniAgent'):
        """Register agent with capacity precalculation"""
        
        self.agents[agent_id] = agent
                
        await self._precalculate_agent_capabilities(agent_id)
        
        print(f"✅ Agent {agent_id} registered with capabilities cached")
    
    async def _precalculate_agent_capabilities(self, agent_id: str):
        """Precalculate capacities for common queries"""
        
        common_intents = [
            "help", "hello", "generate script", "eplan documentation",
            "execute", "code generation", "api reference", "run script",
            "feedback", "validation", "general question"
        ]
        
        agent = self.agents[agent_id]
        capabilities = {}
        
        for intent in common_intents:
            try:
                start_time = time.time()
                confidence = await agent.can_handle(intent)
                response_time = (time.time() - start_time) * 1000
                
                capabilities[intent] = {
                    "confidence": confidence,
                    "cached_at": time.time(),
                    "response_time_ms": response_time
                }
                
            except Exception as e:
                print(f"⚠️ Failed to precalculate capability for {agent_id}/{intent}: {e}")
                capabilities[intent] = {"confidence": 0.0, "cached_at": time.time()}
        
        self.agent_capability_cache[agent_id] = capabilities
    
    async def find_capable_agents(self, intent: str, min_confidence: float = 0.5) -> List[Tuple[str, float]]:
        """Find capable agents with optimized routing"""
        
        start_time = time.time()
        capable_agents = []
        
        cached_results = self._check_capability_cache(intent)
        if cached_results:
            for agent_id, confidence in cached_results:
                if confidence >= min_confidence:
                    capable_agents.append((agent_id, confidence))
            
            if capable_agents:
                response_time = (time.time() - start_time) * 1000
                print(f"🚀 Fast routing via cache: {len(capable_agents)} agents ({response_time:.1f}ms)")
                return sorted(capable_agents, key=lambda x: x[1], reverse=True)
        
        evaluation_tasks = []
        for agent_id, agent in self.agents.items():
            task = asyncio.create_task(
                self._evaluate_agent_capability(agent_id, agent, intent)
            )
            evaluation_tasks.append(task)
        
        evaluations = await asyncio.gather(*evaluation_tasks, return_exceptions=True)
        
        for i, result in enumerate(evaluations):
            if isinstance(result, Exception):
                print(f"⚠️ Agent evaluation failed: {result}")
                continue
            
            agent_id, confidence, response_time = result
            
            self.routing_monitor.record_routing_decision(
                agent_id, intent, confidence, "full_evaluation", response_time
            )
            
            if confidence >= min_confidence:
                capable_agents.append((agent_id, confidence))
        
        capable_agents.sort(key=lambda x: x[1], reverse=True)
        
        total_time = (time.time() - start_time) * 1000
        print(f"🔍 Full routing evaluation: {len(capable_agents)} capable agents ({total_time:.1f}ms)")
        
        return capable_agents
    
    def _check_capability_cache(self, intent: str) -> List[Tuple[str, float]]:
        """Check capabilities cache"""
        
        cached_results = []
        current_time = time.time()
        
        for agent_id, capabilities in self.agent_capability_cache.items():
            if intent in capabilities:
                cached_data = capabilities[intent]
                if current_time - cached_data["cached_at"] < self.cache_ttl:
                    cached_results.append((agent_id, cached_data["confidence"]))
                    continue
            
            for cached_intent, cached_data in capabilities.items():
                if (current_time - cached_data["cached_at"] < self.cache_ttl and 
                    self._intents_similar(intent, cached_intent)):
                    cached_results.append((agent_id, cached_data["confidence"]))
                    break
        
        return cached_results if len(cached_results) >= len(self.agents) * 0.8 else None
    
    def _intents_similar(self, intent1: str, intent2: str) -> bool:
        """Determine if two intents are similar for cache"""
        
        # Simple similarity check - can be enhanced
        words1 = set(intent1.lower().split())
        words2 = set(intent2.lower().split())
        
        intersection = len(words1.intersection(words2))
        union = len(words1.union(words2))
        
        similarity = intersection / union if union > 0 else 0
        return similarity > 0.6
    
    async def _evaluate_agent_capability(self, agent_id: str, agent, intent: str) -> Tuple[str, float, float]:
        """Evaluate individual agent capacity"""
        
        start_time = time.time()
        
        try:
            confidence = await agent.can_handle(intent)
            response_time = (time.time() - start_time) * 1000
            
            if agent_id not in self.agent_capability_cache:
                self.agent_capability_cache[agent_id] = {}
            
            self.agent_capability_cache[agent_id][intent] = {
                "confidence": confidence,
                "cached_at": time.time(),
                "response_time_ms": response_time
            }
            
            return agent_id, confidence, response_time
            
        except Exception as e:
            response_time = (time.time() - start_time) * 1000
            print(f"⚠️ Agent {agent_id} capability evaluation failed: {e}")
            return agent_id, 0.0, response_time
    
    async def broadcast(self, message: AgentMessage):
        """Broadcast optimizado con routing inteligente"""
        
        self.message_history.append({
            "timestamp": time.time(),
            "sender": message.sender,
            "recipients": message.recipients,
            "intent": message.intent,
            "correlation_id": message.correlation_id
        })
        
        if len(self.message_history) > 1000:
            self.message_history = self.message_history[-500:]
        
        self.pending_messages[message.correlation_id] = {
            "message": message,
            "sent_at": time.time(),
            "status": "pending"
        }
        
        delivery_tasks = []
        for recipient in message.recipients:
            if recipient in self.agents:
                task = asyncio.create_task(
                    self._deliver_message(recipient, message)
                )
                delivery_tasks.append(task)
            else:
                print(f"⚠️ Recipient {recipient} not found for message {message.correlation_id}")
        
        deliveries = await asyncio.gather(*delivery_tasks, return_exceptions=True)
        
        successful_deliveries = sum(1 for d in deliveries if not isinstance(d, Exception))
        
        if message.correlation_id in self.pending_messages:
            self.pending_messages[message.correlation_id]["status"] = (
                "delivered" if successful_deliveries == len(message.recipients) 
                else "partial_delivery"
            )
            self.pending_messages[message.correlation_id]["delivered_count"] = successful_deliveries
    
    async def _deliver_message(self, recipient: str, message: AgentMessage):
        """Individual message delivery with retry"""
        
        agent = self.agents[recipient]
        max_retries = 3
        retry_delay = 0.1
        
        for attempt in range(max_retries):
            try:
                await agent.receive_message(message)
                return True
                
            except Exception as e:
                if attempt < max_retries - 1:
                    await asyncio.sleep(retry_delay * (2 ** attempt))  # Exponential backoff
                    continue
                else:
                    print(f"❌ Failed to deliver message to {recipient} after {max_retries} attempts: {e}")
                    raise
        
        return False
    
    async def smart_route_message(self, sender: str, intent: str, payload: dict, 
                                 priority: int = 1, heavy_context: dict = None) -> bool:
        """Automatic intelligent routing based on intent"""
        
        start_time = time.time()
        
        capable_agents = await self.find_capable_agents(intent, min_confidence=0.5)
        
        if not capable_agents:
            print(f"⚠️ No capable agents found for intent: {intent}")
            return False
        
        recipients = []
        
        best_agent, best_confidence = capable_agents[0]
        recipients.append(best_agent)
        
        for agent_id, confidence in capable_agents[1:3]: 
            if best_confidence - confidence < 0.2:
                recipients.append(agent_id)
        
        message = AgentMessage(
            sender=sender,
            recipients=recipients,
            intent="smart_routed_" + intent,
            payload=payload,
            priority=priority
        )
        
        if heavy_context:
            message.payload["has_heavy_context"] = True
            message.payload["heavy_context_note"] = "Context available via filesystem"
        
        await self.broadcast(message)
        
        routing_time = (time.time() - start_time) * 1000
        print(f"🎯 Smart routed '{intent}' to {recipients} ({routing_time:.1f}ms)")
        
        return True
    
    def get_system_status(self) -> dict:
        """Get full status of the messaging system"""
        
        total_agents = len(self.agents)
        recent_messages = len([m for m in self.message_history 
                              if time.time() - m["timestamp"] < 300])  
        
        pending_count = len([m for m in self.pending_messages.values() 
                           if m["status"] == "pending"])
        
        routing_summary = self.routing_monitor.get_performance_summary()
        
        agent_health = {}
        for agent_id, agent in self.agents.items():
            try:
                is_working = getattr(agent, 'working', False)
                agent_health[agent_id] = {
                    "status": "working" if is_working else "idle",
                    "cached_capabilities": len(self.agent_capability_cache.get(agent_id, {}))
                }
            except:
                agent_health[agent_id] = {"status": "unknown", "cached_capabilities": 0}
        
        return {
            "message_bus": {
                "total_agents": total_agents,
                "recent_messages_5min": recent_messages,
                "pending_messages": pending_count,
                "message_history_size": len(self.message_history)
            },
            "routing_system": routing_summary,
            "agent_health": agent_health,
            "cache_stats": {
                "agents_cached": len(self.agent_capability_cache),
                "total_cached_capabilities": sum(len(caps) for caps in self.agent_capability_cache.values())
            }
        }
    
    def print_system_status(self):
        """Print system status in a readable manner"""
        
        status = self.get_system_status()
        
        print(f"\n📨 MessageBus System Status")
        print("=" * 50)
        
        # Message Bus stats
        bus_stats = status["message_bus"]
        print(f"Agents: {bus_stats['total_agents']}")
        print(f"Recent Messages (5min): {bus_stats['recent_messages_5min']}")
        print(f"Pending Messages: {bus_stats['pending_messages']}")
        
        # Routing stats
        routing_stats = status["routing_system"]
        if "error" not in routing_stats:
            print(f"Routing Health: {routing_stats['health_status']}")
            print(f"Total Decisions: {routing_stats['total_decisions']}")
            print(f"Deterministic Rate: {routing_stats['deterministic_rate']:.1%}")
        
        # Agent health
        print(f"\n🤖 Agent Health:")
        for agent_id, health in status["agent_health"].items():
            cached_caps = health["cached_capabilities"]
            status_icon = "🔄" if health["status"] == "working" else "💤"
            print(f"{agent_id:12} {status_icon} {health['status']:7} | {cached_caps:2d} cached")
        
        # Cache performance
        cache_stats = status["cache_stats"]
        print(f"\n💾 Cache: {cache_stats['agents_cached']} agents, {cache_stats['total_cached_capabilities']} capabilities")
        
        print("=" * 50)
    
    async def cleanup_old_data(self):
        """Clean up old data for optimization"""
        
        current_time = time.time()
        cutoff_time = current_time - 3600  
        
        old_history_size = len(self.message_history)
        self.message_history = [m for m in self.message_history if m["timestamp"] > cutoff_time]
        
        old_pending = list(self.pending_messages.keys())
        for msg_id, msg_data in list(self.pending_messages.items()):
            if msg_data["sent_at"] < cutoff_time:
                del self.pending_messages[msg_id]
        
        cache_cutoff = current_time - self.cache_ttl
        cleaned_cache_entries = 0
        
        for agent_id in list(self.agent_capability_cache.keys()):
            agent_cache = self.agent_capability_cache[agent_id]
            old_cache_size = len(agent_cache)
            
            for intent in list(agent_cache.keys()):
                if agent_cache[intent]["cached_at"] < cache_cutoff:
                    del agent_cache[intent]
            
            cleaned_cache_entries += old_cache_size - len(agent_cache)
        
        messages_cleaned = old_history_size - len(self.message_history)
        pending_cleaned = len(old_pending) - len(self.pending_messages)
        
        if messages_cleaned > 0 or pending_cleaned > 0 or cleaned_cache_entries > 0:
            print(f"🧹 Cleanup: {messages_cleaned} messages, {pending_cleaned} pending, {cleaned_cache_entries} cache entries")
    
    async def test_agent_routing(self, test_queries: List[str] = None) -> Dict:
        """Quick test of the routing system"""
        
        if test_queries is None:
            test_queries = [
                "hello",
                "generate eplan script", 
                "execute script",
                "eplan documentation",
                "check results"
            ]
        
        print(f"🧪 Testing routing with {len(test_queries)} queries...")
        
        results = []
        total_start_time = time.time()
        
        for query in test_queries:
            start_time = time.time()
            
            try:
                capable_agents = await self.find_capable_agents(query, min_confidence=0.3)
                response_time = (time.time() - start_time) * 1000
                
                result = {
                    "query": query,
                    "capable_agents": capable_agents,
                    "response_time_ms": response_time,
                    "success": len(capable_agents) > 0
                }
                
                print(f"  '{query}' -> {len(capable_agents)} agents ({response_time:.1f}ms)")
                
            except Exception as e:
                result = {
                    "query": query,
                    "error": str(e),
                    "response_time_ms": (time.time() - start_time) * 1000,
                    "success": False
                }
                
                print(f"  '{query}' -> ERROR: {e}")
            
            results.append(result)
        
        total_time = (time.time() - total_start_time) * 1000
        success_rate = sum(1 for r in results if r["success"]) / len(results)
        avg_response_time = sum(r["response_time_ms"] for r in results) / len(results)
        
        summary = {
            "total_queries": len(test_queries),
            "success_rate": success_rate,
            "avg_response_time_ms": avg_response_time,
            "total_time_ms": total_time,
            "results": results
        }
        
        print(f"📊 Routing test complete: {success_rate:.1%} success, {avg_response_time:.1f}ms avg")
        
        return summary
    
    def __del__(self):
        """Cleanup al destruir MessageBus"""
        self.running = False

