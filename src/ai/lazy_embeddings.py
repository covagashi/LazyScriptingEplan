# src/ai/lazy_embeddings.py
import asyncio
import time
import numpy as np
from pathlib import Path
from typing import Dict, List, Optional, Any
from sentence_transformers import SentenceTransformer
import pickle
from ..core.intelligent_cache import cache_manager

class LazyEmbeddingModel:
    """Modelo de embeddings con carga lazy y cache inteligente"""
    
    def __init__(self, model_name: str = 'sentence-transformers/all-MiniLM-L6-v2'):
        self.model_name = model_name
        self.model: Optional[SentenceTransformer] = None
        self.loading = False
        self.load_time = None
        
        # Cache específico para embeddings
        self.cache = cache_manager.get_cache("embeddings")
        
        # Métricas
        self.metrics = {
            "cache_hits": 0,
            "cache_misses": 0,
            "embeddings_computed": 0,
            "load_operations": 0
        }
    
    async def _load_model(self):
        """Carga lazy del modelo"""
        if self.model is not None:
            return
        
        if self.loading:
            # Esperar si ya está cargando
            while self.loading:
                await asyncio.sleep(0.1)
            return
        
        self.loading = True
        start_time = time.time()
        
        try:
            # Intentar carga local primero
            model_path = Path("C:/Users/cd.lopez/.cache/huggingface/transformers/sentence-transformers--all-MiniLM-L6-v2")
            if model_path.exists():
                self.model = SentenceTransformer(str(model_path))
            else:
                self.model = SentenceTransformer(self.model_name, local_files_only=True)
            
            self.load_time = time.time() - start_time
            self.metrics["load_operations"] += 1
            
        finally:
            self.loading = False
    
    async def encode_batch_async(self, texts: List[str], batch_size: int = 32) -> np.ndarray:
        """Encoding asíncrono por lotes con cache"""
        
        # Verificar cache primero
        cache_results = {}
        uncached_texts = []
        uncached_indices = []
        
        for i, text in enumerate(texts):
            cached = self.cache.get(data=text)
            if cached is not None:
                cache_results[i] = cached
                self.metrics["cache_hits"] += 1
            else:
                uncached_texts.append(text)
                uncached_indices.append(i)
                self.metrics["cache_misses"] += 1
        
        # Si todo está en cache
        if not uncached_texts:
            return np.array([cache_results[i] for i in range(len(texts))])
        
        # Cargar modelo si es necesario
        await self._load_model()
        
        # Procesar textos no cacheados por lotes
        new_embeddings = {}
        
        for batch_start in range(0, len(uncached_texts), batch_size):
            batch_texts = uncached_texts[batch_start:batch_start + batch_size]
            batch_indices = uncached_indices[batch_start:batch_start + batch_size]
            
            # Ejecutar en thread pool para no bloquear
            loop = asyncio.get_event_loop()
            batch_embeddings = await loop.run_in_executor(
                None, 
                self.model.encode,
                batch_texts
            )
            
            # Guardar en cache y resultados
            for i, (idx, embedding) in enumerate(zip(batch_indices, batch_embeddings)):
                new_embeddings[idx] = embedding
                # Cache con TTL de 1 hora para embeddings
                self.cache.put(
                    embedding.tolist(),
                    data=uncached_texts[batch_start + i],
                    ttl=3600,
                    tags=["embeddings"]
                )
            
            self.metrics["embeddings_computed"] += len(batch_embeddings)
        
        # Combinar resultados cached y nuevos
        all_results = {}
        all_results.update(cache_results)
        all_results.update(new_embeddings)
        
        # Ordenar por índice original
        final_embeddings = [all_results[i] for i in range(len(texts))]
        
        return np.array(final_embeddings)
    
    async def encode_single_async(self, text: str) -> np.ndarray:
        """Encoding de un solo texto con cache"""
        results = await self.encode_batch_async([text])
        return results[0]
    
    def get_metrics(self) -> Dict[str, Any]:
        """Métricas del modelo lazy"""
        
        cache_stats = self.cache.get_stats()
        total_requests = self.metrics["cache_hits"] + self.metrics["cache_misses"]
        cache_hit_rate = (self.metrics["cache_hits"] / total_requests * 100) if total_requests > 0 else 0
        
        return {
            "model_loaded": self.model is not None,
            "load_time": self.load_time,
            "load_operations": self.metrics["load_operations"],
            "cache_hit_rate": cache_hit_rate,
            "embeddings_computed": self.metrics["embeddings_computed"],
            "cache_stats": cache_stats
        }


class LazyRAG:
    """RAG base con embeddings lazy y cache inteligente"""
    
    def __init__(self, name: str):
        self.name = name
        self.embedding_model = LazyEmbeddingModel()
        self.documents = []
        self.embeddings: Optional[np.ndarray] = None
        self.embeddings_loaded = False
        
        # Cache específico para búsquedas
        self.search_cache = cache_manager.get_cache(f"rag_{name}")
        
        # Configuración lazy
        self.chunk_size = 100  # Procesar embeddings por chunks
        self.preload_threshold = 50  # Cargar si hay menos de 50 docs
    
    async def add_documents_lazy(self, documents: List[Dict]):
        """Agregar documentos sin calcular embeddings inmediatamente"""
        self.documents.extend(documents)
        self.embeddings_loaded = False
        
        # Si son pocos documentos, precargar
        if len(documents) <= self.preload_threshold:
            await self._ensure_embeddings_loaded()
    
    async def _ensure_embeddings_loaded(self):
        """Asegurar que los embeddings estén cargados"""
        if self.embeddings_loaded:
            return
        
        if not self.documents:
            return
        
        # Crear textos para embeddings
        texts = []
        for doc in self.documents:
            if 'searchable_text' in doc:
                texts.append(doc['searchable_text'])
            elif 'text' in doc:
                texts.append(doc['text'])
            else:
                texts.append(str(doc))
        
        # Calcular embeddings en chunks
        all_embeddings = []
        
        for chunk_start in range(0, len(texts), self.chunk_size):
            chunk_texts = texts[chunk_start:chunk_start + self.chunk_size]
            chunk_embeddings = await self.embedding_model.encode_batch_async(chunk_texts)
            all_embeddings.append(chunk_embeddings)
            
            # Yield control periodically
            await asyncio.sleep(0.01)
        
        # Combinar chunks
        if all_embeddings:
            self.embeddings = np.vstack(all_embeddings)
            self.embeddings_loaded = True
    
    async def search_async(self, query: str, top_k: int = 5, threshold: float = 0.3) -> List[Dict]:
        """Búsqueda semántica asíncrona con cache"""
        
        # Verificar cache de búsqueda
        search_key = f"{query}_{top_k}_{threshold}"
        cached_results = self.search_cache.get(data=search_key)
        if cached_results is not None:
            return cached_results
        
        # Asegurar embeddings cargados
        await self._ensure_embeddings_loaded()
        
        if not self.embeddings_loaded or len(self.documents) == 0:
            return []
        
        # Calcular embedding de query
        query_embedding = await self.embedding_model.encode_single_async(query)
        
        # Calcular similitudes
        similarities = np.dot(self.embeddings, query_embedding) / (
            np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(query_embedding)
        )
        
        # Filtrar y ordenar resultados
        results = []
        for i, score in enumerate(similarities):
            if score >= threshold:
                results.append({
                    'document': self.documents[i],
                    'score': float(score),
                    'match_type': 'semantic'
                })
        
        results.sort(key=lambda x: x['score'], reverse=True)
        final_results = results[:top_k]
        
        # Cache resultados por 10 minutos
        self.search_cache.put(
            final_results,
            data=search_key,
            ttl=600,
            tags=["search_results"]
        )
        
        return final_results
    
    def get_status(self) -> Dict[str, Any]:
        """Estado del RAG lazy"""
        return {
            "name": self.name,
            "documents_count": len(self.documents),
            "embeddings_loaded": self.embeddings_loaded,
            "embeddings_shape": self.embeddings.shape if self.embeddings is not None else None,
            "embedding_model_metrics": self.embedding_model.get_metrics(),
            "search_cache_stats": self.search_cache.get_stats()
        }


# Mixin para agentes existentes
class LazyLoadingMixin:
    """Mixin para agregar lazy loading a agentes existentes"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lazy_components = {}
    
    async def lazy_load_component(self, component_name: str, loader_func):
        """Cargar componente bajo demanda"""
        if component_name not in self.lazy_components:
            self.lazy_components[component_name] = await loader_func()
        return self.lazy_components[component_name]
    
    def get_lazy_status(self) -> Dict[str, bool]:
        """Estado de componentes lazy"""
        return {name: component is not None 
                for name, component in self.lazy_components.items()}