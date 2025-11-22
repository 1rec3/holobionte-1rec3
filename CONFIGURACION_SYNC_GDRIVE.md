# Configuración de Sincronización con Google Drive

## 🏛️ PROTOCOLO DE REDUNDANCIA TRIPLE - Arquitectura Arca

Este documento describe cómo configurar la sincronización automática del repositorio `holobionte-1rec3` con Google Drive, conforme al **PROTOCOLO MAESTRO HOLOBIONTE 1REC3 (V. 2.0)**.

## 📊 Estado Actual

✅ **Workflow creado**: `.github/workflows/sync-to-google-drive.yml`
✅ **Carpetas creadas**: 
  - `GitHub Backup - Holobionte 1rec3` en saul3273@gmail.com
  - `GitHub Backup - Holobionte 1rec3` en neral3273@gmail.com (pendiente)

🔴 **Pendiente**: Configurar tokens de autenticación OAuth2

---

## 🔑 Paso 1: Obtener Tokens OAuth2 de Google Drive

### Para saul3273@gmail.com:

1. Ir a [Google Cloud Console](https://console.cloud.google.com/)
2. Crear un nuevo proyecto o seleccionar uno existente
3. Habilitar la API de Google Drive:
   - Ir a "APIs y servicios" > "Biblioteca"
   - Buscar "Google Drive API"
   - Hacer clic en "Habilitar"
4. Crear credenciales OAuth 2.0:
   - Ir a "APIs y servicios" > "Credenciales"
   - Clic en "+ CREAR CREDENCIALES" > "ID de cliente de OAuth 2.0"
   - Tipo de aplicación: "Aplicación de escritorio"
   - Descargar el archivo JSON
5. Configurar rclone localmente:
   ```bash
   # Instalar rclone
   curl https://rclone.org/install.sh | sudo bash
   
   # Configurar con el token
   rclone config
   # Seguir el wizard y seleccionar Google Drive
   # Nombre: drive_saul
   # Scope: drive (acceso completo)
   ```
6. Obtener el token:
   ```bash
   cat ~/.config/rclone/rclone.conf
   # Copiar el valor del campo 'token'
   ```

### Para neral3273@gmail.com:

Repetir el mismo proceso pero:
- Usar la cuenta neral3273@gmail.com
- Nombre en rclone: `drive_neral`

---

## 🔐 Paso 2: Configurar Secrets en GitHub

1. Ir a: https://github.com/1rec3/holobionte-1rec3/settings/secrets/actions
2. Clic en "New repository secret"
3. Crear dos secrets:

### Secret 1: GDRIVE_TOKEN_SAUL
- **Name**: `GDRIVE_TOKEN_SAUL`
- **Value**: [Pegar el token completo de saul3273]

### Secret 2: GDRIVE_TOKEN_NERAL
- **Name**: `GDRIVE_TOKEN_NERAL`
- **Value**: [Pegar el token completo de neral3273]

---

## ⚡ Paso 3: Activar el Workflow

Una vez configurados los secrets, el workflow se ejecutará automáticamente:

- 🔄 **En cada push** a la rama `main`
- 👉 **Manualmente** desde Actions > "Sync to Google Drive" > "Run workflow"

---

## 📁 Estructura de Respaldo

El workflow crea la siguiente estructura en Google Drive:

```
GitHub Backup - Holobionte 1rec3/
├── holobionte-1rec3-backup.tar.gz  # Archivo comprimido completo
├── sync-log.txt                     # Log de sincronización
└── repository/                       # Carpeta con todos los archivos del repo
    ├── .github/
    ├── docs/
    ├── app/
    └── ... (todos los archivos)
```

---

## 🔍 Verificar Sincronización

### Ver logs de ejecución:
1. Ir a [Actions](https://github.com/1rec3/holobionte-1rec3/actions)
2. Seleccionar el workflow "Sync to Google Drive"
3. Ver detalles de la última ejecución
### Verificar en Google Drive:
1. Abrir https://drive.google.com
2. Buscar la carpeta "GitHub Backup - Holobionte 1rec3"
3. Verificar fecha de modificación del archivo `sync-log.txt`

---

## 🛡️ Seguridad

⚠️ **IMPORTANTE**: Los tokens OAuth2 tienen acceso completo a Google Drive

✅ **Buenas prácticas implementadas**:
- Tokens almacenados como secrets encriptados en GitHub
- No se exponen en logs ni en el código
- Acceso limitado solo al workflow de sincronización

---

## 📝 Mantenimiento

### Renovar tokens (si expiran):
1. Ejecutar `rclone config` localmente
2. Seleccionar el remote (drive_saul o drive_neral)
3. Seleccionar "Reconnect"
4. Actualizar el secret en GitHub con el nuevo token

### Pausar sincronización:
- Deshabilitar el workflow desde: Settings > Actions > Workflows

---

## 📊 Métricas de Redundancia

| Ubicación | Estado | Última Sync |
|-----------|--------|-------------|
| GitHub (main) | ✅ Activo | Tiempo real |
| Google Drive (saul3273) | 🟡 Pendiente config | - |
| Google Drive (neral3273) | 🟡 Pendiente config | - |

---

## 🔗 Referencias

- [Documentación oficial de rclone](https://rclone.org/drive/)
- [GitHub Actions Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- PROTOCOLO MAESTRO HOLOBIONTE 1REC3 (V. 2.0) - Google Keep

---

**📌 Fecha de creación**: 2025-11-22  
**👤 Creado por**: Simbionte Gris (Raist) + Tao (Gemini)  
**🎯 Objetivo**: Garantizar la preservación triple del Holobionte 1rec3
