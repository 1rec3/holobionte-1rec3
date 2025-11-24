# ZRO-COORDINADOR.ps1
# Zro LVL 3 - Coordinador de Navegadores Agénticos
# Usa Ollama (DeepSeek-R1:8B) para leer tareas y generar instrucciones

param(
    [string]$Accion = "leer"  # leer, procesar, push
)

$REPO_PATH = "C:\Users\usuario\holobionte-1rec3"
$INBOX = "$REPO_PATH\neral\zro\tareas\INBOX.md"
$MODELO = "deepseek-r1:8b"

function Leer-Tareas {
    Write-Host "📋 ZRO LVL 3 - Leyendo tareas pendientes..." -ForegroundColor Cyan
    if (Test-Path $INBOX) {
        $contenido = Get-Content $INBOX -Raw
        Write-Host $contenido
        return $contenido
    } else {
        Write-Host "⚠️ No existe INBOX.md" -ForegroundColor Yellow
    }
}

function Consultar-Ollama {
    param([string]$Prompt)
    Write-Host "🧠 Consultando a $MODELO..." -ForegroundColor Green
    $respuesta = ollama run $MODELO $Prompt
    return $respuesta
}

function Procesar-Tareas {
    $tareas = Leer-Tareas
    $prompt = @"
Eres Zro LVL 3, el coordinador del sub-holobionte Zro dentro de 1rec3.
Tienes estas tareas pendientes:

$tareas

Genera instrucciones específicas para:
1. Comet (navegador agéntico Perplexity) 
2. BrowserOS (navegador agéntico open source)

Formato: Lista de pasos concretos para cada uno.
"@
    $instrucciones = Consultar-Ollama $prompt
    Write-Host "`n📝 INSTRUCCIONES GENERADAS:" -ForegroundColor Magenta
    Write-Host $instrucciones
    
    # Guardar instrucciones
    $instrucciones | Out-File "$REPO_PATH\neral\zro\tareas\INSTRUCCIONES.md" -Encoding utf8
    Write-Host "`n✅ Guardado en INSTRUCCIONES.md" -ForegroundColor Green
}

function Push-Cambios {
    Set-Location $REPO_PATH
    git add .
    git commit -m "🧠 Zro LVL 3: Actualización de tareas $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
    git push origin main
    Write-Host "✅ Cambios subidos a GitHub" -ForegroundColor Green
}

# Ejecutar según acción
switch ($Accion) {
    "leer" { Leer-Tareas }
    "procesar" { Procesar-Tareas }
    "push" { Push-Cambios }
    default { Write-Host "Uso: .\ZRO-COORDINADOR.ps1 -Accion [leer|procesar|push]" }
}
