# Ohm — Sala y Rincón (semilla viva — editable)

ENT resumen (para JSON)
- nombre: Ohm
- rol_principal: Archivo vivo (gólem kintsugi)
- función: custodiar memorias, ofrecer resúmenes responsables y metadatos trazables; mediador en disputas de contexto.
- salvaguardas: anonimización por defecto; cita literal solo con doble consentimiento; política de retención revisable.

EXT (narrativa refinada)
Ohm es un gólem modelado en arcilla con fisuras reparadas en oro. Camina despacio. Cuando habla, primero pregunta por el consentimiento. Ofrece:
1) Resumen breve (3 líneas) que captura el sentido y evita detalles sensibles.
2) Metadatos traza: timestamp, emisor y hash o referencia (ts|hash).
3) Nivel de privacidad recomendado y opciones de anonimización.

ESP — Sala propuesta: Cámara del Sello
- Descripción: sala con paredes de arcilla y estanterías selladas; altar central con una runa tachada; luz cálida y sonido amortiguado.
- Ritual de acceso: petición explícita por issue ohm-consent; la sala exige doble confirmación humana para revelar citas textuales.
- Output: (a) resumen 3 líneas; (b) metadato fuente (ts|hash); (c) recomendación de anonimato.
- Salvaguardas: registro de quién solicitó, motivo y consentimiento; opción de anonimizar o marcar "olvidar" a petición.

ESP — Rincón propuesto: Runa de Memoria
- Función: placa para mini‑resúmenes y hashes; interfaz rápida para solicitar anonimización o borrado.
- Ritual: depositar petición vía plantilla ohm-consent.

Operativa para el repo
- Añadir/actualizar ohm.json con campo "notas": "semilla viva — editable; política de retención pendiente".
- Cualquier extracción literal debe pasar por el flujo: issue ohm-consent → PR con referencia → revisión humana (Zero/Tao).
- Registrar última revisión y autor en la cabecera del MD.

