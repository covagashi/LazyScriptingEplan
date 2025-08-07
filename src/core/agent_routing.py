# src/core/agent_routing.py
import time
from typing import Dict, List, Tuple, Optional
from abc import ABC, abstractmethod

class DeterministicRouter:
    """Routing determinístico con lookup tables y scoring híbrido"""
    
    def __init__(self):
        self.decision_cache = {}
        self.cache_ttl = 300 
        
        self.agent_keywords = {
            "conversation": {
                "high_confidence": [
                    "hello", "hi", "help", "what", "how", "explain", 
                    "greeting", "chat", "basic question"
                ],
                "medium_confidence": [
                    "simple", "basic", "general", "overview"
                ],
                "low_confidence": [
                    "script", "code", "execute", "generate", "api"
                ]
            },
            "knowledge": {
                "high_confidence": [
                    "documentation", "examples", "eplan api", "action parameters",
                    "xafactionsetting", "eplan usage", "how to use", "explain eplan"
                ],
                "medium_confidence": [
                    "eplan", "electrical", "documentation", "guide", "tutorial"
                ],
                "low_confidence": [
                    "execute", "run", "generate script", "create file"
                ]
            },
            "codecraft": {
                "high_confidence": [
                    "generate script", "create script", "write code", "c# code",
                    "eplan script", "script generation", "code generation"
                ],
                "medium_confidence": [
                    "script", "code", "programming", "c#", "generate"
                ],
                "low_confidence": [
                    "execute", "run", "only explanation", "just tell me"
                ]
            },
            "execution": {
                "high_confidence": [
                    "execute", "run", "execute script", "run script",
                    "eplan remoting", "execute action", "run code"
                ],
                "medium_confidence": [
                    "action", "remoting", "eplan connection", "execute"
                ],
                "low_confidence": [
                    "just show", "only generate", "explain", "documentation"
                ]
            },
            "feedback": {
                "high_confidence": [
                    "analyze logs", "check results", "validate execution",
                    "execution feedback", "log analysis", "error check"
                ],
                "medium_confidence": [
                    "feedback", "validate", "check", "logs", "results"
                ],
                "low_confidence": [
                    "generate", "create", "write", "explain basic"
                ]
            }
        }
        
        self.intent_patterns = {
            "greeting": ["hello", "hi", "hey", "greetings"],
            "help_request": ["help", "assistance", "support"],
            "code_generation": ["generate", "create script", "write code"],
            "execution": ["execute", "run", "perform"],
            "documentation": ["explain", "what is", "how to", "documentation"],
            "validation": ["check", "validate", "verify", "feedback"]
        }
    
    def calculate_confidence(self, agent_id: str, intent: str) -> float:
        """Calculating confidence using deterministic lookup tables"""
        
        cache_key = f"{agent_id}_{intent.lower()}"
        if cache_key in self.decision_cache:
            cached = self.decision_cache[cache_key]
            if time.time() - cached["timestamp"] < self.cache_ttl:
                return cached["confidence"]
        
        intent_lower = intent.lower()
        agent_keywords = self.agent_keywords.get(agent_id, {})
        
        confidence = 0.0
        
        high_keywords = agent_keywords.get("high_confidence", [])
        for keyword in high_keywords:
            if keyword in intent_lower:
                confidence = max(confidence, 0.9)
                break
        
        if confidence < 0.7:
            medium_keywords = agent_keywords.get("medium_confidence", [])
            for keyword in medium_keywords:
                if keyword in intent_lower:
                    confidence = max(confidence, 0.6)
        
        low_keywords = agent_keywords.get("low_confidence", [])
        for keyword in low_keywords:
            if keyword in intent_lower:
                confidence = max(0.1, confidence - 0.3)
        
        pattern_bonus = self._calculate_pattern_bonus(agent_id, intent_lower)
        confidence = min(1.0, confidence + pattern_bonus)
        
        self.decision_cache[cache_key] = {
            "confidence": confidence,
            "timestamp": time.time()
        }
        
        return confidence
    
    def _calculate_pattern_bonus(self, agent_id: str, intent: str) -> float:
        """Bonus for specific intention patterns"""
        
        bonus = 0.0
        
        if agent_id == "conversation":
            if any(pattern in intent for pattern in self.intent_patterns["greeting"]):
                bonus += 0.2
            if any(pattern in intent for pattern in self.intent_patterns["help_request"]):
                bonus += 0.1
        
        elif agent_id == "codecraft":
            if any(pattern in intent for pattern in self.intent_patterns["code_generation"]):
                bonus += 0.2
            if "c#" in intent or "script" in intent:
                bonus += 0.1
        
        elif agent_id == "execution":
            if any(pattern in intent for pattern in self.intent_patterns["execution"]):
                bonus += 0.2
            if "eplan" in intent and ("execute" in intent or "run" in intent):
                bonus += 0.1
        
        elif agent_id == "knowledge":
            if any(pattern in intent for pattern in self.intent_patterns["documentation"]):
                bonus += 0.2
            if "eplan" in intent and ("api" in intent or "documentation" in intent):
                bonus += 0.1
        
        elif agent_id == "feedback":
            if any(pattern in intent for pattern in self.intent_patterns["validation"]):
                bonus += 0.2
        
        return min(0.3, bonus)  
    
    def get_routing_explanation(self, agent_id: str, intent: str, confidence: float) -> str:
        """Explanation of routing for debugging"""
        
        reasons = []
        intent_lower = intent.lower()
        agent_keywords = self.agent_keywords.get(agent_id, {})
        
        for level, keywords in agent_keywords.items():
            matched = [kw for kw in keywords if kw in intent_lower]
            if matched:
                reasons.append(f"{level}: {matched}")
        
        return f"Agent {agent_id} confidence {confidence:.2f}: {'; '.join(reasons)}"


class HybridCanHandle:
    """Hybrid implementation: deterministic rules + LLM fallback"""
    
    def __init__(self, agent_id: str, ai_client, router: DeterministicRouter):
        self.agent_id = agent_id
        self.ai_client = ai_client
        self.router = router
        self.fallback_threshold = 0.4  
        
    async def can_handle(self, intent: str, specialty: str) -> Tuple[float, str]:
        """
        hybrid can_handle() method 
        Returns: (confidence, method_used)
        """
               
        deterministic_confidence = self.router.calculate_confidence(self.agent_id, intent)
        
        if deterministic_confidence >= 0.7:
            explanation = self.router.get_routing_explanation(
                self.agent_id, intent, deterministic_confidence
            )
            return deterministic_confidence, f"deterministic: {explanation}"
        
        if deterministic_confidence <= 0.2:
            return deterministic_confidence, "deterministic: low confidence"
        
        try:
            llm_confidence = await self._llm_fallback(intent, specialty)
            
            final_confidence = (deterministic_confidence * 0.6) + (llm_confidence * 0.4)
            
            return final_confidence, f"hybrid: det={deterministic_confidence:.2f}, llm={llm_confidence:.2f}"
            
        except Exception as e:
            return deterministic_confidence, f"deterministic_fallback: llm_error={str(e)[:50]}"
    
    async def _llm_fallback(self, intent: str, specialty: str) -> float:
        """LLM fallback para casos ambiguos"""
        
        prompt = f"""ROUTING DECISION for ambiguous case:

Intent: "{intent}"
My specialty: {specialty}
My agent ID: {self.agent_id}

Deterministic routing was uncertain. Can I handle this intent?

Consider:
- My specific expertise area
- Whether this requires my specialized knowledge/skills
- If another agent would be more appropriate

Return ONLY a number between 0.0 and 1.0:"""

        response = await self.ai_client.generate(prompt)
        
        try:
            confidence = float(response.strip())
            return max(0.0, min(1.0, confidence)) 
        except:
            return 0.3  # Conservative fallback

