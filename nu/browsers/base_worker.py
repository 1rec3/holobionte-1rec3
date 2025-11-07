"""Clase base para BrowserWorkers especializados.

Cada worker:
- Actúa en paralelo
- Toma decisiones locales
- Reporta a Nuandi  
- Recibe new tasks
"""

import asyncio
import uuid
import time
from abc import ABC, abstractmethod
from typing import Dict, Optional
import logging

logger = logging.getLogger(__name__)


class BrowserWorker(ABC):
    """Clase base abstracta para BrowserWorkers"""
    
    def __init__(self, domain: str):
        self.worker_id = str(uuid.uuid4())[:8]
        self.domain = domain
        self.is_busy = False
        self.last_action = None
        self.error_count = 0
        self.created_at = time.time()
        
        logger.info(f"🌐 BrowserWorker creado: {domain} (ID: {self.worker_id})")
    
    async def initialize(self):
        """Inicializa recursos del worker"""
        logger.info(f"🔧 Inicializando {self.domain} worker...")
        # En Fase 1, inicialización mínima
        # En Fase 2+: inicializar browser-use session
        logger.info(f"✅ {self.domain} worker inicializado")
    
    async def get_status(self) -> Dict:
        """Reporta estado actual del worker"""
        return {
            "worker_id": self.worker_id,
            "domain": self.domain,
            "is_busy": self.is_busy,
            "last_action": self.last_action,
            "error_count": self.error_count,
            "uptime": time.time() - self.created_at,
            "timestamp": time.time()
        }
    
    async def execute(self, task: Dict) -> Dict:
        """Ejecuta una tarea específica"""
        task_type = task.get(\'type\', \'unknown\')
        logger.info(f"▶️ [{self.domain}] Ejecutando: {task_type}")
        
        self.is_busy = True
        try:
            result = await self._execute_specific_task(task)
            self.last_action = task_type
            logger.info(f"✅ [{self.domain}] Tarea completada")
            return result
        except Exception as e:
            self.error_count += 1
            logger.error(f"❌ [{self.domain}] Error: {e}")
            return {"status": "error", "error": str(e), "task": task_type}
        finally:
            self.is_busy = False
    
    @abstractmethod
    async def _execute_specific_task(self, task: Dict) -> Dict:
        """Implementación específica por subclase"""
        pass
    
    async def close(self):
        """Cierra recursos del worker"""
        logger.info(f"🔒 {self.domain} worker cerrado")
