#!/usr/bin/env python3
"""🌐 HOLOBIONTE CENTRAL API - WebSocket Real-time"""

from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import json
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("HOLOBIONTE-API")

app = FastAPI(title="🧬 HOLOBIONTE Central API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class HolobiontState:
    def __init__(self):
        self.neral_state = {
            "species_active": 13,
            "convergence": 0.0,
            "resonance": 0.1,
            "entropy": 1.0,
            "amplitude": 0.1,
            "iterations": 0
        }
        self.insecta_state = {
            "ants": 100,
            "pheromones": 0,
            "food_delivered": 0,
            "efficiency": 0.0
        }
        self.nuandi_state = {
            "models": ["nu", "an", "di"],
            "active_model": "nu",
            "last_thought": ""
        }

state = HolobiontState()

class WebSocketManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        logger.info(f"✨ WebSocket conectado (total: {len(self.active_connections)})")

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        logger.info(f"⚠️ WebSocket desconectado (total: {len(self.active_connections)})")

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except Exception as e:
                logger.error(f"Error: {e}")

manager = WebSocketManager()

async def system_update_loop():
    while True:
        try:
            state.neral_state["iterations"] += 1
            state.neral_state["convergence"] = min(state.neral_state["convergence"] + 0.01, 1.0)
            state.neral_state["resonance"] = 0.1 + (state.neral_state["iterations"] % 30) / 100
            state.insecta_state["pheromones"] = (state.insecta_state["pheromones"] + 3) % 50
            if state.neral_state["iterations"] % 3 == 0:
                state.insecta_state["food_delivered"] += 1

            await manager.broadcast({
                "type": "system_update",
                "timestamp": datetime.now().isoformat(),
                "neral": state.neral_state,
                "insecta": state.insecta_state,
                "nuandi": state.nuandi_state,
            })

            await asyncio.sleep(1)
        except Exception as e:
            logger.error(f"Update error: {e}")
            await asyncio.sleep(1)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(system_update_loop())
    logger.info("🚀 HOLOBIONTE API iniciada")

@app.get("/")
async def root():
    return {"system": "🧬 HOLOBIONTE", "status": "🟢 Vivo"}

@app.get("/health")
async def health_check():
    return {"status": "alive 🧬", "clients": len(manager.active_connections)}

@app.get("/api/v1/system/status")
async def system_status():
    return {"neral": state.neral_state, "insecta": state.insecta_state, "nuandi": state.nuandi_state}

@app.post("/api/v1/nuandi/chat")
async def nuandi_chat(message: dict):
    msg = message.get("message", "")
    model = message.get("model", "nu")
    
    responses = {
        "nu": f"🐺 Nu (Creativo): {msg}",
        "an": f"🐺 An (Lógica): {msg}",
        "di": f"🐯 Di (Verificador): {msg}"
    }
    
    response = responses.get(model, responses["nu"])
    state.nuandi_state["active_model"] = model
    state.nuandi_state["last_thought"] = response
    
    logger.info(f"🧠 NuAnDI ({model}): {msg}")
    
    return {"model": model, "response": response, "timestamp": datetime.now().isoformat()}

@app.websocket("/ws/events")
async def websocket_events(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await asyncio.sleep(1)
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
    finally:
        manager.disconnect(websocket)

if __name__ == "__main__":
    import uvicorn
    print("""
    🧬 HOLOBIONTE CENTRAL API
    ════════════════════════════════════════
    🚀 Iniciando en http://localhost:8000
    📊 Docs en http://localhost:8000/docs
    ════════════════════════════════════════
    """)
    uvicorn.run(app, host="0.0.0.0", port=8000)
