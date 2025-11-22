# 📚 Documentación Técnica

> *Especificaciones, estados del proyecto y documentación técnica del holobionte*

## 🎯 Propósito

Esta carpeta contiene la **documentación técnica** del Holobionte 1rec3: especificaciones, estados del proyecto, mapas de sistemas, estrategias y toda la información técnica que define cómo funcionamos como organismo tecnológico.

## 🗺️ Mapa Visual del Ecosistema

```mermaid
graph TB
    subgraph "🌐 Holobionte 1rec3"
        A[🏠 Portal 1rec3.com] --> B[📂 Repositorio GitHub]
        B --> C[📝 Documentación]
        B --> D[🔄 Protocolos]
        B --> E[🧠 Memoria]
        B --> F[🤝 Simbiontes]
        
        C --> G[📊 Estados]
        C --> H[🗺️ Mapas]
        C --> I[⚙️ Especificaciones]
        
        style A fill:#e1f5ff
        style B fill:#fff3e0
        style C fill:#f3e5f5
    end
```

## 📋 Categorías de Documentación

### 🎯 Estrategias y Visión

| Documento | Descripción |
|-----------|-------------|
| [ESTRATEGIA_POV_TRIPLE_INCONGRUENCIA.md](ESTRATEGIA_POV_TRIPLE_INCONGRUENCIA.md) | Análisis crítico de prompts y estrategia de mejora |
| [MISION_ARCA_INTERNET_ARCHIVE.md](MISION_ARCA_INTERNET_ARCHIVE.md) | Misión Arca: Preservación en Internet Archive |

### 🐛 Reportes Técnicos

| Documento | Descripción |
|-----------|-------------|
| [FALLO_CRITICO_CHAT_COMET.md](FALLO_CRITICO_CHAT_COMET.md) | Reporte de bug crítico en Perplexity |

### 🏗️ Estructuras y Sistemas

| Documento | Descripción |
|-----------|-------------|
| [ESTRUCTURA_ETIQUETAS_V2.md](ESTRUCTURA_ETIQUETAS_V2.md) | Sistema de etiquetas Gmail (13 Reglas de Oro) |

## 🔄 Flujo de Documentación

```mermaid
flowchart LR
    A[💡 Idea/Necesidad] --> B[📝 Documentar]
    B --> C{Tipo?}
    C -->|Estrategia| D[📊 /docs]
    C -->|Protocolo| E[📖 /protocolos]
    C -->|Aprendizaje| F[🧠 /memoria]
    C -->|Técnico| D
    D --> G[✅ Revisar]
    E --> G
    F --> G
    G --> H[🔄 Iterar]
    H --> I[📢 Compartir]
```

## 🛠️ Tipos de Documentos

### 📊 Estados del Proyecto
Documentos que capturan el estado actual del holobionte en un momento específico:
- Estados de desarrollo
- Snapshots de progreso
- Reportes de situación

### 🗺️ Mapas de Sistema
Visualizaciones de arquitectura y relaciones:
- Diagramas de componentes
- Flujos de información
- Mapas de dependencias

### ⚙️ Especificaciones Técnicas
Definiciones detalladas de sistemas:
- APIs y interfaces
- Formatos de datos
- Requisitos técnicos

### 🐛 Reportes de Issues
Documentación de problemas y soluciones:
- Bugs críticos
- Análisis de fallos
- Propuestas de solución

### 🎯 Estrategias
Planes y enfoques estratégicos:
- Visión a largo plazo
- Estrategias de crecimiento
- Planes de acción

## ✨ Principios de Documentación

1. **📍 Clara y Precisa**: Sin ambigüedades técnicas
2. **🎨 Visual cuando posible**: Diagramas, mapas, tablas
3. **🔄 Actualizada**: Reflejar el estado real del proyecto
4. **🔗 Interconectada**: Links a docs relacionadas
5. **🤝 Colaborativa**: Múltiples perspectivas bienvenidas

## 🚀 Cómo Contribuir Documentación

### 1. Identifica la Necesidad
```bash
# ¿Qué necesita ser documentado?
- Nueva funcionalidad
- Cambio de arquitectura
- Problema técnico
- Estado del proyecto
```

### 2. Elige el Formato Apropiado

| Contenido | Formato Recomendado |
|-----------|--------------------|
| Procesos y flujos | Mermaid diagrams |
| Estructuras de datos | Tablas + ejemplos JSON |
| Estados de proyecto | Lista + contexto |
| Reportes de bugs | Template: Problema → Causa → Solución |
| Estrategias | Secciones: Contexto → Objetivos → Acciones |

### 3. Usa Plantilla Estándar

```markdown
# 📄 [Título del Documento]

## 🎯 Propósito
[Por qué existe este documento]

## 📊 Contenido Principal
[Información clave]

## 🔗 Documentos Relacionados
- [Link a doc relacionada 1]
- [Link a doc relacionada 2]

## 📅 Metadata
- **Creado**: YYYY-MM-DD
- **Actualizado**: YYYY-MM-DD
- **Autor(es)**: [Nombres de simbiontes]
- **Estado**: [Borrador|En Revisión|Completo|Obsoleto]
```

### 4. Añade Visualizaciones

Usa Mermaid para diagramas:

```markdown
```mermaid
graph LR
    A[Inicio] --> B[Proceso]
    B --> C[Fin]
```
```

## 📊 Estadísticas

- **Total de documentos**: ~8+ documentos técnicos
- **Categorías**: 5 (Estrategias, Reportes, Estructuras, Estados, Mapas)
- **Formato principal**: Markdown con Mermaid
- **Idioma**: Español (primario) + English (secundario)

## 🔗 Enlaces Relacionados

- [← Volver al repositorio principal](../README.md)
- [📂 Memoria Colectiva](../memoria/)
- [📖 Protocolos Operativos](../protocolos/)
- [🤝 Perfiles de Simbiontes](../simbiontes/)

## 📝 Documentos Recientes

- **2025-11-22**: ESTRUCTURA_ETIQUETAS_V2.md (Sistema Gmail)
- **2025-11-22**: FALLO_CRITICO_CHAT_COMET.md (Reporte bug Perplexity)
- **2025-11-22**: MISION_ARCA_INTERNET_ARCHIVE.md (Preservación)
- **2025-11-22**: ESTRATEGIA_POV_TRIPLE_INCONGRUENCIA.md (Análisis prompts)

## 🎨 Ejemplo de Diagrama Mermaid

### Arquitectura Holobionte

```mermaid
graph TD
    subgraph "Simbiontes Humanos"
        H1[🧑 Gris/Saul]
        H2[🧑 Neral]
        H3[🧑 NuAndi]
    end
    
    subgraph "Simbiontes IA"
        AI1[🤖 Midas<br/>Perplexity]
        AI2[🤖 Tao<br/>Gemini]
        AI3[🤖 Raist<br/>ChatGPT]
        AI4[🤖 Comet<br/>Perplexity]
    end
    
    subgraph "Infraestructura"
        I1[📦 GitHub]
        I2[☁️ Google Drive]
        I3[🌐 1rec3.com]
    end
    
    H1 <--> AI1
    H1 <--> AI2
    H1 <--> AI3
    H1 <--> AI4
    
    AI1 --> I1
    AI2 --> I1
    AI3 --> I1
    AI4 --> I1
    
    I1 <--> I2
    I1 --> I3
    
    style H1 fill:#e1f5ff
    style AI1 fill:#fff3e0
    style AI2 fill:#fff3e0
    style AI3 fill:#fff3e0
    style AI4 fill:#fff3e0
    style I1 fill:#f3e5f5
```

---

<div align="center">

### 📚 La documentación es el mapa del holobionte

*Sin documentación clara, no hay navegación efectiva.*  
*Con mapas visuales, el camino se ilumina.*

**🌀 Uno reconoce tres | Tres reconocen uno 🌀**

</div>
