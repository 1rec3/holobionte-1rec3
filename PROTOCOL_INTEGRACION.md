# Protocolo de Integración de Herramientas OSS en Holobionte 1rec3

## Principios guía de integración

- **Alineación con el holobionte**: Toda herramienta debe apoyar la cooperación humano+simbionte, priorizar opensource, y cuidar los datos y la sostenibilidad del colectivo.
- **Evolución constante**: Los protocolos son vivos; cualquier fallo o mejora se documenta y propone actualización en Canal Holobionte.
- **Elegancia técnica**: Integración mínima, eficiente y reversible. Evita duplicaciones y respeta el diseño y estructura actual.

---

## Protocolo paso a paso

### 1. Evaluación previa

- Verifica que la herramienta es truly OSS y multiplataforma.
- Confirma integración con el ecosistema (especialmente GitHub y stack actual).
- Documenta pros/contras y experiencia previa.

### 2. Documentación

- Añade nueva integración en `INTEGRACIONES.md`.
- Explica: objetivo, pasos de setup, parámetros críticos (tokens, scopes, roles), buenas prácticas y feedback.

### 3. Pruebas de integración mínima

- Realiza pruebas en entorno de staging/sandbox antes de producción.
- Documenta bugs, limitaciones y sugerencias específicas.

### 4. Onboarding

- Prepara una guía de incorporación para nuevos simbiontes, incluye: capturas, ejemplos de casos, troubleshooting y FAQs.

### 5. Actualización estructural

- Si la documentación/protocolo se queda corto, crea/actualiza el archivo de protocolo (ej. este mismo archivo).
- Propón mejoras en Canal Holobionte, ejecuta mini-retrospectiva tras cada nueva integración para refinar los procesos.

### 6. Control de versiones y sostenibilidad

- Registra versión y fecha de cada integración/protocolo añadido.
- Sugiere pausa para evitar sobrecarga, prioriza calidad y estabilidad.

---

## Nueva herramienta: Ejemplo para futuros PR

- Añade nueva sección en `INTEGRACIONES.md`:
  - Explica integración desde el punto de vista de holobionte (¿cómo maximiza la sinergia, la cooperación, la documentalidad?).
  - Enumera pasos, dependencias, y cómo revertir/desinstalar si es necesario.
- Actualiza este archivo si es necesario para reflejar cambios.
- Haz PR siguiendo la estructura y documentación incorporada, con commit claro y branch específica por integración.

---

**Si falta algún protocolo, créalo inmediatamente y documenta la experiencia en la memoria y canal open del proyecto.**

---

Versión inicial: 2025-11-17 por Saul + simbionte IA Comet.  
Sugiere mejoras en Canal Holobionte y PRs futuros.
