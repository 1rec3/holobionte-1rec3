#!/usr/bin/env python3
import subprocess
from pathlib import Path

class NuAndi:
    def __init__(self):
        self.repo_path = Path.home() / "1rec3"
        self.holobionte_path = Path.home() / "holobionte"
        self.llama_path = self.holobionte_path / "llama.cpp/build/bin/llama-cli"
        self.model_path = self.holobionte_path / "models/qwen32b.gguf"
        self.browseros_path = self.holobionte_path / "apps/BrowserOS.AppImage"
        self.shared_path = self.holobionte_path / "shared"
    
    def execute_terminal(self, command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
            return {"stdout": result.stdout, "stderr": result.stderr, "returncode": result.returncode}
        except Exception as e:
            return {"error": str(e)}
    
    def query_llm(self, prompt, max_tokens=200):
        """Consulta rápida al LLM (reducido a 200 tokens)"""
        cmd = f'{self.llama_path} -m {self.model_path} -ngl 50 -c 2048 -n {max_tokens} -p "{prompt}" 2>/dev/null'
        result = self.execute_terminal(cmd)
        # Extrae solo la respuesta del modelo
        output = result.get("stdout", "")
        # Limpia output de llama.cpp
        lines = output.split('\n')
        response_lines = []
        capture = False
        for line in lines:
            if 'NuAndi:' in line or capture:
                capture = True
                response_lines.append(line)
        return '\n'.join(response_lines).strip() if response_lines else "Error al generar respuesta"
    
    def git_status(self):
        return self.execute_terminal(f"cd {self.repo_path} && git status")
    
    def launch_browseros(self, url="https://www.google.com"):
        """Lanza BrowserOS con URL específica"""
        cmd = f'{self.browseros_path} --app={url} &'
        return self.execute_terminal(cmd)

nuandi = NuAndi()

if __name__ == "__main__":
    print("🤖 NuAndi operativo")
    print(f"📁 Repo: {nuandi.repo_path}")
    print(f"🧠 LLM: {nuandi.model_path.name}")
    print(f"🌐 Browser: {nuandi.browseros_path.name}")
