# src/core/memory_manager.py
import asyncio
import time
import psutil
import gc
from typing import Dict, List, Any
from pathlib import Path

class AutoMemoryManager:
    """Automatic memory management for the agent system"""
    
    def __init__(self, memory_limit_mb: int = 500):
        self.memory_limit_bytes = memory_limit_mb * 1024 * 1024
        self.cleanup_tasks = []
        self.monitoring = False
        
        # Cleanup strategies
        self.cleanup_strategies = [
            self._cleanup_old_contexts,
            self._cleanup_expired_caches,
            self._cleanup_completed_flows,
            self._force_garbage_collection
        ]
    
    async def start_monitoring(self):
        """Start automatic memory monitoring"""
        self.monitoring = True
        asyncio.create_task(self._memory_monitor_loop())
        print("🧠 Auto memory management started")
    
    async def _memory_monitor_loop(self):
        """Main monitoring loop"""
        while self.monitoring:
            try:
                current_memory = self._get_memory_usage()
                
                if current_memory > self.memory_limit_bytes:
                    await self._trigger_cleanup(current_memory)
                
                await asyncio.sleep(30)  # Check every 30 seconds
                
            except Exception as e:
                print(f"Memory monitor error: {e}")
                await asyncio.sleep(60)
    
    def _get_memory_usage(self) -> int:
        """Get current memory usage"""
        process = psutil.Process()
        return process.memory_info().rss
    
    async def _trigger_cleanup(self, current_memory: int):
        """Trigger cleanup when memory limit exceeded"""
        print(f"🧹 Memory cleanup triggered: {current_memory / 1024 / 1024:.1f}MB")
        
        initial_memory = current_memory
        
        for strategy in self.cleanup_strategies:
            try:
                await strategy()
                
                new_memory = self._get_memory_usage()
                freed = initial_memory - new_memory
                
                if freed > 0:
                    print(f"   Freed {freed / 1024 / 1024:.1f}MB")
                
                if new_memory < self.memory_limit_bytes:
                    break
                    
            except Exception as e:
                print(f"Cleanup strategy error: {e}")
    
    async def _cleanup_old_contexts(self):
        """Clean up old filesystem contexts"""
        context_path = Path("C:/temp/Agent/Context")
        if not context_path.exists():
            return
        
        cutoff_time = time.time() - (24 * 3600)  # 24 hours
        cleaned = 0
        
        for context_file in context_path.glob("*.json"):
            if context_file.stat().st_mtime < cutoff_time:
                try:
                    context_file.unlink()
                    cleaned += 1
                except:
                    pass
        
        if cleaned > 0:
            print(f"   Cleaned {cleaned} old context files")
    
    async def _cleanup_expired_caches(self):
        """Clean up expired cache entries"""
        from .intelligent_cache import cache_manager
        
        cleaned = 0
        for cache in cache_manager.caches.values():
            initial_entries = len(cache.cache)
            cache.cleanup_expired()
            cleaned += initial_entries - len(cache.cache)
        
        if cleaned > 0:
            print(f"   Cleaned {cleaned} expired cache entries")
    
    async def _cleanup_completed_flows(self):
        """Clean up old completed message flows"""
        # This would be called on the message bus dashboard
        # Keeping only last 50 completed flows instead of 100
        pass
    
    async def _force_garbage_collection(self):
        """Force Python garbage collection"""
        collected = gc.collect()
        if collected > 0:
            print(f"   Garbage collected {collected} objects")
    
    def get_memory_stats(self) -> Dict[str, Any]:
        """Get current memory statistics"""
        process = psutil.Process()
        memory_info = process.memory_info()
        
        return {
            "current_mb": memory_info.rss / 1024 / 1024,
            "limit_mb": self.memory_limit_bytes / 1024 / 1024,
            "usage_percent": (memory_info.rss / self.memory_limit_bytes) * 100,
            "monitoring": self.monitoring
        }