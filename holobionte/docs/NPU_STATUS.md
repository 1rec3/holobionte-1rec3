# NPU XDNA Status - 23 Nov 2025

## Hardware
✅ Device: /dev/accel/accel0
✅ Driver: amdxdna (kernel module)
✅ Specs: 50 TOPS (Ryzen AI)

## Software Stack
❌ Ollama: No soporta NPU (solo CPU/GPU)
⚠️  llama.cpp: Soporte experimental
❌ XRT: No instalado completamente

## Por qué no funciona ahora

1. Ollama no tiene backend NPU
2. AMD XRT inmaduro para XDNA
3. Drivers en desarrollo (beta)
4. Toolchain incompleto

## Roadmap NPU

### Corto plazo (imposible ahora):
- Ollama no planea NPU support
- Esperar AMD XRT stable

### Mediano plazo (3-6 meses):
- Compilar llama.cpp con XDNA
- Test modelos pequeños (7B)
- Benchmark vs GPU

### Largo plazo (2026):
- Stack maduro AMD
- Integración nativa
- Offload automático CPU→GPU→NPU

## Alternativa ACTUAL

✅ Usar GPU Radeon 890M (funciona)
✅ Esperar madurez NPU stack
✅ Threadripper futuro (GPU clusters)
