"""Tests para Nu/Nuandi - Fase 1"""

import pytest
import asyncio
import sys
import os

# Añadir path para imports
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from core.nuandi import Nuandi
from core.reasoning import OllamaReasoning
from browsers.freelancer_worker import FreelancerWorker


@pytest.mark.asyncio
async def test_nuandi_initialization():
    """Test que Nu se inicializa correctamente"""
    nu = Nuandi()
    assert nu is not None
    assert nu.cycle_count == 0
    assert len(nu.browsers) == 0
    assert nu.is_running == False


@pytest.mark.asyncio
async def test_create_browser_worker():
    """Test creación de BrowserWorker"""
    nu = Nuandi()
    worker = await nu.create_browser_worker(\'freelancer\')
    
    assert worker is not None
    assert worker.domain == \'freelancer\'
    assert len(nu.browsers) == 1
    assert worker.is_busy == False
    
    await nu.shutdown()


@pytest.mark.asyncio
async def test_multiple_workers():
    """Test creación de múltiples workers"""
    nu = Nuandi()
    
    await nu.create_browser_worker(\'freelancer\')
    await nu.create_browser_worker(\'upwork\')
    await nu.create_browser_worker(\'github\')
    
    assert len(nu.browsers) == 3
    domains = [w.domain for w in nu.browsers]
    assert \'freelancer\' in domains
    assert \'upwork\' in domains
    assert \'github\' in domains
    
    await nu.shutdown()


@pytest.mark.asyncio
async def test_perception_cycle():
    """Test ciclo de percepción"""
    nu = Nuandi()
    await nu.create_browser_worker(\'freelancer\')
    
    perceptions = await nu.perceive()
    assert len(perceptions) == 1
    assert perceptions[0][\'domain\'] == \'freelancer\'
    assert \'worker_id\' in perceptions[0]
    
    await nu.shutdown()


@pytest.mark.asyncio
async def test_worker_task_execution():
    """Test ejecución de tarea en worker"""
    worker = FreelancerWorker()
    await worker.initialize()
    
    task = {
        \'type\': \'search_projects\',
        \'params\': {\'keywords\': [\'python\']}
    }
    
    result = await worker.execute(task)
    assert result[\'status\'] == \'success\'
    assert worker.last_action == \'search_projects\'
    
    await worker.close()


@pytest.mark.asyncio
async def test_parallel_execution():
    """Test ejecución paralela de tareas"""
    nu = Nuandi()
    
    await nu.create_browser_worker(\'freelancer\')
    await nu.create_browser_worker(\'upwork\')
    await nu.create_browser_worker(\'github\')
    
    tasks = [
        {\'type\': \'search_projects\', \'domain\': \'freelancer\', \'params\': {}},
        {\'type\': \'check_messages\', \'domain\': \'upwork\', \'params\': {}},
        {\'type\': \'monitor_issues\', \'domain\': \'github\', \'params\': {\'repo\': \'test\'}}
    ]
    
    results = await nu.execute_parallel(tasks)
    assert len(results) == 3
    
    await nu.shutdown()


if __name__ == "__main__":
    pytest.main(["-v", __file__])
