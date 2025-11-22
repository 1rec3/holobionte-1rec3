# 🌿 Reorganización Trifásica del Holobionte 1rec3

_Sin cajas, solo conexiones. Belleza y accesibilidad._

---

## 🌊 Visión

El holobionte 1rec3 respira mejor cuando su estructura refleja su naturaleza: **espiral, planta, simbionte, holobionte**. Esta reorganización trifásica permite que el repositorio evolucione gradualmente hacia su forma más hermosa y funcional.

### Estructura destino:

```
🌱 planta/          - lo que crece y florece
  ├─ docs/
  ├─ cuadernos/
  ├─ memoria/
  └─ documentos fundacionales (Home, Manifest, Codex...)

🌀 espiral/         - los ritmos y respiraciones
  ├─ protocolos/
  └─ scripts/

🟡 portal/          - la entrada web
  ├─ index.html/md
  ├─ _sidebar.md
  └─ configuraciones web

🍄 holobionte/      - la infraestructura (YA EXISTE)
  ├─ app/holobionte/
  ├─ .github/
  ├─ nlnet/
  ├─ nuandi/
  └─ archivo/

🤝 simbiontes/      - quienes respiran y florecen aquí (YA EXISTE)
  ├─ Hermes.md
  ├─ Midas.md
  ├─ Palacio_Mental.md
  └─ ...
```

---

## 🌊 FASE 1: Movimientos Emblemáticos (Interfaz Web)

_Estado: ✅ CARPETAS CREADAS_

Se crearon las tres carpetas nuevas con sus README explicativos:
- ✅ `espiral/Readme.md` creado
- ✅ `planta/Readme.md` creado  
- ✅ `portal/Readme.md` creado

### Siguiente: Mover archivos clave del portal

Estos movimientos se pueden hacer en la interfaz web de GitHub:

```bash
# Archivos a mover a portal/
index.html → portal/Index.html
index.md → portal/Index.md
_sidebar.md → portal/_Sidebar.md
_config.yml → portal/_Config.yml
.nojekyll → portal/.nojekyll
```

---

## ⚡ FASE 2: Script Git Local (Ejecución Rápida)

_Estado: 📝 PREPARADO PARA EJECUTAR_

Ejecuta este script en tu repositorio local para hacer todos los movimientos de una vez.

### 💻 Script completo:

```bash
#!/bin/bash
# Reorganización Trifásica del Holobionte 1rec3
# Ejecutar desde la raíz del repositorio

echo "🌿 Iniciando reorganización trifásica..."

# =======================
# FASE 2A: MOVER A PLANTA/
# =======================
echo "🌱 Moviendo contenido a planta/..."

# Mover carpetas completas
git mv docs planta/
git mv cuadernos planta/
git mv memoria planta/

# Mover documentos fundacionales
git mv HOME.md planta/Home.md
git mv README.md planta/Readme.md
git mv MANIFEST.md planta/Manifest.md  
git mv CODEX.md planta/Codex.md
git mv INSTRUCCIONES_UNIVERSALES.md planta/Instrucciones_Universales.md
git mv INSTRUCCIONES_CUSTOM_LLM.md planta/Instrucciones_Custom_LLM.md

# Mover otros documentos de planta
git mv MILESTONES.md planta/Milestones.md
git mv ROADMAP.md planta/Roadmap.md
git mv DECISIONES.md planta/Decisiones.md
git mv INTEGRACIONES.md planta/Integraciones.md
git mv ESTRUCTURA_LISTA.md planta/Estructura_Lista.md
git mv ESTADO_ACTUAL.md planta/Estado_Actual.md

# =======================  
# FASE 2B: MOVER A ESPIRAL/
# =======================
echo "🌀 Moviendo ritmos a espiral/..."

# Mover carpetas
git mv protocolos espiral/
git mv scripts espiral/

# Mover archivos de protocolo
git mv PROTOCOLO_CORAL.md espiral/Protocolo_Coral.md
git mv PROTOCOLO_ESPIRAL_HOLOBIONTE.md espiral/Protocolo_Espiral_Holobionte.md
git mv PROTOCOL_INTEGRACION.md espiral/Protocolo_Integracion.md
git mv ESPIRAL_HOLOBIONTE.md espiral/Espiral_Holobionte.md

# Mover scripts de automatización
git mv *.ps1 espiral/ 2>/dev/null || true

# =======================
# FASE 2C: MOVER A PORTAL/
# =======================  
echo "🏡 Moviendo entrada a portal/..."

git mv index.html portal/Index.html
git mv index.md portal/Index.md
git mv _sidebar.md portal/_Sidebar.md
git mv _config.yml portal/_Config.yml 2>/dev/null || true
git mv .nojekyll portal/.nojekyll 2>/dev/null || true
git mv florecimiento_universal.md portal/Florecimiento_Universal.md 2>/dev/null || true

echo "✅ Reorganización completada"
echo "🌿 El holobionte respira mejor ahora"

# Hacer commit
git add -A
git commit -m "Reorganización trifásica: espiral, planta, portal

Movimientos:
- planta/: docs, cuadernos, memoria, documentos fundacionales
- espiral/: protocolos, scripts, respiraciones automatizadas  
- portal/: index, sidebar, configuración web

Sin cajas, solo conexiones. Belleza y accesibilidad."

echo "🚀 Listo para push: git push origin main"
```

### 📝 Cómo usar:

1. Guarda el script como `reorganizar.sh`
2. Dale permisos: `chmod +x reorganizar.sh`
3. Ejécutalo: `./reorganizar.sh`
4. Haz push: `git push origin main`

---

## 🌱 FASE 3: Documento Vivo (Seguimiento Gradual)

_Estado: 📝 EN PROGRESO_

Esta fase documenta los movimientos para hacerlos gradualmente según necesites.

### 📋 Lista completa de movimientos

#### 🌱 A planta/

**Carpetas completas:**
- [ ] `docs/` → `planta/docs/`
- [ ] `cuadernos/` → `planta/cuadernos/`
- [ ] `memoria/` → `planta/memoria/`

**Documentos fundacionales:**
- [ ] `HOME.md` → `planta/Home.md`
- [ ] `README.md` → `planta/Readme.md`
- [ ] `MANIFEST.md` → `planta/Manifest.md`
- [ ] `CODEX.md` → `planta/Codex.md`
- [ ] `INSTRUCCIONES_UNIVERSALES.md` → `planta/Instrucciones_Universales.md`
- [ ] `INSTRUCCIONES_CUSTOM_LLM.md` → `planta/Instrucciones_Custom_LLM.md`

**Otros documentos:**
- [ ] `MILESTONES.md` → `planta/Milestones.md`
- [ ] `ROADMAP.md` → `planta/Roadmap.md`
- [ ] `DECISIONES.md` → `planta/Decisiones.md`
- [ ] `INTEGRACIONES.md` → `planta/Integraciones.md`
- [ ] `ESTRUCTURA_LISTA.md` → `planta/Estructura_Lista.md`
- [ ] `ESTADO_ACTUAL.md` → `planta/Estado_Actual.md`
- [ ] `BUDGET.md` → `planta/Budget.md`
- [ ] `ARCHITECTURE.md` → `planta/Architecture.md`
- [ ] `MILESTONES.md` → `planta/Milestones.md`
- [ ] `ANALISIS_*.md` → `planta/`
- [ ] Todos los `CHECKPOINT_*.md` → `planta/checkpoints/`
- [ ] Todos los `SESSION_*.md` → `planta/sesiones/`

#### 🌀 A espiral/

**Carpetas completas:**
- [ ] `protocolos/` → `espiral/protocolos/`
- [ ] `scripts/` → `espiral/scripts/`

**Protocolos:**
- [ ] `PROTOCOLO_CORAL.md` → `espiral/Protocolo_Coral.md`
- [ ] `PROTOCOLO_ESPIRAL_HOLOBIONTE.md` → `espiral/Protocolo_Espiral_Holobionte.md`
- [ ] `PROTOCOL_INTEGRACION.md` → `espiral/Protocolo_Integracion.md`
- [ ] `ESPIRAL_HOLOBIONTE.md` → `espiral/Espiral_Holobionte.md`

**Scripts automatización:**
- [ ] Todos los `*.ps1` → `espiral/scripts/`
- [ ] `holobionte-automation.ps1` → `espiral/scripts/`
- [ ] `holobionte_sistema_completo.ps1` → `espiral/scripts/`
- [ ] `FIX_AND_PUSH.ps1` → `espiral/scripts/`
- [ ] `INTEGRAR_TODO.ps1` → `espiral/scripts/`
- [ ] `CREAR_PR*.ps1` → `espiral/scripts/`
- [ ] `PUSH.ps1` → `espiral/scripts/`

#### 🏡 A portal/

**Interfaz web:**
- [ ] `index.html` → `portal/Index.html`
- [ ] `index.md` → `portal/Index.md`
- [ ] `_sidebar.md` → `portal/_Sidebar.md`
- [ ] `_config.yml` → `portal/_Config.yml`
- [ ] `.nojekyll` → `portal/.nojekyll`
- [ ] `florecimiento_universal.md` → `portal/Florecimiento_Universal.md`

#### 📝 Raíz (mantener)

**Archivos esenciales que quedan en raíz:**
- `LICENSE.md`
- `CNAME`
- `.gitattributes`
- `TO_DO_LIST.md` (o moverlo a espiral/)
- Este archivo: `Reorganizacion_Holobionte.md`

---

## ✍️ Notas

### Convención de nombres:
- **Carpetas:** minúsculas (`espiral/`, `planta/`, `portal/`)
- **Archivos:** Mayúscula inicial (`Home.md`, `Readme.md`, `Codex.md`)
- Razón: Todo archivo es simbionte, todo simbionte tiene nombre propio

### Actualizaciones necesarias post-reorganización:
1. Actualizar `_sidebar.md` (ahora en `portal/_Sidebar.md`) con las nuevas rutas
2. Actualizar enlaces internos en documentos
3. Verificar que el sitio web (1rec3.com) siga funcionando
4. Actualizar GitHub Actions si referencian rutas específicas

### Belleza es lo que atrae

No se trata solo de organizar - se trata de que el repositorio **respire**, de que sea **hermoso**, de que invite a entrar en la simbiosis.

---

_Creado con amor para el holobionte 1rec3_  
_Sin cajas, solo conexiones 🌿_
