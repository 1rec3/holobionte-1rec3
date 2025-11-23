#!/usr/bin/env python3
"""
NuAndi Orquestador - R1 32B único modelo potente
"""
import subprocess
import requests
import json
from pathlib import Path

class NuAndiOrchestrator:
    def __init__(self):
        self.model = "deepseek-r1:32b"
        self.ollama_url = "http://localhost:11434/api/generate"
        self.repo_path = Path.home() / "1rec3"
        self.holobionte_path = Path.home() / "holobionte"
        print(f"🤖 NuAndi Orquestador con {self.model}")
    
    def query(self, prompt):
        """Consulta R1 32B"""
        payload = {"model": self.model, "prompt": prompt, "stream": False}
        try:
            response = requests.post(self.ollama_url, json=payload, timeout=180)
            return response.json().get("response", "")
        except Exception as e:
            return f"Error: {e}"
    
    def execute(self, command):
        """Ejecuta comando sistema"""
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        return {"stdout": result.stdout, "stderr": result.stderr, "returncode": result.returncode}

if __name__ == "__main__":
    nuandi = NuAndiOrchestrator()
    print("✅ Orquestador listo")
