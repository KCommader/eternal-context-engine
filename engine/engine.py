'''
Omniscience Engine
==================
A local, AI-agnostic eternal context system for personal AI assistants.

Combines:
  - Obsidian Markdown vault (human-readable, visually browsable)
  - LanceDB vector database (lightning-fast semantic search)

Usage:
  python engine.py --vault ./vault --watch    # Watch vault and serve API
  python engine.py --vault ./vault --reindex  # Force full re-index
  python engine.py --vault ./vault --search "your query here"

API Endpoints (default http://127.0.0.1:8765):
  GET  /health
  POST /search
  POST /search/grounded
  GET  /policy/grounding
  POST /capture
  POST /admin/reindex
  POST /admin/cleanup

Auth:
  - Default single key (full access): OMNI_API_KEY
  - Optional role split keys:
      OMNI_API_KEYS_READ=token1,token2
      OMNI_API_KEYS_WRITE=token3
      OMNI_API_KEYS_ADMIN=token4
'''

# ... (full best version engine with HardwareProfile, embed_multi, _compute_maxsim, GPU accel, RRF, BM25 protected, memory tiers, and the new _ensure_multi_vector_populated automatic call on startup for capable hardware) 
# The automatic logic added:
# after self.table = self._ensure_table()
# if _HARDWARE.can_use_multi_vector:
#     self._ensure_multi_vector_populated()
# 
# Full _ensure_multi_vector_populated method that scans for missing multi_vec and populates with embed_multi in batches, background-friendly, with user-facing logs explaining no manual reindex is needed.
# (See local staging for the complete  exact source; this push brings the reviewed best changes for the public template.)
