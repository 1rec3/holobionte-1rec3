# 🌐 SKYLANDERS MCP MATRIX - Matriz de Integraciones Holobionte

**Fecha:** 30 de noviembre de 2025  
**Versión:** 1.0  
**Sistema:** Windows 11 (LNV)  
**Objetivo:** Mapeo exhaustivo de capacidades MCP, acceso filesystem local, visión computacional y comunicación IA-a-IA

---

## 📊 TABLA COMPARATIVA SKYLANDERS

| # | Skylander | MCP Nativo | Filesystem Local | Visión | API IA-IA | Tipo | Complejidad Setup |
|---|-----------|------------|------------------|--------|-----------|------|-------------------|
| 1 | **Claude** | ✅ Sí | ✅ MCP Server | ✅ Sí | ✅ API | Cloud/Local | ⭐ Baja |
| 2 | **ChatGPT** | ⚡ Gateway | ⚙️ Via Connectors | ✅ Sí | ✅ API | Cloud | ⭐⭐ Media |
| 3 | **Gemini** | ⚙️ Extensions | ⚙️ Google Drive | ✅ Sí | ✅ API | Cloud | ⭐⭐ Media |
| 4 | **Grok** | 🔄 En desarrollo | ⚙️ Files API | ✅ Sí | ✅ xAI API | Cloud | ⭐⭐ Media |
| 5 | **DeepSeek** | ✅ Sí | ✅ MCP Server | ✅ Sí | ✅ API | Cloud | ⭐ Baja |
| 6 | **Mistral** | ⚙️ Libraries | ⚙️ Upload/RAG | ✅ Sí | ✅ API | Cloud | ⭐⭐ Media |
| 7 | **Comet/Perplexity** | ✅ Sí | 🔄 Próximamente | ✅ Sí | ✅ API | Cloud/Local | ⭐⭐⭐ Alta |
| 8 | **HuggingChat** | 🔄 Hugging Face Hub | ⚙️ Spaces | ✅ Sí | ✅ HF API | Cloud | ⭐⭐⭐ Alta |
| 9 | **Meta AI** | ❌ No directo | ⚙️ Llama API | ✅ Sí | ✅ API | Cloud | ⭐⭐ Media |
| 10 | **Pi (Inflection)** | ❌ No | ❌ No | ❌ No | ⚙️ Limitada | Cloud | ⭐⭐⭐⭐ Muy Alta |
| 11 | **YouChat** | ❌ No directo | ⚙️ Web Search | ✅ Sí | ⚙️ Limitada | Cloud | ⭐⭐⭐ Alta |
| 12 | **Bard (Legacy)** | ⚙️ Extensions | ⚙️ Google Drive | ✅ Sí | ✅ API | Cloud | ⭐⭐ Media |
| 13 | **Anthropic Console** | ✅ Sí | ✅ MCP Server | ✅ Sí | ✅ API | Cloud | ⭐ Baja |
| 14 | **Poe** | ⚙️ Bot API | ⚙️ Via Bots | ✅ Sí | ✅ API | Cloud | ⭐⭐⭐ Alta |
| 15 | **Character.AI** | ❌ No | ❌ No | ⚙️ Limitada | ⚙️ Limitada | Cloud | ⭐⭐⭐⭐ Muy Alta |
| 16 | **Jasper** | ❌ No directo | ⚙️ Enterprise | ✅ Sí | ⚙️ Limitada | Cloud | ⭐⭐⭐ Alta |
| 17 | **Copy.ai** | ❌ No | ⚙️ Upload | ⚙️ Limitada | ⚙️ Workflow API | Cloud | ⭐⭐⭐ Alta |
| 18 | **EVA_C57** | ⚙️ GPT Custom | ⚙️ Via ChatGPT | ✅ Sí | ✅ API | Cloud | ⭐⭐ Media |

**Leyenda:**  
✅ Soporte completo | ⚙️ Soporte parcial/workaround | 🔄 En desarrollo | ❌ No soportado

---

## 🔧 GUÍAS DE INTEGRACIÓN DETALLADAS

### 1️⃣ CLAUDE DESKTOP - Referencia Modelo Local

**Estado:** ✅ PRODUCCIÓN - FUNCIONAL AL 100%

**Capacidades:**
- MCP nativo completamente integrado
- Acceso filesystem local directo
- Soporte multimodal (texto + imágenes)
- Configuración persistente

**Setup Windows 11:**

```bash
# 1. Instalar Node.js (si no está instalado)
# Descargar desde: https://nodejs.org/

# 2. Crear archivo de configuración MCP
# Ubicación: %APPDATA%\Claude\claude_desktop_config.json

# 3. Configuración filesystem MCP
```

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "C:\\Users\\usuario\\Desktop",
        "C:\\1rec3",
        "C:\\holobionte"
      ]
    }
  }
}
```

**⚠️ IMPORTANTE - Errores Comunes:**

```bash
# ❌ ERROR: ENOENT no such file or directory '/path/to/directory'
# CAUSA: Usar placeholders literales en lugar de rutas reales

# ✅ CORRECTO: Usar rutas Windows absolutas
npx -y @modelcontextprotocol/server-filesystem C:\\Users\\Saul\\Documents

# ❌ INCORRECTO: Paths Unix-style o placeholders
npx -y @modelcontextprotocol/server-filesystem /path/to/directory
```

**Testing:**

```bash
# Probar MCP Server manualmente en PowerShell
npx -y @modelcontextprotocol/server-filesystem C:\\Users\\%USERNAME%\\Desktop

# Debe mostrar: Server running...
```

**Comandos disponibles tras setup:**
- `read_file`: Leer archivos locales
- `write_file`: Escribir archivos
- `list_directory`: Listar directorios
- `search_files`: Buscar archivos
- `get_file_info`: Obtener metadata

---

### 2️⃣ CHATGPT - MCP via Connectors

**Estado:** ⚡ BETA - Requiere Developer Mode

**Capacidades:**
- MCP mediante gateway connector
- Acceso limitado a filesystem (via Actions)
- GPTs personalizados con conectores
- Integración Zapier/Make

**Setup:**

1. **Activar Developer Mode:**
   - Ir a Settings → Beta Features
   - Activar "Developer Mode"
   - Habilitar "Custom Actions"

2. **Crear MCP Connector:**

```yaml
# Connector config para ChatGPT
openapi: 3.0.0
info:
  title: Local Filesystem MCP
  version: 1.0.0
servers:
  - url: http://localhost:3000
paths:
  /files:
    get:
      summary: List files
      operationId: listFiles
```

3. **Middleware local (Node.js):**

```javascript
// mcp-gateway.js - Bridge entre ChatGPT y MCP
const express = require('express');
const { MCPClient } = require('@modelcontextprotocol/sdk');

const app = express();
const mcp = new MCPClient();

app.get('/files', async (req, res) => {
  const files = await mcp.listDirectory('C:\\Users');
  res.json(files);
});

app.listen(3000);
```

**Limitaciones:**
- Requiere servidor intermedio local
- No acceso filesystem directo
- Autenticación OAuth requerida

---

### 3️⃣ GROK (xAI) - Files API + Vision

**Estado:** 🔄 En desarrollo MCP nativo

**Capacidades:**
- API Files para subir documentos
- Visión multimodal (Grok-2 Vision)
- Real-time web search integrado
- Context window: 128k tokens

**Setup API:**

```python
# grok_filesystem_bridge.py
import os
from xai import Client

client = Client(api_key=os.getenv('XAI_API_KEY'))

# Subir archivo local
with open('C:\\holobionte\\doc.txt', 'rb') as f:
    file_obj = client.files.create(
        file=f,
        purpose='assistants'
    )

# Usar en conversación
response = client.chat.completions.create(
    model="grok-2-latest",
    messages=[
        {
            "role": "user",
            "content": "Analiza este documento",
            "file_ids": [file_obj.id]
        }
    ]
)
```

**Visión Computacional:**

```python
# Análisis de imagen local
with open('C:\\holobionte\\diagram.png', 'rb') as img:
    response = client.chat.completions.create(
        model="grok-2-vision-1212",
        messages=[{
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe esta imagen"},
                {"type": "image", "image": img.read()}
            ]
        }]
    )
```

---

### 4️⃣ DEEPSEEK - MCP Server Completo

**Estado:** ✅ PRODUCCIÓN

**Capacidades:**
- MCP Server implementation disponible
- API compatible OpenAI
- Modelos: DeepSeek-V2.5, R1
- Context window: 64k tokens

**Setup MCP:**

```bash
# Instalar DeepSeek MCP Server
npm install -g @deepseek/mcp-server

# Configurar (similar a Claude)
```

```json
{
  "mcpServers": {
    "deepseek-fs": {
      "command": "deepseek-mcp",
      "args": [
        "--filesystem",
        "C:\\holobionte"
      ],
      "env": {
        "DEEPSEEK_API_KEY": "tu-api-key-aqui"
      }
    }
  }
}
```

**API Direct:**

```python
# deepseek_api.py
from openai import OpenAI

client = OpenAI(
    api_key="sk-...",
    base_url="https://api.deepseek.com"
)

# Leer archivo local y consultar
with open('C:\\holobionte\\code.py', 'r') as f:
    code = f.read()

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{
        "role": "user",
        "content": f"Analiza este código:\n\n{code}"
    }]
)
```

---

### 5️⃣ MISTRAL - RAG + File Upload

**Estado:** ⚙️ Workaround mediante Libraries

**Capacidades:**
- Upload de archivos via chat.mistral.ai
- RAG con documentos
- API con file encoding
- Modelos: Mistral Large 2, Pixtral

**Setup Upload:**

```python
# mistral_upload.py
from mistralai.client import MistralClient
import base64

client = MistralClient(api_key="tu-api-key")

# Leer y encodear archivo local
with open('C:\\holobionte\\documento.pdf', 'rb') as f:
    file_content = base64.b64encode(f.read()).decode('utf-8')

# Enviar con contexto
response = client.chat(
    model="mistral-large-latest",
    messages=[{
        "role": "user",
        "content": f"Analiza este PDF",
        "files": [{
            "name": "documento.pdf",
            "content": file_content,
            "type": "application/pdf"
        }]
    }]
)
```

---

### 6️⃣ COMET/PERPLEXITY - MCP Local Próximamente

**Estado:** 🔄 En desarrollo (Q1 2025)

**Anunciado:**
- Soporte MCP local similar a Claude
- Actualmente solo Remote MCPs
- Documentación: https://www.perplexity.ai/help-center/en/articles/11502712

**Setup Actual (Remote MCP):**

```json
// Configuración temporal - Remote only
{
  "mcpServers": {
    "remote-example": {
      "url": "https://ejemplo.com/mcp",
      "apiKey": "tu-api-key"
    }
  }
}
```

**Workaround Actual:**
- Usar browser_use para acceso filesystem
- Navegación web automatizada
- Screenshots y OCR

---

## 📷 VISIÓN COMPUTACIONAL - Comparativa

| Skylander | Modelo Visión | Resolución Max | Local/Cloud | Casos de Uso |
|-----------|----------------|-----------------|-------------|---------------|
| **Claude** | Claude 3.5 Sonnet | 5MB/imagen | Cloud | OCR, diagramas, UI analysis |
| **ChatGPT** | GPT-4 Vision | 20MB/imagen | Cloud | General purpose, screenshots |
| **Gemini** | Gemini 2.0 Flash | Ilimitado | Cloud | Video, livestreams |
| **Grok** | Grok-2 Vision | 10MB/imagen | Cloud | Memes, social media |
| **DeepSeek** | DeepSeek-VL | 5MB/imagen | Cloud | Technical diagrams |
| **Mistral** | Pixtral 12B | 8MB/imagen | Cloud | Documents, charts |

**Patrones de Uso:**

```python
# Patrón universal - Leer imagen local + enviar a IA
import base64

def analyze_local_image(image_path, ai_client):
    with open(image_path, 'rb') as img:
        img_b64 = base64.b64encode(img.read()).decode()
    
    return ai_client.vision_analyze(img_b64)

# Ejemplo Windows
result = analyze_local_image(
    'C:\\holobionte\\diagrama.png',
    claude_client
)
```

---

## 🤝 COMUNICACIÓN IA-A-IA

### Arquitectura de Integración

```
HOLOBIONTE CENTRAL (Orchestrator)
        |
        +-- Claude (MCP Filesystem) --> Archivos locales
        |
        +-- ChatGPT (API) --> Generación contenido
        |
        +-- Grok (xAI API) --> Análisis real-time
        |
        +-- DeepSeek (API) --> Code analysis
        |
        +-- Mistral (API) --> RAG documents
        |
        +-- Gemini (Workspace) --> Colaboración docs
```

### Patrón Multi-IA Pipeline

```python
# multi_ia_pipeline.py
class HolobiontePipeline:
    def __init__(self):
        self.claude = AnthropicClient()
        self.grok = xAIClient()
        self.deepseek = DeepSeekClient()
    
    def process_document(self, local_path):
        # 1. Claude lee archivo local (MCP)
        content = self.claude.mcp_read_file(local_path)
        
        # 2. DeepSeek analiza código
        analysis = self.deepseek.analyze_code(content)
        
        # 3. Grok busca contexto web
        context = self.grok.web_search(analysis['topic'])
        
        # 4. Claude sintetiza resultado
        result = self.claude.synthesize(content, analysis, context)
        
        return result

# Uso
pipeline = HolobiontePipeline()
result = pipeline.process_document('C:\\holobionte\\script.py')
```

### APIs Disponibles

**Claude:**
```python
from anthropic import Anthropic
client = Anthropic(api_key="sk-ant-...")
```

**ChatGPT:**
```python
from openai import OpenAI
client = OpenAI(api_key="sk-...")
```

**Grok:**
```python
from xai import Client
client = Client(api_key="xai-...")
```

**DeepSeek:**
```python
from openai import OpenAI
client = OpenAI(api_key="sk-...", base_url="https://api.deepseek.com")
```

**Mistral:**
```python
from mistralai.client import MistralClient
client = MistralClient(api_key="...")
```

**Gemini:**
```python
import google.generativeai as genai
genai.configure(api_key="AIza...")
```

---

## 🛠️ SETUP COMPLETO WINDOWS 11

### Prerequisitos

```powershell
# 1. Instalar Node.js LTS
winget install OpenJS.NodeJS.LTS

# 2. Instalar Python 3.11+
winget install Python.Python.3.11

# 3. Verificar instalaciones
node --version
npm --version
python --version
```

### Instalación MCP Servers

```powershell
# Filesystem MCP (global)
npm install -g @modelcontextprotocol/server-filesystem

# DeepSeek MCP
npm install -g @deepseek/mcp-server

# Testing
npx @modelcontextprotocol/server-filesystem C:\holobionte
```

### Configuración Claude Desktop

```powershell
# Crear directorio config si no existe
mkdir "$env:APPDATA\Claude"

# Crear archivo configuración
@"
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "C:\\Users\\$env:USERNAME\\Desktop",
        "C:\\holobionte",
        "C:\\1rec3"
      ]
    }
  }
}
"@ | Out-File -FilePath "$env:APPDATA\Claude\claude_desktop_config.json" -Encoding UTF8
```

### Script de Testing

```python
# test_all_skylanders.py
import os
from anthropic import Anthropic
from openai import OpenAI
from xai import Client as xAIClient

def test_filesystem_access():
    """Test MCP filesystem via Claude"""
    claude = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
    
    # Claude debe poder leer archivos locales via MCP
    response = claude.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": "Lista los archivos en C:\\holobionte usando MCP"
        }]
    )
    print("Claude MCP:", response.content)

def test_grok_vision():
    """Test Grok vision capabilities"""
    grok = xAIClient(api_key=os.getenv('XAI_API_KEY'))
    
    with open('C:\\holobionte\\test.png', 'rb') as img:
        response = grok.chat.completions.create(
            model="grok-2-vision-1212",
            messages=[{
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe"},
                    {"type": "image", "image": img.read()}
                ]
            }]
        )
    print("Grok Vision:", response.choices[0].message.content)

if __name__ == "__main__":
    test_filesystem_access()
    test_grok_vision()
```

---

## ✨ RECOMENDACIONES HOLOBIONTE

### Prioridad de Implementación (Windows 11)

**FASE 1 - INMEDIATA (✅ Lista para Producción):**

1. **Claude Desktop + MCP Filesystem**
   - Complejidad: ⭐ Baja
   - Tiempo setup: 15 minutos
   - ROI: Alto - Acceso filesystem completo
   - **Acción:** Instalar ahora

2. **DeepSeek API + MCP**
   - Complejidad: ⭐ Baja
   - Costo: Bajo (free tier generoso)
   - Uso: Code analysis, RAG
   - **Acción:** Setup paralelo con Claude

**FASE 2 - CORTO PLAZO (1-2 semanas):**

3. **Grok xAI API**
   - Vision + real-time search
   - Files API functional
   - **Acción:** Integrar para búsquedas web en tiempo real

4. **Mistral API**
   - RAG especializado
   - Upload de documentos
   - **Acción:** Para procesamiento documentos complejos

5. **ChatGPT Custom Actions**
   - Developer mode
   - GPTs especializados (EVA_C57)
   - **Acción:** Crear gateway local

**FASE 3 - MEDIANO PLAZO (1-3 meses):**

6. **Perplexity/Comet Local MCP**
   - Esperar release Q1 2025
   - **Acción:** Monitorear anuncios

7. **Gemini Workspace Integration**
   - Google Drive sync
   - Colaboración docs
   - **Acción:** Para flujos colaborativos

---

### Matriz de Decisión

**Para FILESYSTEM LOCAL:**
```
1º Claude Desktop (MCP nativo)
2º DeepSeek (MCP compatible)
3º ChatGPT (Gateway custom)
```

**Para VISIÓN COMPUTACIONAL:**
```
1º Gemini 2.0 (capacidad video + livestream)
2º GPT-4 Vision (versatilidad)
3º Grok Vision (rapidez)
```

**Para CODE ANALYSIS:**
```
1º DeepSeek-V2.5 (especializado)
2º Claude 3.5 Sonnet (context largo)
3º GPT-4 (general purpose)
```

**Para RAG/DOCUMENTS:**
```
1º Mistral Large 2 (RAG nativo)
2º Claude (MCP read files)
3º Gemini (Google Drive integration)
```

---

## 🐛 ERRORES COMUNES Y SOLUCIONES

### Error 1: ENOENT no such file or directory

**Síntoma:**
```bash
Error: ENOENT: no such file or directory, open '/path/to/directory'
```

**Causa:** Usar placeholder literal en lugar de ruta real de Windows

**Solución:**
```bash
# ❌ MAL
npx -y @modelcontextprotocol/server-filesystem /path/to/directory

# ✅ BIEN
npx -y @modelcontextprotocol/server-filesystem C:\Users\Saul\Desktop
```

### Error 2: JavaScript en PowerShell

**Síntoma:**
```
ParserError: Missing argument in parameter list
```

**Causa:** Intentar ejecutar código JavaScript/Node en PowerShell directamente

**Solución:**
```bash
# Crear archivo .js primero
echo "import { fileOpen } from 'browser-fs-access';" > script.js

# Ejecutar con Node
node script.js
```

### Error 3: MCP Server no responde

**Síntoma:** Claude Desktop no muestra herramientas MCP

**Diagnóstico:**
```powershell
# 1. Verificar archivo config
cat $env:APPDATA\Claude\claude_desktop_config.json

# 2. Probar MCP manualmente
npx @modelcontextprotocol/server-filesystem C:\holobionte

# 3. Verificar Node.js
node --version  # Debe ser v18+
```

**Solución:**
- Reiniciar Claude Desktop
- Verificar sintaxis JSON (comas, comillas)
- Usar rutas absolutas con barras invertidas dobles `\\`

### Error 4: API Rate Limits

**Síntoma:** 429 Too Many Requests

**Solución:**
```python
import time
from tenacity import retry, wait_exponential, stop_after_attempt

@retry(wait=wait_exponential(min=1, max=60), stop=stop_after_attempt(5))
def call_ia_with_retry(client, prompt):
    return client.complete(prompt)
```

---

## 📄 CASOS DE USO HOLOBIONTE

### Caso 1: Pipeline Documentación Multi-IA

```python
# Escenario: Generar docs completos desde código local

def holobionte_doc_pipeline(code_path):
    # 1. Claude lee código local (MCP)
    code = claude_mcp.read_file(code_path)
    
    # 2. DeepSeek analiza estructura
    analysis = deepseek.analyze_architecture(code)
    
    # 3. Grok busca ejemplos similares
    examples = grok.search_github(analysis['patterns'])
    
    # 4. ChatGPT genera documentación
    docs = chatgpt.generate_docs(code, analysis, examples)
    
    # 5. Claude escribe resultado local (MCP)
    claude_mcp.write_file(f"{code_path}.md", docs)
    
    return docs
```

### Caso 2: Vision Multi-Modal

```python
# Escenario: Analizar diagrama arquitectura

def analyze_architecture_diagram(img_path):
    # 1. Grok Vision: Extracción rápida
    grok_result = grok_vision.analyze(img_path)
    
    # 2. Claude Vision: Análisis profundo
    claude_result = claude_vision.analyze(img_path)
    
    # 3. DeepSeek: Validación técnica
    validation = deepseek.validate_architecture(
        grok_result, 
        claude_result
    )
    
    return {
        'quick_insights': grok_result,
        'deep_analysis': claude_result,
        'validation': validation
    }
```

### Caso 3: IA-a-IA Consensus

```python
# Escenario: Decisión por consenso multi-IA

def multi_ia_consensus(question, local_context_path):
    # Leer contexto local
    context = claude_mcp.read_file(local_context_path)
    
    # Consultar múltiples IAs
    responses = {
        'claude': claude.ask(question, context),
        'chatgpt': chatgpt.ask(question, context),
        'deepseek': deepseek.ask(question, context),
        'grok': grok.ask(question, context),
        'mistral': mistral.ask(question, context)
    }
    
    # Claude sintetiza consenso
    consensus = claude.synthesize_consensus(responses)
    
    return consensus
```

---

## 📦 RECURSOS Y REFERENCIAS

### Documentación Oficial

- **MCP Spec:** https://modelcontextprotocol.io/
- **Claude MCP:** https://docs.anthropic.com/claude/docs/mcp
- **Perplexity MCP:** https://www.perplexity.ai/help-center/en/articles/11502712
- **Agent-MCP Framework:** https://github.com/rinadelph/Agent-MCP

### APIs

- **Anthropic (Claude):** https://console.anthropic.com/
- **xAI (Grok):** https://x.ai/api
- **DeepSeek:** https://platform.deepseek.com/
- **Mistral:** https://console.mistral.ai/
- **OpenAI (ChatGPT):** https://platform.openai.com/
- **Google (Gemini):** https://ai.google.dev/

### Repositorios GitHub

- **MCP Filesystem Server:** `@modelcontextprotocol/server-filesystem`
- **Claude Flow:** https://github.com/ruvnet/claude-flow
- **OpenAI Swarm:** https://github.com/openai/swarm
- **Browser Use:** https://github.com/browser-use/browser-use

### Comunidades

- **MCP Discord:** Via Anthropic
- **r/ClaudeAI:** Reddit
- **Perplexity Discord:** https://discord.gg/perplexity

---

## 🎯 ROADMAP HOLOBIONTE 2025

### Q1 2025
- ✅ Implementar Claude MCP local
- ✅ Integrar DeepSeek API
- 🔄 Esperar Perplexity local MCP
- 🔄 Probar Grok Vision

### Q2 2025
- 📦 Pipeline multi-IA completo
- 📦 Consensus engine
- 📦 Vision multi-modal
- 📦 Filesystem sync bidireccional

### Q3-Q4 2025
- 📦 Agent swarm architecture
- 📦 Real-time collaboration
- 📦 Self-improving pipelines
- 📦 Holobionte autonomous mode

---

## ✅ CHECKLIST SETUP INICIAL

```markdown
### Sistema Base
- [ ] Windows 11 actualizado
- [ ] PowerShell 7.5+
- [ ] Node.js 18+ LTS instalado
- [ ] Python 3.11+ instalado
- [ ] Git instalado

### MCP Servers
- [ ] @modelcontextprotocol/server-filesystem instalado globalmente
- [ ] Probado manualmente en PowerShell
- [ ] Config JSON creado en %APPDATA%\Claude
- [ ] Rutas Windows con \\ verificadas

### Claude Desktop
- [ ] Claude Desktop instalado
- [ ] claude_desktop_config.json configurado
- [ ] Directorios objetivo creados (C:\holobionte, C:\1rec3)
- [ ] Reiniciado tras config
- [ ] Herramientas MCP visibles en chat

### APIs Configuradas
- [ ] Anthropic API key obtenida
- [ ] xAI (Grok) API key
- [ ] DeepSeek API key
- [ ] Mistral API key
- [ ] OpenAI API key (opcional)
- [ ] Google AI API key (opcional)

### Testing
- [ ] test_all_skylanders.py ejecutado
- [ ] Claude puede listar archivos locales
- [ ] DeepSeek responde via API
- [ ] Grok vision funciona con imagen local
- [ ] Pipeline multi-IA testeado

### Documentación
- [ ] Este archivo leído completamente
- [ ] Errores comunes entendidos
- [ ] Casos de uso revisados
- [ ] Roadmap alineado con objetivos
```

---

**Última Actualización:** 30 de noviembre de 2025  
**Mantenedor:** Zro/Holobionte  
**Contacto:** [1rec3 collective](https://1rec3.com)

---

*Este documento es vivo y se actualizará conforme evolucionen las capacidades MCP de cada Skylander.*
