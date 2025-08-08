# src/core/error_handling.py
import asyncio
import time
import random
from typing import Callable, Any, Dict, Optional
from enum import Enum

class CircuitState(Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"

class CircuitBreaker:
    def __init__(self, failure_threshold: int = 5, timeout: int = 60):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failure_count = 0
        self.state = CircuitState.CLOSED
        self.last_failure_time = 0
    
    async def call(self, func: Callable, *args, **kwargs) -> Any:
        if self.state == CircuitState.OPEN:
            if time.time() - self.last_failure_time > self.timeout:
                self.state = CircuitState.HALF_OPEN
            else:
                raise Exception("Circuit breaker is OPEN")
        
        try:
            result = await func(*args, **kwargs)
            if self.state == CircuitState.HALF_OPEN:
                self.reset()
            return result
        except Exception as e:
            self.record_failure()
            raise e
    
    def record_failure(self):
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        if self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN
    
    def reset(self):
        self.failure_count = 0
        self.state = CircuitState.CLOSED

async def retry_with_exponential_backoff(
    func: Callable, 
    max_retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 60.0,
    exceptions: tuple = (Exception,)
) -> Any:
    for attempt in range(max_retries + 1):
        try:
            return await func()
        except exceptions as e:
            if attempt == max_retries:
                raise e
            
            delay = min(base_delay * (2 ** attempt) + random.uniform(0, 1), max_delay)
            await asyncio.sleep(delay)

class ErrorHandler:
    def __init__(self):
        self.circuit_breakers: Dict[str, CircuitBreaker] = {}
    
    def get_circuit_breaker(self, key: str) -> CircuitBreaker:
        if key not in self.circuit_breakers:
            self.circuit_breakers[key] = CircuitBreaker()
        return self.circuit_breakers[key]
    
    async def safe_call(self, func: Callable, operation_key: str, *args, **kwargs) -> tuple[bool, Any]:
        """Safe call with circuit breaker and retry logic"""
        circuit = self.get_circuit_breaker(operation_key)
        
        try:
            async def wrapped_func():
                return await circuit.call(func, *args, **kwargs)
            
            result = await retry_with_exponential_backoff(wrapped_func, max_retries=2)
            return True, result
        except Exception as e:
            return False, str(e)