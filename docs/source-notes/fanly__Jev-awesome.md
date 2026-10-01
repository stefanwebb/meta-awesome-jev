# fanly/Jev-awesome
- **One-liner:** Small, Chinese-first, developer-focused Jev catalog of 14 curated entries. Each card explains what Jev owns in the project, what to read first, and what hasn't been verified. It comes with three Chinese guide essays and a heavily engineered collector pipeline.
- **Language(s):** Chinese (primary README and guides), English (short README.en.md)
- **Type:** curated-list + tutorial/study-guide
- **Scale:** 14 curated entries and 118 in an inbox (not featured). The radar has about 132 auto-discovered items. Categories: Official & Changes (2) · Getting Started & Patterns (2) · Applications & Tools (4) · SDKs & Integrations (3) · Evals & Limits (1) · Research & Alternatives (2). Featured launch-v1: 10 repos. Three guides: start-here, choose-your-path, browser-agent-code-tour.
- **Quality flags:** Very small curated set. It disclosed that an AI agent (`cursor:delegated-editor`) produced the curation with no human per-item review and no reproduction. The repo is mostly Python pipeline code (371 files, tests, config) rather than content. Scheduled collection is off by default. Honest verification levels (discovered / source_checked / code_located / reproduced / benchmarked), and automation may not self-promote to reproduced/benchmarked. Not promotional.
- **Unique value:** Chinese-language explainers on **where in the control flow Jev belongs**, a decision tree for picking between the official API, adapter, LocalJev and kev, and a code tour of jev-ultrafast. A name-disambiguation table. The radar tracks official Python SDK release versions.

## Facts claimed about Jev
- The official Python SDK is PyPI `typesafe-sdk`. The client is `TypeSafeClient.system_one` with `Choice` / `Noul` / `Score` and needs `TYPESAFE_API_KEY`. Docs at docs.typesafe.ai/sdk/python.
- **typesafe-sdk-python releases: v0.5.7 (2026-09-12), v0.6.0 (2026-09-15), v0.7.0 (2026-09-18)** (radar).
- Official Confidence doc: **confidence only applies to Choice/Score; Noul has no confidence**. This agrees with wh000wh000 and contradicts bakiabaci's `verdict.confidence` on noul.
- Primitives doc: field semantics for Choice/Score/Noul and "isolation within the same request" (questions in one request are isolated from each other).
- The official skill does not call the model itself. Read `skills/typesafe-ai/SKILL.md` first.
- jev-ultrafast needs `TYPESAFE_API_KEY` plus `TEXT_MODEL_API_KEY`, and Chrome/Browser Harness. Its entry point is `jev_ultrafast/agent.py`. Its cloud-product waitlist is a different deliverable from the open local demo. The 7.1 s claim was not reproduced here.
- githubnext/localjev is a GitHub Next local `POST /v1/systemone`-compatible implementation (Bun + Diffusion), community/research, not official.
- jaredpalmer/kev is described as a "tiny Jev-like model built on top of Qwen2.5-0.5B" with LoRA/readout heads, and the author says some checkpoints failed their release gate. This **contradicts bakiabaci's "Qwen3.5/3.8 (0.8B–27B)"**, though it may reflect different versions.
- iammrduncan/typesafe-ai-benchmark compares Qwen structured output on Cerebras vs Jev vs local Needle. The author says Needle was measured under different conditions.

## Key insights / patterns
- One-sentence rule: Jev belongs at the step of "calibrated judgment among finite options", not "writing long text from scratch".
- Control-flow split: perceive/collect → **decide (Jev)** → generate (another model) → execute. Coupling decision and generation in one LLM makes the action space uncontrolled, hard to test, audit and rate-limit.
- Placement table:
  - Browser agent: choose CLICK/TYPE_TEXT; don't let it invent city names.
  - Support triage: department Choice + urgent Noul; don't write the reply.
  - SQL/graph: row/edge predicate; don't generate SQL.
  - Guardrails: violation / policy choice, but not a whole compliance system.
- When NOT to use Jev yet:
  - There are no discrete candidates (open set, or thousands changing daily).
  - You want long-form or creative output.
  - You haven't designed human takeover for low confidence / `BLOCKED` / refusal.
- Selection path:
  - Production with budget: official SDK + primitives + confidence docs.
  - Learning question design: the official SKILL.md.
  - No key: system-one-adapter-python (LLM stand-in) or LocalJev, clearly labeled as not Jev quality.
  - Research: kev, pointing the SDK `base_url` at a local server.
  - Comparisons: read benchmark methods and raw exports.
- jev-ultrafast lessons:
  - Enumerate executable actions first, then ask Jev.
  - Text generation is an optional side effect.
  - Measure decision latency, text-gen latency and page-load wait separately.
  - Ask target heads speculatively in the same request and execute only the one matching the chosen operation.
- neo4jev pattern: per-hop Choice (which edge) plus Noul (goal reached?) in the same request, with beam search in the app layer.
- pg-jev: returns per-row probabilities (jev / jev_prob) with no vector column. Cost and latency scale per row.
- Name-confusion warning: LocalJev and kev are compatible or independent, not official. awesome-jev lists are navigation, not evidence.

## Standout entries
- [typesafe-ai/typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) — official Python SDK (official)
- [typesafe-ai/typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) — official JS/TS SDK (official)
- [TypeSafe Confidence](https://docs.typesafe.ai/confidence.md) — confidence only on Choice/Score (official docs)
- [TypeSafe Primitives](https://docs.typesafe.ai/primitives.md) — question types and in-request isolation (official docs)
- [typesafe-sdk-python v0.7.0](https://github.com/typesafe-ai/typesafe-sdk-python/releases/tag/v0.7.0) — SDK release 2026-09-18 (official)
- [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) — decision/generation split browser agent (browser)
- [droidrun/mobile-jev](https://github.com/droidrun/mobile-jev) — Android device agent (mobile)
- [githubnext/localjev](https://github.com/githubnext/localjev) — GitHub Next local /v1/systemone-compatible server (research)
- [jaredpalmer/kev](https://github.com/jaredpalmer/kev) — trainable Jev-like model (research)
- [iammrduncan/typesafe-ai-benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark) — LLM structured output vs Jev benchmark (benchmark)
- [jexp/neo4jev](https://github.com/jexp/neo4jev) — graph navigation via Choice + Noul (integration)
- [realZachi/pg-jev](https://github.com/realZachi/pg-jev) — Postgres semantic filter extension (integration)
- [yzfly/awesome-jev-zh](https://github.com/yzfly/awesome-jev-zh) — Chinese sibling list (list)
