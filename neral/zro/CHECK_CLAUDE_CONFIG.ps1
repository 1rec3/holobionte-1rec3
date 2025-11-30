# 🔍 SCRIPT DIAGNÓSTICO: Claude Desktop MCP Configuration Checker
# Para usuario: saul3273
# Sistema: Windows 11 (LNV)
# Fecha: 30 noviembre 2025

Write-Host "="*70 -ForegroundColor Cyan
Write-Host "  CLAUDE DESKTOP MCP - DIAGNÓSTICO DE CONFIGURACIÓN" -ForegroundColor Yellow
Write-Host "  Usuario: $env:USERNAME" -ForegroundColor Green
Write-Host "  Sistema: Windows 11" -ForegroundColor Green
Write-Host "="*70 -ForegroundColor Cyan
Write-Host ""

# Ubicación del archivo de configuración
$configPath = "$env:APPDATA\Claude\claude_desktop_config.json"

Write-Host "[1] Verificando ubicación del archivo..." -ForegroundColor Magenta
Write-Host "    Ruta: $configPath" -ForegroundColor Gray

if (Test-Path $configPath) {
    Write-Host "    ✅ Archivo encontrado" -ForegroundColor Green
    Write-Host ""
    
    # Leer y mostrar el contenido
    Write-Host "[2] Contenido actual de claude_desktop_config.json:" -ForegroundColor Magenta
    Write-Host "-"*70 -ForegroundColor Gray
    
    $configContent = Get-Content $configPath -Raw
    Write-Host $configContent -ForegroundColor White
    
    Write-Host "-"*70 -ForegroundColor Gray
    Write-Host ""
    
    # Parsear JSON y analizar servidores MCP
    Write-Host "[3] Análisis de servidores MCP configurados:" -ForegroundColor Magenta
    
    try {
        $config = $configContent | ConvertFrom-Json
        
        if ($config.mcpServers) {
            $serverCount = ($config.mcpServers | Get-Member -MemberType NoteProperty).Count
            Write-Host "    Servidores MCP detectados: $serverCount" -ForegroundColor Cyan
            Write-Host ""
            
            foreach ($serverName in ($config.mcpServers | Get-Member -MemberType NoteProperty | Select-Object -ExpandProperty Name)) {
                Write-Host "    🔧 Servidor: $serverName" -ForegroundColor Yellow
                $server = $config.mcpServers.$serverName
                
                Write-Host "       - Comando: $($server.command)" -ForegroundColor White
                
                if ($server.args) {
                    Write-Host "       - Argumentos:" -ForegroundColor White
                    foreach ($arg in $server.args) {
                        Write-Host "         * $arg" -ForegroundColor Gray
                    }
                }
                
                if ($server.env) {
                    Write-Host "       - Variables de entorno:" -ForegroundColor White
                    foreach ($envVar in ($server.env | Get-Member -MemberType NoteProperty | Select-Object -ExpandProperty Name)) {
                        $value = $server.env.$envVar
                        # Ocultar valores sensibles parcialmente
                        if ($value.Length -gt 10) {
                            $hiddenValue = $value.Substring(0,5) + "..." + $value.Substring($value.Length-5)
                        } else {
                            $hiddenValue = "***"
                        }
                        Write-Host "         * $envVar = $hiddenValue" -ForegroundColor Gray
                    }
                }
                Write-Host ""
            }
        } else {
            Write-Host "    ⚠️ No hay servidores MCP configurados" -ForegroundColor Yellow
        }
    } catch {
        Write-Host "    ❌ Error al parsear JSON: $_" -ForegroundColor Red
    }
    
} else {
    Write-Host "    ❌ Archivo NO encontrado" -ForegroundColor Red
    Write-Host "    ⚠️ Claude Desktop aún no ha sido configurado" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "    Para crear el archivo:" -ForegroundColor Cyan
    Write-Host "    1. Abre Claude Desktop" -ForegroundColor White
    Write-Host "    2. Ve a: Claude > Settings > Developer" -ForegroundColor White
    Write-Host "    3. Click en 'Edit Config'" -ForegroundColor White
}

Write-Host ""
Write-Host "[4] Verificando Node.js (requerido para MCP):" -ForegroundColor Magenta

try {
    $nodeVersion = node --version
    Write-Host "    ✅ Node.js instalado: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "    ❌ Node.js NO encontrado" -ForegroundColor Red
    Write-Host "    ⚠️ Instalar con: winget install OpenJS.NodeJS.LTS" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "[5] Verificando NPM:" -ForegroundColor Magenta

try {
    $npmVersion = npm --version
    Write-Host "    ✅ NPM instalado: $npmVersion" -ForegroundColor Green
} catch {
    Write-Host "    ❌ NPM NO encontrado" -ForegroundColor Red
}

Write-Host ""
Write-Host "[6] Verificando MCP Filesystem Server:" -ForegroundColor Magenta

try {
    Write-Host "    Testeando acceso a @modelcontextprotocol/server-filesystem..." -ForegroundColor Gray
    $testResult = npm list -g @modelcontextprotocol/server-filesystem 2>&1
    
    if ($testResult -match "empty") {
        Write-Host "    ⚠️ No instalado globalmente" -ForegroundColor Yellow
        Write-Host "    Para instalar: npm install -g @modelcontextprotocol/server-filesystem" -ForegroundColor Cyan
    } else {
        Write-Host "    ✅ MCP Filesystem Server accesible" -ForegroundColor Green
    }
} catch {
    Write-Host "    ❌ Error al verificar" -ForegroundColor Red
}

Write-Host ""
Write-Host "[7] Directorios Holobionte sugeridos:" -ForegroundColor Magenta

$holobionteDirs = @(
    "C:\holobionte",
    "C:\1rec3",
    "$env:USERPROFILE\Desktop",
    "$env:USERPROFILE\Documents\holobionte-1rec3"
)

foreach ($dir in $holobionteDirs) {
    if (Test-Path $dir) {
        Write-Host "    ✅ $dir (existe)" -ForegroundColor Green
    } else {
        Write-Host "    ❌ $dir (no existe)" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "="*70 -ForegroundColor Cyan
Write-Host "  DIAGNÓSTICO COMPLETADO" -ForegroundColor Yellow
Write-Host "="*70 -ForegroundColor Cyan
Write-Host ""

# Recomendaciones
Write-Host "💡 RECOMENDACIONES:" -ForegroundColor Yellow
Write-Host ""

if (-not (Test-Path $configPath)) {
    Write-Host "1. Crear configuración MCP inicial" -ForegroundColor White
    Write-Host "   - Abre Claude Desktop > Settings > Developer > Edit Config" -ForegroundColor Gray
    Write-Host ""
}

if (-not (Test-Path "C:\holobionte")) {
    Write-Host "2. Crear directorio Holobionte:" -ForegroundColor White
    Write-Host "   mkdir C:\holobionte" -ForegroundColor Gray
    Write-Host ""
}

Write-Host "3. Consultar guía completa:" -ForegroundColor White
Write-Host "   GitHub: holobionte-1rec3/neral/zro/SKYLANDERS_MCP_MATRIX.md" -ForegroundColor Gray
Write-Host ""

Write-Host "Presiona cualquier tecla para salir..." -ForegroundColor Cyan
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
