[FULL GOOD VERSION ASSEMBLED FROM THE read_file CHUNKS:
<div align="center">

<img src="assets/logo.svg" alt="Eternal Context Engine" width="720" />

### Eternal Memory for Any AI — Local, Private, Portable
#### Eternal Context Engine (ECE)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)](https://python.org)
[![MCP](https://img.shields.io/badge/MCP-stdio%20%2B%20HTTP-purple?style=flat-square)](https://modelcontextprotocol.io)
[![LanceDB](https://img.shields.io/badge/Vector%20DB-LanceDB-orange?style=flat-square)](https://lancedb.com)
[![License](https://img.shields.io/badge/License-AGPL%20v3%20%2F%20Commercial-blue?style=flat-square)](LICENSE)
[![Obsidian](https://img.shields.io/badge/Vault-Obsidian%20Native-7C3AED?style=flat-square&logo=obsidian)](https://obsidian.md)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)

</div>

Your AI shouldn't start from scratch every session. The more you use an AI, the more it fucking hallucinates. The Eternal Context Engine (ECE) aims to change that by being the eternal context — your AI's permanent, searchable long-term memory stored as Markdown files you can read, edit, and browse in Obsidian.

**Works with**: Claude Desktop, Claude Code, Cursor, Zed, Gemini CLI, Custom AI, or any MCP-compatible AI.

> No cloud. No subscriptions. No lock-in. Your context lives on your machine — or on a USB drive.

---

## The Problem: The Longer the Conversation, the Worse the AI Gets

Every AI has this problem — Grok, Claude, GPT, Gemini, Codex, all of them. The longer a conversation runs, the more the model degrades. It forgets decisions. It contradicts itself. It loses track of your architecture, your constraints, what you already ruled out. The hallucinations get more frequent, not less. You spend more time correcting than building.

When the conversation gets long enough, the provider compacts it — silently replacing your entire history with a summary. Suddenly your AI has no idea what you were building or why.

Understanding *why* this happens — what compaction actually is, what gets lost and why the AI can't tell — is covered in full in [Bootstrap — Surviving Compaction](#bootstrap--surviving-compaction).

**The Eternal Context Engine (ECE) was built to fix this permanently.** Your context lives in your vault, not in the conversation. The AI is always grounded to what's actually true — regardless of how long the conversation runs, how many times it compacts, or which AI you're using. No re-explaining. No re-hallucinating. No momentum lost.

---

## What It Does

```
Your Notes (Markdown)  →  Vault (Obsidian Graph View)
         ↓
    Engine indexes with LanceDB (local vector DB)
         ↓
  MCP Server / REST API  →  Any AI on your machine or network
         ↓
  AI remembers you. Every session. Across machines.
```

- **Write notes in Markdown** → Engine indexes them automatically
- **AI searches your vault** via MCP or REST API — gets relevant context instantly
- **Visualize your knowledge** in Obsidian's Graph View as it grows (the graph is the primary interface — open Ctrl/Cmd+G the moment you open the vault)
- **Migrate in 60 seconds** — copy folder, reinstall deps (reindex only if you changed embedding model)
- **Multi-agent ready** — shared vault for all agents, private namespaces per agent. Grok, Claude, Gemini, or any other AI can run simultaneously off the same vault without stepping on each other's memory
- **Higher-fidelity recall (multi-vector late interaction)** — Hardware-aware per-token embeddings + MaxSim (ColBERT-style) + RRF fusion with BM25 + dense. On capable machines this lets the AI actually assimilate *fine details and current state* (exact `hot_windows: [4-6h,15-18h,19-23h UTC]`, precise bot config values, the literal list of decisions from last week) instead of blurry topic matches. BM25 is always first-class and protected. Low-power machines stay fast and excellent with the hybrid baseline.
- **GPU acceleration (additive, only on power hardware)** — NVIDIA (CUDA / DGX Spark) and AMD (ROCm) are detected and used automatically for `embed_multi` token extraction and the MaxSim matrix math when the hardware profile already permits multi-vector. Brand-agnostic via PyTorch "cuda" device. One correct torch wheel install and it just lights up. See ECE-MULTI-VECTOR-UPGRADE.md.
- **Automatic multi-vector population** — On HIGH or capable BALANCED+GPU hardware the engine *automatically* finds chunks missing per-token data (historical notes) and populates them in the background on startup. You never run a manual `reindex` just to get the best recall. New writes have always been automatic. This is the detail that makes ECE superior to most other "eternal memory" attempts — full power just works.

**The automatic + multi-vector + GPU story in one sentence**: Buy or use a machine with decent RAM + GPU, run the engine once, and from that moment forward your AI gets the highest-fidelity recall possible with zero extra commands or configuration. Constrained machines (RPi, old laptops) continue to work great with the protected BM25+light-dense path. No dulling of the elite experience for those who can run it.

---

## Quick Start

```bash
# 1. Clone
git clone https://github.com/KCommader/eternal-context-engine
cd eternal-context-engine

# 2. Setup (creates venv, installs deps, scaffolds vault)
bash setup.sh

# 3. Fill in your identity
# Edit: vault/Core/USER.md, vault/Core/SOUL.md, vault/Core/COMPANY-SOUL.md

# 4. Start the engine
python engine/omniscience.py start

# 5. Connect your AI (see below)
```

**One-command setup** — writes the right MCP config for your AI runtime automatically:
```bash
python engine/omniscience.py setup-ai claude-code      # Claude Code
python engine/omniscience.py setup-ai claude-desktop   # Claude Desktop
python engine/omniscience.py setup-ai cursor           # Cursor
python engine/omniscience.py setup-ai zed              # Zed
```

After `setup-ai`, your AI reads `CLAUDE.md` at startup and calls `bootstrap_agent(reason="session_start")` automatically. Compaction becomes a non-event.

> Manual MCP config snippets are in [Connecting Your AI](#connecting-your-ai) below.

---

## Interface

The primary beautiful interface is **Obsidian** (open the `vault/` folder).

- Graph View (Ctrl/Cmd+G) for the connected knowledge network.
- Full support for backlinks, properties, Dataview queries, themes, mobile, canvases, etc.
- The shipped `.obsidian/` config makes it look premium out of the box (folder colors, callouts, graph tuning).

The template itself is the engine + vault + Obsidian experience. Extremely efficient and effective 3D frontends (high-performance graph visualization integrated with the live engine) are developed as the local/core part of the full ECE system (separate from this clean public template).

Delete the demo Knowledge notes and replace with your real content. The graph and Obsidian config remain.

---

## License

**Dual License — AGPL v3 / Commercial**

- **Free use** (personal, research, open source): [AGPL-3.0](LICENSE) applies. You must open-source any modifications or derivative services.
- **Commercial use** (proprietary products, SaaS, closed-source): requires a separate commercial license from KCommander. [Open an issue](https://github.com/KCommader/eternal-context-engine/issues) to inquire.
- **Contributors**: by submitting a PR you assign copyright to KCommander (see [LICENSE](LICENSE)). This is required to maintain dual-licensing rights.

Copyright © 2026 KCommander. All rights reserved.

---

## Contributing

Issues and PRs welcome. The goal is a simple, portable, powerful memory layer — keep it lean.

See [CONTRIBUTING.md](CONTRIBUTING.md) for ideas on where to contribute and the core principles (portable, Markdown-first, no lock-in). If it pushes the mission forward, it belongs here.
]}