# 🚀 Roadmap Potencia - 32B + NPU

## Estado Actual (23 Nov 2025)

✅ R1 8B funcionando (GPU)
✅ RAM: 32GB (suficiente 8B)
⏳ NPU: Hardware listo, software inmaduro
❌ 32B: Necesita optimización

---

## Plan R1 32B

### Requisitos
- RAM: 32GB mínimo (tenemos ✅)
- GPU VRAM: 16GB+ (tenemos 512MB ❌)
- Contexto limitado: 2048 tokens
- Swap: 64GB adicional

### Setup 32B

\`\`\`bash
# 1. Aumenta swap
sudo fallocate -l 64G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# 2. Limita contexto Ollama
sudo tee -a /etc/systemd/system/ollama.service.d/override.conf << 'END'
Environment="OLLAMA_CONTEXT_LENGTH=2048"
Environment="OLLAMA_MAX_VRAM=512MB"
END

sudo systemctl daemon-reload
sudo systemctl restart ollama

# 3. Descarga 32B
ollama pull deepseek-r1:32b

# 4. Test (será LENTO en CPU)
time curl http://localhost:11434/api/generate -d '{
  "model":"deepseek-r1:32b",
  "prompt":"test",
  "stream":false
}'
\`\`\`

### Resultado Esperado
- ⏱️  Tiempo: 60-90s por respuesta
- 💾 RAM: ~28-30GB usado
- 🎯 Calidad: Mejor razonamiento

---

## Plan NPU Integration

### Timeline

**Dic 2025:** Monitor NPU
- Script check NPU usage
- Logs actividad

**Ene-Feb 2026:** Test experimental
- llama.cpp + XRT
- Modelo 7B en NPU
- Benchmark vs GPU

**Mar-Abr 2026:** Threadripper
- 7980X (128 threads)
- Multi-GPU (2x RTX)
- NPU como acelerador

**May 2026:** Production
- Offload automático
- CPU→GPU→NPU
- Clustering devices

---

## Plan Voice Integration

### Objetivo
Chat por voz en tiempo real

### Stack
- Input: Web Speech API (nativo)
- TTS: piper-tts (local)
- Latencia: <500ms

### Implementación

\`\`\`javascript
// Voice input
const recognition = new webkitSpeechRecognition();
recognition.lang = 'es-ES';
recognition.onresult = (event) => {
  const transcript = event.results[0][0].transcript;
  sendMessage(transcript);
};

// Voice output (piper-tts)
async function speak(text) {
  const audio = await fetch('http://localhost:5000/tts', {
    method: 'POST',
    body: JSON.stringify({ text })
  });
  const audioBlob = await audio.blob();
  new Audio(URL.createObjectURL(audioBlob)).play();
}
\`\`\`

---

## Prioridades

1. **Repo Understanding** ✅ (hoy)
2. **Voice Chat** (próxima semana)
3. **32B Test** (este mes)
4. **NPU Monitor** (próximo mes)
5. **Threadripper** (Mar 2026)

