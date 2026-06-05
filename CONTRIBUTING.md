# Contributing to Eternal Context Engine (ECE)

Thank you for your interest. ECE is AGPLv3 (or commercial dual license).

## Development

- The `engine/` is the heart. Changes to retrieval (multi-vector, RRF, BM25 primacy, hardware gates, GPU accel) must preserve "excellent everywhere, elite on power hardware" and never remove the fallback paths.
- `frontend/index.html` is self-contained (CDNs only). Keep it zero-build, picturesque + functional.
- `vault/` in the template must stay a clean generic scaffold. Real user data, skills, or internal notes never go here.
- Always run `python engine/omniscience.py doctor` and basic smoke after engine changes.
- For Obsidian experience: the shipped `.obsidian/` (graph.json + snippets/ece.css + bookmarks etc.) is intentional so new users see the beautiful connected interface immediately.

## Pull Requests

- Keep the README picturesque and maximally informative (purpose paragraph first, every function/tool detailed enough that someone understands ECE from the description alone).
- Update any retrieval or hardware docs for changes.
- No personal, brand, client, or internal project references in public template files.

## License

By contributing you agree your code is offered under the same dual license as the project (AGPLv3 + commercial option held by the original author).

Questions? Open an issue.
