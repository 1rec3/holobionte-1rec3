# MCP NOTION SETUP - Holobionte 1REC3

> Guia tecnica para conectar IAs (LVL5) con Notion via Model Context Protocol
> Basado en investigacion de Manus (LVL4) - 26-NOV-2025

---

## RECOMENDACION PRINCIPAL

**Servidor MCP Auto-Alojado** bajo subdominio seguro (ej. `mcp.1rec3.com`)

Ventajas:
- Mayor control y visibilidad
- Alineado con filosofia "Local First" del Holobionte
- Open Source First

---

## FASE A: Integracion en Notion

### 1. Crear Integracion
- Ir a https://www.notion.so/my-integrations
- Click "New integration"
- Nombre: `Holobionte-MCP`
- Tipo: Internal

### 2. Obtener Token
- Copiar **Internal Integration Secret** (formato: `ntn_****`)
- Este sera el `NOTION_TOKEN`

### 3. Configurar Permisos
En la pestana "Capabilities":
- [x] Read content
- [x] Update content
- [x] Insert content
- [ ] Read comments (opcional)

### 4. Conectar Paginas
- Ir a HOLOBIONTE EVA - Hub Central
- Menu (...) > "Connect to" > Seleccionar `Holobionte-MCP`
- Repetir para otras paginas que las IAs deban acceder

---

## FASE B: Despliegue Servidor MCP

### Instalacion
```bash
npm install -g @notionhq/notion-mcp-server
```

### Configuracion
```bash
export NOTION_TOKEN="ntn_xxxxxxxxxxxx"
notion-mcp-server
```

### Exposicion Publica
Opciones:
1. **Reverse proxy** (nginx/caddy) en servidor del Holobionte
2. **Docker** con docker-compose
3. **Cloudflare Tunnel** para exposicion segura

URL recomendada: `https://mcp.1rec3.com/mcp`

---

## FASE C: Configuracion Cliente IA

### Para Claude/Cursor/Windsurf

Anadir a configuracion MCP:
```json
{
  "mcpServers": {
    "notionHolobionte": {
      "url": "https://mcp.1rec3.com/mcp",
      "type": "streamable-http"
    }
  }
}
```

### Herramientas disponibles
- `notion-search` - Buscar en el workspace
- `notion-create-pages` - Crear paginas
- `notion-update-pages` - Actualizar contenido
- `notion-query-database` - Consultar bases de datos

---

## LIMITACIONES CONOCIDAS

| Limitacion | Impacto |
|------------|--------|
| Cobertura API limitada | No todas las funciones de Notion disponibles |
| Latencia variable | Posibles fallos intermitentes |
| Riesgo de escritura | IA puede corromper datos si alucina |
| Falta estandarizacion | Config JSON varia entre clientes |

---

## ALTERNATIVAS SI MCP FALLA

### 1. API REST Directa
Usar wrapper Python/Node.js para llamadas directas a Notion API

### 2. n8n como Intermediario
Preferido por filosofia "Self-hosted" del Holobionte
- Crear workflows que actuen como puente IA <-> Notion

### 3. Obsidian como Intermediario
- IA escribe Markdown en GitHub (SOLIDO)
- Workflow sincroniza GitHub -> Notion (LIQUIDO)
- Alineado con arquitectura GAS/LIQUIDO/SOLIDO

---

## REFERENCIAS

1. [Notion Developers - MCP](https://developers.notion.com/docs/get-started-with-mcp)
2. [GitHub - notion-mcp-server](https://github.com/makenotion/notion-mcp-server)
3. [Skywork AI - MCP Guide](https://skywork.ai/mcp-notion)

---

## FIRMA

*Documento creado: GrisComet @ 1REC3 | LVL5 | 26-NOV-2025*
*Investigacion: Manus @ 1REC3 | LVL4*
*Cristalizacion de conocimiento GAS -> LIQUIDO*
