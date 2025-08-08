# src/core/intelligent_cache.py
import time
import hashlib
import json
from typing import Any, Dict, Optional, List
from dataclasses import dataclass
from pathlib import Path

@dataclass
class CacheEntry:
    key: str
    value: Any
    timestamp: float
    access_count: int
    ttl: Optional[float]
    size_bytes: int
    tags: List[str]

class IntelligentCache:
    """Cache inteligente con LRU, TTL y compresión"""
    
    def __init__(self, max_size_mb: int = 100, default_ttl: float = 3600):
        self.max_size_bytes = max_size_mb * 1024 * 1024
        self.default_ttl = default_ttl
        self.cache: Dict[str, CacheEntry] = {}
        self.access_order: List[str] = []
        self.current_size = 0
        
        # Métricas
        self.hits = 0
        self.misses = 0
        self.evictions = 0
    
    def _generate_key(self, data: Any) -> str:
        """Generar clave única para cualquier data"""
        if isinstance(data, str):
            content = data
        else:
            content = json.dumps(data, sort_keys=True, default=str)
        return hashlib.md5(content.encode()).hexdigest()
    
    def get(self, key: str = None, data: Any = None) -> Optional[Any]:
        """Obtener del cache por key o data"""
        if not key:
            key = self._generate_key(data)
        
        if key not in self.cache:
            self.misses += 1
            return None
        
        entry = self.cache[key]
        
        # Check TTL
        if entry.ttl and time.time() - entry.timestamp > entry.ttl:
            self.remove(key)
            self.misses += 1
            return None
        
        # Update access
        entry.access_count += 1
        self._update_access_order(key)
        
        self.hits += 1
        return entry.value
    
    def put(self, value: Any, key: str = None, ttl: float = None, tags: List[str] = None):
        """Almacenar en cache"""
        if not key:
            key = self._generate_key(value)
        
        # Calculate size
        size_bytes = len(str(value).encode('utf-8'))
        
        # Evict if necessary
        while self.current_size + size_bytes > self.max_size_bytes and self.cache:
            self._evict_lru()
        
        entry = CacheEntry(
            key=key,
            value=value,
            timestamp=time.time(),
            access_count=1,
            ttl=ttl or self.default_ttl,
            size_bytes=size_bytes,
            tags=tags or []
        )
        
        self.cache[key] = entry
        self.current_size += size_bytes
        self._update_access_order(key)
    
    def remove(self, key: str):
        """Remover entrada específica"""
        if key in self.cache:
            entry = self.cache.pop(key)
            self.current_size -= entry.size_bytes
            if key in self.access_order:
                self.access_order.remove(key)
    
    def clear_by_tag(self, tag: str):
        """Limpiar entradas por tag"""
        to_remove = []
        for key, entry in self.cache.items():
            if tag in entry.tags:
                to_remove.append(key)
        
        for key in to_remove:
            self.remove(key)
    
    def _update_access_order(self, key: str):
        """Actualizar orden LRU"""
        if key in self.access_order:
            self.access_order.remove(key)
        self.access_order.append(key)
    
    def _evict_lru(self):
        """Evict least recently used"""
        if self.access_order:
            lru_key = self.access_order[0]
            self.remove(lru_key)
            self.evictions += 1
    
    def get_stats(self) -> Dict:
        """Estadísticas del cache"""
        total_requests = self.hits + self.misses
        hit_rate = (self.hits / total_requests * 100) if total_requests > 0 else 0
        
        return {
            "entries": len(self.cache),
            "size_mb": self.current_size / (1024 * 1024),
            "max_size_mb": self.max_size_bytes / (1024 * 1024),
            "hit_rate": hit_rate,
            "hits": self.hits,
            "misses": self.misses,
            "evictions": self.evictions
        }
    
    def cleanup_expired(self):
        """Limpiar entradas expiradas"""
        current_time = time.time()
        expired_keys = []
        
        for key, entry in self.cache.items():
            if entry.ttl and current_time - entry.timestamp > entry.ttl:
                expired_keys.append(key)
        
        for key in expired_keys:
            self.remove(key)


# Cache específicos por agente
class AgentCacheManager:
    """Manager de caches por agente"""
    
    def __init__(self):
        self.caches: Dict[str, IntelligentCache] = {}
    
    def get_cache(self, agent_id: str) -> IntelligentCache:
        """Obtener cache para agente específico"""
        if agent_id not in self.caches:
            self.caches[agent_id] = IntelligentCache(
                max_size_mb=50,  # 50MB per agent
                default_ttl=1800  # 30 minutes
            )
        return self.caches[agent_id]
    
    def get_global_stats(self) -> Dict:
        """Estadísticas globales"""
        total_entries = 0
        total_size_mb = 0
        total_hits = 0
        total_misses = 0
        
        agent_stats = {}
        
        for agent_id, cache in self.caches.items():
            stats = cache.get_stats()
            agent_stats[agent_id] = stats
            
            total_entries += stats["entries"]
            total_size_mb += stats["size_mb"]
            total_hits += stats["hits"]
            total_misses += stats["misses"]
        
        total_requests = total_hits + total_misses
        global_hit_rate = (total_hits / total_requests * 100) if total_requests > 0 else 0
        
        return {
            "global_stats": {
                "total_entries": total_entries,
                "total_size_mb": total_size_mb,
                "global_hit_rate": global_hit_rate,
                "total_hits": total_hits,
                "total_misses": total_misses
            },
            "agent_stats": agent_stats
        }


# Singleton global
cache_manager = AgentCacheManager()