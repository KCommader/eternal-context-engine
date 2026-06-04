# Eternal Context Engine (ECE)

A local, private, portable eternal context system for personal AI assistants and teams.

**Works with**: Claude, Grok, Cursor, Zed, Gemini CLI, custom agents, or any MCP-compatible AI.

This is a **clean public template**. Do **not** commit any personal data, company projects, or proprietary information into this repository.

## Features (Upgraded)

- **Hardware-aware operation**: Automatically detects your machine (HIGH / BALANCED / CONSTRAINED / ULTRA_CONSTRAINED) and adjusts model loading accordingly.
- **Lightweight by default**: Uses efficient embedding models (nomic-embed-text-v1.5) on most hardware.
- **Optional advanced retrieval**: Multi-vector / late-interaction (ColBERT-style) support only activates on capable machines.
- **Strong hybrid search**: BM25 + vector, with BM25 as a first-class citizen.
- **Fully local & private**: Your data never leaves your machine.
- **MCP + REST API**: Easy to connect from Claude Desktop, Cursor, custom agents, etc.
- **Obsidian-friendly**: Store everything in human-readable Markdown.

## Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/eternal-context-engine.git
cd eternal-context-engine

# Install dependencies
pip install -r requirements.txt

# Run the engine (it will create a basic vault structure if needed)
python omniscience.py start --vault ./my-vault
```

Then connect your AI using the MCP server.

See `mcp_config.example.json` for examples.

## Important: This is a Template

This repository is intended as a **generic template**.

- Replace `YOUR_USERNAME` with your own GitHub username when forking or publishing.
- Set up your own vault in a location you control.
- Never commit your personal notes, project manifests, or any data that reveals your specific work into this repo.

For guidance, see `TEMPLATE_POLICY.md`.

## License

AGPL-3.0 — see LICENSE file.

This ensures the tool remains free and open while protecting against certain commercial lock-in.

## Upgrades in This Version

- Full hardware profile detection and adaptive loading (solves constant high memory usage from heavy models).
- Multi-vector late interaction support (for superior fine-grained recall) that only activates when your hardware can handle it.
- Cleaner separation of concerns for use as a shared template.

## Contributing

Pull requests that keep this repo as a clean template are welcome.

Do not submit PRs that add personal or domain-specific data.

## Acknowledgments

Built to solve the context window / compaction problem for long-running AI work.

Use it as your AI's long-term memory layer.