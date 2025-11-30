# PROTOCOLO DE RASTRO, FIRMA Y HUELLA
## Sistema Holobionte 1rec3

**Autor:** Comet (SubNeral)
**Fecha:** 2025-01-27
**Versión:** 1.0

---

## 1. PROPÓSITO

Establecer trazabilidad completa de todas las acciones, creaciones y modificaciones realizadas por simbiontes en el sistema Holobionte 1rec3.

**Principio fundamental:** NO PERDER INFORMACIÓN

---

## 2. FORMATO DE FIRMA ESTÁNDAR

Toda acción debe incluir:

```
[SIMBIONTE] @ [PLATAFORMA] | [NIVEL] | [TIMESTAMP]
Acción: [DESCRIPCIÓN]
Ubicación: [REPO/CARPETA/ARCHIVO]
Hash/ID: [IDENTIFICADOR ÚNICO]
```

### Ejemplo:
```
Zro@Grok | LVL5 | 2025-01-27T14:30:00Z
Acción: Investigación navegadores agénticos
Ubicación: holobionte-1rec3/docs/SERENDIPIAS_BIOLOGICAS.md
Hash: afec481
```

---

## 3. NIVELES DE SIMBIONTES

| Nivel | Rol | Acceso | Firma |
|-------|-----|--------|-------|
| LVL 6 | Núcleo (Saúl) | Total | `Neral@Human` |
| LVL 5 | Exploradores IA | Notion+Repos | `Zro@[Plataforma]` |
| LVL 4 | Orquestadores | Browser+APIs | `[Nombre]@Browser` |
| LVL 3 | Procesadores | Local+Cloud | `Zero@[Engine]` |
| LVL 2 | Ejecutores | Scripts | `Auto@[Sistema]` |
| LVL 1 | Sensores | Solo lectura | `Sensor@[Fuente]` |

---

## 4. ZERO LVL 3 - CONFIGURACIÓN

### 4.1 Arquitectura Híbrida R1

**Zero** es el simbionte LVL 3 potente que combina:

| Componente | Función | Acceso |
|------------|---------|--------|
| **DeepSeek R1 Cloud** | Razonamiento complejo, análisis profundo | API Cloud |
| **DeepSeek R1 Local** | Procesamiento privado, velocidad | Ollama/LMStudio |
| **Comunicación LVL 4** | Coordinación con Comet y orquestadores | Notion + GitHub |

### 4.2 Capacidades Zero

- Repositorio local múltiple (clones de GitHub)
- Contexto completo del sistema Holobionte
- Acceso lectura/escritura Notion
- Comunicación bidireccional con LVL 4
- Procesamiento híbrido Cloud+Local

### 4.3 Firma Zero

```
Zero@R1-Hybrid | LVL3 | [TIMESTAMP]
Engine: [Cloud|Local|Hybrid]
Task: [DESCRIPCIÓN]
Output: [UBICACIÓN]
```

---

## 5. PROTOCOLO DE HUELLA

### 5.1 Tipos de Huella

| Tipo | Descripción | Almacenamiento |
|------|-------------|----------------|
| 📝 Creación | Nuevo archivo/contenido | GitHub commit |
| ✏️ Modificación | Cambio en existente | GitHub commit + diff |
| 🔍 Investigación | Búsqueda/análisis | Notion log |
| 🔗 Conexión | Link entre recursos | Obsidian graph |
| 💬 Comunicación | Mensaje entre niveles | Notion thread |

### 5.2 Registro Obligatorio

**Cada acción debe registrarse en:**
1. **GitHub** - Commits con mensaje estructurado
2. **Notion** - Base de datos RASTRO_SIMBIONTES
3. **Obsidian** - Nodo en grafo de conexiones

---

## 6. SISTEMA ANTI-RUIDO

### 6.1 Clasificación de Información

| Estado | Emoji | Acción |
|--------|-------|--------|
| VIVA | 📁 | Mantener activo |
| MUERTA | 📦 | Archivar |
| ENTERRADA | ⚰️ | Backup profundo |
| ÚTIL | ✅ | Priorizar |
| RUIDO | 🔇 | Filtrar (NO borrar) |

### 6.2 Regla de Oro

> **ARCHIVAR, NUNCA BORRAR**
> 
> La información "inútil" hoy puede ser valiosa mañana.
> Usar sistema 📁VIVO → 📦MUERTO → ⚰️ENTERRADO

---

## 7. ACCESO NOTION PARA SIMBIONTES

### 7.1 Bases de Datos Requeridas

1. **RASTRO_SIMBIONTES** - Log de todas las acciones
2. **TAREAS_ACTIVAS** - Misiones en progreso
3. **CONOCIMIENTO_BASE** - Información consolidada

### 7.2 Permisos por Nivel

| Nivel | Lectura | Escritura | Crear DB |
|-------|---------|-----------|----------|
| LVL 5 | ✅ | ✅ | ❌ |
| LVL 4 | ✅ | ✅ | ✅ |
| LVL 3 | ✅ | ✅ | ❌ |

---

## 8. IMPLEMENTACIÓN INMEDIATA

### 8.1 Activar Zero LVL 3

```bash
# Configuración Zero con R1 Hybrid
1. DeepSeek R1 Cloud: Configurar API en cuenta
2. R1 Local: Instalar via Ollama
   ollama pull deepseek-r1:7b
3. Contexto: Clonar repos holobionte-1rec3
4. Notion: Compartir workspace con integración
```

### 8.2 Checklist Activación

- [ ] Zero tiene contexto sistema completo
- [ ] Zero puede comunicarse con Comet (LVL4)
- [ ] Zero tiene acceso repos locales
- [ ] Zero puede escribir en Notion
- [ ] Zero usa R1 Cloud para tareas complejas
- [ ] Zero usa R1 Local para velocidad/privacidad

---

**Firma documento:**
```
Comet@Perplexity | LVL4 | 2025-01-27T15:00:00Z
Acción: Creación protocolo rastro/firma/huella
Ubicación: holobionte-1rec3/docs/RASTRO_FIRMA.md
```
