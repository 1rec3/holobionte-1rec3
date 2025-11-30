#!/usr/bin/env python3
"""
NuAndi Auto-Mejora
"""
import requests
import json
from pathlib import Path
from datetime import datetime

class NuAndiAutoImprove:
    def __init__(self):
        self.model = "deepseek-r1:32b"
        self.ollama_url = "http://localhost:11434/api/generate"
        self.holobionte_path = Path.home() / "holobionte"
        self.log_path = self.holobionte_path / "logs" / "auto_improve.log"
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        print("🌱 NuAndi Auto-Mejora iniciado")
    
    def query_r1(self, prompt, context=""):
        system_prompt = f"""Eres NuAndi, cerebro del Holobionte NERAL.
Hardware: Ryzen AI 9 HX 370, Radeon 890M, NPU XDNA, 32GB RAM
{context}"""
        
        full_prompt = f"{system_prompt}\n\n{prompt}"
        payload = {"model": self.model, "prompt": full_prompt, "stream": False}
        
        try:
            response = requests.post(self.ollama_url, json=payload, timeout=180)
            return response.json().get("response", "")
        except Exception as e:
            return f"Error: {e}"
    
    def scan_simbiontes(self):
        simbiontes_path = self.holobionte_path / "simbiontes"
        simbiontes = []
        
        for item in simbiontes_path.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                files = list(item.glob("*.py")) + list(item.glob("*.js"))
                simbiontes.append({
                    "name": item.name,
                    "path": str(item),
                    "files": len(files),
                    "size": sum(f.stat().st_size for f in files)
                })
        
        return simbiontes
    
    def optimize_holobionte(self):
        simbiontes = self.scan_simbiontes()
        
        print(f"\n📊 Simbiontes: {len(simbiontes)}")
        for s in simbiontes:
            print(f"  - {s['name']}: {s['files']} archivos")
        
        analysis = self.query_r1(
            f"Estructura:\n{json.dumps(simbiontes, indent=2)}\n\n¿Cómo optimizar?"
        )
        
        print(f"\n🧠 R1 Análisis:\n{analysis[:500]}...")
        
        with open(self.log_path, 'a') as f:
            f.write(f"\n=== {datetime.now()} ===\n{analysis}\n")
        
        return analysis

if __name__ == "__main__":
    nuandi = NuAndiAutoImprove()
    nuandi.optimize_holobionte()
    print(f"\n✅ Log: {nuandi.log_path}")
