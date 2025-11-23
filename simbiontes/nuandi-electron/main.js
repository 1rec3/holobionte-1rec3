const { app, BrowserWindow, ipcMain } = require('electron');
const { spawn } = require('child_process');
const path = require('path');
const http = require('http');

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 900,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.js')
    },
    backgroundColor: '#667eea'
  });

  mainWindow.loadFile('renderer/index.html');
  mainWindow.webContents.openDevTools();
  mainWindow.on('closed', () => { mainWindow = null; });
}

app.whenReady().then(createWindow);
app.on('window-all-closed', () => { if (process.platform !== 'darwin') app.quit(); });
app.on('activate', () => { if (BrowserWindow.getAllWindows().length === 0) createWindow(); });

// FIX: Handler LLM
ipcMain.handle('query-llm', async (event, prompt) => {
  console.log('🔥 Query recibido:', prompt);
  
  return new Promise((resolve, reject) => {
    const postData = JSON.stringify({
      model: "deepseek-r1:8b",
      prompt: prompt,
      stream: false
    });

    const options = {
      hostname: 'localhost',
      port: 11434,
      path: '/api/generate',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(postData)
      },
      timeout: 60000
    };

    console.log('📡 Enviando a Ollama...');

    const req = http.request(options, (res) => {
      let data = '';
      
      res.on('data', (chunk) => { 
        data += chunk; 
        console.log('📥 Chunk recibido:', chunk.length, 'bytes');
      });
      
      res.on('end', () => {
        console.log('✅ Respuesta completa');
        try {
          const response = JSON.parse(data);
          console.log('✅ JSON parseado OK');
          resolve(response.response || 'Sin respuesta');
        } catch (e) {
          console.error('❌ Error parsing JSON:', e);
          resolve('Error: ' + data.substring(0, 200));
        }
      });
    });

    req.on('error', (e) => { 
      console.error('❌ Error request:', e);
      reject(e); 
    });
    
    req.on('timeout', () => {
      console.error('⏱️ Timeout');
      req.destroy();
      reject(new Error('Timeout'));
    });

    req.write(postData);
    req.end();
  });
});

ipcMain.handle('exec-command', async (event, command) => {
  return new Promise((resolve) => {
    const proc = spawn('bash', ['-c', command]);
    let stdout = '', stderr = '';
    proc.stdout.on('data', (data) => { stdout += data.toString(); });
    proc.stderr.on('data', (data) => { stderr += data.toString(); });
    proc.on('close', (code) => { resolve({ stdout, stderr, returncode: code }); });
  });
});

ipcMain.handle('launch-browser', async (event, url) => {
  const browserPath = path.join(process.env.HOME, 'holobionte/apps/BrowserOS.AppImage');
  spawn(browserPath, [`--app=${url}`], { detached: true });
  return `BrowserOS abierto: ${url}`;
});

console.log('🤖 NuAndi Electron + DeepSeek R1 8B LISTO');

// ================================================
// REPO UNDERSTANDING - Handler /read
// ================================================
const { execSync } = require('child_process');

ipcMain.handle('read-file', async (event, filePath) => {
  console.log('📖 Reading file:', filePath);
  
  const repoPath = path.join(process.env.HOME, '1rec3');
  const fullPath = path.join(repoPath, filePath);
  const fs = require('fs');
  
  try {
    // Lee contenido
    const content = fs.readFileSync(fullPath, 'utf8');
    
    // Análisis básico
    const lines = content.split('\n').length;
    const size = (content.length / 1024).toFixed(2);
    
    // Envía a R1 para análisis profundo
    const analysisPrompt = `Analiza este archivo del repositorio Holobionte NERAL:

Archivo: ${filePath}
Líneas: ${lines}
Tamaño: ${size} KB

Código:
\`\`\`
${content.substring(0, 3000)}${content.length > 3000 ? '\n... (truncado)' : ''}
\`\`\`

Responde:
1. Propósito del archivo
2. Funciones/componentes clave
3. 2-3 mejoras concretas posibles
`;

    const analysis = await new Promise((resolve) => {
      const postData = JSON.stringify({
        model: "deepseek-r1:8b",
        prompt: analysisPrompt,
        stream: false
      });

      const options = {
        hostname: 'localhost',
        port: 11434,
        path: '/api/generate',
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Content-Length': Buffer.byteLength(postData)
        },
        timeout: 90000
      };

      const req = http.request(options, (res) => {
        let data = '';
        res.on('data', (chunk) => { data += chunk; });
        res.on('end', () => {
          try {
            const response = JSON.parse(data);
            resolve(response.response || 'Sin análisis');
          } catch (e) {
            resolve('Error parseando análisis');
          }
        });
      });

      req.on('error', () => resolve('Error conectando Ollama'));
      req.on('timeout', () => resolve('Timeout análisis'));
      req.write(postData);
      req.end();
    });
    
    return {
      success: true,
      content: content,
      stats: { lines, size: size + ' KB' },
      analysis: analysis
    };
    
  } catch (e) {
    return {
      success: false,
      error: e.message
    };
  }
});

// Handler para listar archivos del repo
ipcMain.handle('list-repo-files', async (event, query) => {
  console.log('📂 Listing repo files:', query || 'all');
  
  try {
    const indexPath = path.join(process.env.HOME, '1rec3/holobionte/simbiontes/nuandi/repo_index.json');
    const indexContent = require('fs').readFileSync(indexPath, 'utf8');
    const index = JSON.parse(indexContent);
    
    let files = Object.keys(index);
    
    if (query) {
      files = files.filter(f => f.toLowerCase().includes(query.toLowerCase()));
    }
    
    return {
      success: true,
      files: files.slice(0, 50), // Máximo 50 resultados
      total: files.length
    };
    
  } catch (e) {
    return {
      success: false,
      error: e.message
    };
  }
});

console.log('📚 Repo Understanding handlers añadidos');

// ================================================
// ORCHESTRATOR HANDLERS
// ================================================

ipcMain.handle('sync-repo', async (event) => {
  console.log('📦 Syncing repo...');
  
  const result = await new Promise((resolve) => {
    const proc = spawn('python3', [
      path.join(process.env.HOME, '1rec3/holobionte/simbiontes/nuandi/orchestrator.py')
    ]);
    
    let output = '';
    proc.stdout.on('data', (data) => { output += data.toString(); });
    proc.on('close', () => {
      try {
        resolve(JSON.parse(output));
      } catch (e) {
        resolve({ status: "processed" });
      }
    });
  });
  
  return result;
});

ipcMain.handle('open-browser', async (event, url) => {
  console.log('🌐 Opening browser:', url);
  
  const browserPath = path.join(process.env.HOME, 'holobionte/apps/BrowserOS.AppImage');
  
  try {
    spawn(browserPath, [`--app=${url}`], { detached: true });
    return { status: "ok", url };
  } catch (e) {
    return { status: "error", error: e.message };
  }
});

ipcMain.handle('open-repo-file', async (event, filePath) => {
  const githubUrl = `https://github.com/1rec3/holobionte-1rec3/blob/main/${filePath}`;
  const browserPath = path.join(process.env.HOME, 'holobionte/apps/BrowserOS.AppImage');
  
  try {
    spawn(browserPath, [`--app=${githubUrl}`], { detached: true });
    return { status: "ok", file: filePath };
  } catch (e) {
    return { status: "error", error: e.message };
  }
});

console.log('🎯 Orchestrator handlers integrados');
