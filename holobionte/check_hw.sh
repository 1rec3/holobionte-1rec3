#!/bin/bash
# Check hardware on-demand (no loop)

echo "📊 HARDWARE STATUS - $(date +%H:%M:%S)"
echo ""
echo "🔥 CPU: $(grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {printf "%.1f%%", usage}')"
echo "💾 RAM: $(free -h | awk '/^Mem/ {print $3 "/" $2}')"
echo "🎮 GPU: $(rocm-smi --showmeminfo vram 2>/dev/null | grep -q "VRAM" && echo "OK" || echo "N/A")"
echo "⚡ NPU: $([ -e /dev/accel/accel0 ] && echo "disponible (50 TOPS)" || echo "N/A")"
