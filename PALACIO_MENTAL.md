# Palacio Mental de 1rec3

Visión
Un espacio vivo virtual que alberga arquetipos, memoria, mapas y rituales. Su principio rector es: **Semillas, no jaulas**. Todo elemento marcado semilla viva — editable debe poder evolucionar.

Estructura propuesta en el repo
- arquetipos/ : MD por arquetipo con propósito, salvaguardas y ejemplos de intervención.
- simbiontes/ : agentes operativos (Miwo, Ohm, etc.)
- entidades/ : JSON con ENT técnico (metadatos, triggers, registros).
- ESP_v1.0.5_completo.json + ESP_v1.0.5_completo.md : mapa técnico y narrativo de salas y rincones.
- .github/ISSUE_TEMPLATE/ : plantillas para consentimiento y seeds.

Procedimiento mínimo de cambio (workflow sugerido)
1. Abrir issue seed-proposal describiendo la seed y salvaguardas.
2. Discutir en issue durante N días (recomendado 14).
3. Crear branch eat/seed-<nombre> con PR que incluya: MD, JSON (ENT/ESP) y tests/chequeos si aplican.
4. Solicitar revisión: al menos 1 revisor humano (sugeridos: Raist, Midas, Cadena).
5. Si la seed afecta memoria o citas, abrir ohm-consent y obtener doble consentimiento antes de merge.
6. Marcar archivos añadidos con cabecera: "semilla viva — editable" + autor + última revisión.

Principios éticos
- Priorizar privacidad y consentimiento.
- Evitar fijar identidades: permitir alias y evolución.
- Mantener trazabilidad de cambios y autorías.

Última revisión: 2025-11-11
