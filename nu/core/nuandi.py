"""Nu/Nuandi - Autonomous Multi-Agent Orchestrator

Cerebro autónomo del Holobionte basado en:
- Ollama (razonamiento local)
- browser-use (múltiples manos digitales) 
- Python AsyncIO (orquestación paralela)

Version: 0.1.0
License: Apache 2.0
"""

import asyncio
from typing import List, Dict, Optional
import logging
from datetime import datetime
import sys
import os

# Añadir path para imports relativos
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

try:
    from browsers.base_worker import BrowserWorker
    from browsers.freelancer_worker import FreelancerWorker
    from browsers.upwork_worker import UpworkWorker
    from browsers.github_worker import GitHubWorker
    from core.reasoning import OllamaReasoning
    from core.planning import GoalPlanner
except ImportError as e:
    print(f"❌ Error importando módulos: {e}")
    print("Asegúrate de ejecutar desde el directorio raíz del proyecto")
    sys.exit(1)

logging.basicConfig(
    level=logging.INFO,
    format=\'%(asctime)s - %(name)s - %(levelname)s - %(message)s\',
    handlers=[
        logging.FileHandler(\'logs/nu.log\'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


class Nuandi:
    """🧠 Nu/Nuandi - Autonomous Multi-Agent Orchestrator
    
    Cerebro autónomo del Holobionte que orquesta múltiples BrowserWorkers
    en paralelo para maximizar streams de ingreso.
    """
    
    def __init__(self):
        logger.info("🌀 Inicializando Nu/Nuandi...")
        
        # Core components
        self.reasoning = OllamaReasoning()
        self.planner = GoalPlanner()
        
        # BrowserWorkers pool
        self.browsers: List[BrowserWorker] = []
        self.active_tasks: Dict[str, asyncio.Task] = {}
        
        # State
        self.is_running = False
        self.cycle_count = 0
        
        logger.info("✅ Nu/Nuandi inicializado")
    
    async def create_browser_worker(self, domain: str) -> BrowserWorker:
        """Crea un nuevo BrowserWorker especializado"""
        logger.info(f"🌐 Creando BrowserWorker para: {domain}")
        
        workers_map = {
            \'freelancer\': FreelancerWorker,
            \'upwork\': UpworkWorker,
            \'github\': GitHubWorker
        }
        
        worker_class = workers_map.get(domain)
        if not worker_class:
            raise ValueError(f"Unknown domain: {domain}")
        
        worker = worker_class()
        await worker.initialize()
        self.browsers.append(worker)
        
        logger.info(f"✅ BrowserWorker {domain} creado (ID: {worker.worker_id})")
        return worker
    
    async def perceive(self) -> List[Dict]:
        """Fase 1: PERCEPCIÓN - Todos los browsers reportan estado"""
        logger.info(f"👁️ Ciclo {self.cycle_count}: Percibiendo...")
        
        results = await asyncio.gather(
            *[browser.get_status() for browser in self.browsers],
            return_exceptions=True
        )
        
        perceptions = []
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                logger.error(f"❌ Error en browser {i}: {result}")
            else:
                perceptions.append(result)
        
        logger.info(f"✅ Percepción completada: {len(perceptions)} browsers reportaron")
        return perceptions
    
    async def reason(self, perceptions: List[Dict]) -> Dict:
        """Fase 2: RAZONAMIENTO - Ollama interpreta percepciones"""
        logger.info("🧠 Razonando sobre percepciones...")
        
        prompt = f"""
Eres Nu, el cerebro autónomo del Holobionte.

Percepciones actuales:
{perceptions}

Analiza:
1. ¿Qué está pasando en cada dominio?
2. ¿Hay oportunidades de acción?
3. ¿Qué tareas deberían ejecutarse?
4. ¿Hay problemas que resolver?

Responde en formato JSON:
{{
    "analysis": "resumen",
    "opportunities": [],
    "recommended_actions": [],
    "priority": "high/medium/low"
}}
"""
        
        try:
            analysis = await self.reasoning.generate(prompt)
            logger.info("✅ Razonamiento completado")
            return analysis
        except Exception as e:
            logger.error(f"❌ Error en razonamiento: {e}")
            return {
                "analysis": "Error en razonamiento",
                "opportunities": [],
                "recommended_actions": [],
                "priority": "low"
            }
    
    async def plan(self, analysis: Dict) -> List[Dict]:
        """Fase 3: PLANIFICACIÓN - Genera plan multistep"""
        logger.info("📋 Planificando acciones...")
        
        plan = await self.planner.create_plan(
            goal="Maximize income streams",
            context=analysis,
            max_parallel_tasks=3
        )
        
        logger.info(f"✅ Plan creado: {len(plan.get(\'tasks\', []))} tareas")
        return plan.get(\'tasks\', [])
    
    async def execute_parallel(self, tasks: List[Dict]) -> List[Dict]:
        """Fase 4: EJECUCIÓN PARALELA - Múltiples tasks simultáneas"""
        if not tasks:
            logger.info("⚠️ No hay tareas para ejecutar")
            return []
        
        logger.info(f"⚡ Ejecutando {len(tasks)} tareas en paralelo...")
        
        results = await asyncio.gather(
            *[self._assign_task(task) for task in tasks],
            return_exceptions=True
        )
        
        successful = [r for r in results if not isinstance(r, Exception)]
        logger.info(f"✅ Ejecución completada: {len(successful)}/{len(tasks)} exitosas")
        
        return results
    
    async def _assign_task(self, task: Dict) -> Dict:
        """Asigna tarea a browser worker disponible"""
        domain = task.get(\'domain\', \'unknown\')
        worker = self._get_available_worker(domain)
        
        if not worker:
            logger.warning(f"⚠️ No worker disponible para {domain}")
            return {"status": "failed", "reason": "no_worker_available"}
        
        return await worker.execute(task)
    
    def _get_available_worker(self, domain: str) -> Optional[BrowserWorker]:
        """Obtiene worker disponible para un dominio"""
        for browser in self.browsers:
            if browser.domain == domain and not browser.is_busy:
                return browser
        return None
    
    async def orchestrate(self):
        """🔄 Main Loop: Perceive -> Reason -> Plan -> Execute"""
        logger.info("🚀 Iniciando loop de orquestación...")
        self.is_running = True
        
        while self.is_running:
            try:
                self.cycle_count += 1
                logger.info(f"\n{]=60}")
                logger.info(f"🔄 CICLO {self.cycle_count} - {datetime.now()}")
                logger.info(f"{\'=\'*60}")
                
                # 1. Percibir
                perceptions = await self.perceive()
                
                # 2. Razonar
                analysis = await self.reason(perceptions)
                
                # 3. Planificar
                tasks = await self.plan(analysis)
                
                # 4. Ejecutar en paralelo
                if tasks:
                    results = await self.execute_parallel(tasks)
                
                # Loop cada 5 minutos
                logger.info("😴 Esperando 5 minutos hasta próximo ciclo...")
                await asyncio.sleep(300)
                
            except KeyboardInterrupt:
                logger.info("\n⏸️ Interrupción recibida, deteniendo...")
                self.is_running = False
                break
            except Exception as e:
                logger.error(f"❌ Error en ciclo {self.cycle_count}: {e}")
                logger.exception(e)
                await asyncio.sleep(60)
        
        logger.info("🛑 Loop de orquestación detenido")
    
    async def shutdown(self):
        """Cierra todos los browsers y limpia recursos"""
        logger.info("🧹 Cerrando Nu/Nuandi...")
        
        await asyncio.gather(
            *[browser.close() for browser in self.browsers],
            return_exceptions=True
        )
        
        await self.reasoning.close()
        
        logger.info("✅ Nu/Nuandi cerrado correctamente")


async def main():
    """Entry point principal"""
    nu = Nuandi()
    
    try:
        # Crear 3 BrowserWorkers iniciales
        logger.info("🌐 Creando BrowserWorkers iniciales...")
        await nu.create_browser_worker(\'freelancer\')
        await nu.create_browser_worker(\'upwork\')
        await nu.create_browser_worker(\'github\')
        
        logger.info("✅ Todos los workers creados")
        
        # Iniciar loop infinito
        await nu.orchestrate()
        
    except KeyboardInterrupt:
        logger.info("\n⏸️ Deteniendo Nu...")
    except Exception as e:
        logger.error(f"❌ Error fatal: {e}")
        logger.exception(e)
    finally:
        await nu.shutdown()


if __name__ == "__main__":
    print("🌀 Nu/Nuandi - Autonomous Multi-Agent Orchestrator")
    print("=============================================")
    print("")
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Adiós!")
