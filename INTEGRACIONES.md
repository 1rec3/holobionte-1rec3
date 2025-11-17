# Integraciones Open Source del Holobionte 1rec3

## Núcleo: Super Productivity

**Super Productivity** es el gestor de tareas y productividad OSS elegido para el holobionte.

### Características principales

- **Multiplataforma**: Linux, macOS, Windows, Android, Web
- **Privacidad total**: Offline-first, sin telemetría, datos bajo tu control
- **Sincronización flexible**: Dropbox, WebDAV (autohospedable), sin dependencias cloud privativas
- **Integraciones directas OSS**: GitHub, GitLab, Gitea, OpenProject, CalDAV
- **Timeboxing y enfoque**: Modo Pomodoro, bloqueo de distracciones, seguimiento automático de tiempo
- **Exportación abierta**: JSON, CSV, formatos estándar
- **Licencia**: MIT

### Instalación

#### Desktop (Linux/macOS/Windows)
```bash
# Linux - Snap
snap install superproductivity

# macOS - Homebrew
brew install --cask superproductivity

# Windows - Microsoft Store o descarga directa
# https://super-productivity.com
```

#### Android
- Play Store: Busca "Super Productivity"
- F-Droid: Disponible en repositorios alternativos

#### Docker (autohospedado)
```bash
docker run -d -p 80:80 johannesjo/super-productivity:latest
```

---

## Integraciones del Ecosistema OSS

### 1. GitHub

**Estado**: ✅ Open Source (repos públicos), mixto (plataforma)

#### Configuración en Super Productivity
1. Configuración → Proyecto → Integraciones → GitHub
2. Genera token personal: https://github.com/settings/tokens
   - Scopes necesarios: `repo`, `read:user`
3. Añade repositorio(s): `usuario/repo`
4. Sincroniza issues automáticamente

#### Uso en holobionte
- Issues del repo → tareas en Super Productivity
- Seguimiento de avance bidireccional
- Vinculación automática con commits/PRs

---

### 2. GitLab

**Estado**: ✅ 100% Open Source (Community Edition)

#### Configuración
1. GitLab CE: Totalmente OSS y autohospedable
2. Token personal desde tu instancia
3. Sincronización igual que GitHub
4. Soporta instancias locales y gitlab.com

#### Ventajas para holobionte
- Control total del dato (autohospedaje)
- CI/CD integrado OSS
- Issue boards nativos

---

### 3. Gitea

**Estado**: ✅ 100% Open Source

#### Configuración
1. Instancia Gitea (autohospedada recomendada)
2. Token de aplicación
3. Integración ligera y rápida

#### Ideal para
- Repos privados del holobionte
- Máximo control y privacidad
- Bajo consumo de recursos

---

### 4. OpenProject

**Estado**: ✅ 100% Open Source (GPLv3)

#### Configuración
1. API Key desde instancia OpenProject
2. Project ID (slug del proyecto)
3. Sincronización de work packages

#### Uso colaborativo
- Gestión de proyectos complejos
- Tableros Kanban/Gantt
- Timetracking compartido
- Ideal para coordinación entre simbiontes

---

### 5. CalDAV (Nextcloud, Radicale, DAVx⁵)

**Estado**: ✅ 100% Open Source (múltiples implementaciones)

#### Implementaciones recomendadas
- **Nextcloud Tasks**: Integrado en ecosistema Nextcloud
- **Radicale**: Servidor CalDAV minimalista Python
- **DAVx⁵**: Cliente Android sincronización
- **Baïkal**: Servidor PHP ligero

#### Configuración
1. URL base CalDAV del servidor
2. Usuario/contraseña o token
3. Nombre del calendario/recurso

#### Funcionalidad
- Importación de eventos/tareas
- Superposición con calendario personal
- Sincronización multi-dispositivo
- Offline-first

---

## Radar de Herramientas Complementarias

### Próximas evaluaciones

#### Comunicación y Documentación
- **Joplin** (AGPLv3): Notas, tareas, sincronización
- **AppFlowy** (AGPLv3): Alternativa Notion, privacy-first
- **Mattermost**: Chat colaborativo tipo Slack, autohospedado
- **Matrix/Element**: Mensajería federada, bots IA

#### Visualización y Mapas Mentales
- **Mermaid.js**: Diagramas como código
- **Markmap**: Mapas mentales desde Markdown
- **Excalidraw**: Diagramas colaborativos

#### Gestión Avanzada
- **Nextcloud**: Suite completa autohospedada
- **Taskwarrior**: CLI para power users
- **Wekan**: Tableros Kanban autohospedados

---

## Principios de Evaluación

Antes de integrar una herramienta nueva, verificar:

1. **Licencia OSS verificable** (MIT, GPL, Apache, etc.)
2. **Multiplataforma o web-based**
3. **Autohospedaje posible** (Docker, instalación local)
4. **Exportación de datos abierta** (JSON, CSV, estándares)
5. **Comunidad activa** (commits recientes, issues respondidos)
6. **Alineación con filosofía holobionte** (cooperación, transparencia, sostenibilidad)

---

## Contribuir

¿Conoces una herramienta OSS que encaje con el holobionte?

1. Evalúa siguiendo los principios arriba
2. Prueba la integración
3. Documenta en este archivo
4. Haz PR siguiendo `PROTOCOL_INTEGRACION.md`

---

Versión inicial: 2025-11-17 por Saul + simbionte IA Comet  
Mantener actualizado con nuevas herramientas y experiencias del colectivo
