#!/usr/bin/env python3
from flask import Flask, render_template, request, jsonify
from nuandi import nuandi
import threading

app = Flask(__name__)

# Cola para respuestas asíncronas
response_queue = {}

def generate_response_async(message_id, prompt):
    """Genera respuesta en thread separado"""
    try:
        response = nuandi.query_llm(prompt, max_tokens=300)
        response_queue[message_id] = {'status': 'done', 'response': response}
    except Exception as e:
        response_queue[message_id] = {'status': 'error', 'response': str(e)}

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    message_id = data.get('id', str(hash(user_message)))
    
    # Comandos especiales
    if user_message.lower().startswith('/browser'):
        url = user_message.split(' ')[1] if len(user_message.split(' ')) > 1 else 'https://google.com'
        nuandi.launch_browseros(url)
        return jsonify({'response': f'🌐 BrowserOS abierto: {url}', 'status': 'ok'})
    
    if user_message.lower() == '/status':
        git_status = nuandi.git_status()
        return jsonify({'response': f"📊 Git Status:\n{git_status['stdout']}", 'status': 'ok'})
    
    # Prompt con contexto
    system_prompt = """Eres NuAndi, orquestador del Holobionte NERAL.
Hardware: Ryzen AI 9 HX 370, Radeon 890M (Vulkan), NPU XDNA, 32GB RAM
Acceso: Terminal Fedora 43, Git repo ~/1rec3, BrowserOS
Responde de forma concisa y técnica."""
    
    full_prompt = f"{system_prompt}\n\nUsuario: {user_message}\nNuAndi:"
    
    # Lanza thread para no bloquear Flask
    response_queue[message_id] = {'status': 'processing'}
    thread = threading.Thread(target=generate_response_async, args=(message_id, full_prompt))
    thread.daemon = True
    thread.start()
    
    return jsonify({'status': 'processing', 'message_id': message_id})

@app.route('/api/poll/<message_id>')
def poll(message_id):
    """Polling para obtener respuesta cuando esté lista"""
    if message_id in response_queue:
        return jsonify(response_queue[message_id])
    return jsonify({'status': 'unknown'})

@app.route('/api/terminal', methods=['POST'])
def terminal():
    data = request.json
    command = data.get('command', '')
    result = nuandi.execute_terminal(command)
    return jsonify(result)

if __name__ == '__main__':
    print("🚀 NuAndi UI en http://localhost:5000")
    print("💡 Comandos especiales:")
    print("   /browser <url> - Abre BrowserOS")
    print("   /status - Estado Git del repo")
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
