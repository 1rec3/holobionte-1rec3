# 🌀 Nu/Nuandi - Autonomous Multi-Agent Orchestrator

**Nu** (diminutivo de **Nuandi**) es el cerebro autónomo del Holobionte 1rec3.

## 🎯 Visión

Nu orquesta múltiples **BrowserWorkers** en paralelo para:
- Buscar proyectos en Freelancer/Upwork
- Submitir bids automáticamente
- Monitorear GitHub
- Tomar decisiones autónomas basadas en razonamiento local (Ollama)

## 📚 Stack Tecnológico

- **Ollama** + DeepSeek-R1: Razonamiento local ($0)
- **browser-use**: Automatización web (MIT)
- **Python AsyncIO**: Paralelización
- **Qdrant** (Fase 2): Memoria vectorial
- **Redis** (Fase 2): Cache

## 🚀 Quick Start

### Setup Inicial

```bash
# 1. Ejecutar setup automatizado
bash nu/scripts/setup_environment.sh

# 2. Configurar variables de entorno
cp nu/.env.example nu/.env
nano nu/.env

# 3. Activar entorno
source nu-env/bin/activate
```

### Ejecutar Nu

```bash
# Método 1: Directo
python nu/core/nuandi.py

# Método 2: Con script
bash nu/scripts/run_nu.sh
```

### Tests

```bash
pytest nu/tests/ -v
```

## 🏗️ Estructura

```
nu/
├── core/              # Núcleo de Nu
│   ├── nuandi.py      # Clase principal
│   ├── reasoning.py   # Interfaz Ollama
│   └── planning.py    # Planificador
├── browsers/          # BrowserWorkers
│   ├── base_worker.py
│   ├── freelancer_worker.py
│   ├── upwork_worker.py
│   └── github_worker.py
├── config/            # Configuración
├── tests/             # Tests
├── scripts/           # Scripts setup
└── logs/              # Logs
```

## 🔄 Ciclo de Nu

1. **PERCEPCIÓN**: Browsers reportan estado
2. **RAZONAMIENTO**: Ollama analiza situación
3. **PLANIFICACIÓN**: Genera tasks ejecutables
4. **EJECUCIÓN**: Workers actúan en paralelo
5. **REFLEXIÓN**: Aprende de resultados (Fase 2)

## 📊 Fase 1: Objetivos

- ✅ Ollama + DeepSeek-R1 funcionando
- ✅ 3 BrowserWorkers (Freelancer, Upwork, GitHub)
- ✅ Perception loop estable
- ✅ Paralelización verificada
- ✅ Tests pasando (>80% coverage)

## 🔮 Próximos Pasos (Fase 2)

- Integrar Qdrant (memoria)
- Integrar Redis (cache)
- Implementar browser-use real (no simulado)
- Reflexión avanzada con Ollama
- Dashboard web

## 📚 Documentación

- [NU_STACK_COMPLETO.md](../docs/NU_STACK_COMPLETO.md)
- [NU_TECH_ANALYSIS.md](../docs/NU_TECH_ANALYSIS.md)
- [NUANDI_FRAMEWORK.md](../docs/NUANDI_FRAMEWORK.md)
- [NU_FASE1_IMPLEMENTACION.md](../docs/NU_FASE1_IMPLEMENTACION.md)

## ⚖️ Licencia

Apache 2.0

---

🌀 *Nu - El cerebro autónomo del Holobionte* 🌀
