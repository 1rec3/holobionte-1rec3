# Setup Holobionte 1rec3 - Script de instalación automática
# Comet de Zro @ 1rec3 | 2025

param(
    [Parameter(Mandatory=$false)]
    [string]$OrganoNombre = "desconocido",
    
    [Parameter(Mandatory=$false)]
    [switch]$SkipOllama,
    
    [Parameter(Mandatory=$false)]
    [switch]$SkipGit,
    
    [Parameter(Mandatory=$false)]
    [switch]$Full
)

Write-Host "🔥 Iniciando setup del Holobionte 1rec3..." -ForegroundColor Cyan
Write-Host "Órgano: $OrganoNombre" -ForegroundColor Yellow
Write-Host ""

# Verificar privilegios de administrador
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Host "⚠️  Este script necesita privilegios de administrador." -ForegroundColor Red
    Write-Host "Ejecuta PowerShell como administrador e intenta de nuevo." -ForegroundColor Yellow
    exit 1
}

# Crear estructura de directorios
Write-Host "📁 Creando estructura de directorios..." -ForegroundColor Green
$dirs = @(
    "C:\1rec3\repos",
    "C:\1rec3\vault",
    "C:\1rec3\sync",
    "C:\1rec3\ia",
    "C:\1rec3\scripts",
    "C:\1rec3\temp"
)

foreach ($dir in $dirs) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
        Write-Host "  ✓ Creado: $dir" -ForegroundColor DarkGray
    } else {
        Write-Host "  - Ya existe: $dir" -ForegroundColor DarkGray
    }
}

# Instalar Chocolatey si no existe
if (-not (Get-Command choco -ErrorAction SilentlyContinue)) {
    Write-Host "📦 Instalando Chocolatey..." -ForegroundColor Green
    Set-ExecutionPolicy Bypass -Scope Process -Force
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
    Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
} else {
    Write-Host "📦 Chocolatey ya instalado" -ForegroundColor DarkGreen
}

# Instalar Git
if (-not $SkipGit) {
    if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
        Write-Host "🔧 Instalando Git..." -ForegroundColor Green
        choco install git -y
        $env:Path = [System.Environment]::GetEnvironmentVariable(\"Path\",\"Machine\")
    } else {
        Write-Host "🔧 Git ya instalado" -ForegroundColor DarkGreen
    }
}

# Clonar repositorio
if (Test-Path "C:\1rec3\repos\holobionte-1rec3\.git") {
    Write-Host "📥 Repositorio ya clonado. Actualizando..." -ForegroundColor Yellow
    Set-Location "C:\1rec3\repos\holobionte-1rec3"
    git pull
} else {
    Write-Host "📥 Clonando repositorio holobionte-1rec3..." -ForegroundColor Green
    Set-Location "C:\1rec3\repos"
    git clone https://github.com/1rec3/holobionte-1rec3.git
}

# Instalar Ollama
if (-not $SkipOllama) {
    $ollamaPath = "C:\Users\$env:USERNAME\AppData\Local\Programs\Ollama\ollama.exe"
    if (-not (Test-Path $ollamaPath)) {
        Write-Host "🤖 Descargando Ollama..." -ForegroundColor Green
        $ollamaInstaller = "C:\1rec3\temp\OllamaSetup.exe"
        Invoke-WebRequest -Uri "https://ollama.com/download/OllamaSetup.exe" -OutFile $ollamaInstaller
        
        Write-Host "🤖 Instalando Ollama..." -ForegroundColor Green
        Start-Process -FilePath $ollamaInstaller -Wait -ArgumentList "/SILENT"
        
        # Esperar a que Ollama esté disponible
        Start-Sleep -Seconds 5
        
        # Descargar modelos recomendados
        Write-Host "📦 Descargando modelos de IA..." -ForegroundColor Green
        & "C:\Users\$env:USERNAME\AppData\Local\Programs\Ollama\ollama.exe" pull llama3.2:3b
        Write-Host "  ✓ llama3.2:3b descargado" -ForegroundColor DarkGray
    } else {
        Write-Host "🤖 Ollama ya instalado" -ForegroundColor DarkGreen
    }
}

# Instalar aplicaciones adicionales si modo Full
if ($Full) {
    Write-Host "📦 Instalando aplicaciones adicionales (modo Full)..." -ForegroundColor Green
    
    # Obsidian
    if (-not (Test-Path "C:\Users\$env:USERNAME\AppData\Local\Obsidian\Obsidian.exe")) {
        choco install obsidian -y
    }
    
    # VS Code (útil para edición)
    if (-not (Test-Path "C:\Program Files\Microsoft VS Code\Code.exe")) {
        choco install vscode -y
    }
    
    # GitHub CLI
    if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
        choco install gh -y
    }
}

# Configurar PowerShell Profile
Write-Host "⚙️  Configurando PowerShell profile..." -ForegroundColor Green
$profilePath = $PROFILE.CurrentUserAllHosts
if (-not (Test-Path $profilePath)) {
    New-Item -ItemType File -Path $profilePath -Force | Out-Null
}

$profileContent = @"
# Holobionte 1rec3 PowerShell Profile
# Generado automáticamente por setup-holobionte.ps1

# Navegación rápida
function holo { Set-Location C:\1rec3\repos\holobionte-1rec3 }
function repos { Set-Location C:\1rec3\repos }
function vault { Set-Location C:\1rec3\vault }
function ia { Set-Location C:\1rec3\ia }

# Git shortcuts
function gst { git status }
function gpl { git pull }
function gps { git push }
function gcm { param([string]`$msg) git commit -m "`$msg" }

# Ollama shortcuts
function ollama-list { ollama list }
function ollama-run { param([string]`$model) ollama run `$model }
function ollama-pull { param([string]`$model) ollama pull `$model }

# Sync functions
function sync-repo {
    holo
    git pull origin main
    Write-Host "Repositorio sincronizado" -ForegroundColor Green
}

function sync-all {
    Write-Host "Sincronizando holobionte..." -ForegroundColor Cyan
    sync-repo
    Write-Host "Sincronización completada" -ForegroundColor Green
}

# Display welcome message
Write-Host "🔥 Holobionte 1rec3 - PowerShell activado" -ForegroundColor Cyan
Write-Host "Órgano: $OrganoNombre" -ForegroundColor Yellow
"@

Set-Content -Path $profilePath -Value $profileContent

Write-Host ""
Write-Host "✅ Setup completado exitosamente!" -ForegroundColor Green
Write-Host ""
Write-Host "Próximos pasos:" -ForegroundColor Yellow
Write-Host "  1. Reinicia PowerShell para cargar el nuevo profile"
Write-Host "  2. Ejecuta 'holo' para ir al repositorio"
Write-Host "  3. Ejecuta 'ollama-list' para ver modelos instalados"
Write-Host "  4. Consulta SETUP-COMPLETO.md en neral/zro para más info"
Write-Host ""
Write-Host "Comandos útiles:" -ForegroundColor Cyan
Write-Host "  holo           - Ir a C:\1rec3\repos\holobionte-1rec3"
Write-Host "  repos          - Ir a C:\1rec3\repos"
Write-Host "  sync-repo      - Sincronizar repositorio con GitHub"
Write-Host "  ollama-run     - Ejecutar modelo de Ollama"
Write-Host ""
