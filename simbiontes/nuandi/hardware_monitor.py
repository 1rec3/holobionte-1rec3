#!/usr/bin/env python3
"""
Hardware Monitor - CPU, RAM, GPU, NPU en tiempo real
"""
import subprocess
import time
import psutil
from pathlib import Path

class HardwareMonitor:
    def __init__(self):
        self.gpu_available = self.check_gpu()
        self.npu_available = self.check_npu()
    
    def check_gpu(self):
        """Verifica si GPU AMD está disponible"""
        try:
            result = subprocess.run(['rocm-smi'], capture_output=True, timeout=2)
            return result.returncode == 0
        except:
            return False
    
    def check_npu(self):
        """Verifica si NPU está disponible"""
        return Path("/dev/accel/accel0").exists()
    
    def get_cpu_stats(self):
        """Stats CPU"""
        return {
            "usage": psutil.cpu_percent(interval=0.5),
            "cores": psutil.cpu_count(),
            "freq": psutil.cpu_freq().current if psutil.cpu_freq() else 0
        }
    
    def get_ram_stats(self):
        """Stats RAM"""
        mem = psutil.virtual_memory()
        return {
            "total": mem.total // (1024**3),  # GB
            "used": mem.used // (1024**3),
            "available": mem.available // (1024**3),
            "percent": mem.percent
        }
    
    def get_gpu_stats(self):
        """Stats GPU AMD"""
        if not self.gpu_available:
            return {"error": "GPU no disponible"}
        
        try:
            result = subprocess.run(
                ['rocm-smi', '--showmeminfo', 'vram', '--json'],
                capture_output=True,
                timeout=2,
                text=True
            )
            # Parse JSON output
            return {"raw": result.stdout}
        except:
            return {"error": "rocm-smi falló"}
    
    def get_npu_stats(self):
        """Stats NPU XDNA"""
        if not self.npu_available:
            return {"error": "NPU no disponible"}
        
        # TODO: Implementar lectura NPU cuando driver esté maduro
        return {"status": "disponible", "tops": 50}
    
    def print_stats(self):
        """Imprime stats formateadas"""
        cpu = self.get_cpu_stats()
        ram = self.get_ram_stats()
        gpu = self.get_gpu_stats()
        npu = self.get_npu_stats()
        
        print(f"\n{'='*60}")
        print(f"📊 HARDWARE MONITOR - {time.strftime('%H:%M:%S')}")
        print(f"{'='*60}")
        
        print(f"\n🔥 CPU: {cpu['usage']:.1f}% | {cpu['cores']} cores | {cpu['freq']:.0f} MHz")
        print(f"💾 RAM: {ram['used']}/{ram['total']} GB ({ram['percent']:.1f}%)")
        print(f"🎮 GPU: {gpu.get('error', 'OK')}")
        print(f"⚡ NPU: {npu.get('status', 'N/A')} ({npu.get('tops', 0)} TOPS)")
        
        # Alertas
        if ram['percent'] > 90:
            print(f"\n⚠️  ALERTA: RAM al {ram['percent']:.1f}%")
        if cpu['usage'] > 90:
            print(f"\n⚠️  ALERTA: CPU al {cpu['usage']:.1f}%")

if __name__ == "__main__":
    monitor = HardwareMonitor()
    
    print("🌟 Monitor Hardware iniciado (Ctrl+C para salir)")
    
    try:
        while True:
            monitor.print_stats()
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n\n👋 Monitor detenido")
