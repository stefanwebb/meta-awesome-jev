# heyjunpenn/awesome-jev
- **One-liner:** Large, daily-updated catalog of 962 GitHub projects built with Jev, with evidence-labelling scheme, backed by the jevbest.com Astro/Cloudflare site.
- **Language(s):** English, plus full translations: Simplified Chinese, Japanese, Korean, Spanish, Portuguese (Brazil) (README.*.md)
- **Type:** curated-list (large, semi-automated; also contains a project/code site with sponsor/Stripe backend)
- **Scale:** ~962 repos (~980 links) in 11 categories: Official (6), SDKs & clients (59), Jev-like models (80), Frameworks & integrations (82), Agent tooling (232), Browser & computer use (76), Applications (131), Games & simulations (73), Demos & playgrounds (66), Benchmarks & research (116), Other lists (41); plus "Repository-level code references" (3), "What Jev is", official resources table, inclusion criteria. Tables with stars/language/added-date. CHANGELOG.md with daily additions.
- **Quality flags:** Likely semi-automated (CHANGELOG "generated from the verified catalog"; stars snapshot 2026-09-18–30). Some entries look loosely related / mislabelled (e.g. `cequence-io/openai-scala-client`, `OpenRouterTeam/ai-sdk-provider`, `nshkrdotcom/typesafe_sdk` described as an ai-sdk port) — keyword-match inclusion leaks. Duplicate names (two "laya" repos, two "jeff"). Very high star counts for some "Jev-like models" (laya ★17,709) should be treated cautiously. Has paid sponsor placements (sponsor D1 DB, Stripe) — mildly promotional. Claims per-entry evidence labels (Call site verified, etc.) but README tables do not show labels per entry.
- **Unique value:** Biggest single catalog in batch; the only one with a large "Jev-like models" section (80 open replicas/alternatives) and 41 "Other lists" (a map of the awesome-jev ecosystem); evidence/verification taxonomy (Public source / Call site verified / Demo only / README claim / Maintainer runbook / Reviewer reproduced / Author-reported metric / Third-party reproduced); six-language translations.

## Facts claimed about Jev
- Jev = TypeSafe AI's "System One model for typed decisions inside software"; takes a **state** plus one or more typed **questions**, returns structured answers; "does not generate prose."
- Three primitives: `Choice` (select one option; returns option, probabilities, confidence), `Score` (ordered rubric; score, level probabilities, confidence), `Noul` (estimate whether a statement is true; probability 0–1). NOTE: boolean primitive is named **"Noul"** here (docs URL https://docs.typesafe.ai/primitives/noul) — other lists may call it Boolean/Bool.
- Questions in one request share the same state and are evaluated independently.
- Official SDKs: Python `pip install typesafe-sdk` (sync + async, github.com/typesafe-ai/typesafe-sdk-python); JS/TS `npm install @typesafe-ai/sdk` (github.com/typesafe-ai/typesafe-sdk-js); official agent skills repo typesafe-ai/skills (★765); System One adapter (Python) — drop-in TypeSafeClient replacement backed by OpenAI/Anthropic for comparison; Daggerverse modules; Overwatch (observability/eval).
- Community SDK entries mention model alias `jev-latest` as default (kisshan13/typesafe-ai-go) and endpoint schema `/v1/systemone` (LitJev entry).
- Official URLs: typesafe.ai, docs.typesafe.ai (/introduction, /primitives, /confidence, /patterns, /api, /models — "aliases, versions, pricing, and limits"), evals.typesafe.ai (workflow evaluations).
- Third-party claims in entries: jev-column-race "Jev vs Gemini 3.8 Flash: labelling 1,000 app reviews, 4.1× faster and 7× cheaper"; laya "33 ms" single-pass multilingual replica; von "Sub-15ms"; AgentJev-0.6B "~50ms".
- No pricing/latency/context-length numbers for Jev itself stated in README.

## Key insights / patterns
- Split complex decisions into narrow questions and compose in ordinary code; keep authorization, arithmetic, thresholds, side effects and fallback in code.
- Disclaimer: "Schema-valid output is not the same as a correct decision" — evaluate on own data, set thresholds per risk, keep consequential actions behind deterministic checks, human fallback.
- Entry anatomy: state → question → answer → code action; primitive + pattern (e.g. "Typed tool dispatch").
- Big open-replica wave: many projects read next-token/option logits from open models (Qwen3.5, Gemma, DiffusionGemma, ModernBERT, GLiNER) in a single prefill-only forward pass to emulate Jev's API (Simple Jev, LocalJev, openjev-sglang, LitJev, mini-jev). Training with strictly proper scoring rules ("RLCD") recurs (laya, Verdict-open-jev).
- Recurring uses: RAG reranking (Milvus bootcamp, TrainLCD), LLM guardrails (agentgateway), coding-agent gating/routing (mu, Keel, pi-jev-router), context filtering (omp-statify), browser-agent action choice, game agents (Doom, chess).
- Calibration tooling niche: jev-calibrate, jevcal, jeval (set human hand-off line from mistake cost), jev-benchmarks (selective risk).

## Standout entries
- [TypeSafe agent skills](https://github.com/typesafe-ai/skills) — official agent skill for Claude Code/Codex (official)
- [TypeSafe Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python) — official, `pip install typesafe-sdk` (official)
- [TypeSafe JavaScript SDK](https://github.com/typesafe-ai/typesafe-sdk-js) — official, `@typesafe-ai/sdk` (official)
- [System One adapter (Python)](https://github.com/typesafe-ai/system-one-adapter-python) — LLM-backed drop-in for comparing Jev vs chat models (official)
- [TypeSafe Overwatch](https://github.com/typesafe-ai/Overwatch) — observe/evaluate System One workflows (official)
- [Workflow evaluations](https://evals.typesafe.ai/) — TypeSafe's published eval methodology (official)
- [agentgateway Jev guardrail example](https://github.com/agentgateway/agentgateway/tree/main/examples/llm-guardrail-jev) — Jev as proxy guardrail (integration)
- [Milvus Search with Jev](https://github.com/milvus-io/bootcamp/tree/master/bootcamp/RAG/search_with_jev) — RAG result selection (integration)
- [NanoJev](https://github.com/TianyuCodings/NanoJev) — open 0.6B Jev replica with training pipeline/weights (research)
- [jevlike](https://github.com/vinnylarouge/jevlike) — small option-scoring model, Doom/chess demos (research)
- [Simple Jev](https://github.com/featherless-ai/simple-jev) — open-model logits-based Jev-style server (Jev-like model)
- [jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas) — evidence map of where Jev holds up vs breaks (evaluation)
- [jev-calibrate](https://github.com/smkrv/jev-calibrate) — calibrate questions against own labels (tool)
- [jevbench](https://github.com/fstandhartinger/jevbench) — JevBench v1 for Jev-class models (benchmark)
- [zod-jev](https://github.com/jomatsu/zod-jev) — semantic validation of request bodies as calibrated probabilities (SDK/pattern)
