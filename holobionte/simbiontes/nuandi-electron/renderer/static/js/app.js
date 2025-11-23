const chatContainer = document.getElementById('chatContainer');
const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');

function addMessage(content, type) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type}`;
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    contentDiv.innerHTML = content.replace(/\n/g, '<br>');
    messageDiv.appendChild(contentDiv);
    chatContainer.appendChild(messageDiv);
    chatContainer.scrollTop = chatContainer.scrollHeight;
    return messageDiv;
}

async function sendMessage() {
    const message = messageInput.value.trim();
    if (!message) return;
    
    addMessage(message, 'user');
    messageInput.value = '';
    sendButton.disabled = true;
    
    const assistantMsg = addMessage('⏳ Procesando...', 'assistant');
    
    try {
        // Comandos especiales
        if (message.toLowerCase().startsWith('/browser')) {
            const url = message.split(' ')[1] || 'https://google.com';
            const result = await window.nuandi.launchBrowser(url);
            assistantMsg.querySelector('.message-content').innerHTML = `🌐 ${result}`;
        }
        else if (message.toLowerCase() === '/status') {
            const result = await window.nuandi.execCommand('cd ~/1rec3 && git status');
            assistantMsg.querySelector('.message-content').innerHTML = `📊 Git Status:<br><pre>${result.stdout}</pre>`;
        }
        else if (message.toLowerCase().startsWith('/read')) {
            const filepath = message.split(' ')[1];
            const content = await window.nuandi.readFile(filepath);
            assistantMsg.querySelector('.message-content').innerHTML = `📄 ${filepath}:<br><pre>${content.substring(0, 500)}...</pre>`;
        }
        else {
            // Consulta al LLM
            const systemPrompt = `Eres NuAndi, orquestador del Holobionte NERAL.
Hardware: Ryzen AI 9 HX 370, Radeon 890M, NPU XDNA, 32GB RAM
Acceso: Sistema completo, terminal, Git, BrowserOS
Responde de forma concisa y técnica.`;
            
            const fullPrompt = `${systemPrompt}\n\nUsuario: ${message}\nNuAndi:`;
            const response = await window.nuandi.queryLLM(fullPrompt);
            assistantMsg.querySelector('.message-content').textContent = response;
        }
    } catch (error) {
        assistantMsg.querySelector('.message-content').textContent = `Error: ${error.message}`;
    }
    
    sendButton.disabled = false;
    messageInput.focus();
}

sendButton.addEventListener('click', sendMessage);
messageInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});

// Mensaje de bienvenida con info del sistema
window.addEventListener('DOMContentLoaded', async () => {
    const sysInfo = await window.nuandi.execCommand('uname -a');
    console.log('Sistema:', sysInfo.stdout);
});
