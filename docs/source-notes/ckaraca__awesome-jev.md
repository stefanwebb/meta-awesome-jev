# ckaraca/awesome-jev
- **One-liner:** A clean, star-sorted awesome list of about 130 tools, integrations and experiments built on Jev. It is strong on official TypeSafe repos and on big-framework integrations.
- **Language(s):** English
- **Type:** curated-list
- **Scale:** ~130 entries. Sections: Official resources / Frameworks & integrations / Browser & computer use / Mobile & robotics / Coding agents & developer tools / MCP servers & agent skills / Observability / Data, search & classification / Trading / Games & fun / Apps with Jev inside / Community SDKs / Open models & replications / Other lists. Stars are refreshed weekly by a workflow (`scripts/sort_by_stars.py`), and a lychee link-check runs too.
- **Quality flags:** Well curated: short factual descriptions, safety-default notes on trading and device entries, and a note that "stars belong to the whole repository". There is no benchmarks, papers or articles section. Some star counts look very high for a 2-week-old ecosystem (laya 27.2k, fast-jev-compaction 7.1k); treat them as the list's own claims. It names another list "AbdelStark/awesome-typesafe", while the repo in this batch is AbdelStark/awesome-typesafe-jev (it may have been renamed).
- **Unique value:** The best single index here of **official TypeSafe GitHub repos and docs pages**, plus Jev integrations in major frameworks (Composio, Vercel AI SDK, Rig, Ax, ReqLLM/Ash, Arize Phoenix/OpenInference, virattt/ai-hedge-fund, trycua/cua, vercel-labs/json-render and ai-cli).

## Facts claimed about Jev
- Available on **Vercel AI Gateway as `typesafe-ai/jev`**, "no waitlist needed".
- Official docs pages: /introduction/quickstart, /primitives (Choice, Score, Noul), /patterns ("Confidence-gated routing, composite scoring, speculative fan-out, intent routing"). There is also console.typesafe.ai (API keys and **live request inspection**) and **evals.typesafe.ai** (published workflows, model comparisons, methodology).
- Official GitHub org `typesafe-ai`: `skills` (official agent skills for Claude Code/Codex, ⭐2.3k), `system-one-adapter-python` (drop-in `TypeSafeClient` replacement backed by ordinary LLM APIs, for local testing), `typesafe-sdk-js` (TS SDK with inferred answer types) and `typesafe-sdk-python` (sync and async).
- The Vercel AI SDK exposes Jev through the "experimental evaluation API" for Choice, Score and **Boolean** questions.
- Rust `rig-typesafeai` crate. Elixir `req_llm` supports TypeSafe or OpenRouter.
- OpenInference records TypeSafe SDK calls as OTel spans.
- Per-entry claims: awlevin computer use costs about **$0.0002/step**. Voice browser takes ~300 ms per spoken word. tax-doc-classifier reports **100% strict accuracy on 261 IRS forms at ~$0.001/page**. jev-drone runs its control loop at 2.5 Hz.
- feder-cr/jev (jevos) supports Noul only, not Choice or Score.

## Key insights / patterns
- Recurring architecture: **Jev picks and an LLM generates**. Examples: browser-use (Jev picks the element, a small LLM types text), JevSeek (Jev routes, DeepSeek generates arguments), quackd (LLM plans, Jev handles cheap steps), minecraft-agent (LLM planner plus Jev picking from bounded actions).
- Coding-agent uses: **context compaction** (score each tool call and drop the stale ones: fast-jev-compaction, save-token-jev-clean), **model/effort routing per turn** (jev-router, jev-codex-router, codex-jev-router), **rule adherence checks** (abide, jev-rules), **"done" verification hooks** (jev-belay, pi-warden) and semantic linting.
- Design principle (jev-plays-pokemon-red): "code owns the route and the arithmetic, Jev picks only at branches", with Brier-scored predictions.
- Safety-default notes: trading bots dry-run by default, sending stays manual in the chat assistant, and some integrations are opt-in or off by default. That is good practice for a meta-list to copy.
- Privacy caveats are called out: jevgrep sends source code to the hosted provider, and jev-chat sends chat context to providers.
- There are many open replications (Laya, Kev, SemIf/openjev, NanoJev, AnyJev by Nokia, ollaya, rizzo-flow, simple-jev, openjev-sglang). Several expose a TypeSafe-compatible `/v1/systemone` endpoint.

## Standout entries
- [Documentation](https://docs.typesafe.ai/) — official docs (official)
- [Patterns](https://docs.typesafe.ai/patterns) — confidence-gated routing, composite scoring, speculative fan-out (official)
- [Workflow evals](https://evals.typesafe.ai/) — official evals and methodology (official/benchmark)
- [typesafe-ai/skills](https://github.com/typesafe-ai/skills) — official agent skills (official)
- [typesafe-ai/system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) — LLM-backed drop-in client for testing (official tool)
- [typesafe-ai/typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) — official TS SDK (SDK)
- [typesafe-ai/typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) — official Python SDK (SDK)
- [vercel/ai](https://github.com/vercel/ai) — AI SDK TypeSafe provider (integration)
- [ComposioHQ/composio](https://github.com/ComposioHQ/composio) — Jev tool selection (integration)
- [Arize-ai/openinference](https://github.com/Arize-ai/openinference) — tracing TypeSafe calls (observability)
- [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) — browser agent (project)
- [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) — Claude Code compaction plugin (dev tool)
- [jkudish/jev-mcp](https://github.com/jkudish/jev-mcp) — MCP server (MCP)
- [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) — open decision model (open model)
- [jaredpalmer/kev](https://github.com/jaredpalmer/kev) — tiny trainable Jev-like model (open model)
