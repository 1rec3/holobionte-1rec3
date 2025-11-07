#!/bin/bash
set -e

echo "🚀 Nu - Setup Fase 1"
echo "=================="

# 1. Crear entorno virtual Python
echo "📦 Creando entorno virtual..."
python3 -m venv nu-env
source nu-env/bin/activate

# 2. Instalar dependencias Python
echo "📥 Instalando dependencias Python..."
pip install --upgrade pip
pip install browser-use playwright pytest pytest-asyncio pyyaml python-dotenv aiohttp coloredlogs

# 3. Instalar Playwright browsers
echo "🌐 Instalando navegadores Playwright..."
playwright install chromium

# 4. Instalar Ollama
echo "🧠 Instalando Ollama..."
if ! command -v ollama &> /dev/null; then
    curl -fsSL https://ollama.com/install.sh | sh
else
    echo "✅ Ollama ya instalado"
fi

# 5. Descargar modelo DeepSeek-R1
echo "🤖 Descargando DeepSeek-R1..."
ollama pull deepseek-r1:7b

# 6. Iniciar servidor Ollama en background
echo "🔥 Iniciando servidor Ollama..."
ollama serve &
sleep 5

# 7. Verificar instalación
echo "✅ Verificando instalación..."
python -c "import browser_use; print(\'browser-use:\', browser_use.__version__)"
ollama list

echo ""
echo "✨ Setup completado!"
echo "Para activar el entorno: source nu-env/bin/activate"
echo "Para ejecutar Nu: python nu/core/nuandi.py"
