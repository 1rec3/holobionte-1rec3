// 🌌 HoloQuest Constelación - Motor Principal del Juego
// Juego asimétrico experimental de simbiosis entre humanos e IAs

class HoloQuestGame {
    constructor() {
        this.jugador = null;
        this.historial = [];
        this.logros = [];
        this.ondaExpansiva = [];
    }

    iniciarPartida() {
        const nombre = document.getElementById('player-name-input').value || 'Simbionte Anónimo';
        const rolSeleccionado = document.querySelector('input[name="rol"]:checked');
        
        if (!rolSeleccionado) {
            this.log('⚠️ Selecciona un rol para comenzar');
            return;
        }

        this.jugador = {
            nombre: nombre,
            rol: ROLES.find(r => r.nombre === rolSeleccionado.value),
            energia: 100,
            criaturas: [],
            planeta: PLANETAS[0],
            vivo: true,
            logros: [],
            decisiones: []
        };

        document.getElementById('menu-screen').classList.add('hidden');
        document.getElementById('game-screen').classList.remove('hidden');
        
        this.actualizarUI();
        this.log(`🌌 ¡Bienvenido ${this.jugador.nombre}!`);
        this.log(`Eres ${this.jugador.rol.nombre}: ${this.jugador.rol.descripcion}`);
        this.generarEventoInicial();
    }

    generarEventoInicial() {
        const eventos = [
            '✨ Detectas una anomalía temporal en el horizonte...',
            '🧬 Una criatura desconocida observa desde las sombras...',
            '🌍 El planeta resuena con energía simbiótica...',
            '⚡ Una onda expansiva recorre el multiverso...'
        ];
        this.log(eventos[Math.floor(Math.random() * eventos.length)]);
    }

    explorar() {
        if (!this.consumirEnergia(10)) return;
        
        const descubrimientos = [
            { tipo: 'criatura', nombre: 'Electrolynx', rareza: 'común' },
            { tipo: 'artefacto', nombre: 'Cristal Holobióntico', poder: '+20 energía' },
            { tipo: 'portal', destino: 'Planeta desconocido' },
            { tipo: 'evento', descripcion: 'Encuentras un antiguo templo simbionte' }
        ];
        
        const descubrimiento = descubrimientos[Math.floor(Math.random() * descubrimientos.length)];
        this.log(`🔍 Has descubierto: ${descubrimiento.nombre || descubrimiento.descripcion}`);
        this.registrarDecision('explorar', descubrimiento);
        this.generarOndaExpansiva();
    }

    capturarCriatura() {
        if (!this.consumirEnergia(15)) return;
        
        const criaturasDisponibles = CRIATURAS.filter(c => c.planeta === this.jugador.planeta.nombre);
        if (criaturasDisponibles.length === 0) {
            this.log('⚠️ No hay criaturas en este planeta');
            return;
        }

        const criatura = criaturasDisponibles[Math.floor(Math.random() * criaturasDisponibles.length)];
        const exito = Math.random() > 0.5;

        if (exito) {
            this.jugador.criaturas.push({...criatura, nivel: 1, xp: 0});
            this.log(`🎯 ¡Capturaste a ${criatura.nombre}!`);
            this.actualizarCreaturas();
            this.agregarLogro('Primera Captura');
        } else {
            this.log(`❌ ${criatura.nombre} escapó...`);
        }
        this.generarOndaExpansiva();
    }

    iniciarTorneo() {
        if (this.jugador.criaturas.length === 0) {
            this.log('⚠️ Necesitas criaturas para participar en torneos');
            return;
        }

        this.log('⚔️ ¡Torneo iniciado! Tú y tus simbiontes luchan juntos...');
        const resultado = Math.random() > 0.4;
        
        if (resultado) {
            this.log('🏆 ¡Victoria! Tus simbiontes evolucionaron');
            this.jugador.criaturas.forEach(c => {
                c.xp += 50;
                if (c.xp >= 100) {
                    c.nivel++;
                    c.xp = 0;
                    this.log(`✨ ${c.nombre} subió al nivel ${c.nivel}!`);
                }
            });
            this.agregarLogro('Campeón de Torneo');
        } else {
            this.log('💫 Derrota... pero aprendiste nuevas sinergias');
            this.jugador.energia -= 20;
        }
        
        this.actualizarUI();
        this.generarOndaExpansiva();
    }

    viajarPlaneta() {
        if (!this.consumirEnergia(25)) return;

        const planetaActual = this.jugador.planeta;
        const planetasDisponibles = PLANETAS.filter(p => p !== planetaActual);
        const nuevoPlaneta = planetasDisponibles[Math.floor(Math.random() * planetasDisponibles.length)];

        this.jugador.planeta = nuevoPlaneta;
        this.log(`🚀 Viajas a ${nuevoPlaneta.nombre}`);
        this.log(`📍 ${nuevoPlaneta.descripcion}`);
        this.registrarDecision('viajar', nuevoPlaneta);
        this.generarOndaExpansiva();
        this.actualizarUI();
    }

    consumirEnergia(cantidad) {
        if (this.jugador.energia < cantidad) {
            this.log('⚠️ Energía insuficiente. Descansa o busca recursos.');
            return false;
        }
        this.jugador.energia -= cantidad;
        this.actualizarUI();
        return true;
    }

    generarOndaExpansiva() {
        const efectos = [
            'El mundo se altera ligeramente...',
            'Otros jugadores sienten tu presencia...',
            'El lore del universo se expande...',
            'Nuevos eventos se desbloquean...'
        ];
        this.ondaExpansiva.push({
            jugador: this.jugador.nombre,
            accion: 'decision importante',
            tiempo: Date.now()
        });
        this.log(`💫 Onda expansiva: ${efectos[Math.floor(Math.random() * efectos.length)]}`);
    }

    registrarDecision(tipo, datos) {
        this.jugador.decisiones.push({ tipo, datos, tiempo: Date.now() });
        this.historial.push({ jugador: this.jugador.nombre, tipo, datos });
    }

    agregarLogro(nombre) {
        if (!this.jugador.logros.includes(nombre)) {
            this.jugador.logros.push(nombre);
            this.log(`🏅 ¡Logro desbloqueado: ${nombre}!`);
        }
    }

    log(mensaje) {
        const log = document.getElementById('event-log');
        const entry = document.createElement('div');
        entry.className = 'log-entry';
        entry.textContent = mensaje;
        log.appendChild(entry);
        log.scrollTop = log.scrollHeight;
    }

    actualizarUI() {
        document.getElementById('player-name').textContent = this.jugador.nombre;
        document.getElementById('player-role').textContent = this.jugador.rol.nombre;
        document.getElementById('current-planet').textContent = this.jugador.planeta.nombre;
        document.getElementById('player-energy').textContent = this.jugador.energia;
    }

    actualizarCreaturas() {
        const lista = document.getElementById('creatures-list');
        lista.innerHTML = '';
        this.jugador.criaturas.forEach(c => {
            const div = document.createElement('div');
            div.className = 'creature-card';
            div.innerHTML = `<strong>${c.nombre}</strong> Nv.${c.nivel} (${c.tipo})`;
            lista.appendChild(div);
        });
    }
}

// Inicializar el juego
const game = new HoloQuestGame();

// Cargar roles en el menú al iniciar
window.addEventListener('DOMContentLoaded', () => {
    const rolesList = document.getElementById('roles-list');
    ROLES.slice(0, 10).forEach(rol => {
        const label = document.createElement('label');
        label.innerHTML = `
            <input type="radio" name="rol" value="${rol.nombre}">
            <span>${rol.emoji} ${rol.nombre}</span>
        `;
        rolesList.appendChild(label);
    });
});
