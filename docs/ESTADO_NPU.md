# Estado NPU Integration (22 Nov 2025)

## Hardware
- NPU: AMD XDNA (Ryzen AI 9 HX 370)
- GPU: Radeon 890M (Vulkan)
- Driver: amdxdna cargado correctamente

## Intentos NPU
1. ❌ onnxruntime-amd-npu: No existe en PyPI
2. ❌ xdna-driver compile: Requiere XRT completo
3. ❌ llama.cpp xet-la: Rama no existe
4. ✅ Driver kernel: Funcionando (lsmod)

## Solución temporal
- Usar GPU (Vulkan) + CPU híbrido
- 40 capas GPU + 25 CPU
- Rendimiento aceptable: ~8-12 tok/s

## Next steps NPU
- Esperar a AMD libere XRT para Ryzen AI Linux
- O reverse engineer xdna protocol
- O contribuir a llama.cpp backend NPU
