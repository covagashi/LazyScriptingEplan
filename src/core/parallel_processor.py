# src/core/parallel_processor.py
import asyncio
import time
from typing import List, Dict, Any, Callable, Optional
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor
from ..core.message_bus import AgentMessage

@dataclass
class ParallelTask:
    task_id: str
    coroutine: Any
    priority: int = 1
    max_retries: int = 3
    timeout: float = 30.0
    dependencies: List[str] = None

class ParallelProcessor:
    """Procesador paralelo para operaciones de agentes"""
    
    def __init__(self, max_concurrent: int = 5):
        self.max_concurrent = max_concurrent
        self.active_tasks: Dict[str, asyncio.Task] = {}
        self.completed_tasks: Dict[str, Any] = {}
        self.failed_tasks: Dict[str, str] = {}
        
        # Thread pool para operaciones CPU-intensive
        self.thread_pool = ThreadPoolExecutor(max_workers=3)
        
        # Semaforo para limitar concurrencia
        self.semaphore = asyncio.Semaphore(max_concurrent)
        
        # Métricas
        self.metrics = {
            "tasks_executed": 0,
            "tasks_failed": 0,
            "average_execution_time": 0,
            "concurrent_peak": 0
        }
    
    async def execute_parallel_tasks(self, tasks: List[ParallelTask]) -> Dict[str, Any]:
        """Ejecutar múltiples tareas en paralelo respetando dependencias"""
        
        start_time = time.time()
        
        # Organizar tareas por dependencias
        ready_tasks = [task for task in tasks if not task.dependencies]
        waiting_tasks = [task for task in tasks if task.dependencies]
        
        results = {}
        
        # Ejecutar tareas listas
        while ready_tasks or waiting_tasks:
            
            # Ejecutar tareas sin dependencias
            if ready_tasks:
                batch_results = await self._execute_batch(ready_tasks)
                results.update(batch_results)
                ready_tasks.clear()
            
            # Revisar tareas esperando
            newly_ready = []
            for task in waiting_tasks[:]:
                if all(dep_id in results for dep_id in task.dependencies):
                    newly_ready.append(task)
                    waiting_tasks.remove(task)
            
            ready_tasks.extend(newly_ready)
            
            # Evitar loop infinito
            if not ready_tasks and waiting_tasks:
                # Forzar ejecución de tareas restantes
                ready_tasks = waiting_tasks[:]
                waiting_tasks.clear()
        
        execution_time = time.time() - start_time
        self._update_metrics(len(tasks), execution_time)
        
        return results
    
    async def _execute_batch(self, tasks: List[ParallelTask]) -> Dict[str, Any]:
        """Ejecutar lote de tareas en paralelo"""
        
        # Ordenar por prioridad
        tasks.sort(key=lambda t: t.priority, reverse=True)
        
        # Crear tareas asyncio
        async_tasks = []
        for task in tasks:
            async_task = asyncio.create_task(
                self._execute_single_task(task)
            )
            async_tasks.append((task.task_id, async_task))
        
        # Actualizar pico de concurrencia
        current_concurrent = len(async_tasks)
        if current_concurrent > self.metrics["concurrent_peak"]:
            self.metrics["concurrent_peak"] = current_concurrent
        
        # Esperar resultados
        results = {}
        for task_id, async_task in async_tasks:
            try:
                result = await async_task
                results[task_id] = result
                self.completed_tasks[task_id] = result
            except Exception as e:
                self.failed_tasks[task_id] = str(e)
                results[task_id] = None
        
        return results
    
    async def _execute_single_task(self, task: ParallelTask) -> Any:
        """Ejecutar tarea individual con retry y timeout"""
        
        async with self.semaphore:  # Limitar concurrencia
            
            for attempt in range(task.max_retries + 1):
                try:
                    # Ejecutar con timeout
                    result = await asyncio.wait_for(
                        task.coroutine,
                        timeout=task.timeout
                    )
                    
                    self.metrics["tasks_executed"] += 1
                    return result
                    
                except asyncio.TimeoutError:
                    if attempt == task.max_retries:
                        raise TimeoutError(f"Task {task.task_id} timed out after {task.timeout}s")
                    await asyncio.sleep(0.5 * (attempt + 1))  # Exponential backoff
                
                except Exception as e:
                    if attempt == task.max_retries:
                        self.metrics["tasks_failed"] += 1
                        raise e
                    await asyncio.sleep(0.5 * (attempt + 1))
    
    async def execute_cpu_intensive(self, func: Callable, *args, **kwargs) -> Any:
        """Ejecutar función CPU-intensive en thread pool"""
        
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            self.thread_pool,
            lambda: func(*args, **kwargs)
        )
    
    def _update_metrics(self, task_count: int, execution_time: float):
        """Actualizar métricas de ejecución"""
        
        current_avg = self.metrics["average_execution_time"]
        total_executions = self.metrics["tasks_executed"] + self.metrics["tasks_failed"]
        
        if total_executions > 0:
            self.metrics["average_execution_time"] = (
                (current_avg * (total_executions - task_count) + execution_time) 
                / total_executions
            )
    
    def get_metrics(self) -> Dict[str, Any]:
        """Obtener métricas del procesador"""
        
        total_tasks = self.metrics["tasks_executed"] + self.metrics["tasks_failed"]
        success_rate = 0
        if total_tasks > 0:
            success_rate = (self.metrics["tasks_executed"] / total_tasks) * 100
        
        return {
            **self.metrics,
            "success_rate": success_rate,
            "active_tasks": len(self.active_tasks),
            "completed_tasks": len(self.completed_tasks),
            "failed_tasks": len(self.failed_tasks)
        }


class MessageBatchProcessor:
    """Procesador de lotes de mensajes"""
    
    def __init__(self, max_batch_size: int = 10, batch_timeout: float = 0.5):
        self.max_batch_size = max_batch_size
        self.batch_timeout = batch_timeout
        self.message_batches: Dict[str, List[AgentMessage]] = {}
        self.batch_timers: Dict[str, asyncio.Task] = {}
        self.processor = ParallelProcessor(max_concurrent=8)
    
    async def add_message_to_batch(self, agent_id: str, message: AgentMessage, 
                                 process_func: Callable):
        """Agregar mensaje a lote para procesamiento paralelo"""
        
        if agent_id not in self.message_batches:
            self.message_batches[agent_id] = []
        
        self.message_batches[agent_id].append((message, process_func))
        
        # Procesar si alcanza el tamaño máximo
        if len(self.message_batches[agent_id]) >= self.max_batch_size:
            await self._process_batch(agent_id)
        else:
            # Configurar timer para procesamiento automático
            if agent_id not in self.batch_timers:
                self.batch_timers[agent_id] = asyncio.create_task(
                    self._batch_timer(agent_id)
                )
    
    async def _batch_timer(self, agent_id: str):
        """Timer para procesamiento automático del lote"""
        await asyncio.sleep(self.batch_timeout)
        
        if agent_id in self.message_batches and self.message_batches[agent_id]:
            await self._process_batch(agent_id)
        
        # Limpiar timer
        if agent_id in self.batch_timers:
            del self.batch_timers[agent_id]
    
    async def _process_batch(self, agent_id: str):
        """Procesar lote de mensajes en paralelo"""
        
        if agent_id not in self.message_batches:
            return
        
        batch = self.message_batches[agent_id][:]
        self.message_batches[agent_id].clear()
        
        # Cancelar timer si existe
        if agent_id in self.batch_timers:
            self.batch_timers[agent_id].cancel()
            del self.batch_timers[agent_id]
        
        # Crear tareas paralelas
        tasks = []
        for i, (message, process_func) in enumerate(batch):
            task = ParallelTask(
                task_id=f"{agent_id}_msg_{i}",
                coroutine=process_func(message),
                priority=message.priority,
                timeout=15.0
            )
            tasks.append(task)
        
        # Ejecutar en paralelo
        await self.processor.execute_parallel_tasks(tasks)


# Singleton global
parallel_processor = ParallelProcessor()
batch_processor = MessageBatchProcessor()