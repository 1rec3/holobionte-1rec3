#!/usr/bin/env python3
"""
BrowserOS Controller - Desde NuAndi al navegador
"""

import subprocess
import os
from urllib.parse import quote

class BrowserController:
    def __init__(self):
        self.browser_path = os.path.expanduser("~/holobionte/apps/BrowserOS.AppImage")
        self.is_available = os.path.exists(self.browser_path)
    
    def open_url(self, url):
        """Abre URL en BrowserOS"""
        if not url.startswith(('http://', 'https://')):
            url = f"https://{url}"
        
        try:
            subprocess.Popen(
                [self.browser_path, f"--app={url}"],
                detach=True
            )
            return {"status": "ok", "url": url}
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def open_repo_file(self, file_path):
        """Abre archivo del repo en GitHub"""
        github_url = f"https://github.com/1rec3/holobionte-1rec3/blob/main/{file_path}"
        return self.open_url(github_url)
    
    def search(self, query):
        """Busca en navegador"""
        search_url = f"https://duckduckgo.com/?q={quote(query)}"
        return self.open_url(search_url)

if __name__ == "__main__":
    browser = BrowserController()
    print(f"BrowserOS disponible: {browser.is_available}")
