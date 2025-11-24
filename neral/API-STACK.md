# 🔌 API STACK - Holobionte 1rec3

> Stack de APIs de IA organizado por presupuesto

---

## 📊 Resumen de Planes

| Plan | Presupuesto | APIs Incluidas | Tokens/día estimados |
|------|-------------|----------------|---------------------|
| **Plan Cero** | $0/mes | Groq, Google AI, OpenRouter, HuggingChat, Cerebras, Ollama | ~500K+ |
| **Plan Intermedio** | $50-200/mes | + Paid tiers + Together AI + Manus Pro | ~2M+ |
| **Plan Ilimitado** | $500-5000+/mes | + OpenAI Enterprise + Anthropic + GPU cloud | Ilimitado |

---

# 🆓 PLAN CERO ($0/mes)

> Maximizar capacidad con APIs gratuitas

## APIs Cloud Gratuitas

### 1. Groq (PRIORIDAD ALTA)
```
URL: https://console.groq.com/
Modelos: Llama 3.3 70B, Llama 3.1 8B, Mixtral 8x7B, Gemma 2 9B
Límites: 14,400 req/día (~6,000 con modelos grandes)
Velocidad: Extremadamente rápida (LPU)
Latencia: ~100-300ms
API Key: Gratis
```

**Uso recomendado:**
- Consultas rápidas y frecuentes
- Procesamiento de texto en batch
- Navegadores agénticos que necesiten velocidad

### 2. Google AI Studio
```
URL: https://aistudio.google.com/
Modelos: Gemini 2.0 Flash, Gemini 1.5 Pro, Gemini 1.5 Flash
Límites: 60 req/min, 1500 req/día (Gemini 1.5 Flash)
Contexto: Hasta 1M tokens (Gemini 1.5 Pro)
API Key: Gratis con cuenta Google
```

**Uso recomendado:**
- Documentos largos (contexto masivo)
- Análisis multimedia (imágenes, audio, video)
- Tareas que requieran razonamiento profundo

### 3. OpenRouter (Free Tier)
```
URL: https://openrouter.ai/
Modelos gratuitos: Llama 3.1 8B, Mistral 7B, varios open source
Límites: ~50 req/día en tier gratuito
Ventaja: Acceso unificado a múltiples proveedores
```

**Uso recomendado:**
- Backup cuando otras APIs estén saturadas
- Experimentación con diferentes modelos
- Routing inteligente

### 4. HuggingChat
```
URL: https://huggingface.co/chat/
Modelos: Llama 3.3 70B, Qwen 2.5 72B, DeepSeek, Command R+
Límites: Sin límite claro (uso razonable)
Interfaz: Web (no API directa, pero se puede automatizar)
```

**Uso recomendado:**
- Conversaciones largas
- Investigación y análisis
- Cuando se necesite modelo potente sin límites

### 5. Cerebras
```
URL: https://inference.cerebras.ai/
Modelos: Llama 3.3 70B, Llama 3.1 8B
Límites: Generoso en tier gratuito
Velocidad: Muy rápida (chips especializados)
```

**Uso recomendado:**
- Alternativa a Groq cuando esté saturado
- Inferencia rápida

### 6. Mistral (Le Chat)
```
URL: https://chat.mistral.ai/
Modelos: Mistral Large, Codestral
Límites: Uso razonable gratuito
```

**Uso recomendado:**
- Tareas de código
- Alternativa europea

## IA Local (Ollama)

### Modelos para Zro (LNV - más potente)
```bash
# Modelos recomendados según specs
ollama pull llama3.2:3b      # Ligero, respuestas rápidas
ollama pull llama3.1:8b      # Balance calidad/velocidad
ollama pull qwen2.5:7b       # Excelente razonamiento
ollama pull deepseek-coder:6.7b  # Para código
ollama pull phi3:medium      # Microsoft, eficiente
```

### Modelos para Kao (LNVold - 4GB RAM)
```bash
# Solo modelos pequeños
ollama pull llama3.2:1b      # Mínimo viable
ollama pull qwen2.5:1.5b     # Muy ligero
ollama pull phi3:mini        # Microsoft mini
ollama pull tinyllama        # Ultra ligero
```

## Configuración Plan Cero

### Prioridad de Routing
```
1. Ollama local (sin límites, privacidad)
2. Groq (velocidad, límites generosos)
3. Google AI Studio (contexto largo)
4. HuggingChat (backup ilimitado)
5. Cerebras (backup rápido)
6. OpenRouter (último recurso)
```

### Script de Rotación
```python
# Pseudocódigo para rotar APIs
apis_priority = [
    {"name": "ollama", "endpoint": "http://localhost:11434"},
    {"name": "groq", "endpoint": "https://api.groq.com/v1"},
    {"name": "google", "endpoint": "https://generativelanguage.googleapis.com"},
    {"name": "cerebras", "endpoint": "https://inference.cerebras.ai"}
]

def get_completion(prompt):
    for api in apis_priority:
        try:
            return call_api(api, prompt)
        except RateLimitError:
            continue
    return fallback_huggingchat(prompt)
```

---

# 💰 PLAN INTERMEDIO ($50-200/mes)

> Escalar capacidad manteniendo costos controlados

## APIs de Pago (Tier Developer)

### Groq Developer ($20-50/mes)
```
Límites: 100K+ tokens/min
Prioridad: Cola preferente
Modelos: Todos disponibles
```

### Together AI (~$20-50/mes)
```
URL: https://www.together.ai/
Modelos: Llama, Mixtral, CodeLlama, etc.
Precio: ~$0.20/1M tokens (modelos pequeños)
Ventaja: Fine-tuning disponible
```

### Anthropic Claude (Pay-as-you-go)
```
Claude 3.5 Sonnet: $3/1M input, $15/1M output
Claude 3 Haiku: $0.25/1M input, $1.25/1M output
Límite presupuesto: $50-100/mes
```

### OpenAI (Pay-as-you-go)
```
GPT-4o-mini: $0.15/1M input, $0.60/1M output
GPT-4o: $2.50/1M input, $10/1M output
Límite presupuesto: $30-50/mes
```

### Manus Pro (~$30/mes)
```
Navegador agéntico profesional
Tareas automatizadas ilimitadas
Integración con holobionte
```

### MultiOn (~$20/mes)
```
API de automatización web
Complemento para navegadores agénticos
```

## Distribución Presupuesto Intermedio

```
Total: $150/mes ejemplo

Groq Developer:     $30/mes (velocidad)
Together AI:        $30/mes (fine-tuning)
Claude pay-as-go:   $40/mes (calidad)
OpenAI pay-as-go:   $30/mes (GPT-4o-mini)
Manus Pro:          $20/mes (automatización)
---
Total:              $150/mes
```

---

# 🚀 PLAN ILIMITADO ($500-5000+/mes)

> Capacidad enterprise sin restricciones

## APIs Enterprise

### OpenAI Enterprise ($500+/mes)
```
GPT-4 Turbo ilimitado
Acceso prioritario
SLA garantizado
Fine-tuning avanzado
```

### Anthropic Enterprise ($500+/mes)
```
Claude 3.5 Opus
Límites extendidos
Soporte dedicado
```

### Google Vertex AI (Variable)
```
Gemini Ultra
Procesamiento masivo
Integración GCP
```

## GPU Cloud

### RunPod ($50-200/mes)
```
GPUs bajo demanda: A100, H100
Ollama con modelos 70B+
Fine-tuning local
```

### Lambda Labs ($100-500/mes)
```
GPUs para training
Modelos custom
```

### Vast.ai ($30-100/mes)
```
GPUs económicas
Ideal para inferencia batch
```

## Stack Completo Ilimitado

```
Enterprise APIs:     $1500/mes
- OpenAI Enterprise: $500
- Anthropic:         $500
- Google Vertex:     $500

GPU Cloud:           $300/mes
- RunPod A100:       $200
- Vast.ai backup:    $100

Herramientas:        $200/mes
- Manus Enterprise:  $100
- MultiOn Pro:       $50
- BrowserOS Pro:     $50

Total:               $2000/mes
```

---

## 🎯 Recomendación por Fase

### Fase Actual (Supervivencia)
**Plan Cero** - Maximizar APIs gratuitas
- Ollama en Zro + Kao
- Groq + Google AI Studio
- HuggingChat como backup

### Fase Crecimiento (Post-financiación inicial)
**Plan Intermedio** - $100-150/mes
- Mantener APIs gratuitas
- Añadir Claude + GPT-4o-mini para calidad
- Manus Pro para automatización

### Fase Expansión (Ingresos estables)
**Plan Ilimitado** - Escalar según necesidad
- Enterprise APIs para misiones críticas
- GPU cloud para modelos propios
- Redundancia completa

---

## 📋 Checklist de Activación

### Plan Cero (Hoy)
- [x] Cuenta Groq creada
- [ ] API Key Groq configurada
- [x] Google AI Studio acceso
- [ ] API Key Google configurada
- [ ] OpenRouter cuenta
- [x] HuggingChat activo
- [ ] Cerebras cuenta
- [x] Ollama instalado Zro
- [ ] Ollama instalado Kao
- [ ] Script de rotación implementado

### Plan Intermedio (Cuando financiación)
- [ ] Groq Developer upgrade
- [ ] Together AI cuenta
- [ ] Claude API configurada
- [ ] OpenAI API configurada
- [ ] Manus Pro suscripción

### Plan Ilimitado (Futuro)
- [ ] Enterprise contracts
- [ ] GPU cloud setup
- [ ] Fine-tuning pipeline

---

*Documentado por Comet de Zro @ 1rec3 | 2025*
