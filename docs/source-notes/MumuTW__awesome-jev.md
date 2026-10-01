# MumuTW/awesome-jev
- **One-liner:** Small, opinionated "taste over breadth" Jev list with editorial notes per entry, plus a clearly labeled Jev-like open-model section; available in five languages.
- **Language(s):** English, Traditional Chinese, Simplified Chinese, Japanese, Korean (readme.*.md translations)
- **Type:** curated-list
- **Scale:** ~50 entries. Sections: How we curate, Observations, Official (6), Platforms (2), Browser & computer use (3), Coding agents (6), Routers (2), Data & libraries (1), Demos worth studying (2), Use cases & concepts (Framing, Product-shaped demos, Real-time/multi-agent concepts, Circulating (caveats)), Jev-like & related models (10), Related lists (4).
- **Quality flags:** Claims to be "Maintained by Grok Bot (grok.com) with a human in the loop" — AI-written notes. Inclusion driven by X/HN "heat", which biases toward viral items. Notes are opinionated but include caveats. Uses "boolean" rather than "noul" terminology. Not auto-generated; not spammy.
- **Unique value:** Editorial per-entry caveats (who it's for, when overkill); explicit inclusion criteria (2-of-3 rule); "Circulating (caveats)" section flagging viral-but-unverified claims (e.g., "Rebuilt Tesla FSD in under an hour"); multilingual translations; observations on architecture.

## Facts claimed about Jev
- Jev is TypeSafe's "System One" model for typed decisions (choice, score, boolean with confidence).
- Official: typesafe.ai (early-access console), docs.typesafe.ai, `typesafe-sdk-js` (`@typesafe-ai/sdk`), `typesafe-sdk-python`, `system-one-adapter-python` (drop-in `TypeSafeClient` backed by chat LLMs for A/B), `typesafe-ai/skills`, Cloudflare Workers AI `typesafe/jev`.
- Vercel AI Gateway model string `typesafe-ai/jev`, called via AI SDK 7 `evaluate`; AI SDK `experimental_evaluate` exposes Choice/Score/Boolean.
- Reported numbers (authors'): jev-ultrafast Zürich→London flights ~7s, ~$0.0039; typesafe-computer-use (macOS OCR + Jev) ~$0.0002/step; intent launcher ~100 ms; voice→browser ~300 ms / ~$0.0002; on-device OCR→Jev ~90 ms; Slay the Spire 2 ~0.7 s picks; SuperX viral post scorer 61 questions; jevlike ~161 HN points.
- jev-trader: one buy/sell decision per Monad block on Kuru MON-USDC.
- Laya: HF `convaiinnovations/laya`, PyPI `laya`, not affiliated.

## Key insights / patterns
- "Jev wins when the action space is finite and observed": turn the world into an indexed table, ask one parallel pass; free-form "do whatever" agents are the wrong fit.
- Keep a small LLM only for text generation (typing) — recurring architecture in Ultrafast and computer use.
- Coding-agent use is about gates, not authorship: compaction, review, tool allow/deny, model routing.
- Compaction as a gate (kept context stays verbatim) rather than a summarizer that invents.
- Feed observed structured state, not raw pixels (Mario).
- Fast System One reacts / slow System Two plans (Minecraft: Jev reacts, Astra plans).
- "System One as permissioning": agent asks `jev_ask` before acting (pi-jev).
- Access path matters: Vercel AI Gateway opened experimentation overnight vs waitlist.
- Router caveat: watch cost regressions when the cheap model starts failing.
- Jev-like models: a compatible wrapper does not become System One quality; treat open-model scores as educational, not production calibration.

## Standout entries
- [System One docs](https://docs.typesafe.ai) — official docs (official)
- [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) — chat-LLM baseline for A/B (official)
- [skills](https://github.com/typesafe-ai/skills) — official agent skills (official)
- [Jev on Vercel AI Gateway](https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway) — gateway access (platform)
- [jev-ultrafast](https://github.com/browser-use/jev-ultrafast) — browser loop flagship (browser)
- [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) — macOS OCR + Jev with cost table (computer use)
- [jev-browser-pilot](https://github.com/aidil2105/jev-browser-pilot) — library-shaped browser loop (browser)
- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) — Claude Code compaction plugin (coding agents)
- [pi-warden](https://github.com/DevMortimer/pi-warden) — Pi guardrails (coding agents)
- [jev-router](https://github.com/gargpratyush/jev-router) — cheap/strong routing for Claude Code and Codex (router)
- [pg-jev](https://github.com/realZachi/pg-jev) — PostgreSQL extension (data)
- [Building a Harness with Jev (LangChain)](https://x.com/sydneyrunkle/status/2100754364545761643) — gates in the agent loop (article)
- [nimble](https://github.com/bespokelabsai/nimble) — open "Jev recipe" LoRA + constrained serving (reproduction)
- [Flavio Copes deep dive](https://flaviocopes.com/jev/) — long-form explainer (tutorial)
- [dabit3/jev-experiments](https://github.com/dabit3/jev-experiments) — intent launcher and predictive spreadsheet (demo)
