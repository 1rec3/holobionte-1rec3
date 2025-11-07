#!/bin/bash
# Nu - Run Script

set -e

echo "🌀 Iniciando Nu/Nuandi..."

# Activar entorno virtual
if [ -d "nu-env" ]; then
    source nu-env/bin/activate
else
    echo "❌ Error: Entorno virtual no encontrado"
    echo "Ejecuta: bash nu/scripts/setup_environment.sh"
    exit 1
fi

# Verificar Ollama está corriendo
if ! curl -s http://localhost:11434/api/tags > /dev/null; then
    echo "🔥 Iniciando servidor Ollama..."
    ollama serve &
    sleep 5
fi

# Ejecutar Nu
echo "🚀 Ejecutando Nu..."
cd nu
python core/nuandi.py
