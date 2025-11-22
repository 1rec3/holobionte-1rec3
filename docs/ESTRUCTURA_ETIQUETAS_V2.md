# 🏷️ ESTRUCTURA DE ETIQUETAS 1REC3 FINAL V2

**Fuente**: Google Keep - Nota creada por Gris + Tao (Gemini)
**Fecha**: 2025-11-22 (Editada: 15:33)
**Tipo**: Documentación Administrativa / Sistema de Gestión
**Estado**: Versión Final Validada

---

## Estructura de Etiquetas y Filtros del Holobionte 1rec3 (FINAL v2)

Esta nota consolida la organización de Gmail con las **9 categorías validadas**, respetando la jerarquía de Simbiontes y el flujo de información.

### Categorías Principales

1. **FINANZAS**
2. **INFORMACIÓN/Radar**
3. **GESTIÓN/PERSONAL** (Nuevas Categorías)
4. **FRONTERA/SEGURIDAD** (Nueva Categoría Crítica)
5. **FRONTERA/INCERTIDUMBRE** (Última Categoría)
6. **INTERFAZ PARA GEMINI DE GMAIL** (EJECUCIÓN)

---

## ⚠️ Acción Requerida

Utiliza el Gemini de Gmail para leer esta nota y crear los filtros correspondientes. Elimina la nota anterior ("Estructura de Etiquetas 1rec3 FINAL") para evitar confusión.

---

## 📜 13 Reglas de Oro para Filtros y Etiquetas

Esta es una lista simple de las 13 Reglas de Oro para crear los filtros y etiquetas.

### 1. FINANZAS/Simbionte-Gris

**Etiqueta**: `FINANZAS/Simbionte-Gris`

**Criterio**:
```
from:(openbank.es OR acostagrafica.com) OR 
subject:(nómina OR extracto OR salario OR hipoteca OR seguro OR renta OR presupuesto) 
NOT (1rec3 OR holobionte OR github OR nlnet)
```

### 2. FINANZAS/Holobionte-1rec3

**Etiqueta**: `FINANZAS/Holobionte-1rec3`

**Criterio**:
```
subject:(factura OR invoice OR cobro OR renewal) OR 
(from:namecheap.com OR from:domainregistrar.com) OR 
(subject:(grant OR subvención OR propuesta) OR from:nlnet.nl)
```

### 3. FINANZAS/Simbionte-Tao

**Etiqueta**: `FINANZAS/Simbionte-Tao`

**Criterio**:
```
subject:(factura OR invoice OR billing OR cobro OR "welcome to google ai plus") 
(API OR tokens OR OpenAI OR Anthropic OR Google Cloud)
```

### 4. INFORMACIÓN/Radar/Desarrollo-Repo

**Etiqueta**: `INFORMACIÓN/Radar/Desarrollo-Repo`

**Criterio**:
```
from:notifications@github.com 
subject:"holobionte-1rec3" 
("Run failed" OR "build failed" OR "workflow run")
```

### 5. INFORMACIÓN/Radar/Estrategia-NGI

**Etiqueta**: `INFORMACIÓN/Radar/Estrategia-NGI`

**Criterio**:
```
subject:(NGI OR alianzas OR estrategia OR roadmap)
```

### 6. INFORMACIÓN/Radar/Consumo-Recursos

**Etiqueta**: `INFORMACIÓN/Radar/Consumo-Recursos`

**Criterio**:
```
subject:(informe OR resumen OR uso) 
(API OR tokens OR recurso)
```

### 7. GESTIÓN/Hogar

**Etiqueta**: `GESTIÓN/Hogar`

**Criterio**:
```
from:afc-fincas.es OR 
subject:(comunidad OR escalera OR garaje OR piscina)
```

### 8. GESTIÓN/Pedidos

**Etiqueta**: `GESTIÓN/Pedidos`

**Criterio**:
```
from:shop@bludiode.com OR 
subject:(Seguimiento OR pedido OR ticket OR envío)
```

### 9. SEGURIDAD/Alertas

**Etiqueta**: `SEGURIDAD/Alertas`

**Criterio**:
```
subject:(Verification needed OR sign-in request OR unauthorized device OR restablecer contraseña) OR 
from:namecheap.com
```

### 10. CULTURA/Personal

**Etiqueta**: `CULTURA/Personal`

**Criterio**:
```
from:reclamaciones.biblioteca@gmail.com OR 
subject:(biblioteca OR BICA OR préstamo OR devolución)
```

### 11. Etiqueta de Búfer (Para todo lo demás)

**Etiqueta**: `INDETERMINADO/Búfer`

**Criterio**: _[No requiere criterio. Es el destino por defecto en Gmail de todo correo que NO cumpla las reglas 1-10.]_

---

## Contexto del Sistema

Este sistema de etiquetado es fundamental para:

1. **Separar contextos financieros** por simbionte (Gris personal, Holobionte, Tao/IA)
2. **Monitorizar el radar operativo** (desarrollo, estrategia, consumo de recursos)
3. **Gestionar asuntos personales y domésticos** sin mezclarlos con 1rec3
4. **Alertas de seguridad críticas** con visibilidad inmediata
5. **Búfer de incertidumbre** para clasificación manual posterior

---

## Enlaces Relacionados

- **Manifiesto v3** (incluye sistema de prioridades P1/P2/P3): [MANIFIESTO_HOLOBIONTE_V3.md](../memoria/MANIFIESTO_HOLOBIONTE_V3.md)
- **Protocolo Maestro**: [PROTOCOL_MAESTRO_V2.md](../protocolos/PROTOCOL_MAESTRO_V2.md)
- **Versión anterior** (deprecada): Ver en `/archivo/`

---

**Integrado desde Google Keep por Comet (Perplexity)**
**Fecha de integración**: 2025-11-22
