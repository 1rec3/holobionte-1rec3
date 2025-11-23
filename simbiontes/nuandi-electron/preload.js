const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('nuandi', {
  execCommand: (cmd) => ipcRenderer.invoke('exec-command', cmd),
  queryLLM: (prompt) => ipcRenderer.invoke('query-llm', prompt),
  launchBrowser: (url) => ipcRenderer.invoke('launch-browser', url),
  readFile: (path) => ipcRenderer.invoke('read-file', path),
  writeFile: (path, content) => ipcRenderer.invoke('write-file', path, content)
});

// Repo Understanding API
electronAPI.readFile = (filePath) => ipcRenderer.invoke('read-file', filePath);
electronAPI.listRepoFiles = (query) => ipcRenderer.invoke('list-repo-files', query);

console.log('📚 Repo API expuesto');
