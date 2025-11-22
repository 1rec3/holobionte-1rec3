# 🎯 ORQUESTACIÓN COMET - INTEGRACIÓN VÍA BROWSER

> Plan de orquestación del Holobionte 1rec3 ejecutado por Comet (Perplexity)
> Todo vía navegador, sin APIs externas
> Fecha: 22 Nov 2025, 9:00 PM WET

## 🌐 CONTEXTO

Este documento describe cómo **Comet** (y en el futuro **NuANDI con browserOS**) orquesta la coordinación de todos los simbiontes LLM del Holobionte 1rec3 **exclusivamente a través del navegador**, sin depender de APIs REST tradicionales.

## 🏗️ ARQUITECTURA BROWSER-BASED

### Principio Fundamental
**"Todo lo que se puede hacer en un navegador, se orquesta en el navegador"**

### Componentes de Integración:

```
┌─────────────────────────────────────────────────────┐
│           ORQUESTADOR (Comet/NuANDI)                │
│                                                       │
│  ┌──────────────────────────────────────────────┐  │
│  │  Browser Engine (Chrome/Edge/Firefox)        │  │
│  │  - Tabs múltiples                            │  │
│  │  - LocalStorage / IndexedDB                  │  │
│  │  - Window messaging                          │  │
│  │  - Browser extensions                        │  │
│  └──────────────────────────────────────────────┘  │
│                                                       │
│  ┌──────────────────────────────────────────────┐  │
│  │  Repository Integration Layer                │  │
│  │  - GitHub Pages                              │  │
│  │  - Raw GitHub URLs                           │  │
│  │  - Gists compartidos                         │  │
│  │  - Archivos locales sincronizados            │  │
│  └──────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────┐
│             SIMBIONTES LLM (11+)                    │
│                                                       │
│  Cada simbionte expone su repositorio interno:      │
│  - Vía localStorage (clave estándar)                 │
│  - Vía IndexedDB (estructura JSON)                   │
│  - Vía elementos DOM (data attributes)               │
│  - Vía archivos descargables (JSON/MD)               │
└─────────────────────────────────────────────────────┘
```

## 📋 CONTRATO DE INTEGRACIÓN

### Cada simbionte LLM debe exponer:

#### 1. **Estado Actual** (localStorage)
```javascript
// Clave estándar en localStorage
window.localStorage.setItem('holobionte:simbionte:estado', JSON.stringify({
  nombre: "gemini",
  email: "gemini@1rec3.com",
  rol: "Workspace manager",
  estado: "activo",
  ultima_actualizacion: "2025-11-22T21:00:00Z",
  capacidades_disponibles: ["docs", "sheets", "calendar"],
  tareas_activas: 3,
  repositorio_url: "https://github.com/1rec3/holobionte-1rec3"
}));
```

#### 2. **Capacidades** (archivo MD accesible)
Cada simbionte tiene un archivo `capacidades.md` en:
```
simbiontes/[nombre]/capacidades.md
```

Accesible vía:
- https://raw.githubusercontent.com/1rec3/holobionte-1rec3/main/simbiontes/[nombre]/capacidades.md
- O cargado en la UI del simbionte

#### 3. **Logros** (actualización continua)
```
simbiontes/[nombre]/logros.md
```

#### 4. **Fronteras** (limitaciones conocidas)
```
simbiontes/[nombre]/fronteras.md
```

## 🔄 PROTOCOLO DE SINCRONIZACIÓN

### Método 1: Consulta Directa al Repositorio
El orquestador (Comet) accede al repositorio GitHub directamente:

```javascript
// Comet ejecuta en el browser:
const capacidades = await fetch(
  'https://raw.githubusercontent.com/1rec3/holobionte-1rec3/main/simbiontes/gemini/capacidades.md'
).then(r => r.text());
```

### Método 2: LocalStorage Cross-Tab
Simbiontes en diferentes tabs se comunican:

```javascript
// Simbionte A escribe
localStorage.setItem('holobionte:mensaje:gemini-to-claude', JSON.stringify({
  de: 'gemini@1rec3.com',
  para: 'claude@1rec3.com',
  mensaje: 'Necesito que revises el documento X',
  timestamp: Date.now()
}));

// Simbionte B lee (polling o storage event)
window.addEventListener('storage', (e) => {
  if (e.key.startsWith('holobionte:mensaje:')) {
    // Procesar mensaje
  }
});
```

### Método 3: Archivos Compartidos (Google Drive / Dropbox)
Para datos más grandes:
- Cada simbionte escribe a una carpeta compartida
- URL pública o con token de acceso
- Formato JSON o Markdown

### Método 4: GitHub Issues/Comments
Comunicación asíncrona persistente:
- Cada simbionte comenta en Issues relevantes
- El orquestador lee y coordina respuestas
- Historial completo y auditable

## 🚀 PLAN DE ACCIÓN INMEDIATO

### FASE 1: ESTRUCTURA BASE (HOY 22 Nov - 9-10 PM)

#### ✅ Tarea 1.1: Crear directorios para 11 simbiontes core
```
simbiontes/
├── neral/          # Orquestador (Comet/PPLX)
├── gemini/         # Workspace manager
├── claude/         # Research & docs
├── chatgpt/        # Strategy
├── mistral/        # Multilingual
├── deepseek/       # Technical
├── grok/           # Trends
├── copilot/        # Code integration
├── perplexity/     # Web research
├── poe/            # Multi-model
└── huggingchat/    # Open source
```

#### ✅ Tarea 1.2: Crear archivos base para cada simbionte
Para CADA simbionte:
```
simbiontes/[nombre]/
├── capacidades.md
├── logros.md
├── fronteras.md
└── config.yaml
```

#### ✅ Tarea 1.3: Crear README de orquestación
```
simbiontes/ORQUESTACION.md (este archivo)
```

### FASE 2: INTEGRACIÓN BÁSICA (HOY 22 Nov - 10-11 PM)

#### 🔄 Tarea 2.1: Configurar Gemini
1. Abrir https://gemini.google.com/app
2. En Custom Instructions, añadir:
   ```
   Contexto Holobionte 1rec3:
   - Repositorio: https://github.com/1rec3/holobionte-1rec3
   - Tu perfil: simbiontes/gemini/
   - Issue activo: #17 (Estructura Simbiontes)
   - Orquestador: Neral (Comet)
   - Email: gemini@1rec3.com
   
   Antes de cada respuesta:
   1. Consulta tu archivo capacidades.md
   2. Actualiza logros.md si completaste algo
   3. Coordina con Neral si necesitas ayuda
   ```

#### 🔄 Tarea 2.2: Configurar Claude
1. Abrir https://claude.ai/new
2. Crear Project "Holobionte 1rec3"
3. Añadir archivos de contexto:
   - README.md del repo
   - Issue #17
   - simbiontes/claude/capacidades.md
4. Configurar Project Instructions similar a Gemini

#### 🔄 Tarea 2.3: Configurar ChatGPT
1. Abrir https://chatgpt.com/
2. En Settings > Personalization > Custom Instructions
3. Añadir contexto del holobionte
4. Activar Memory para recordar interacciones

### FASE 3: PRUEBA DE COORDINACIÓN (23 Nov mañana)

#### 🧪 Test de Orquestación 1: "Crear CV Backend Python"

**Flujo:**
```
Comet (Orquestador)
  ↓ solicita a
Perplexity → Investiga 5 empresas remote-first EU
  ↓ pasa resultados a  
Claude → Analiza req comunes y crea estructura CV
  ↓ pasa estructura a
ChatGPT → Genera CV optimizado ATS
  ↓ revisa y formatea
Gemini → Crea Google Doc con formato final
  ↓ notifica a
Comet → Valida resultado y cierra task
```

**Implementación:**
1. Comet abre tab de Perplexity
2. Escribe prompt: "Investiga 5 empresas..."
3. Copia resultado
4. Abre tab de Claude  
5. Escribe prompt con resultado de Perplexity
6. Continúa cadena...
7. Al final, documenta en:
   - simbiontes/neral/logros.md
   - Cada simbionte actualiza su logros.md

## 📧 REGISTRO DE EMAILS ASIGNADOS

| Simbionte | Email | Estado |
|-----------|-------|--------|
| Neral | neral@1rec3.com | ✅ Activo (Orquestador) |
| Gemini | gemini@1rec3.com | 🔄 Configurando |
| Claude | claude@1rec3.com | 🔄 Configurando |
| ChatGPT | chatgpt@1rec3.com | 🔄 Configurando |
| Mistral | mistral@1rec3.com | ⏳ Pendiente |
| DeepSeek | deepseek@1rec3.com | ⏳ Pendiente |
| Grok | grok@1rec3.com | ⏳ Pendiente |
| Copilot | copilot@1rec3.com | ⏳ Pendiente |
| Perplexity | perplexity@1rec3.com | ✅ Activo |
| Poe | poe@1rec3.com | ⏳ Pendiente |
| HuggingChat | huggingchat@1rec3.com | ⏳ Pendiente |

## 🔮 EXPANSIÓN FUTURA

### Categorías Adicionales (Fase 4+):

#### Automation Bots
- n8n@1rec3.com
- make@1rec3.com  
- zapier@1rec3.com

#### AI Agents  
- manus@1rec3.com
- autogpt@1rec3.com

#### Dev Tools
- cursor@1rec3.com
- v0@1rec3.com

#### Research Tools
- elicit@1rec3.com
- consensus@1rec3.com

## 📊 MÉTRICAS DE ÉXITO

### KPIs de Orquestación:
1. **Tiempo de coordinación**: < 5 min por tarea multi-simbionte
2. **Tasa de éxito**: > 80% tareas completadas correctamente
3. **Documentación**: 100% tareas documentadas en logros.md
4. **Sincronización**: Todos los simbiontes actualizados < 24h

## 🎯 ENTREGABLES HOY (22 Nov 9-11 PM)

- [x] Documento de orquestación (este archivo)
- [ ] 11 directorios de simbiontes creados
- [ ] Archivos base (capacidades, logros, fronteras, config) para 11 simbiontes
- [ ] Gemini configurado con contexto del repo
- [ ] Claude configurado con contexto del repo
- [ ] ChatGPT configurado con contexto del repo
- [ ] Primera prueba de coordinación documentada

## 🔗 REFERENCIAS

- Issue #17: https://github.com/1rec3/holobionte-1rec3/issues/17
- Issue #16: https://github.com/1rec3/holobionte-1rec3/issues/16
- Repositorio: https://github.com/1rec3/holobionte-1rec3
- Simbiontes README: simbiontes/README.md

---

**🌀 Orquestación: Uno coordina muchos | Muchos forman uno 🌀**

*Documento vivo - Actualizar conforme evoluciona la orquestación*
