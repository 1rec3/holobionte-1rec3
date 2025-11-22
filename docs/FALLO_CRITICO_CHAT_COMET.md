# ⚠️ FALLO CRÍTICO: HISTORIAL DE CHAT COMET

**Fuente**: Google Keep - Nota creada por Gris + Tao (Gemini)
**Fecha**: 2025-11-22 (Editada: 16:50)
**Tipo**: Reporte Técnico / Bug Report
**Estado**: Documentado para presentación a Perplexity

---

## Fallo Crítico en Historial de Chat de Comet (Perplexity)

### Plataformas Afectadas

- **Versión Beta Móvil** (iOS/Android)
- **Versión Desktop** (Windows/macOS)

---

## 1. Fallo en Versión Beta Móvil (Crítico)

### Impacto

**Imposibilidad** de acceder o guardar historial de chat.

### Pasos para Reproducir (PoC)

1. Abrir la aplicación Comet Beta en el móvil.
2. Iniciar una nueva conversación y realizar una pregunta simple (ej. "¿Qué hora es?").
3. Cerrar la aplicación (o cambiar de tarea).
4. Volver a abrir Comet.

### Observación Esperada del Fallo

El chat anterior **no aparece en el historial**, o el intento de seleccionarlo (si se muestra brevemente) falla, llevando al usuario a una nueva ventana de chat.

---

## 2. Fallo en Versión Desktop (Windows)

### Impacto

Dificultad severa para la **gestión y cambio de contexto**.

### Pasos para Reproducir (PoC)

1. Abrir Comet en Windows.
2. Crear 3-4 conversaciones distintas sobre temas diferentes.
3. Intentar alternar rápidamente entre la conversación 1 y la 3 usando la interfaz de historial.

### Observación Esperada del Fallo

El sistema es **lento**, a menudo redirige al último chat en lugar del seleccionado, o el chat anterior tarda en cargar su contexto, demostrando **inestabilidad en la persistencia del estado**.

---

## Estrategia

Documentar estos pasos con **capturas/vídeo** para la presentación a Perplexity como prueba de valor.

---

## Contexto del Holobionte

Este documento forma parte de la identificación de limitaciones técnicas críticas en herramientas utilizadas por el Holobionte 1rec3. La documentación detallada de estos fallos permite:

1. **Proporcionar feedback valioso** a los desarrolladores de Perplexity
2. **Demostrar capacidad analítica** del equipo del Holobionte
3. **Establecer colaboración** con plataformas de IA avanzadas

---

## Enlaces Relacionados

- **Estrategia PoV**: [ESTRATEGIA_POV_TRIPLE_INCONGRUENCIA.md](./ESTRATEGIA_POV_TRIPLE_INCONGRUENCIA.md)
- **Protocolo Maestro**: [PROTOCOL_MAESTRO_V2.md](../protocolos/PROTOCOL_MAESTRO_V2.md)
- **Perfil Tao**: [TAO.md](../simbiontes/TAO.md)

---

**Integrado desde Google Keep por Comet (Perplexity)**
**Fecha de integración**: 2025-11-22
