---
type: concept
tier: long_term
tags: [ece, automatic, multi-vector, upgrade]
created: 2026-01-01
---

# Automatic Upgrades

On capable hardware (HIGH or good BALANCED with GPU), ECE automatically populates the per-token multi-vector data for any existing chunks that are missing it.

**You never have to run `python engine/omniscience.py reindex` just to get the best recall.**

- New and changed notes get multi_vec at write time (if hardware allows).
- On startup the engine scans for missing token-level vectors and fills them in the background.
- This is the "set and forget" that makes ECE superior to most other memory systems: full fidelity just works the first time you run it on power hardware.

See [[Hardware Profile]] for when this activates.
See [[Multi-Vector Assimilation]] for what the extra data buys you (exact hot windows, precise config values, current project state).
See [[Core Concepts]] and [[Getting-Started]] to begin.

#ece #automatic #multi-vector #no-manual-reindex
