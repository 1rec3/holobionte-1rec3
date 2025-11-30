
// ================================================
// REPO COMMANDS - /read y /list
// ================================================

// Procesa comandos repo
async function handleRepoCommand(command, args) {
  if (command === '/read') {
    if (!args) {
      addMessage('❌ Uso: /read <archivo>', 'system');
      return;
    }
    
    addMessage(`📖 Leyendo ${args}...`, 'system');
    
    const result = await window.electronAPI.readFile(args);
    
    if (result.success) {
      addMessage(`
📄 **${args}**
📊 ${result.stats.lines} líneas, ${result.stats.size}

🤖 **Análisis R1:**
${result.analysis}

💾 Contenido disponible en consola DevTools
`, 'assistant');
      console.log('File content:', result.content);
    } else {
      addMessage(`❌ Error: ${result.error}`, 'system');
    }
  }
  
  if (command === '/list') {
    addMessage('📂 Listando archivos...', 'system');
    
    const result = await window.electronAPI.listRepoFiles(args || '');
    
    if (result.success) {
      const filesList = result.files.slice(0, 20).map(f => `• ${f}`).join('\n');
      addMessage(`
📂 **Archivos del repo** (${result.total} total)

${filesList}

${result.total > 20 ? '... (mostrando primeros 20)' : ''}

💡 Usa: /read <archivo> para analizar
`, 'assistant');
    } else {
      addMessage(`❌ Error: ${result.error}`, 'system');
    }
  }
}

// Modifica sendMessage() para detectar comandos
const originalSendMessage = sendMessage;
sendMessage = async function() {
  const userInput = document.getElementById('userInput').value.trim();
  
  if (userInput.startsWith('/read ') || userInput.startsWith('/list')) {
    const [command, ...argsParts] = userInput.split(' ');
    const args = argsParts.join(' ');
    
    addMessage(userInput, 'user');
    document.getElementById('userInput').value = '';
    
    await handleRepoCommand(command, args);
    return;
  }
  
  // Comportamiento original para mensajes normales
  return originalSendMessage.apply(this, arguments);
};

console.log('📚 Repo commands integrados');

// ================================================
// AVATARES ASCII ANIMADOS TIEMPO REAL
// ================================================

const asciiAvatars = {
  thinking: [
    `
    🤔
   /|\\
    |
   / \\`,
    `
    🤔
   \\|/
    |
   / \\`,
    `
    🤔
   /|\\
    |
   / \\`
  ],
  happy: [
    `
    😊
   \\|/
    |
   / \\`,
    `
    😊
   /|\\
    |
   / \\`
  ],
  coding: [
    `
    💻
   /|\\
    |
   / \\`,
    `
    💻
   \\|/
    |
   / \\`
  ],
  searching: [
    `
    🔍
   /|\\
    |
   / \\`,
    `
    🔎
   \\|/
    |
   / \\`
  ],
  neutral: `
    🤖
   /|\\
    |
   / \\`
};

let currentAvatar = 'neutral';
let avatarFrame = 0;
let avatarInterval = null;

function showAvatar(state, duration = 3000) {
  currentAvatar = state;
  avatarFrame = 0;
  
  const avatarEl = document.getElementById('ascii-avatar');
  if (!avatarEl) return;
  
  // Limpia interval anterior
  if (avatarInterval) clearInterval(avatarInterval);
  
  const frames = Array.isArray(asciiAvatars[state]) 
    ? asciiAvatars[state] 
    : [asciiAvatars[state]];
  
  // Muestra primer frame
  avatarEl.textContent = frames[0];
  avatarEl.style.display = 'block';
  
  // Anima si tiene múltiples frames
  if (frames.length > 1) {
    avatarInterval = setInterval(() => {
      avatarFrame = (avatarFrame + 1) % frames.length;
      avatarEl.textContent = frames[avatarFrame];
    }, 500);
  }
  
  // Auto-oculta después de duración
  if (duration > 0) {
    setTimeout(() => {
      avatarEl.style.display = 'none';
      if (avatarInterval) {
        clearInterval(avatarInterval);
        avatarInterval = null;
      }
    }, duration);
  }
}

// Modifica sendMessage para mostrar avatares
const originalSendMessage = window.sendMessage || function() {};
window.sendMessage = async function() {
  showAvatar('thinking', 5000);
  await originalSendMessage.apply(this, arguments);
  showAvatar('happy', 2000);
};

console.log('🎭 Avatares ASCII cargados');

// Estados avatar automáticos
function updateAvatarByContext(userMessage, assistantResponse) {
  const msg = userMessage.toLowerCase();
  
  if (msg.includes('código') || msg.includes('programa')) {
    showAvatar('coding', 4000);
  } else if (msg.includes('busca') || msg.includes('encuentra')) {
    showAvatar('searching', 4000);
  } else if (msg.includes('piensa') || msg.includes('analiza')) {
    showAvatar('thinking', 6000);
  } else if (assistantResponse && assistantResponse.length > 100) {
    showAvatar('happy', 3000);
  } else {
    showAvatar('neutral', 2000);
  }
}

console.log('🎭 Estados contextuales activos');
