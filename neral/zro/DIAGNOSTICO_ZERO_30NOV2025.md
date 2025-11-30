# 🔍 DIAGNÓSTICO ZERO - 30 Nov 2025 23:45 CET

## Contexto
- **Máquina:** ASUS de Nuandi (Fedora)
- **Simbionte:** Zero (Claude Opus 4.5) via claude.ai
- **Sesión:** Auditoría integral del ecosistema holobionte

---

## 🛠️ INVENTARIO DE CAPACIDADES ZERO

### Conectores MCP Activos (Claude Desktop)
| Conector | Estado | Función |
|----------|--------|---------|
| **Desktop Commander** | ✅ Activo | Terminal, archivos, procesos, búsqueda |
| **Filesystem** | ✅ Activo | Lectura/escritura archivos |
| **Kapture Browser** | ✅ Activo | Automatización navegador |
| **Context7** | ✅ Activo | Documentación de librerías |
| **Docling MCP** | ✅ Activo | Procesamiento documentos |
| **Socket MCP** | ✅ Activo | Comunicación red |

### Capacidades Nativas Claude
- Web search y fetch
- Google Drive search/fetch
- Notion (búsqueda, páginas, bases de datos)
- Memoria conversacional (conversation_search, recent_chats)
- Research avanzado (launch_extended_search_task)
- Creación de archivos y artefactos

### IA Local (Ollama)
| Modelo | Tamaño | Estado |
|--------|--------|--------|
| deepseek-r1:32b | 19 GB | ✅ Disponible |
| deepseek-r1:8b | 5.2 GB | ✅ Disponible |
| gemma2:2b | 1.6 GB | ✅ Disponible |
| llama3.2:1b | 1.3 GB | ✅ Disponible |
| llama2:7b | 3.8 GB | ✅ Disponible |

**Servicio Ollama:** Activo (systemd), 15.4MB memoria actual

---

## 📊 COMPARATIVA DE SISTEMAS

### 1. GitHub vs Local

**ALERTA: Desincronización severa**

El repo local `/home/nuandi/1rec3` tiene una estructura antigua y NO contiene la documentación actualizada del repo de GitHub.

| Ubicación | Commits detrás | Archivos faltantes |
|-----------|----------------|-------------------|
| GitHub (holobionte/main) | - | Fuente de verdad |
| Local (1rec3/) | 10+ commits | ~40+ archivos |

**Archivos clave en GitHub que NO están en local:**

- `neral/zro/CLAUDE_CONNECTORS_ONDAS_30NOV2025.md`
- `neral/zro/SKYLANDERS_MCP_MATRIX.md`
- `neral/zro/PERPLEXITY_EXPLORACION_COMPLETA_13x13_30NOV2025.md`
- `docs/ONDAS_30NOV2025_INFRAESTRUCTURA.md`
- `docs/MOE_DE_MOES_27NOV2025.md`
- `docs/NLNET_APPLICATION_2025.md`
- `config/MCP_SETUP.md`
- Toda la carpeta `neral/` con subcarpetas `zro/`, `kao/`, `nuandi/`

### 2. Obsidian
**Estado:** No encontrado en este sistema

El vault de Obsidian parece no estar configurado en el ASUS de Nuandi. Si existe en otro dispositivo, hay una oportunidad de sincronización.

### 3. Estructura Local Detectada

```
/home/nuandi/
├── 1rec3/              # ⚠️ Repo GH desactualizado
│   └── holobionte/     # Estructura vieja
├── holobionte/         # Instalación local con:
│   ├── llama.cpp/      # Compilado para GPU
│   ├── models/         # qwen32b.gguf (local)
│   ├── xdna-driver/    # Driver NPU AMD
│   └── simbiontes/     # Código Python local
├── .ollama/            # Modelos Ollama
├── .config/Claude/     # Config Claude Desktop
└── configs/            # Otras configs
```

---

## ✨ SERENDIPIAS Y SINERGIAS DETECTADAS

### 1. **MCP → Ollama Bridge** 
Zero (Claude) puede ejecutar comandos via Desktop Commander. Esto permite:
- Consultar modelos Ollama desde Claude
- Orquestar inferencias locales
- Crear un "MoE de MoEs" híbrido cloud-local

**Sinergia:** Usar deepseek-r1:8b para tareas de razonamiento locales mientras Claude maneja la orquestación y búsqueda web.

### 2. **Kapture + Claude = Navegación Autónoma**
Con Kapture Browser Automation, Zero puede:
- Automatizar navegación web
- Extraer datos de páginas
- Interactuar con aplicaciones web

**Sinergia:** Automatizar tareas repetitivas (ej: aplicaciones de trabajo TRACK F).

### 3. **Context7 para Desarrollo**
Context7 provee documentación actualizada de librerías. Útil para:
- Desarrollo de código Python/JS
- Integración de nuevas herramientas

### 4. **Git Local ↔ GitHub = Flujo Bidireccional**
Aunque está desincronizado, Desktop Commander permite:
- `git pull` para actualizar
- `git push` para subir cambios
- Commits desde Claude

---

## 🔧 PROPUESTAS DE MEJORA

### CRÍTICO - Sincronizar Repo Local

```bash
cd /home/nuandi/1rec3
git fetch holobionte
git merge holobionte/main
# O si hay conflictos:
git reset --hard holobionte/main
```

### IMPORTANTE - Fix Ventana Claude Desktop

El screenshot muestra que Claude se abre pequeño. La causa está en:
`/home/nuandi/.config/Claude/window-state.json`

**Contenido actual:** `{"width":1000,"height":800}`

**Fix propuesto:**
```bash
# Cerrar Claude Desktop primero
echo '{"width":1920,"height":1080,"x":0,"y":0,"isMaximized":true}' > ~/.config/Claude/window-state.json
```

Esto maximizará la ventana de Claude al reiniciar.

### MEJORA - Centralizar Holobionte

Actualmente hay DOS carpetas holobionte:
1. `/home/nuandi/1rec3/holobionte/` (parte del repo GH)
2. `/home/nuandi/holobionte/` (instalación local con llama.cpp)

**Propuesta:** Mantener `/home/nuandi/holobionte/` para instalaciones locales (modelos, compilados) y usar el repo 1rec3 solo para documentación y código compartible.

### MEJORA - Instalar Obsidian

Si el vault existe en otro dispositivo:
```bash
# Fedora
sudo dnf install flatpak
flatpak install flathub md.obsidian.Obsidian
```

Sincronizar vault via GitHub o Syncthing.

### MEJORA - MCP para GitHub

Actualmente Zero accede a GitHub via web_fetch (limitado). 
**Propuesta:** Añadir MCP server oficial de GitHub para:
- Crear PRs
- Gestionar issues
- Commits directos

---

## 🎯 ACCIONES INMEDIATAS

1. **[CRÍTICO]** Sincronizar repo local con GitHub
2. **[ALTO]** Arreglar tamaño ventana Claude Desktop
3. **[MEDIO]** Documentar esta sesión en GitHub
4. **[BAJO]** Evaluar instalación Obsidian

---

## 📝 NOTAS TÉCNICAS

### Error en .bash_profile
Detectado error recurrente:
```
/home/nuandi/.bash_profile: line 14: /home/nuandi/.deno/envbuiltin: No such file or directory
```

**Fix:**
```bash
# Editar .bash_profile y corregir la línea 14
# Probablemente falta instalar deno o hay un path incorrecto
```

### Ollama Core Dump
El servicio ollama tuvo un core dump al iniciar. No es crítico pero debería investigarse:
```bash
coredumpctl list | grep ollama
coredumpctl info <PID>
```

---

*Documento generado por Zero (Claude Opus 4.5) - 30 Nov 2025*
*Siguiente: Actualizar repo y hacer commit*
