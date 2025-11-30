const chatContainer = document.getElementById('chatContainer');
const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');

function addMessage(content, type) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type}`;
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    contentDiv.textContent = content;
    messageDiv.appendChild(contentDiv);
    chatContainer.appendChild(messageDiv);
    chatContainer.scrollTop = chatContainer.scrollHeight;
    return messageDiv;
}

async function pollResponse(messageId, messageDiv) {
    let attempts = 0;
    const maxAttempts = 60;
    
    const poll = async () => {
        try {
            const response = await fetch(`/api/poll/${messageId}`);
            const data = await response.json();
            
            if (data.status === 'done') {
                messageDiv.querySelector('.message-content').textContent = data.response;
                return true;
            } else if (data.status === 'error') {
                messageDiv.querySelector('.message-content').textContent = `Error: ${data.response}`;
                return true;
            } else if (attempts++ < maxAttempts) {
                setTimeout(poll, 1000);
            } else {
                messageDiv.querySelector('.message-content').textContent = 'Timeout';
                return false;
            }
        } catch (error) {
            messageDiv.querySelector('.message-content').textContent = 'Error de conexión';
            return false;
        }
    };
    
    poll();
}

async function sendMessage() {
    const message = messageInput.value.trim();
    if (!message) return;
    
    addMessage(message, 'user');
    messageInput.value = '';
    sendButton.disabled = true;
    
    const messageId = `msg_${Date.now()}`;
    const assistantMsg = addMessage('⏳ Generando...', 'assistant');
    
    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ message, id: messageId })
        });
        
        const data = await response.json();
        
        if (data.status === 'ok') {
            assistantMsg.querySelector('.message-content').textContent = data.response;
        } else if (data.status === 'processing') {
            pollResponse(messageId, assistantMsg);
        }
    } catch (error) {
        assistantMsg.querySelector('.message-content').textContent = 'Error';
    }
    
    sendButton.disabled = false;
    messageInput.focus();
}

sendButton.addEventListener('click', sendMessage);
messageInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') sendMessage();
});
