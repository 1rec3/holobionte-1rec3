#!/bin/bash
# Test NPU con llama.cpp (experimental)

echo "🧪 TEST NPU con llama.cpp"
echo ""

# Verifica si llama.cpp existe
if [ -d ~/holobionte/llama.cpp ]; then
    echo "✅ llama.cpp encontrado"
    
    # Verifica build con XDNA
    if [ -f ~/holobionte/llama.cpp/build/bin/llama-cli ]; then
        echo "✅ llama-cli encontrado"
        
        # Test NPU
        echo ""
        echo "📊 Intentando usar NPU..."
        export GGML_NPU=1
        
        # Necesitarías modelo en GGUF format
        if [ -f ~/.ollama/models/blobs/sha256-* ]; then
            echo "⚠️  Modelos Ollama en formato propietario"
            echo "   Necesitas convertir a GGUF para llama.cpp"
        fi
    else
        echo "❌ llama-cli no compilado"
    fi
else
    echo "❌ llama.cpp no instalado"
    echo "   Para NPU necesitas compilar con XRT support"
fi

echo ""
echo "💡 ESTADO NPU:"
echo "   - Hardware: ✅ Disponible (XDNA 50 TOPS)"
echo "   - Driver: ⚠️  Básico (sin optimización)"
echo "   - Software: ❌ No integrado en Ollama"
echo "   - Alternativa: llama.cpp + XRT (proyecto futuro)"
