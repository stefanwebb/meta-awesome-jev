# JohnDotOwl/awesome-jev
- **One-liner:** Script-generated (GitHub search → projects.json → README) awesome list of 318 Jev projects in 10 categories, snapshot 2026-09-18.
- **Language(s):** English
- **Type:** auto-generated-list (semi-curated: descriptions/categories kept once edited)
- **Scale:** 318 entries (header), ~328 bullets. Categories: Official (14); SDKs and clients; Integrations (~19); Agent tooling; Browser and computer use; Applications (largest, ~120); Games and simulations; Demos and playgrounds (~9); Benchmarks and research (~21); Other lists (13). scripts/harvest.mjs (GitHub search), categories.mjs (keyword classify + noise filter), build.mjs, refresh.mjs; data/projects.json.
- **Quality flags:** Mostly auto-harvested; descriptions are GitHub descriptions. Stale (2026-09-18, 3 days post-launch). Minor duplicates (jev-synergy-screening listed twice under two owners; several Go "jev" clients). Misclassification (jev-sec-bench under SDKs). Not promotional. Used as a source by mabodx (284 entries).
- **Unique value:** Early, clean baseline; notable integrations not seen elsewhere (Vercel AI SDK provider page, Neon AI Gateway proxy, Home Assistant Assist agent, daggerverse docs site); a well-described "Other lists" section (13 sibling lists with sites/descriptions).

## Facts claimed about Jev
- Jev takes a state + typed questions (Choice, Score, Noul), returns typed answers with calibrated probabilities in one request; does not generate text.
- Model id `jev-latest`; docs docs.typesafe.ai; **early access since 2026-09-15**.
- HTTP API: POST /v1/systemone. Launch post covers "architecture, RLCD training, pricing, Doom and Wikiracing demos, and FAQ".
- Official repos: typesafe-sdk-js, typesafe-sdk-python (docs.typesafe.ai/sdk/python), system-one-adapter-python ("Drop-in TypeSafeClient replacement backed by LLM APIs"), skills, daggerverse (site daggerverse.docs.typesafe.ai).
- Vercel AI SDK provider: `@ai-sdk/typesafe-ai` plus `experimental_evaluate` using jev-latest (https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai); Vercel AI Gateway hosts `typesafe-ai/jev`.
- Verdict-open-jev: ModernBERT (151M) with "RLCD" calibrated uncertainty (community reproduction).
- nshkrdotcom/typesafe_sdk description claims "Jev is their current flagship model and is the first System One model".

## Key insights / patterns
- Integration surface: Postgres extension (pg-jev), Neo4j graph navigation by classifying neighbouring relationships (neo4jev), Home Assistant entities (HA-Jev) and Assist agent, Laravel, Neon AI Gateway routing, GitHub Action PR judge ("one parallel call, policy in code").
- Many vertical demos by the same author (ndolinschi: cartshield fraud disposition, lanebreak ticket routing, pulselane clinic triage) — typical "typed decision + policy in code" apps.
- Benchmarks worth noting: tool-call risk classification with "whether the confidence score is worth routing on" (themsquared/jev-benchmark); rubric eval cheap enough per PR (jev-evals); one-second bitbank trading judgments logged for calibration (jev-tick-lab); switchboard guardrail/router with independent accuracy/calibration/latency eval.
- Harvest heuristics exclude noise (name collisions) — cf. isNoise in categories.mjs.

## Standout entries
- [Quick start](https://docs.typesafe.ai/introduction/quickstart) — official quick start (official)
- [HTTP API](https://docs.typesafe.ai/api) — /v1/systemone contract (official)
- [daggerverse](https://github.com/typesafe-ai/daggerverse) — official Dagger modules (official)
- [Vercel AI SDK provider](https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai) — @ai-sdk/typesafe-ai + experimental_evaluate (integration)
- [pg-jev](https://github.com/realZachi/pg-jev) — Postgres extension (database)
- [neo4jev](https://github.com/jexp/neo4jev) — Neo4j graph navigation (database)
- [HA-Jev](https://github.com/AboveColin/HA-Jev) — Home Assistant integration (IoT)
- [jev-pr-judge](https://github.com/juanegido/jev-pr-judge) — PR verdicts as GitHub Action (devtools)
- [jev-atlas](https://github.com/gorock007/jev-atlas) — evidence-first field guide for humans and agents (guide)
- [themsquared/jev-benchmark](https://github.com/themsquared/jev-benchmark) — tool-call risk classification benchmark (benchmark)
- [switchboard](https://github.com/aniruddh-krovvidi/switchboard) — guardrail + router with independent eval (tool)
- [openjev-sglang](https://github.com/ekzhang/openjev-sglang) — prefill-only Jev-compatible endpoint (open reproduction)
- [Verdict-open-jev](https://github.com/Heman10x-NGU/Verdict-open-jev) — ModernBERT decision engine with audit (open reproduction)
- [daf-jev](https://github.com/docxology/daf-jev) — Python toolkit: builders, gates, calibration, MCP (tool)
- [OmniJev/awesome-jev](https://github.com/OmniJev/awesome-jev) — papers/reproductions list (list)
