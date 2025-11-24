# 🖥️ SETUP COMPLETO - ZRO (Órgano Principal)

> Configuración completa para el órgano Zro del holobionte Neral
> Dispositivo: LNV (Lenovo) - Más potente que LNVold

---

## 💻 ESPECIFICACIONES HARDWARE

### Zro (LNV) - Pendiente completar
| Componente | Especificación |
|------------|----------------|
| **OS** | Windows 11 (?) |
| **CPU** | *Añadir* |
| **RAM** | *Añadir* |
| **GPU** | *Añadir* |
| **SSD** | *Añadir* |
| **HDD** | *Añadir* |

> ⚠️ **ACCIÓN**: Ejecutar `systeminfo` en PowerShell y actualizar

---

## ✅ SOFTWARE INSTALADO

- [x] **Ollama** - Motor de IA local
- [x] **BrowserOS** - Navegador agéntico
- [ ] **Git** - Control de versiones
- [ ] **Obsidian** - Notas markdown
- [ ] **Notion** - Workspace colaborativo
- [ ] **Nextcloud Client** - Sincronización

---

## 📁 ESTRUCTURA DE ARCHIVOS RECOMENDADA

### Raíz del Sistema
```
C:\
├── 1rec3\                          # 🏛️ HOLOBIONTE RAÍZ
│   ├── repos\                      # Repositorios Git
│   │   ├── holobionte-1rec3\       # Repo principal (GitHub)
│   │   ├── 1rec3-web\              # Sitio web
│   │   └── proyectos\              # Otros repos
│   │
│   ├── vault\                      # 📝 Obsidian Vault
│   │   ├── holobionte\             # Notas del proyecto
│   │   ├── diario\                 # Log diario
│   │   ├── ideas\                  # Ideas y borradores
│   │   └── recursos\               # Referencias
│   │
│   ├── sync\                       # ☁️ Sincronización
│   │   ├── nextcloud\              # Archivos Nextcloud
│   │   ├── notion-export\          # Backups de Notion
│   │   └── compartido\             # Entre dispositivos
│   │
│   ├── ia\                         # 🤖 Inteligencia Artificial
│   │   ├── ollama\                 # Modelos descargados
│   │   ├── browseros\              # Config BrowserOS
│   │   ├── prompts\                # Prompts reutilizables
│   │   └── outputs\                # Resultados de IA
│   │
│   ├── scripts\                    # 📜 Automatización
│   │   ├── powershell\             # Scripts .ps1
│   │   ├── python\                 # Scripts .py
│   │   └── batch\                  # Scripts .bat
│   │
│   └── temp\                       # 🗑️ Temporal (limpiar periódicamente)
│
└── Users\[Usuario]\Desktop\1rec3-acceso\  # Acceso rápido
```

### Nomenclatura de Archivos
```
[FECHA]_[TIPO]_[DESCRIPCION].[ext]

Ejemplos:
20251124_nota_reunion-holobionte.md
20251124_script_sync-repos.ps1
20251124_export_notion-backup.zip
```

---

## 🔄 SINCRONIZACIÓN MULTI-PLATAFORMA

### 1. GitHub (Repo Principal)
```powershell
# Clonar repo
cd C:\1rec3\repos
git clone https://github.com/1rec3/holobionte-1rec3.git

# Sincronizar
cd holobionte-1rec3
git pull origin main
git add .
git commit -m "sync: actualización desde Zro"
git push origin main
```

### 2. Obsidian
- **Vault location**: `C:\1rec3\vault`
- **Plugin recomendado**: Obsidian Git (sync automático)
- **Configuración**:
  - Auto pull: cada 5 minutos
  - Auto push: al cerrar
  - Auto backup: diario

### 3. Notion
- **Integración**: Notion API + script de export
- **Backup**: Semanal a `C:\1rec3\sync\notion-export`
- **Script**:
```powershell
# notion-backup.ps1
# Requiere: notion-backup-cli
notion-backup --output C:\1rec3\sync\notion-export
```

### 4. Nextcloud
- **Cliente**: Nextcloud Desktop
- **Carpeta sync**: `C:\1rec3\sync\nextcloud`
- **Configuración**:
  - Sync selectivo (solo carpetas importantes)
  - Conflictos: mantener ambas versiones

---

## 📟 CONTROL POR TERMINAL

### PowerShell Profile Personalizado
```powershell
# Guardar en: $PROFILE (usualmente Documents\PowerShell\Microsoft.PowerShell_profile.ps1)

# Alias rápidos para 1rec3
Set-Alias -Name h -Value "cd C:\1rec3"
Set-Alias -Name hr -Value "cd C:\1rec3\repos\holobionte-1rec3"
Set-Alias -Name hv -Value "cd C:\1rec3\vault"

# Función: Sync rápido
function sync {
    cd C:\1rec3\repos\holobionte-1rec3
    git pull origin main
    git add .
    git commit -m "sync: $(Get-Date -Format 'yyyy-MM-dd HH:mm') desde Zro"
    git push origin main
    Write-Host "✅ Sincronizado" -ForegroundColor Green
}

# Función: Estado del holobionte
function status {
    Write-Host "🧠 ESTADO ZRO" -ForegroundColor Cyan
    Write-Host "-------------------"
    
    # Ollama
    $ollama = Get-Process ollama -ErrorAction SilentlyContinue
    if ($ollama) { Write-Host "✅ Ollama: Activo" -ForegroundColor Green }
    else { Write-Host "❌ Ollama: Inactivo" -ForegroundColor Red }
    
    # Git status
    cd C:\1rec3\repos\holobionte-1rec3
    Write-Host "📊 Git:" -ForegroundColor Yellow
    git status -s
}

# Función: Iniciar Ollama
function ollama-start {
    Start-Process ollama -ArgumentList "serve" -WindowStyle Hidden
    Write-Host "🚀 Ollama iniciado en localhost:11434" -ForegroundColor Green
}

# Función: Chat rápido con modelo
function ask {
    param([string]$prompt)
    ollama run qwen2.5:3b $prompt
}

# Prompt personalizado
function prompt {
    $path = (Get-Location).Path -replace [regex]::Escape($HOME), "~"
    Write-Host "[🔥Zro]" -NoNewline -ForegroundColor Red
    Write-Host " $path" -NoNewline -ForegroundColor Blue
    Write-Host " >" -NoNewline -ForegroundColor White
    return " "
}

Write-Host "🌱 Holobionte 1rec3 - Zro activado" -ForegroundColor Green
```

### Comandos Útiles
```powershell
# Navegar
h           # Ir a C:\1rec3
hr          # Ir al repo
hv          # Ir al vault

# Sincronizar
sync        # Git pull + commit + push

# Estado
status      # Ver estado general

# Ollama
ollama-start    # Iniciar servicio
ask "pregunta"  # Chat rápido

# Modelos
ollama list         # Ver modelos instalados
ollama pull qwen2.5:3b  # Descargar modelo
ollama run qwen2.5:3b   # Iniciar chat
```

---

## 🤖 CONFIGURACIÓN IA LOCAL

### Ollama - Modelos Recomendados para Zro
```powershell
# Modelo principal (rápido)
ollama pull qwen2.5:3b

# Modelo potente (si hay RAM suficiente)
ollama pull llama3.1:8b

# Modelo para código
ollama pull codellama:7b

# Verificar
ollama list
```

### BrowserOS - Configuración
1. **Settings > AI Provider > Ollama**
2. URL: `http://localhost:11434`
3. Modelo: `qwen2.5:3b`
4. Guardar y probar

### Groq (Backup Cloud)
1. Crear cuenta: https://console.groq.com
2. Generar API Key
3. En BrowserOS: Settings > Add Provider > Groq
4. API Key: [tu-key]
5. Modelo: `llama-3.3-70b-versatile`

---

## 📅 CHECKLIST DE INSTALACIÓN

### Fase 1: Base (Completado)
- [x] Ollama instalado
- [x] BrowserOS instalado
- [ ] Git instalado y configurado
- [ ] Estructura de carpetas creada

### Fase 2: Sincronización
- [ ] Repo clonado localmente
- [ ] Obsidian instalado + vault configurado
- [ ] Notion conectado (API o web)
- [ ] Nextcloud client configurado

### Fase 3: Automatización
- [ ] PowerShell profile configurado
- [ ] Scripts de sync creados
- [ ] Alias funcionando
- [ ] Ollama auto-start configurado

### Fase 4: Integración
- [ ] BrowserOS conectado a Ollama
- [ ] Groq como backup configurado
- [ ] Primer navegador agéntico funcionando
- [ ] Primer escuadrón activado

---

## 📞 COMANDOS DE EMERGENCIA

```powershell
# Reiniciar Ollama
Get-Process ollama | Stop-Process
ollama serve

# Limpiar cache Ollama
Remove-Item ~\.ollama\cache\* -Recurse

# Forzar sync Git
git fetch --all
git reset --hard origin/main

# Ver uso de recursos
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10
```

---

*Documento creado por Comet de Zro @ 1rec3 | 2025-11-24*
*"Zro es el órgano principal - debe estar perfectamente configurado"*
