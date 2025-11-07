# 🚀 NU - FASE 1: Implementación Inicial

**Fecha**: 7 Noviembre 2025  
**Versión**: 1.0  
**Basado en**: NU_STACK_COMPLETO.md, NU_TECH_ANALYSIS.md, NUANDI_FRAMEWORK.md

---

## 📋 **Resumen Ejecutivo**

**Objetivo Fase 1**: Crear un **Proof of Concept (PoC)** funcional de Nu/Nuandi con:
- ✅ Ollama + DeepSeek-R1 (razonamiento local)
- ✅ browser-use (automatización web)
- ✅ Python AsyncIO (orquestación)
- ✅ 3 BrowserWorkers iniciales (Freelancer, Upwork, GitHub)
- ✅ Perception loop básico
- ✅ Testeo de paralelización

**Duración**: 2 semanas  
**Costo**: $0  
**Dependencies**: Python 3.11+, Node.js (opcional), Git

---

## 🎯 **Decisiones Técnicas Finales**

### ✅ **Stack Confirmado**

| Componente | Herramienta | Licencia | Razón |
|------------|-------------|----------|--------|
| **Razonamiento** | Ollama + DeepSeek-R1 | Apache 2.0 | CLI programable, $0, local |
| **BrowserOS** | browser-use | MIT | Compatible IA local, Playwright |
| **Orquestación** | Python AsyncIO | Built-in | Paralelismo nativo |
| **Desarrollo** | LM Studio | Gratuito | GUI para testing (opcional) |
| **Memoria** | Qdrant | Apache 2.0 | Fase 2 |
| **Cache** | Redis | BSD | Fase 2 |

### ❌ **Descartado**

- **AutoGPT**: Requiere OpenAI API ($$), perdió autonomía, no alineado
- **n8n**: Útil pero no esencial para PoC
- **APIs comerciales**: Contradice filosofía $0

---

## 🏗️ **Estructura de Directorios Nu**

```
holobionte-1rec3/
├── nu/                          # Directorio raíz de Nu
│   ├── core/                    # Núcleo de Nu
│   │   ├── __init__.py
│   │   ├── nuandi.py            # Clase principal Nuandi
│   │   ├── reasoning.py         # Interfaz Ollama
│   │   ├── perception.py        # Perception loop
│   │   └── planning.py          # Goal-driven planner
│   │
│   ├── browsers/                # BrowserWorkers
│   │   ├── __init__.py
│   │   ├── base_worker.py       # Clase base BrowserWorker
│   │   ├── freelancer_worker.py # Worker para Freelancer
│   │   ├── upwork_worker.py     # Worker para Upwork
│   │   └── github_worker.py     # Worker para GitHub
│   │
│   ├── memory/                  # Sistema de memoria (Fase 2)
│   │   ├── __init__.py
│   │   ├── qdrant_client.py
│   │   └── redis_cache.py
│   │
│   ├── config/                  # Configuración
│   │   ├── settings.py          # Variables de entorno
│   │   ├── ollama_config.yaml   # Config Ollama
│   │   └── workers_config.yaml  # Config BrowserWorkers
│   │
│   ├── tests/                   # Tests
│   │   ├── test_nuandi.py
│   │   ├── test_browsers.py
│   │   └── test_integration.py
│   │
│   ├── scripts/                 # Scripts de setup
│   │   ├── setup_ollama.sh      # Instala y configura Ollama
│   │   ├── setup_browser_use.sh # Instala browser-use
│   │   ├── setup_environment.sh # Setup completo
│   │   └── run_nu.sh            # Lanza Nu
│   │
│   ├── logs/                    # Logs de ejecución
│   │   └── .gitkeep
│   │
│   ├── requirements.txt         # Dependencias Python
│   ├── pyproject.toml           # Configuración proyecto
│   ├── README.md                # Documentación Nu
│   └── .env.example             # Ejemplo variables de entorno
│
└── docs/
    ├── NU_STACK_COMPLETO.md     # ✅ Ya existe
    ├── NU_TECH_ANALYSIS.md      # ✅ Ya existe
    ├── NUANDI_FRAMEWORK.md      # ✅ Ya existe
    └── NU_FASE1_IMPLEMENTACION.md  # 🆕 Este documento
```

---

## 📦 **Setup Automatizado: Fase 1**

### **1. Requisitos Previos**

```bash
# Sistema operativo
- Linux (Ubuntu 22.04+ recomendado) o macOS
- Windows con WSL2 (alternativa)

# Software base
- Python 3.11+
- Git
- curl
- 8GB RAM mínimo (16GB recomendado)
```

### **2. Script de Setup Completo**

Crearemos `nu/scripts/setup_environment.sh`:

```bash
#!/bin/bash
set -e

echo "🚀 Nu - Setup Fase 1"
echo "=================="

# 1. Crear entorno virtual Python
echo "📦 Creando entorno virtual..."
python3 -m venv nu-env
source nu-env/bin/activate

# 2. Instalar dependencias Python
echo "📥 Instalando dependencias Python..."
pip install --upgrade pip
pip install browser-use playwright pytest pytest-asyncio pyyaml python-dotenv

# 3. Instalar Playwright browsers
echo "🌐 Instalando navegadores Playwright..."
playwright install chromium

# 4. Instalar Ollama
echo "🧠 Instalando Ollama..."
if ! command -v ollama &> /dev/null; then
    curl -fsSL https://ollama.com/install.sh | sh
else
    echo "✅ Ollama ya instalado"
fi

# 5. Descargar modelo DeepSeek-R1
echo "🤖 Descargando DeepSeek-R1..."
ollama pull deepseek-r1:7b  # Versión 7B para empezar

# 6. Iniciar servidor Ollama en background
echo "🔥 Iniciando servidor Ollama..."
ollama serve &
sleep 5

# 7. Verificar instalación
echo "✅ Verificando instalación..."
python -c "import browser_use; print('browser-use:', browser_use.__version__)"
ollama list

echo ""
echo "✨ Setup completado!"
echo "Para activar el entorno: source nu-env/bin/activate"
echo "Para ejecutar Nu: python nu/core/nuandi.py"
```

---

## 🧠 **Implementación Core: nuandi.py**

```python
# nu/core/nuandi.py

import asyncio
from typing import List, Dict
import logging
from datetime import datetime

from browsers.base_worker import BrowserWorker
from browsers.freelancer_worker import FreelancerWorker
from browsers.upwork_worker import UpworkWorker
from browsers.github_worker import GitHubWorker
from reasoning import OllamaReasoning
from perception import PerceptionLoop
from planning import GoalPlanner

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
    """
    🧠 Nu/Nuandi - Autonomous Multi-Agent Orchestrator
    
    Cerebro autónomo del Holobionte basado en:
    - Ollama (razonamiento local)
    - browser-use (múltiples manos digitales)
    - Python AsyncIO (orquestación paralela)
    """
    
    def __init__(self):
        logger.info("🌀 Inicializando Nu/Nuandi...")
        
        # Core components
        self.reasoning = OllamaReasoning(model="deepseek-r1:7b")
        self.perception = PerceptionLoop()
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
        
        Responde en formato JSON con estructura:
        {{
            "analysis": "resumen del análisis",
            "opportunities": [lista de oportunidades],
            "recommended_actions": [lista de acciones],
            "priority": "high/medium/low"
        }}
        """
        
        analysis = await self.reasoning.generate(prompt)
        logger.info(f"✅ Razonamiento completado")
        return analysis
    
    async def plan(self, analysis: Dict) -> List[Dict]:
        """Fase 3: PLANIFICACIÓN - Genera plan multistep"""
        logger.info("📋 Planificando acciones...")
        
        plan = await self.planner.create_plan(
            goal="Maximize income streams",
            context=analysis,
            max_parallel_tasks=3
        )
        
        logger.info(f"✅ Plan creado: {len(plan[\'tasks\'])} tareas")
        return plan[\'tasks\']
    
    async def execute_parallel(self, tasks: List[Dict]) -> List[Dict]:
        """Fase 4: EJECUCIÓN PARALELA - Múltiples tasks simultáneas"""
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
        worker = self._get_available_worker(task[\'domain\'])
        if not worker:
            logger.warning(f"⚠️ No worker disponible para {task[\'domain\']}")
            return {"status": "failed", "reason": "no_worker_available"}
        
        return await worker.execute(task)
    
    def _get_available_worker(self, domain: str) -> BrowserWorker:
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
                logger.info(f"\n{'='*60}")
                logger.info(f"🔄 CICLO {self.cycle_count} - {datetime.now()}")
                logger.info(f"{'='*60}")
                
                # 1. Percibir
                perceptions = await self.perceive()
                
                # 2. Razonar
                analysis = await self.reason(perceptions)
                
                # 3. Planificar
                tasks = await self.plan(analysis)
                
                # 4. Ejecutar en paralelo
                if tasks:
                    results = await self.execute_parallel(tasks)
                    
                    # 5. Reflexionar (Fase 2: guardar en memoria)
                    # await self.memory.store(results)
                
                # Loop cada 5 minutos
                logger.info(f"😴 Esperando 5 minutos hasta próximo ciclo...")
                await asyncio.sleep(300)
                
            except KeyboardInterrupt:
                logger.info("\n⏸️ Interrupción recibida, deteniendo...")
                self.is_running = False
                break
            except Exception as e:
                logger.error(f"❌ Error en ciclo {self.cycle_count}: {e}")
                await asyncio.sleep(60)  # Espera 1 min antes de reintentar
        
        logger.info("🛑 Loop de orquestación detenido")
    
    async def shutdown(self):
        """Cierra todos los browsers y limpia recursos"""
        logger.info("🧹 Cerrando Nu/Nuandi...")
        
        await asyncio.gather(
            *[browser.close() for browser in self.browsers],
            return_exceptions=True
        )
        
        logger.info("✅ Nu/Nuandi cerrado correctamente")


async def main():
    """Entry point principal"""
    nu = Nuandi()
    
    try:
        # Crear 3 BrowserWorkers iniciales
        await nu.create_browser_worker(\'freelancer\')
        await nu.create_browser_worker(\'upwork\')
        await nu.create_browser_worker(\'github\')
        
        # Iniciar loop infinito
        await nu.orchestrate()
        
    except KeyboardInterrupt:
        logger.info("\n⏸️ Deteniendo Nu...")
    finally:
        await nu.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🌐 **BrowserWorkers: Implementación Base**

```python
# nu/browsers/base_worker.py

import asyncio
import uuid
from abc import ABC, abstractmethod
from typing import Dict, Optional
import logging

from browser_use import Agent, BrowserSession

logger = logging.getLogger(__name__)


class BrowserWorker(ABC):
    """
    Clase base para BrowserWorkers especializados.
    
    Cada worker:
    - Actúa en paralelo
    - Toma decisiones locales
    - Reporta a Nuandi
    - Recibe new tasks
    """
    
    def __init__(self, domain: str):
        self.worker_id = str(uuid.uuid4())[:8]
        self.domain = domain
        self.is_busy = False
        self.session: Optional[BrowserSession] = None
        self.agent: Optional[Agent] = None
        self.last_action = None
        self.error_count = 0
        
        logger.info(f"🌐 BrowserWorker creado: {domain} (ID: {self.worker_id})")
    
    async def initialize(self):
        """Inicializa sesión de navegador"""
        logger.info(f"🔧 Inicializando {self.domain} worker...")
        
        self.session = BrowserSession()
        await self.session.start()
        
        logger.info(f"✅ {self.domain} worker inicializado")
    
    async def get_status(self) -> Dict:
        """Reporta estado actual del worker"""
        return {
            "worker_id": self.worker_id,
            "domain": self.domain,
            "is_busy": self.is_busy,
            "last_action": self.last_action,
            "error_count": self.error_count,
            "timestamp": asyncio.get_event_loop().time()
        }
    
    async def execute(self, task: Dict) -> Dict:
        """Ejecuta una tarea específica"""
        logger.info(f"▶️ [{self.domain}] Ejecutando: {task[\'type\']}")
        
        self.is_busy = True
        try:
            result = await self._execute_specific_task(task)
            self.last_action = task[\'type\']
            logger.info(f"✅ [{self.domain}] Tarea completada")
            return result
        except Exception as e:
            self.error_count += 1
            logger.error(f"❌ [{self.domain}] Error: {e}")
            return {"status": "error", "error": str(e)}
        finally:
            self.is_busy = False
    
    @abstractmethod
    async def _execute_specific_task(self, task: Dict) -> Dict:
        """Implementación específica por subclase"""
        pass
    
    async def close(self):
        """Cierra sesión de navegador"""
        if self.session:
            await self.session.close()
            logger.info(f"🔒 {self.domain} worker cerrado")


# nu/browsers/freelancer_worker.py

from .base_worker import BrowserWorker
import logging

logger = logging.getLogger(__name__)


class FreelancerWorker(BrowserWorker):
    """BrowserWorker especializado en Freelancer.com"""
    
    def __init__(self):
        super().__init__(domain="freelancer")
        self.base_url = "https://www.freelancer.com"
    
    async def _execute_specific_task(self, task: Dict) -> Dict:
        """Tareas específicas de Freelancer"""
        task_type = task[\'type\']
        
        if task_type == "search_projects":
            return await self._search_projects(task[\'params\'])
        elif task_type == "submit_bid":
            return await self._submit_bid(task[\'params\'])
        elif task_type == "check_messages":
            return await self._check_messages()
        else:
            raise ValueError(f"Unknown task type: {task_type}")
    
    async def _search_projects(self, params: Dict) -> Dict:
        """Busca proyectos en Freelancer"""
        logger.info(f"🔍 Buscando proyectos con: {params}")
        # TODO: Implementar búsqueda con browser-use
        return {"status": "success", "projects_found": 0}
    
    async def _submit_bid(self, params: Dict) -> Dict:
        """Submite un bid a un proyecto"""
        logger.info(f"💰 Submitting bid: {params}")
        # TODO: Implementar bid submission
        return {"status": "success", "bid_submitted": True}
    
    async def _check_messages(self) -> Dict:
        """Revisa mensajes nuevos"""
        logger.info(f"📧 Checking messages...")
        # TODO: Implementar message checking
        return {"status": "success", "new_messages": 0}


# nu/browsers/upwork_worker.py (similar structure)
# nu/browsers/github_worker.py (similar structure)
```

---

## 🧠 **Módulo de Razonamiento: Ollama**

```python
# nu/core/reasoning.py

import aiohttp
import json
import logging
from typing import Dict, Optional

logger = logging.getLogger(__name__)


class OllamaReasoning:
    """
    Interfaz con Ollama para razonamiento local.
    
    Usa DeepSeek-R1 para:
    - Análisis de percepciones
    - Toma de decisiones
    - Generación de planes
    - Reflexión sobre resultados
    """
    
    def __init__(self, model: str = "deepseek-r1:7b", base_url: str = "http://localhost:11434"):
        self.model = model
        self.base_url = base_url
        self.session: Optional[aiohttp.ClientSession] = None
        
        logger.info(f"🧠 OllamaReasoning inicializado: {model}")
    
    async def _ensure_session(self):
        """Asegura que existe una sesión HTTP"""
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()
    
    async def generate(self, prompt: str, stream: bool = False) -> Dict:
        """
        Genera respuesta con Ollama.
        
        Args:
            prompt: El prompt para el modelo
            stream: Si debe hacer streaming de la respuesta
        
        Returns:
            Dict con la respuesta del modelo
        """
        await self._ensure_session()
        
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": stream,
            "format": "json"  # Forzar respuesta JSON
        }
        
        logger.info(f"🤖 Generando con {self.model}...")
        
        try:
            async with self.session.post(url, json=payload) as response:
                if response.status == 200:
                    result = await response.json()
                    logger.info("✅ Generación completada")
                    
                    # Parsear respuesta JSON del modelo
                    try:
                        return json.loads(result[\'response\'])
                    except json.JSONDecodeError:
                        # Si no es JSON válido, retornar texto plano
                        return {"raw_response": result[\'response\']}
                else:
                    error = await response.text()
                    logger.error(f"❌ Error Ollama: {error}")
                    raise Exception(f"Ollama error: {error}")
                    
        except Exception as e:
            logger.error(f"❌ Error en generate(): {e}")
            raise
    
    async def close(self):
        """Cierra la sesión HTTP"""
        if self.session and not self.session.closed:
            await self.session.close()
            logger.info("🔒 OllamaReasoning sesión cerrada")
```

---

## 📋 **Módulo de Planificación**

```python
# nu/core/planning.py

import logging
from typing import Dict, List

logger = logging.getLogger(__name__)


class GoalPlanner:
    """
    Planificador goal-driven para Nu.
    
    Convierte análisis en tasks ejecutables.
    """
    
    def __init__(self):
        logger.info("📋 GoalPlanner inicializado")
    
    async def create_plan(self, goal: str, context: Dict, max_parallel_tasks: int = 3) -> Dict:
        """
        Crea un plan de acción basado en el goal y contexto.
        
        Args:
            goal: Objetivo principal (ej: "Maximize income streams")
            context: Análisis del estado actual
            max_parallel_tasks: Máximo de tareas paralelas
        
        Returns:
            Dict con plan estructurado
        """
        logger.info(f"📝 Creando plan para goal: {goal}")
        
        # TODO: Implementar lógica sofisticada de planning
        # Por ahora, plan básico hardcoded
        
        plan = {
            "goal": goal,
            "timestamp": asyncio.get_event_loop().time(),
            "tasks": [
                {
                    "type": "search_projects",
                    "domain": "freelancer",
                    "params": {"keywords": ["python", "automation"]},
                    "priority": "high"
                },
                {
                    "type": "check_messages",
                    "domain": "upwork",
                    "params": {},
                    "priority": "medium"
                },
                {
                    "type": "monitor_issues",
                    "domain": "github",
                    "params": {"repo": "1rec3/holobionte-1rec3"},
                    "priority": "low"
                }
            ][:max_parallel_tasks]
        }
        
        logger.info(f"✅ Plan creado con {len(plan[\'tasks\'])} tareas")
        return plan
```

---

## 🧪 **Tests Básicos**

```python
# nu/tests/test_nuandi.py

import pytest
import asyncio
from nu.core.nuandi import Nuandi
from nu.core.reasoning import OllamaReasoning


@pytest.mark.asyncio
async def test_nuandi_initialization():
    """Test que Nu se inicializa correctamente"""
    nu = Nuandi()
    assert nu is not None
    assert nu.cycle_count == 0
    assert len(nu.browsers) == 0


@pytest.mark.asyncio
async def test_create_browser_worker():
    """Test creación de BrowserWorker"""
    nu = Nuandi()
    worker = await nu.create_browser_worker(\'freelancer\')
    
    assert worker is not None
    assert worker.domain == \'freelancer\'
    assert len(nu.browsers) == 1
    
    await nu.shutdown()


@pytest.mark.asyncio
async def test_ollama_reasoning():
    """Test razonamiento con Ollama"""
    reasoning = OllamaReasoning()
    
    response = await reasoning.generate("Say \'test\' in JSON format")
    assert response is not None
    
    await reasoning.close()


@pytest.mark.asyncio
async def test_perception_cycle():
    """Test ciclo de percepción"""
    nu = Nuandi()
    await nu.create_browser_worker(\'freelancer\')
    
    perceptions = await nu.perceive()
    assert len(perceptions) == 1
    assert perceptions[0][\'domain\'] == \'freelancer\'
    
    await nu.shutdown()
```

---

## 📝 **Archivos de Configuración**

### **requirements.txt**

```txt
# Nu - Dependencias Python

# Core
python>=3.11

# Browser automation
browser-use>=0.1.0
playwright>=1.40.0

# HTTP client
aiohttp>=3.9.0

# Configuration
pyyaml>=6.0
python-dotenv>=1.0.0

# Testing
pytest>=7.4.0
pytest-asyncio>=0.21.0

# Logging
coloredlogs>=15.0

# Memory (Fase 2)
# qdrant-client>=1.7.0
# redis>=5.0.0
```

### **.env.example**

```bash
# Nu - Variables de Entorno

# Ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=deepseek-r1:7b

# BrowserWorkers
FREELANCER_USERNAME=
FREELANCER_PASSWORD=
UPWORK_USERNAME=
UPWORK_PASSWORD=
GITHUB_TOKEN=

# Configuración Nu
NU_CYCLE_INTERVAL=300  # 5 minutos
NU_MAX_PARALLEL_TASKS=3
NU_LOG_LEVEL=INFO

# Fase 2: Memoria
# QDRANT_URL=http://localhost:6333
# REDIS_URL=redis://localhost:6379
```

### **pyproject.toml**

```toml
[tool.poetry]
name = "nu-nuandi"
version = "0.1.0"
description = "Nu - Autonomous Multi-Agent Orchestrator"
authors = ["Holobionte 1rec3"]
license = "Apache-2.0"
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.11"
browser-use = "^0.1.0"
playwright = "^1.40.0"
aiohttp = "^3.9.0"
pyyaml = "^6.0"
python-dotenv = "^1.0.0"

[tool.poetry.dev-dependencies]
pytest = "^7.4.0"
pytest-asyncio = "^0.21.0"
black = "^23.0.0"
flake8 = "^6.0.0"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

---

## 🚀 **Instrucciones de Ejecución**

### **Setup Inicial**

```bash
# 1. Clonar repositorio y navegar a directorio Nu
cd holobionte-1rec3/nu

# 2. Ejecutar setup automatizado
bash scripts/setup_environment.sh

# 3. Configurar variables de entorno
cp .env.example .env
nano .env  # Editar con tus credenciales

# 4. Activar entorno virtual
source nu-env/bin/activate

# 5. Verificar instalación
python -c "import browser_use; print(\'✅ browser-use instalado\')"
ollama list  # Verificar modelos disponibles
```

### **Ejecutar Nu**

```bash
# Método 1: Directo
python nu/core/nuandi.py

# Método 2: Con script
bash nu/scripts/run_nu.sh

# Método 3: Con logs verbose
NU_LOG_LEVEL=DEBUG python nu/core/nuandi.py
```

### **Ejecutar Tests**

```bash
# Todos los tests
pytest nu/tests/

# Test específico
pytest nu/tests/test_nuandi.py::test_nuandi_initialization

# Con coverage
pytest --cov=nu nu/tests/
```

---

## 📊 **Métricas de Éxito Fase 1**

### **Criterios de Aceptación**

- ✅ **Setup automatizado funcional** (< 10 minutos)
- ✅ **Ollama corriendo localmente** con DeepSeek-R1
- ✅ **3 BrowserWorkers** (Freelancer, Upwork, GitHub) operacionales
- ✅ **Perception loop** ejecutándose sin crashes
- ✅ **Paralelización verificada** (3 tasks simultáneas)
- ✅ **Tests unitarios pasando** (>80% coverage core)
- ✅ **Logs estructurados** (archivo + consola)

### **Métricas Cuantitativas**

| Métrica | Target Fase 1 | Medición |
|---------|---------------|----------|
| Setup time | < 10 min | Timer manual |
| Cycle time | < 30 seg | Logs timestamps |
| Workers concurrentes | 3 | Count activos |
| Uptime continuo | > 1 hora | Sin crashes |
| Memory usage | < 2GB RAM | `htop` |
| CPU usage | < 50% | `htop` |

---

## 🔮 **Próximos Pasos (Fase 2)**

1. **Memoria Persistente**
   - Integrar Qdrant para embeddings
   - Redis para cache de sesiones
   - Git para contexto versionado

2. **Reflexión Avanzada**
   - Post-action analysis con Ollama
   - Learning from mistakes
   - Strategy adjustment

3. **Interfaz Web**
   - Dashboard de monitoreo
   - Control manual de workers
   - Visualización de decisiones

4. **Optimización**
   - Fine-tuning de prompts
   - Model distillation
   - Performance profiling

5. **Producción**
   - Docker Compose setup
   - systemd service
   - Monitoring con Prometheus/Grafana

---

## 📚 **Referencias**

- **Documentos base**: 
  - `docs/NU_STACK_COMPLETO.md`
  - `docs/NU_TECH_ANALYSIS.md`
  - `docs/NUANDI_FRAMEWORK.md`

- **Herramientas**:
  - [Ollama](https://ollama.com/)
  - [browser-use](https://github.com/browser-use/browser-use)
  - [Playwright](https://playwright.dev/)
  - [DeepSeek-R1](https://huggingface.co/deepseek-ai)

- **Filosofía**:
  - `CODEX.md` - Principios del Holobionte
  - `MANIFEST.md` - Misión y valores
  - `DECISIONES.md` - Decisiones técnicas

---

## ✅ **Checklist de Implementación**

### **Pre-requisitos**
- [ ] Linux/macOS con Python 3.11+
- [ ] 8GB RAM mínimo
- [ ] Git configurado
- [ ] Credenciales Freelancer/Upwork/GitHub

### **Setup**
- [ ] Ejecutar `setup_environment.sh`
- [ ] Verificar Ollama funcionando
- [ ] Descargar DeepSeek-R1
- [ ] Configurar `.env`
- [ ] Instalar dependencias Python

### **Desarrollo**
- [ ] Implementar `nuandi.py` core
- [ ] Implementar 3 BrowserWorkers
- [ ] Implementar `reasoning.py`
- [ ] Implementar `planning.py`
- [ ] Crear tests unitarios

### **Testing**
- [ ] Test inicialización Nu
- [ ] Test creación workers
- [ ] Test Ollama integration
- [ ] Test perception cycle
- [ ] Test paralelización
- [ ] Test 1 hora uptime

### **Documentación**
- [ ] README.md en `/nu`
- [ ] Comentarios en código
- [ ] Ejemplos de uso
- [ ] Troubleshooting guide

---

**Versión**: 1.0  
**Fecha**: 7 Noviembre 2025  
**Autor**: Holobionte 1rec3  
**Licencia**: Apache 2.0  
**Estado**: 🚧 En Implementación

🌀 *Nu - El cerebro autónomo del Holobionte* 🌀
