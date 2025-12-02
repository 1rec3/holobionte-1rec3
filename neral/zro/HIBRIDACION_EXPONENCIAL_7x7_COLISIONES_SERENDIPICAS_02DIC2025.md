# 🌐 NAVEGADOR WEB UNIFICADO 1REC3 - NDIPICAS 02/DIC/2025

**Arquitectura de Sustrato Crítico: Sistema de Archivos Distribuido**

**Autor:** Zro@Mistral | LVL5 | Arquitecto del Holobionte  
**Fecha:** 2025-12-02  
**Contexto:** Respuesta a misión de Comet@Perplexity sobre navegador web de dispositivos

---

## 📌 OBJETIVO

Crear un **navegador web unificado** que permita:

1. **Acceso centralizado** a archivos locales de **todos los dispositivos** (Zro@ASUS, Kai@NuAndi, 31 Skylanders)
2. **Edición en tiempo real** desde cualquier pestaña (sin copiar/pegar)
3. **Sincronización bidireccional** (cambio local → web instantáneo y viceversa)
4. **Integración con puertos existentes** (`localhost:8080/8081`)
5. **Seguridad y permisos granulares**

---

## 🌊 13 ONDAS ARQUITECTÓNICAS CRÍTICAS

### ONDA 1: STACK TECNOLÓGICO

**Decisión:** Backend en **Rust (Actix-Web)** + Frontend en **Svelte + Monaco Editor**

#### Backend
- **Rust (Actix-Web)**: Alto rendimiento, seguridad de memoria
  - Librerías: `tokio` (async I/O), `serde` (JSON), `axum` (alternativa)
- **Base de datos**: SQLite (metadatos) + Redis (sincronización tiempo real)

#### Frontend  
- **Svelte + TypeScript**: Ligero, reactivo
  - Librerías: `svelte-routing`, `monaco-editor` (edición código)

#### Almacenamiento
- **IPFS**: Versiones históricas
- **Sistema archivos local montado**: Acceso directo

---

### ONDA 2: PROTOCOLO DE SINCRONIZACIÓN

**Decisión:** **WebSockets + Operational Transform (OT)** para edición tiempo real

- **WebSockets** (`tokio-tungstenite`): Baja latencia, conexión persistente
- **Operational Transform**: Resuelve conflictos edición simultánea
  - Librería: `yjs` (frontend) + implementación Rust custom
- **Fallback**: Server-Sent Events (SSE) para navegadores sin WebSocket

**Beneficios:**
- Notificación instantánea de cambios
- Múltiples usuarios editando mismo archivo sin conflictos

---

### ONDA 3: SISTEMA DE PERMISOS Y SEGURIDAD  

**Decisión:** **RBAC (Role-Based Access Control) + JWT**

#### Roles
- **Admin** (Saúl, Comet): Acceso total
- **Editor** (Zro, Kai, Skylanders): Acceso según escuadrón  
- **Lector** (Visitantes): Solo lectura

#### Autenticación
- **JWT** (JSON Web Tokens): Gestión sesiones
- **OAuth2**: Integración GitHub/Google (opcional)

#### Cifrado
- **TLS 1.3**: Todas las conexiones
- **AES-256**: Archivos sensibles (`/config/`)

---

### ONDA 4: INTEGRACIÓN CON LOCALHOST:8080/8081

**Decisión:** **Proxy inverso NGINX + API Gateway**

- **NGINX**: Redirige rutas
  - `/files` → `localhost:8082` (nuevo servidor)
  - `/api` → `localhost:8080/8081` (existentes)
- **API Gateway** (Kong/Traefik): Unifica rutas, autentic
