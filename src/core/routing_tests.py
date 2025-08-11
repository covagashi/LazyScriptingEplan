# src/core/routing_tests.py
import asyncio
import time
import json
from typing import Dict, List, Tuple
from pathlib import Path
from .agent_routing import DeterministicRouter, HybridCanHandle
from ..ai.gemini_client import GeminiClient

class RoutingTestSuite:
    """Test suite for validate routing consistency and performance"""
    
    def __init__(self, router: DeterministicRouter):
        self.router = router
        self.ai_client = GeminiClient()
        self.test_results = []
        
       
        self.test_cases = [
            ("hello there", "conversation", 0.9),
            ("help me with eplan", "conversation", 0.6),
            ("general question about software", "conversation", 0.5),
             
            ("explain actions parameters", "knowledge", 0.9),
            ("eplan api documentation", "knowledge", 0.9),
            ("how to use eplan actions", "knowledge", 0.8),
            ("what is electrical automation", "knowledge", 0.6),
            
            ("generate script to open project", "codecraft", 0.9),
            ("create c# code for eplan", "codecraft", 0.9),
            ("write script", "codecraft", 0.8),
            ("programming help", "codecraft", 0.7),
            
            ("execute the generated script", "execution", 0.9),
            ("run eplan action", "execution", 0.8),
            ("eplan remoting connection", "execution", 0.7),
            
            ("check execution results", "feedback", 0.9),
            ("analyze eplan logs", "feedback", 0.8),
            ("validate script execution", "feedback", 0.8),
            
            ("eplan script generation and execution", "codecraft", 0.7),
            ("explain and generate code", "knowledge", 0.6),
            ("help with eplan", "conversation", 0.5),
        ]
    
    async def run_comprehensive_tests(self) -> Dict[str, Any]:
        """Run full suite of tests"""
        
        print("🧪 Running Routing Test Suite...")
        
        results = {
            "consistency_tests": await self._test_routing_consistency(),
            "performance_tests": await self._test_routing_performance(),
            "edge_case_tests": await self._test_edge_cases(),
            "circular_prevention_tests": await self._test_circular_prevention(),
            "summary": {}
        }
        
        results["summary"] = self._calculate_summary_metrics(results)
   
        await self._save_test_results(results)
        
        return results
    
    async def _test_routing_consistency(self) -> List[Dict]:
        """Consistency test: same query must give same results"""
        
        print("Testing routing consistency...")
        consistency_results = []
        
        for query, expected_agent, expected_min_confidence in self.test_cases:
            confidences = []
            
            for i in range(5):
                confidence = self.router.calculate_confidence(expected_agent, query)
                confidences.append(confidence)
                await asyncio.sleep(0.01) 
            
            variance = max(confidences) - min(confidences)
            avg_confidence = sum(confidences) / len(confidences)
            
            result = {
                "query": query,
                "expected_agent": expected_agent,
                "expected_min_confidence": expected_min_confidence,
                "avg_confidence": avg_confidence,
                "variance": variance,
                "confidences": confidences,
                "consistent": variance < 0.01,  
                "meets_expected": avg_confidence >= expected_min_confidence
            }
            
            consistency_results.append(result)
            
            status = "✅" if result["consistent"] and result["meets_expected"] else "❌"
            print(f"{status} {query[:30]:30} -> {expected_agent} ({avg_confidence:.3f}±{variance:.3f})")
        
        return consistency_results
    
    async def _test_routing_performance(self) -> Dict[str, Any]:
        """Performance test: response time"""
        
        print("Testing routing performance...")

        det_times = []
        for query, agent, _ in self.test_cases[:10]:  
            start = time.time()
            self.router.calculate_confidence(agent, query)
            det_times.append((time.time() - start) * 2000)  # ms
        

        hybrid_handler = HybridCanHandle("test", self.ai_client, self.router)
        hybrid_times = []
        
        for query, agent, _ in self.test_cases[:5]: 
            start = time.time()
            try:
                confidence, method = await hybrid_handler.can_handle(query, "test specialty")
                hybrid_times.append((time.time() - start) * 1000)
            except Exception as e:
                print(f"⚠️ Hybrid test failed for '{query}': {e}")
                hybrid_times.append(1000)  # 1s timeout
        
        performance_results = {
            "deterministic": {
                "avg_ms": sum(det_times) / len(det_times),
                "max_ms": max(det_times),
                "min_ms": min(det_times),
                "times": det_times
            },
            "hybrid": {
                "avg_ms": sum(hybrid_times) / len(hybrid_times) if hybrid_times else 0,
                "max_ms": max(hybrid_times) if hybrid_times else 0,
                "min_ms": min(hybrid_times) if hybrid_times else 0,
                "times": hybrid_times
            }
        }
        
        print(f"📊 Deterministic avg: {performance_results['deterministic']['avg_ms']:.1f}ms")
        print(f"📊 Hybrid avg: {performance_results['hybrid']['avg_ms']:.1f}ms")
        
        return performance_results
    
    async def _test_edge_cases(self) -> List[Dict]:
        """Test casos edge: queries vacías, muy largas, etc."""
        
        print("Testing edge cases...")
        
        edge_cases = [
            ("", "should_handle_empty"),
            ("a" * 1000, "should_handle_very_long"), 
            ("🤖💻🔧⚡", "should_handle_emojis"),
            ("UPPER CASE QUERY", "should_handle_caps"),
            ("números 123 símbolos @#$", "should_handle_mixed"),
            ("query with\nnewlines\tand\ttabs", "should_handle_whitespace"),
            ("repeated repeated repeated word word", "should_handle_repetition")
        ]
        
        edge_results = []
        
        for query, test_type in edge_cases:
            try:
                agent_results = {}
                for agent in ["conversation", "knowledge", "codecraft", "execution", "feedback"]:
                    confidence = self.router.calculate_confidence(agent, query)
                    agent_results[agent] = confidence
                
                result = {
                    "query": query[:50] + "..." if len(query) > 50 else query,
                    "test_type": test_type,
                    "agent_confidences": agent_results,
                    "max_confidence": max(agent_results.values()),
                    "successful": True,
                    "error": None
                }
                
            except Exception as e:
                result = {
                    "query": query[:50] + "..." if len(query) > 50 else query,
                    "test_type": test_type,
                    "successful": False,
                    "error": str(e)
                }
            
            edge_results.append(result)
            
            status = "✅" if result["successful"] else "❌"
            print(f"{status} {test_type}")
        
        return edge_results
    
    async def _test_circular_prevention(self) -> Dict[str, Any]:
        """Circular routing prevention test"""
        
        print("Testing circular routing prevention...")
        
        ambiguous_queries = [
            "something unclear",
            "vague request", 
            "ambiguous technical thing",
            "help with stuff"
        ]
        
        circular_results = {
            "queries_tested": len(ambiguous_queries),
            "circular_loops_detected": 0,
            "min_confidences": [],
            "successful": True
        }
        
        for query in ambiguous_queries:
            agent_confidences = {}
            
            for agent in ["conversation", "knowledge", "codecraft", "execution", "feedback"]:
                confidence = self.router.calculate_confidence(agent, query)
                agent_confidences[agent] = confidence
            
            min_confidence = min(agent_confidences.values())
            max_confidence = max(agent_confidences.values())
            
            circular_results["min_confidences"].append(min_confidence)
            
            if max_confidence < 0.3:
                circular_results["circular_loops_detected"] += 1
                print(f"⚠️ Potential circular routing for: {query}")
                print(f"   Best confidence: {max_confidence:.3f}")
        
        avg_min_confidence = sum(circular_results["min_confidences"]) / len(circular_results["min_confidences"])
        circular_results["avg_min_confidence"] = avg_min_confidence
        circular_results["successful"] = circular_results["circular_loops_detected"] == 0
        
        if circular_results["successful"]:
            print("✅ No circular routing patterns detected")
        else:
            print(f"❌ {circular_results['circular_loops_detected']} potential circular cases")
        
        return circular_results
    
    def _calculate_summary_metrics(self, results: Dict) -> Dict[str, Any]:
        """Calculate summary metrics"""
        
        consistency_tests = results["consistency_tests"]
        performance_tests = results["performance_tests"]
        
        consistent_count = sum(1 for r in consistency_tests if r["consistent"])
        consistency_rate = consistent_count / len(consistency_tests)
        
        expected_met_count = sum(1 for r in consistency_tests if r["meets_expected"])
        expected_rate = expected_met_count / len(consistency_tests)
        
        det_avg = performance_tests["deterministic"]["avg_ms"]
        meets_100ms_target = det_avg < 100
        
        summary = {
            "consistency_rate": consistency_rate,
            "expected_confidence_rate": expected_rate,
            "avg_response_time_ms": det_avg,
            "meets_100ms_target": meets_100ms_target,
            "circular_prevention_success": results["circular_prevention_tests"]["successful"],
            "overall_success": (
                consistency_rate >= 0.95 and 
                expected_rate >= 0.8 and 
                meets_100ms_target and
                results["circular_prevention_tests"]["successful"]
            )
        }
        
        return summary
    
    async def _save_test_results(self, results: Dict):
        """Save test results"""
        
        results_dir = Path("C:/temp/Agent/TestResults")
        results_dir.mkdir(exist_ok=True, parents=True)
        
        timestamp = int(time.time())
        results_file = results_dir / f"routing_tests_{timestamp}.json"
        
        try:
            with open(results_file, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
            print(f"📄 Test results saved to: {results_file}")
        except Exception as e:
            print(f"⚠️ Failed to save test results: {e}")


class RoutingMonitor:
    """Real-time monitoring of the routing system"""
    
    def __init__(self):
        self.routing_stats = {
            "total_decisions": 0,
            "deterministic_decisions": 0,
            "llm_fallback_decisions": 0,
            "agent_stats": {},
            "performance_metrics": {},
            "recent_decisions": []
        }
        self.start_time = time.time()
    
    def record_routing_decision(self, agent_id: str, query: str, confidence: float, 
                             method: str, response_time_ms: float):
        """Record routing decision"""
        
        self.routing_stats["total_decisions"] += 1
        
        if "deterministic" in method:
            self.routing_stats["deterministic_decisions"] += 1
        elif "llm" in method or "hybrid" in method:
            self.routing_stats["llm_fallback_decisions"] += 1
        
        if agent_id not in self.routing_stats["agent_stats"]:
            self.routing_stats["agent_stats"][agent_id] = {
                "decisions": 0,
                "avg_confidence": 0,
                "response_times": []
            }
        
        agent_stats = self.routing_stats["agent_stats"][agent_id]
        agent_stats["decisions"] += 1
        
        prev_avg = agent_stats["avg_confidence"]
        new_count = agent_stats["decisions"]
        agent_stats["avg_confidence"] = (prev_avg * (new_count - 1) + confidence) / new_count
        
        agent_stats["response_times"].append(response_time_ms)
        if len(agent_stats["response_times"]) > 100:  # Keep last 100
            agent_stats["response_times"].pop(0)
        
        decision_record = {
            "timestamp": time.time(),
            "agent_id": agent_id,
            "query": query[:50],
            "confidence": confidence,
            "method": method,
            "response_time_ms": response_time_ms
        }
        
        self.routing_stats["recent_decisions"].append(decision_record)
        if len(self.routing_stats["recent_decisions"]) > 20:
            self.routing_stats["recent_decisions"].pop(0)
    
    def get_performance_summary(self) -> Dict[str, Any]:
        """Get performance summary"""
        
        uptime = time.time() - self.start_time
        total_decisions = self.routing_stats["total_decisions"]
        
        if total_decisions == 0:
            return {"error": "No routing decisions recorded yet"}
        
        decisions_per_minute = (total_decisions / uptime) * 60 if uptime > 0 else 0
        deterministic_rate = self.routing_stats["deterministic_decisions"] / total_decisions
        
        agent_performance = {}
        for agent_id, stats in self.routing_stats["agent_stats"].items():
            avg_response_time = sum(stats["response_times"]) / len(stats["response_times"]) if stats["response_times"] else 0
            
            agent_performance[agent_id] = {
                "total_decisions": stats["decisions"],
                "avg_confidence": stats["avg_confidence"],
                "avg_response_time_ms": avg_response_time,
                "decision_rate": stats["decisions"] / total_decisions
            }
        
        summary = {
            "uptime_seconds": uptime,
            "total_decisions": total_decisions,
            "decisions_per_minute": decisions_per_minute,
            "deterministic_rate": deterministic_rate,
            "llm_fallback_rate": self.routing_stats["llm_fallback_decisions"] / total_decisions,
            "agent_performance": agent_performance,
            "health_status": self._calculate_health_status(deterministic_rate, agent_performance)
        }
        
        return summary
    
    def _calculate_health_status(self, deterministic_rate: float, agent_performance: Dict) -> str:
        """Calculate the health status of the routing system"""
        
        healthy_deterministic_rate = deterministic_rate > 0.7  
        
        healthy_response_times = True
        for agent_stats in agent_performance.values():
            if agent_stats["avg_response_time_ms"] > 200:  
                healthy_response_times = False
                break
        
        if healthy_deterministic_rate and healthy_response_times:
            return "HEALTHY"
        elif healthy_deterministic_rate or healthy_response_times:
            return "WARNING"
        else:
            return "CRITICAL"
    
    def print_status(self):
        """Print current status"""
        
        summary = self.get_performance_summary()
        
        if "error" in summary:
            print(f"📊 Routing Monitor: {summary['error']}")
            return
        
        print(f"\n📊 Routing System Status ({summary['health_status']})")
        print("=" * 50)
        print(f"Uptime: {summary['uptime_seconds']:.0f}s")
        print(f"Total Decisions: {summary['total_decisions']}")
        print(f"Decisions/min: {summary['decisions_per_minute']:.1f}")
        print(f"Deterministic Rate: {summary['deterministic_rate']:.1%}")
        print(f"LLM Fallback Rate: {summary['llm_fallback_rate']:.1%}")
        
        print("\n🤖 Agent Performance:")
        for agent_id, stats in summary["agent_performance"].items():
            print(f"{agent_id:12} | {stats['total_decisions']:3d} decisions | "
                  f"{stats['avg_confidence']:.2f} conf | {stats['avg_response_time_ms']:5.1f}ms")
        
        print("=" * 50)


async def test_routing_system():
    """Main test function"""
    
    print("🚀 Starting Routing System Tests")
    
    router = DeterministicRouter()
    test_suite = RoutingTestSuite(router)
    monitor = RoutingMonitor()
    
    results = await test_suite.run_comprehensive_tests()
    
    summary = results["summary"]
    print(f"\n📋 Test Results Summary:")
    print(f"Consistency Rate: {summary['consistency_rate']:.1%}")
    print(f"Expected Confidence Rate: {summary['expected_confidence_rate']:.1%}")
    print(f"Avg Response Time: {summary['avg_response_time_ms']:.1f}ms")
    print(f"Meets 100ms Target: {'✅' if summary['meets_100ms_target'] else '❌'}")
    print(f"Circular Prevention: {'✅' if summary['circular_prevention_success'] else '❌'}")
    print(f"Overall Success: {'✅' if summary['overall_success'] else '❌'}")
    
    return results


if __name__ == "__main__":
    asyncio.run(test_routing_system())