# cagbal/awesome-jev
- **One-liner:** Minimal reference list: 4 official TypeSafe repos and 10 community Jev projects, each with a one-sentence description and a strong liability disclaimer.
- **Language(s):** English
- **Type:** curated-list (trivial)
- **Scale:** 14 entries. Sections: Disclaimer · What is Jev? · Official projects (4) · Community projects (10).
- **Quality flags:** Very small. No original analysis. 5 of the 10 community entries are valentynkit's own projects (jev-belay, jev-commit, jev.nvim, jev-skip, jev-plays-pokemon-red), so it may be partly promotional or a contributor cluster. The descriptions are accurate and match other lists. Not stale, not spam.
- **Unique value:** Little. It is a clean minimal starting set. One entry not widely seen elsewhere is y0usaf/typesafe-cli (a terminal CLI for probability, choice and score queries).

## Facts claimed about Jev
- "TypeSafe AI's model for turning unstructured input into fast, typed decisions with probabilities that software can act on directly."
- Official repos: typesafe-sdk-python, typesafe-sdk-js (answer types inferred from the questions), system-one-adapter-python (compare conventional LLMs through a compatible decision interface), skills (teaches coding agents to build workflows).
- No versions, pricing or endpoints are given.

## Key insights / patterns
- Coding-agent guardrails:
  - jev-belay reads the Claude Code transcript and asks four questions before letting an unverified "done" through. It **fails open** on any error.
  - jev-commit checks that the commit message matches the diff, but **blocks only on a leaked credential**. It has an asymmetric blocking policy.
- Semantic editor search without embeddings: jev.nvim uses Treesitter to split functions, Jev scores each, and quickfix ranks by probability.
- Code owns routing, and Jev is called only at branches, scored with Brier (pokemon-red).
- Structured telemetry instead of pixels (typesafe-mario).

## Standout entries
- [typesafe-ai/typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) — official Python SDK (official)
- [typesafe-ai/typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) — official JS/TS SDK (official)
- [typesafe-ai/system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) — LLM comparison adapter (official)
- [typesafe-ai/skills](https://github.com/typesafe-ai/skills) — agent skills (official)
- [jkudish/jev-mcp](https://github.com/jkudish/jev-mcp) — MCP tools for checking/screening/ranking (agent tooling)
- [ellipsis-dev/blink](https://github.com/ellipsis-dev/blink) — Jev-guided file search (developer tools)
- [y0usaf/typesafe-cli](https://github.com/y0usaf/typesafe-cli) — terminal CLI for Jev queries (CLI)
- [valentynkit/jev-belay](https://github.com/valentynkit/jev-belay) — Claude Code "done"-claim gate (guardrails)
- [valentynkit/jev-commit](https://github.com/valentynkit/jev-commit) — pre-commit semantic check (developer tools)
- [valentynkit/jev-skip](https://github.com/valentynkit/jev-skip) — YouTube sponsor detection from captions (application)
