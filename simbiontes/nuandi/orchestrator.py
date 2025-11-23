#!/usr/bin/env python3
"""
NuAndi Orquestador - Sincronización repo + decisiones inteligentes
Integra: Browser, Repositorio, Razonamiento
"""

import os
import json
import subprocess
from pathlib import Path
from datetime import datetime

class HobiontOrchestrator:
    def __init__(self):
        self.repo_path = Path(os.path.expanduser("~/1rec3"))
        self.holobionte_path = self.repo_path / "holobionte"
        self.logs = []
    
    def sync_repo(self, repo_name="1rec3"):
        """Git pull + analiza cambios"""
        try:
            result = subprocess.run(
                ["git", "pull", "origin", "main"],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                timeout=30
            )
            self.log(f"✅ Repo sincronizado: {repo_name}")
            return {"status": "ok", "output": result.stdout}
        except Exception as e:
            self.log(f"❌ Error sync: {e}")
            return {"status": "error", "error": str(e)}
    
    def analyze_changes(self):
        """Analiza qué cambió en repo"""
        try:
            result = subprocess.run(
                ["git", "log", "-1", "--oneline"],
                cwd=self.repo_path,
                capture_output=True,
                text=True
            )
            
            files = subprocess.run(
                ["git", "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD"],
                cwd=self.repo_path,
                capture_output=True,
                text=True
            )
            
            return {
                "last_commit": result.stdout.strip(),
                "changed_files": files.stdout.strip().split('\n')
            }
        except Exception as e:
            return {"error": str(e)}
    
    def get_repo_status(self):
        """Estado actual repo"""
        status = {
            "path": str(self.repo_path),
            "exists": self.repo_path.exists(),
            "timestamp": datetime.now().isoformat()
        }
        
        try:
            result = subprocess.run(
                ["git", "status", "--short"],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                timeout=5
            )
            status["changes"] = result.stdout.count('\n')
            status["dirty"] = len(result.stdout) > 0
        except:
            status["dirty"] = None
        
        return status
    
    def decide_action(self, user_input):
        """
        Inteligencia central - Decide qué hacer
        Browser / Repo / Local compute
        """
        msg = user_input.lower()
        
        if any(w in msg for w in ['browser', 'open', 'url', 'página', 'web']):
            return {"action": "browser", "type": "open_url"}
        
        elif any(w in msg for w in ['repo', 'github', 'git', 'código', 'archivo']):
            return {"action": "repository", "type": "analyze_files"}
        
        elif any(w in msg for w in ['sync', 'sincroniza', 'pull', 'actualiza']):
            return {"action": "sync", "type": "git_sync"}
        
        elif any(w in msg for w in ['status', 'estado', 'cómo', 'qué']):
            return {"action": "status", "type": "system_info"}
        
        else:
            return {"action": "llm", "type": "reasoning"}
    
    def log(self, msg):
        """Registro de actividades"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_msg = f"[{timestamp}] {msg}"
        self.logs.append(log_msg)
        print(log_msg)
    
    def get_orchestration_status(self):
        """Status orquestador"""
        return {
            "repo_status": self.get_repo_status(),
            "last_changes": self.analyze_changes(),
            "logs": self.logs[-10:],  # Últimos 10 logs
            "operational": True
        }

if __name__ == "__main__":
    orchestrator = HobiontOrchestrator()
    print(json.dumps(orchestrator.get_orchestration_status(), indent=2))
