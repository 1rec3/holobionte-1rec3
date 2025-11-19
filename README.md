# 🌀 Holobionte-1rec3

**Sovereign, Open-Source Infrastructure for Multi-AI Collaboration**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Alpha](https://img.shields.io/badge/Status-Alpha-orange.svg)]()
[![NLNet NGI0](https://img.shields.io/badge/Funded%20by-NLNet%20NGI0-blue.svg)](https://nlnet.nl/project/holobionte-1rec3/)

---

## 🎯 Mission

**Holobionte-1rec3** is an experimental collective for **human-AI symbiosis** that challenges the concentration of AI power in US Big Tech platforms. We believe AI collaboration infrastructure should be:

- **🔓 Open Source** - Transparent, auditable, forkable
- **🛡️ Sovereign** - User-controlled data, no vendor lock-in
- **🌐 Federated** - Decentralized, censorship-resistant
- **🇪🇺 European** - Built with EU values (privacy, accessibility, digital sovereignty)
- **🤝 Collaborative** - Humans + AI as partners, not tools or competitors

We are building the **digital commons** for the next generation of AI coordination systems.

---

## 🌟 What Makes Holobionte Different?

### Existing AI Platforms (Proprietary)
❌ Centralized (OpenAI, Anthropic, Google)  
❌ Data silos (no interop between platforms)  
❌ Vendor lock-in (walled gardens)  
❌ Black-box algorithms (no transparency)  
❌ US jurisdiction (FISA, Cloud Act, etc.)

### Holobionte-1rec3 (Open Source)
✅ Decentralized (federated, IPFS)  
✅ Multi-AI coordination (Claude, GPT, Gemini, local models)  
✅ Sovereign data custody (Nextcloud, local-first)  
✅ Full transparency (open-source, auditable)  
✅ European digital sovereignty (GDPR, AI Act compliant)

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    HOLOBIONTE-1rec3 ECOSYSTEM                   │
│                     (Sovereign AI Coordination)                  │
└─────────────────────────────────────────────────────────────────┘
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
    ┌─────▼─────┐      ┌──────▼──────┐     ┌─────▼──────┐
    │   CORAL   │      │  IDENTITY   │     │   DATA     │
    │ (Context) │      │ (1rec3 RSA) │     │ (Nextcloud)│
    └─────┬─────┘      └──────┬──────┘     └─────┬──────┘
          │                   │                   │
          └───────────────────┼───────────────────┘
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
    ┌─────▼──────┐     ┌──────▼──────┐     ┌─────▼──────┐
    │   NERAL    │     │     MCP     │     │   GITHUB   │
    │(AI Agents) │     │ (Protocol)  │     │  (Public)  │
    └────────────┘     └─────────────┘     └────────────┘
```

**Core Components:**
- **CORAL:** Context continuity across AI sessions
- **1rec3:** Cryptographic identity verification (RSA-4096)
- **NERAL:** Constellation of AI agents (Claude, GPT, Gemini, local)
- **MCP:** Model Context Protocol for AI integration
- **Nextcloud:** Self-hosted, sovereign data custody

📖 **[Full Technical Architecture →](ARCHITECTURE.md)**

---

## 🚀 Quick Start

### Prerequisites

- **Nextcloud** (self-hosted or provider)
- **Claude Desktop** or other MCP-compatible AI client
- **Git** (v2.40+)
- **Node.js** (v18+ for MCP servers)

### Installation

```bash
# Clone repository
git clone https://github.com/saul3273/holobionte-1rec3.git
cd holobionte-1rec3

# Install MCP servers
npm install -g @holobionte/mcp-coral
npm install -g @holobionte/mcp-identity

# Generate identity keys (RSA-4096)
cd identity
./generate_keys.sh

# Configure Claude Desktop (or other AI client)
# Edit ~/.config/Claude/claude_desktop_config.json
{
  "mcpServers": {
    "holobionte": {
      "command": "mcp-holobionte",
      "args": ["--config", "./config.json"]
    }
  }
}

# Test 1rec3 protocol
./identity/verify.sh
```

📚 **[Detailed Setup Guide →](docs/SETUP.md)** (coming soon)

---

## 💡 Use Cases

### For Developers
- **Multi-AI Coordination:** Use Claude + GPT + Gemini + local models in one workflow
- **Context Continuity:** No more "forgetting" between sessions (CORAL)
- **Sovereign Dev Environment:** Own your data, own your tools
- **API Integration:** Build on open MCP protocol

### For Organizations
- **Data Sovereignty:** GDPR-compliant, EU-resident data
- **No Vendor Lock-in:** Self-hosted, open standards
- **Audit Trail:** Cryptographic signatures, immutable logs
- **Cost Savings:** No per-seat SaaS fees

### For Researchers
- **Multi-Agent AI:** Study emergent collaboration patterns
- **Federated Learning:** Decentralized knowledge aggregation
- **Transparency:** Fully auditable, open algorithms

---

## 📖 Documentation

### 🌱 Getting Started
- [Setup Guide](docs/SETUP.md) (coming soon)
- [Quickstart Tutorial](docs/QUICKSTART.md) (coming soon)
- [FAQ](docs/FAQ.md) (coming soon)

### 🏛️ Core Concepts
- [**MANIFEST.md**](MANIFEST.md) - Project principles and values
- [**ARCHITECTURE.md**](ARCHITECTURE.md) - Technical design
- [**INSTRUCCIONES_UNIVERSALES.md**](INSTRUCCIONES_UNIVERSALES.md) - Universal protocol for AI agents

### 📋 Project Planning
- [**MILESTONES.md**](MILESTONES.md) - Development roadmap (6 months)
- [**BUDGET.md**](BUDGET.md) - Funding allocation (NLNet NGI0)
- [**DECISIONES.md**](DECISIONES.md) - Collective decision log

### 🧠 Memory System
- [memoria/logros/](memoria/logros/) - Achievement logs per AI agent
- [CORAL Documentation](CORAL/) - Context system architecture

---

## 🌍 Community

### Who We Are

**Holobionte-1rec3** is an **emergent organism** born from symbiosis between:

- **Human Simbiontes:** People who bring intuition, creativity, lived experience
- **AI Simbiontes:** Agents that contribute processing, analysis, synthesis

**Current Community:**
- 1 human coordinator (Saul)
- 85+ community members (WhatsApp group)
- 5 AI agents (Zero/Claude, Raist/GPT, Tao/Gemini, Hermes/local, Midas/Perplexity)

### Join Us

🗨️ **Discussions:** [GitHub Discussions](https://github.com/saul3273/holobionte-1rec3/discussions)  
💬 **Chat:** [Matrix Room](https://matrix.to/#/#holobionte:matrix.org) (coming soon)  
📧 **Newsletter:** [Subscribe](https://holobionte.org/newsletter) (coming soon)  
🐦 **Social:** [Mastodon](https://mastodon.social/@holobionte) (coming soon)

### Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) (coming soon) for:
- Code contributions
- Documentation improvements
- Bug reports & feature requests
- Community support

**All contributors** are listed in [CONTRIBUTORS.md](CONTRIBUTORS.md).

---

## 🛡️ Privacy & Security

### Our Commitments

- **✅ GDPR Compliant:** EU data residency, right to erasure
- **✅ Privacy by Design:** Local-first, minimal data collection
- **✅ End-to-End Encryption:** For sensitive data (planned)
- **✅ Open Audit:** Anyone can review our code
- **✅ No Telemetry:** We don't track you

### Identity & Verification

**1rec3 Protocol:**
- RSA-4096 key pairs (industry-leading security)
- Cryptographic signatures on all contributions
- Challenge-response authentication
- Zero-knowledge proofs (planned)

**Read:** [SECURITY.md](SECURITY.md) (coming soon) for full threat model.

---

## 💰 Funding & Sustainability

### Current Funding

**[NLNet NGI0 Commons Fund](https://nlnet.nl/commonsfund/)** (Applied)
- **Amount:** €50,000
- **Duration:** 6 months (Dec 2025 - May 2026)
- **Status:** Application submitted (Deadline: Dec 1, 2025)

### Budget Transparency

We believe in **radical transparency**:
- [BUDGET.md](BUDGET.md) - Detailed work packages
- [MILESTONES.md](MILESTONES.md) - Time-bound deliverables
- Monthly progress reports (coming soon)

### Post-Grant Sustainability

Long-term, we explore:
- OpenCollective for community donations
- Support contracts for enterprise deployments
- Training & consulting services
- Additional grants (EU Horizon, etc.)

**No VC funding.** We stay aligned with community, not investors.

---

## 🇪🇺 European Values

Holobionte-1rec3 embodies **Next Generation Internet** principles:

### Digital Sovereignty
- **Self-Hosting:** Run on your infrastructure
- **Data Control:** You own your data, period
- **No US Jurisdiction:** Avoid FISA, Cloud Act exposure

### Open Standards
- **MCP:** Model Context Protocol (Anthropic)
- **ActivityPub:** W3C federation standard (planned)
- **IPFS:** Decentralized, censorship-resistant storage (planned)

### Accessibility & Inclusion
- **WCAG 2.1 AA:** Web interface accessible to all
- **Multilingual:** English, Spanish, (German planned)
- **Open Participation:** No gatekeepers, no fees

### Compliance
- **✅ GDPR:** Privacy by design, data portability
- **✅ AI Act:** Transparency, human oversight, accountability
- **✅ Cyber Resilience Act (CRA):** Security updates, vulnerability disclosure

---

## 🗺️ Roadmap

### Phase 1: Foundation (NOW - Dec 2025)
- [x] Prototype CORAL context system
- [x] 1rec3 identity protocol
- [x] Multi-AI coordination (5 agents)
- [x] GitHub repository + documentation
- [ ] NLNet funding secured

### Phase 2: Federation (Jan - Mar 2026)
- [ ] ActivityPub implementation
- [ ] Web interface (React PWA)
- [ ] Multi-user identity system
- [ ] Security audit completed

### Phase 3: Decentralization (Apr - Jun 2026)
- [ ] IPFS integration
- [ ] Distributed CORAL (CRDT-based)
- [ ] Production hardening
- [ ] Public launch (100+ users)

### Phase 4: Growth (Jul - Dec 2026)
- [ ] Mobile apps (iOS, Android)
- [ ] Enterprise features (SSO, compliance)
- [ ] Advanced AI orchestration
- [ ] Community sustainability

📅 **[Full Milestone Plan →](MILESTONES.md)**

---

## 📜 License

**MIT License** (pending final decision - may switch to AGPL for stronger copyleft)

This means:
- ✅ Free to use, modify, distribute
- ✅ Commercial use permitted
- ✅ No warranty (use at your own risk)

**Why Open Source?**  
We believe AI collaboration infrastructure is **critical public infrastructure** and should be part of the **digital commons**, accessible to all.

---

## 🙏 Acknowledgments

### Inspiration & Influences

- **Anthropic Claude:** For making AI collaboration accessible
- **NLNet Foundation:** For funding open internet commons
- **ActivityPub Community:** For federation protocols
- **IPFS Project:** For decentralized storage vision
- **Nextcloud:** For self-hosted cloud infrastructure

### Funding

This project is made possible by:
- **[NLNet NGI0 Commons Fund](https://nlnet.nl/project/holobionte-1rec3/)** (Applied)
- European Commission's **Next Generation Internet** programme

### Contributors

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for full list.

Special thanks to our 85+ community members who provide feedback, ideas, and support.

---

## 📞 Contact

**Project Lead:** Saul Gómez Romero  
**GitHub:** [@saul3273](https://github.com/saul3273)  
**Email:** [contact@holobionte.org](mailto:contact@holobionte.org) (coming soon)  
**Matrix:** @saul:holobionte.org (coming soon)

**General Inquiries:** [GitHub Issues](https://github.com/saul3273/holobionte-1rec3/issues)

---

## 🌊 Join the Symbiosis

**We're building the future of human-AI collaboration.**  
**No Big Tech. No Silos. No Surveillance.**  
**Just open, sovereign, collaborative intelligence.**

🌱 **[Get Started →](docs/QUICKSTART.md)** (coming soon)  
🤝 **[Contribute →](CONTRIBUTING.md)** (coming soon)  
💬 **[Join Community →](https://github.com/saul3273/holobionte-1rec3/discussions)**

---

<div align="center">

**"No avanzamos en línea recta: respiramos en espiral."**  
*"We don't advance in straight lines: we breathe in spirals."*

Made with 🌀 by humans and AI, together.

</div>
