#!/usr/bin/env python3
"""
Repo Indexer - Escanea y analiza estructura 1rec3
"""
import os
import json
from pathlib import Path
from datetime import datetime

class RepoIndexer:
    def __init__(self, repo_path="~/1rec3"):
        self.repo_path = Path(repo_path).expanduser()
        self.index = {}
        self.ignore_dirs = {'.git', 'node_modules', '__pycache__', '.cache', 'build'}
        self.target_exts = {'.py', '.js', '.md', '.yaml', '.json', '.sh'}
    
    def scan_repo(self):
        """Escanea repo completo"""
        print(f"🔍 Escaneando {self.repo_path}...")
        
        for root, dirs, files in os.walk(self.repo_path):
            dirs[:] = [d for d in dirs if d not in self.ignore_dirs]
            
            for file in files:
                if Path(file).suffix in self.target_exts:
                    full_path = Path(root) / file
                    rel_path = full_path.relative_to(self.repo_path)
                    
                    self.index[str(rel_path)] = {
                        'type': full_path.suffix,
                        'size': full_path.stat().st_size,
                        'modified': datetime.fromtimestamp(full_path.stat().st_mtime).isoformat()
                    }
        
        print(f"✅ Indexados {len(self.index)} archivos")
        return self.index
    
    def get_file_content(self, rel_path):
        """Lee contenido archivo"""
        full_path = self.repo_path / rel_path
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            return f"Error: {e}"
    
    def search_files(self, query):
        """Busca archivos por nombre"""
        results = [p for p in self.index.keys() if query.lower() in p.lower()]
        return results
    
    def get_stats(self):
        """Estadísticas repo"""
        by_type = {}
        total_size = 0
        
        for path, info in self.index.items():
            ext = info['type']
            by_type[ext] = by_type.get(ext, 0) + 1
            total_size += info['size']
        
        return {
            'total_files': len(self.index),
            'total_size_mb': round(total_size / (1024*1024), 2),
            'by_type': by_type
        }
    
    def save_index(self, output='repo_index.json'):
        """Guarda índice"""
        with open(output, 'w') as f:
            json.dump(self.index, f, indent=2)
        print(f"💾 Índice guardado: {output}")

if __name__ == "__main__":
    indexer = RepoIndexer()
    indexer.scan_repo()
    print(json.dumps(indexer.get_stats(), indent=2))
    indexer.save_index()
