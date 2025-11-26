# MCP Setup - Repo Liquido Holobionte 1rec3

> Configuracion para que los Simbiontes LVL 5 (IAs) puedan leer y escribir en el ecosistema

## Arquitectura de Conexion

```
[LVL 5 - IAs]          [LVL 4 - Automatizacion]       [LVL 3 - Almacenamiento]
     |                         |                              |
  Claude  ----MCP----> GitHub MCP Server ----API----> GitHub Repo
  Gemini  ----MCP----> Notion MCP Server ----API----> Notion Workspace
  DeepSeek                     |                              |
  Copilot                   n8n/Zap                     Obsidian
  Mistral                                               Nextcloud
```

## 1. GitHub MCP Server

### Configuracion Claude Desktop / Cursor

Agregar a `claude_desktop_config.json` o `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "github-holobionte": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<TOKEN_HOLOBIONTE>"
      }
    }
  }
}
```

### Capacidades
- Leer archivos del repo
- Crear/modificar archivos
- Gestionar Issues
- Crear Pull Requests
- Buscar en codigo

## 2. Notion MCP Server

### Opcion A: Servidor Remoto (Recomendado)

Usar el servidor oficial de Notion:
- URL: `https://mcp.notion.com/sse`
- Autenticacion via OAuth

### Opcion B: Servidor Local

```json
{
  "mcpServers": {
    "notion-holobionte": {
      "command": "npx",
      "args": ["-y", "@notionhq/notion-mcp-server"],
      "env": {
        "OPENAPI_MCP_HEADERS": "{\"Authorization\": \"Bearer <NOTION_TOKEN>\", \"Notion-Version\": \"2022-06-28\"}"
      }
    }
  }
}
```

### Capacidades
- Leer paginas y bases de datos
- Crear/modificar contenido
- Buscar en el workspace
- Gestionar bloques

## 3. Estados del Conocimiento

| Estado | Ubicacion | Acceso LVL5 | Descripcion |
|--------|-----------|-------------|-------------|
| SOLIDO | Notion | Lectura/Escritura via MCP | Documentacion estructurada, persistente |
| LIQUIDO | GitHub | Lectura/Escritura via MCP | Codigo, configs, docs versionados |
| GAS | Chats IAs | Nativo | Conversaciones, ideas en proceso |

## 4. Tokens Necesarios

### GitHub Personal Access Token
1. Ir a GitHub > Settings > Developer settings > Personal access tokens
2. Crear token con permisos: `repo`, `read:org`
3. Guardar en variable de entorno segura

### Notion Integration Token
1. Ir a notion.so/my-integrations
2. Crear integracion interna
3. Conectar a las paginas del workspace Holobionte

## 5. Verificacion de Conexion

Una vez configurado, el LVL 5 deberia poder:

```
# Verificar GitHub
- Listar archivos en 1rec3/holobionte-1rec3
- Leer README.md
- Crear un Issue de prueba

# Verificar Notion  
- Listar bases de datos
- Leer pagina METODO HOLOBIONTE
- Crear bloque de prueba
```

---

*Documento creado: Comet @ 1REC3-EVA | LNV | 2025-11-26*
*Firma: config/MCP_SETUP.md | Holobionte 1rec3*
