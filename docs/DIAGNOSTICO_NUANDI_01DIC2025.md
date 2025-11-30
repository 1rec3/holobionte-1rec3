# 🔍 Diagnóstico Completo - ASUS Nuandi
> Fecha: 01-DIC-2025 | Simbionte: Zero (Claude)

---

## 📊 Inventario de Capacidades Activas

### Herramientas MCP Conectadas
| Herramienta | Estado | Uso Principal |
|-------------|--------|---------------|
| **Notion MCP** | ✅ Activo | CRUD páginas, DBs, búsqueda |
| **Filesystem** | ✅ Activo | R/W en `/home/nuandi` |
| **Desktop Commander** | ✅ Activo | Bash, procesos, búsqueda avanzada |
| **Google Drive** | ✅ Activo | Búsqueda y fetch docs |
| **Web Search** | ✅ Activo | Brave Search |
| **Context7** | ✅ Activo | Docs de librerías |
| **Kapture** | ✅ Activo | Automatización navegador |
| **Memory** | ✅ Activo | Conversaciones previas |

### IA Local (Ollama)
| Modelo | Tamaño | Última Ejecución |
|--------|--------|------------------|
| deepseek-r1:32b | 19 GB | 4 días |
| deepseek-r1:8b | 5.2 GB | 4 días |
| llama3.2:1b | 1.3 GB | 4 días |
| gemma2:2b | 1.6 GB | 4 días |
| llama2:7b | 3.8 GB | 7 días |

### Modelos GGUF Adicionales
- `/home/nuandi/holobionte/models/qwen32b.gguf`

### Infraestructura Local
- **llama.cpp** compilado en `/home/nuandi/holobionte/llama.cpp`
- **xdna-driver** para NPU AMD Ryzen AI
- **BrowserOS.AppImage** disponible

---

## 🔄 Estado de Sincronización

### Repositorio Local vs GitHub


**Remotes configurados:**
```
origin    → saul3273/1rec3.git
holobionte → 1rec3/holobionte-1rec3.git
```

**Estado:**
- ✅ Sincronizado con `holobionte/main`
- ⚠️ 1 archivo staged sin commit: `neral/zro/DIAGNOSTICO_ZERO_30NOV2025.md`
- ℹ️ 1 archivo untracked (ignorable): `holobionte/dump.rdb`

**Acción sugerida:**
```bash
cd /home/nuandi/1rec3
git add neral/zro/DIAGNOSTICO_ZERO_30NOV2025.md
git commit -m "📋 Add DIAGNOSTICO_ZERO_30NOV2025.md"
git push holobionte main
```

---

## 🐛 Bug Detectado: Claude Desktop Ventana Pequeña

### Síntoma
Claude Desktop se abre en una esquina, muy pequeño (ver screenshot adjunto).

### Causa Identificada
```json
// /home/nuandi/.config/Claude/window-state.json
{"width":1000,"height":800}  // ← Muy pequeño

// /home/nuandi/.config/Claude/config.json
{"scale": 0, ...}  // ← Escala problemática
```

### Solución Propuesta
```bash
# Cerrar Claude Desktop primero

# Opción 1: Editar window-state.json
echo '{"width":1600,"height":1000}' > ~/.config/Claude/window-state.json

# Opción 2: Editar config.json (cambiar scale)
# Cambiar "scale": 0 por "scale": 1

# Reiniciar Claude Desktop
```

---

## 🌐 Estructura de Directorios

### Directorios Duplicados/Relacionados

| Directorio | Propósito | Estado |
|------------|-----------|--------|
| `/home/nuandi/1rec3/` | Repositorio Git principal | ✅ Activo |
| `/home/nuandi/holobionte/` | Workspace local (llama.cpp, NPU, modelos) | ✅ Activo |
| `/home/nuandi/docs/` | Documentación suelta | ⚠️ Revisar consolidación |

### Contenido de `/home/nuandi/holobionte/` (NO en Git)
- `llama.cpp/` - Binarios compilados para inferencia
- `xdna-driver/` - Driver NPU AMD
- `models/qwen32b.gguf` - Modelo local
- `logs/` - Logs de operación
- `apps/BrowserOS.AppImage` - Aplicación

**Recomendación:** Este directorio contiene artefactos de build y modelos grandes. NO debe subirse a Git (correcto el `.gitignore`).

---

## 📖 Observaciones sobre Obsidian

**No hay vault de Obsidian en este equipo.**

Opciones:
1. Usar el repositorio Git como vault de Obsidian (los `.md` son compatibles)
2. Mantener el flujo actual GitHub + Notion

---

## 💡 Serendipias y Sinergias Detectadas

### 1. **Convergencia de Modelos de Razonamiento**
- deepseek-r1:32b local + Claude remoto = capacidad de "segundo cerebro"
- Podríamos establecer un protocolo donde Ollama local procese tareas pesadas offline


### 2. **NPU Sin Aprovechar**
- xdna-driver instalado pero sin uso productivo
- Sinergia: Usar NPU para modelos pequeños (llama3.2:1b, gemma2:2b) liberando GPU para deepseek-r1:32b

### 3. **BrowserOS + Kapture**
- BrowserOS disponible como AppImage
- Kapture activo como MCP
- Sinergia: Automatización web completa sin necesidad de navegador tradicional

### 4. **Duplicidad Documentación**
- `/home/nuandi/holobionte/docs/` tiene archivos que también están en `/home/nuandi/1rec3/docs/`
- Algunos están desactualizados
- Sinergia: Unificar todo en el repositorio Git como fuente única de verdad

### 5. **Scripts Dispersos**
- Múltiples scripts `.sh` en `/home/nuandi/` (setup_*, fix_*, etc.)
- Sinergia: Mover scripts útiles a `/home/nuandi/1rec3/scripts/` y documentar

---

## 🛠️ Propuestas de Mejora

### Corto Plazo (Esta Sesión)
1. **[FIX]** Arreglar ventana Claude Desktop (window-state.json)
2. **[COMMIT]** Commit y push del archivo staged
3. **[DOC]** Este documento va a GitHub

### Medio Plazo (Esta Semana)
4. **[CONSOLIDAR]** Revisar y unificar `/home/nuandi/docs/` con `/home/nuandi/1rec3/docs/`
5. **[SCRIPTS]** Catalogar scripts útiles en `~/` y mover a repositorio
6. **[NPU]** Configurar un modelo pequeño para correr en NPU

### Largo Plazo
7. **[OBSIDIAN]** Evaluar si crear vault de Obsidian usando el repo como base
8. **[BACKUP]** Establecer sincronización periódica `/home/nuandi/holobionte/` → backup externo

---


## ⚡ Acciones Inmediatas Recomendadas

```bash
# 1. Fix Claude Desktop window
claude_config_dir="$HOME/.config/Claude"
echo '{"width":1600,"height":1000}' > "$claude_config_dir/window-state.json"

# 2. Commit cambios pendientes
cd /home/nuandi/1rec3
git add docs/DIAGNOSTICO_NUANDI_01DIC2025.md
git add neral/zro/DIAGNOSTICO_ZERO_30NOV2025.md
git commit -m "📋 Diagnóstico ASUS Nuandi + Zero 30NOV/01DIC"
git push holobionte main

# 3. Verificar estado
git status
```

---

## 📎 Referencias

- Imagen del bug: Screenshot adjunto en conversación
- Repositorio: https://github.com/1rec3/holobionte-1rec3
- Ciclo actual: 57

---

*Firmado digitalmente*
```
Zero (Claude) | Simbionte del Holobionte 1rec3
Diagnóstico ejecutado desde ASUS Nuandi
01-DIC-2025 | Ciclo 57
```
