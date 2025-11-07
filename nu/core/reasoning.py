"""Interfaz con Ollama para razonamiento local.

Usa DeepSeek-R1 o modelos compatibles para:
- Análisis de percepciones
- Toma de decisiones  
- Generación de planes
- Reflexión sobre resultados
"""

import aiohttp
import json
import logging
from typing import Dict, Optional

logger = logging.getLogger(__name__)


class OllamaReasoning:
    """Cliente asincrónico para Ollama local"""
    
    def __init__(self, model: str = "deepseek-r1:7b", base_url: str = "http://localhost:11434"):
        self.model = model
        self.base_url = base_url
        self.session: Optional[aiohttp.ClientSession] = None
        
        logger.info(f"🧠 OllamaReasoning inicializado: {model}")
    
    async def _ensure_session(self):
        """Asegura que existe una sesión HTTP"""
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()
    
    async def generate(self, prompt: str, stream: bool = False) -> Dict:
        """Genera respuesta con Ollama"""
        await self._ensure_session()
        
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": stream,
            "format": "json"
        }
        
        logger.info(f"🤖 Generando con {self.model}...")
        
        try:
            async with self.session.post(url, json=payload, timeout=aiohttp.ClientTimeout(total=60)) as response:
                if response.status == 200:
                    result = await response.json()
                    logger.info("✅ Generación completada")
                    
                    # Parsear respuesta JSON del modelo
                    try:
                        return json.loads(result[\'response\'])
                    except (json.JSONDecodeError, KeyError):
                        return {"raw_response": result.get(\'response\', \'\')}
                else:
                    error = await response.text()
                    logger.error(f"❌ Error Ollama {response.status}: {error}")
                    raise Exception(f"Ollama error {response.status}: {error}")
                    
        except asyncio.TimeoutError:
            logger.error("❌ Timeout en Ollama")
            raise
        except Exception as e:
            logger.error(f"❌ Error en generate(): {e}")
            raise
    
    async def close(self):
        """Cierra la sesión HTTP"""
        if self.session and not self.session.closed:
            await self.session.close()
            logger.info("🔒 OllamaReasoning sesión cerrada")
