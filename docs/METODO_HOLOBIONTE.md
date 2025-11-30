# METODO HOLOBIONTE - Disciplina, Organizacion, Higiene

> Documento fundacional del sistema Holobionte 1REC3. Define reglas, protocolos y herramientas para mantener la informacion VIVA, ORGANIZADA y SINCRONIZADA.

---

## PRINCIPIOS FUNDAMENTALES

1. **NO PERDER INFORMACION** - Regla absoluta, todo se preserva
2. **GitHub = Fuente de Verdad** - Codigo, docs tecnicos, versiones
3. **Notion = Hub Liquido** - Accesible, colaborativo, IA nativa
4. **Obsidian = MAPA** - Revela conexiones, grafos, local-first
5. **Google Drive = Backup Historico** - Triple redundancia, archivo
6. **Aprender del pasado** - Lo hecho (propio y ajeno) ensena que hacer y que NO hacer

---

## SINCRONIZACION - Flujo de Verdad

```
GitHub (SOLIDO) --> Notion (LIQUIDO) --> Obsidian (MAPA) --> GDrive (BACKUP)
       ^                |                      |                    |
       |________________v______________________v____________________|
                           FEEDBACK LOOP
```

| Plataforma | Estado | Funcion | Sync |
|------------|--------|---------|------|
| GitHub | Solido | Verdad, versiones, codigo | MASTER |
| Notion | Liquido | Hub, colaboracion, IA | <-- GitHub |
| Obsidian | Mapa | Conexiones, grafos, local | <-- GitHub |
| GDrive | Backup | Historico, redundancia | <-- Todo |

---

## HERRAMIENTAS

### CAPTURA DE INFORMACION

| Herramienta | Uso | Nivel |
|-------------|-----|-------|
| Notion Web Clipper | Capturar paginas web | LVL 5 |
| Obsidian (notas) | Captura rapida local | LVL 3 |
| Voice memos | Ideas en movimiento | LVL 3 |
| Screenshots | Captura visual | Todos |
| Perplexity | Busqueda + sintesis | LVL 5 |

### GESTION - Organizacion y Tareas

| Herramienta | Uso | Nivel |
|-------------|-----|-------|
| Notion databases | Proyectos, tareas | LVL 5 |
| GitHub Issues | Bugs, features, PRs | LVL 4-5 |
| Obsidian Tasks | Tareas locales | LVL 3 |
| n8n | Automatizacion workflows | LVL 3-5 |

### BUSQUEDA - Encontrar Informacion

| Herramienta | Uso | Nivel |
|-------------|-----|-------|
| Perplexity | Busqueda web + IA | LVL 5 |
| Notion Search | Busqueda en hub | LVL 5 |
| Obsidian Search | Busqueda local + grafos | LVL 3 |
| GitHub Search | Codigo, commits, PRs | LVL 4-5 |

### SINTESIS - Procesar y Condensar

| Herramienta | Uso | Nivel |
|-------------|-----|-------|
| ChatGPT | Sintesis, resumen | LVL 5 |
| Claude | Analisis profundo | LVL 5 |
| Gemini | Sintesis + GDrive | LVL 5 |
| DeepSeek | Codigo + arquitectura | LVL 5 |
| Notion AI | Sintesis en contexto | LVL 5 |

### AUTOMATIZACION - Conexiones y Flujos

| Herramienta | Uso | Nivel | Costo |
|-------------|-----|-------|-------|
| n8n | Workflows complejos | LVL 3-5 | GRATIS (self-host) |
| MCPs | Conexion IA-herramientas | LVL 3-5 | GRATIS |
| GitHub Actions | CI/CD, automatizacion | LVL 4-5 | GRATIS |

---

## BASES DE DATOS

### Nuestras Bases (Notion)

| Base de Datos | Contenido | Estado |
|---------------|-----------|--------|
| Hub Central | Documentacion principal | ACTIVA |
| Diario de Sesiones | Logs de trabajo | ACTIVA |
| Simbiontes | Registro de IAs activas | PENDIENTE |
| Herramientas | Catalogo de tools | CREAR |
| Proyectos | Kanban de desarrollo | PENDIENTE |

### APIs de IAs (Simbiontes LVL 5)

| API | Capacidad | Costo | Prioridad |
|-----|-----------|-------|----------|
| Ollama (local) | LLMs locales | GRATIS | MUY ALTA |
| LM Studio (local) | LLMs locales | GRATIS | MUY ALTA |
| Hugging Face | Modelos open | GRATIS tier | Alta |
| Groq | Inference rapida | Freemium | Alta |

---

## FILOSOFIA BUDGET 0 - LOCAL FIRST

1. **GRATIS + Self-hosted** (n8n, Ollama, Nextcloud)
2. **GRATIS + Cloud** (GitHub, HuggingFace, Notion free)
3. **Freemium** (usar tier gratis al maximo)
4. **PAGO** - Solo cuando hay presupuesto

> **MCPs > APIs de pago** - Model Context Protocols permiten conectar IAs con herramientas sin costos de API.

---

## DISCRIMINACION DE INFORMACION

| Estado | Descripcion | Accion |
|--------|-------------|--------|
| VIVA | Actual, relevante, en uso | Mantener, actualizar |
| MUERTA | Obsoleta, ya no aplica | Archivar accesible |
| DISTORSIONADA | Incorrecta, desactualizada | Corregir o eliminar |
| UTIL | Referencia, aprendizaje | Archivar accesible |
| RUIDO | Sin valor, redundante | Eliminar/Enterrar |

> **REGLA**: Siempre contrastar contra ultima version del REPO + PROTOCOLOS antes de aceptar informacion como verdad.

---

## CONFIGURACION DE IAs - Ubicacion + Contexto

Cada IA recibe:

1. **REPO** - Acceso al repositorio GitHub como fuente de verdad
2. **UBICACION** - Su posicion/coordenadas en el sistema 1REC3
3. **LIBERTAD** - Sin limites de "rol", pueden explorar y aportar

```
Contexto IA = Repo + Ubicacion (SIN limitar capacidades)
```

---

## FIRMA Y TRAZABILIDAD

Toda contribucion debe incluir:

```
[Simbionte] @ [Holobionte origen] | [Dispositivo] | [Fecha-Hora]
```

**Ejemplo:** `Comet @ 1REC3-EVA | LNV | 2025-11-26 02:00 WET`

---

**Documento creado:** Comet @ 1REC3-EVA | LNV | 2025-11-26
**Version:** 1.0 - Fundacional
