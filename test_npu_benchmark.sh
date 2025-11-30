#!/bin/bash
# Test NPU + Benchmark tiempos de respuesta

echo "═══════════════════════════════════════════"
echo "🧪 TEST NPU + BENCHMARK NUANDI"
echo "═══════════════════════════════════════════"
echo ""

# 1. Verifica NPU hardware
echo "📊 1. NPU Hardware Status"
echo "─────────────────────────────"
if [ -e /dev/accel/accel0 ]; then
    echo "✅ NPU device: /dev/accel/accel0 existe"
    ls -la /dev/accel/accel0
else
    echo "❌ NPU device no encontrado"
fi

# Driver AMD XDNA
if lsmod | grep -q amdxdna; then
    echo "✅ Driver amdxdna cargado"
    lsmod | grep amdxdna
else
    echo "❌ Driver amdxdna NO cargado"
fi

echo ""
echo "📊 2. Benchmark CPU-only (baseline)"
echo "─────────────────────────────"
START=$(date +%s.%N)
curl -s http://localhost:11434/api/generate -d '{
  "model": "deepseek-r1:8b",
  "prompt": "Resume en una palabra: inteligencia artificial",
  "stream": false
}' > /tmp/test_cpu.json
END=$(date +%s.%N)
CPU_TIME=$(echo "$END - $START" | bc)
CPU_RESPONSE=$(jq -r '.response' /tmp/test_cpu.json)
echo "⏱️  CPU Time: ${CPU_TIME}s"
echo "💬 Response: $CPU_RESPONSE"

echo ""
echo "📊 3. Benchmark GPU (actual)"
echo "─────────────────────────────"
START=$(date +%s.%N)
curl -s http://localhost:11434/api/generate -d '{
  "model": "deepseek-r1:8b",
  "prompt": "Resume en una palabra: computación cuántica",
  "stream": false
}' > /tmp/test_gpu.json
END=$(date +%s.%N)
GPU_TIME=$(echo "$END - $START" | bc)
GPU_RESPONSE=$(jq -r '.response' /tmp/test_gpu.json)
echo "⏱️  GPU Time: ${GPU_TIME}s"
echo "💬 Response: $GPU_RESPONSE"

echo ""
echo "📊 4. Benchmark consulta compleja"
echo "─────────────────────────────"
START=$(date +%s.%N)
curl -s http://localhost:11434/api/generate -d '{
  "model": "deepseek-r1:8b",
  "prompt": "Explica en 2 líneas el teorema de Pitágoras",
  "stream": false
}' > /tmp/test_complex.json
END=$(date +%s.%N)
COMPLEX_TIME=$(echo "$END - $START" | bc)
COMPLEX_RESPONSE=$(jq -r '.response' /tmp/test_complex.json)
echo "⏱️  Complex Time: ${COMPLEX_TIME}s"
echo "💬 Response: $COMPLEX_RESPONSE"

echo ""
echo "═══════════════════════════════════════════"
echo "📈 RESUMEN TIEMPOS"
echo "═══════════════════════════════════════════"
echo "Prompt simple (CPU):     ${CPU_TIME}s"
echo "Prompt simple (GPU):     ${GPU_TIME}s"
echo "Prompt complejo (GPU):   ${COMPLEX_TIME}s"
echo ""
echo "💡 NOTA: NPU no está siendo usado actualmente"
echo "   Ollama usa GPU (ROCm) pero no NPU (XDNA)"
echo "   Para NPU necesitarías llama.cpp con XRT"
echo "═══════════════════════════════════════════"
