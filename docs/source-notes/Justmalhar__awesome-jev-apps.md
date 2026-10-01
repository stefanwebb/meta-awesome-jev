# Justmalhar/awesome-jev-apps
- **One-liner:** 100 runnable, standalone Streamlit/Python apps built on Jev's three primitives, across 10 domains, with a strict app spec and provider config for TypeSafe or OpenRouter.
- **Language(s):** English
- **Type:** project/code (not a list) — an app collection/cookbook with a catalog.json index
- **Scale:** 100 apps, all marked built (✅). Categories: Developer Tools (11), Documents & Contracts (11), Data Engineering (12), AI Infrastructure · Jev + LLM (13), Finance (10), Business & Operations (11), Personal Productivity (10), Trust & Safety (7), Research & Science (8), Realtime & Interactive (7). Plus 00-primitives tour, _shared client, scripts, empty evals/, docs (APP_SPEC.md, openrouter-decisions-api.md).
- **Quality flags:** Single-author, likely heavily AI-assisted (100 apps, AGENTS.md). CI verifies app logic offline, not live responses. evals/ is explicitly "empty on purpose" — no benchmarks. Candid "What Jev is bad at" section. Not promotional beyond pricing framing.
- **Unique value:** Original runnable code for 100 use cases; the first write-up of OpenRouter's undocumented `/api/alpha/decisions` endpoint (with error codes); a codified app spec with six design rules and CI that fails if questions ask for arithmetic/counting/dates; a clear eval bar (public dataset, runnable baseline, cost+latency+accuracy, publish losses).

## Facts claimed about Jev
- Jev is a "System One model"; does not generate text; returns calibrated probabilities. Primitives: Noul (P(yes) 0–1, **no confidence field**), Choice (winner + distribution + confidence), Score (probability-weighted position + distribution + confidence; e.g. `severity = 2.61`).
- **Pricing: "$0.042 per million input tokens. Output tokens are free. ~150ms."** "roughly three orders of magnitude under a frontier chat model." OpenRouter price "same".
- TypeSafe native: `https://api.typesafe.ai/v1/systemone`, model `jev-latest`, key `TYPESAFE_API_KEY`, context **64k (32k state + longest question)**.
- OpenRouter: model `typesafe/jev-1.13`, endpoint `https://openrouter.ai/api/alpha/decisions` (undocumented, verified 2026-09-19), key `OPENROUTER_API_KEY`, **32k context advertised** (halved vs TypeSafe). Not in the public `/api/v1/models` catalog (446 models, 0 hits) though model page https://openrouter.ai/typesafe/jev-1.13 exists; `/chat/completions` returns 400 "is a decisions model ... Use the /api/alpha/decisions endpoint". Endpoint accepts TypeSafe native schema verbatim (`state`: string|record|array; `questions`: record). Errors: 400/401/402/429/529.
- Note: differs from kydlikebtc list, which says OpenRouter uses "a decisions endpoint, separate from chat" and does not record context; the 32k vs 64k discrepancy is specific to this repo.
- Batching: "TypeSafe measured 12.2× cheaper and 10× faster versus looping, with identical answers."
- Weaknesses (citing jaggedness notes jev-1.13): cannot count/arithmetic, cannot compare dates, reads literally, degrades on indirection and large irrelevant state, cannot generate.
- Recommends pinning `jev-1.13.0`, not `jev-latest`, in eval results.

## Key insights / patterns
- Six rules: (1) batch independent questions over the same state in one request; (2) every Choice gets a no-match option (`none`/`unclear`) or it nominates the least-wrong option at plausible confidence; (3) independent properties = separate Nouls, never levels on one rubric; multi-label = one Noul per label; (4) Score levels describe concrete situations, not "low/medium/high"; (5) policy (thresholds, weights) lives in code so tuning costs no inference; (6) confidence is an abstain signal, not correctness; Noul 0.5 = genuinely split, not "medium".
- Second request only when an answer is needed to fetch new evidence/decide next options.
- Recurring architecture: code finds candidates (ast, regex, difflib, parsers, blocking), Jev judges/selects → "verbatim guarantee" (a model that cannot generate cannot invent a value). Arithmetic in pandas/Python.
- Patterns: pairwise Score whose levels ARE the actions (dedupe, entity resolution); beam search over Choice probabilities for deep taxonomies; one Noul per requirement with veto/conjunctive semantics (RFP, policy, expense rules); two-stage tool routing (summaries wide, schemas narrow) over 42-tool MCP catalog; map-reduce over logs/traces; judgments as ML features; ~150ms enables realtime (keystroke validation, game referee, alert routing).
- Use TypeSafe direct for large state/production; OpenRouter for trial/one bill. Read context limit from config.
- Contribution bar: exploit something structural (parallel questions, calibrated abstention, cost delta, 150ms, non-generation); "An LLM app, but with Jev" is what this is not.

## Standout entries
- [00-primitives tour](https://github.com/Justmalhar/awesome-jev-apps/tree/main/00-primitives) — one-request tour of Noul/Choice/Score with distributions (tutorial)
- [OpenRouter decisions API write-up](https://github.com/Justmalhar/awesome-jev-apps/blob/main/docs/openrouter-decisions-api.md) — undocumented endpoint, errors, context caveat (docs)
- [APP_SPEC.md](https://github.com/Justmalhar/awesome-jev-apps/blob/main/docs/APP_SPEC.md) — question-design rules and "never ask the model to" list (guide)
- [Agent tool router](https://github.com/Justmalhar/awesome-jev-apps/tree/main/apps/ai-infrastructure/agent-tool-router) — two-stage cascade over 42 MCP tools (app)
- [LLM guardrails](https://github.com/Justmalhar/awesome-jev-apps/tree/main/apps/ai-infrastructure/llm-guardrails) — screen every input/output/tool call (app)
- [RAG reranker](https://github.com/Justmalhar/awesome-jev-apps/tree/main/apps/ai-infrastructure/rag-reranker) — drop-in cross-encoder replacement (app)
- [Model router](https://github.com/Justmalhar/awesome-jev-apps/tree/main/apps/ai-infrastructure/model-router) — calibrated difficulty + abstain (app)
- [Semantic Ctrl-F](https://github.com/Justmalhar/awesome-jev-apps/tree/main/apps/documents/semantic-ctrl-f) — verbatim clause retrieval (app)
- [Entity resolver](https://github.com/Justmalhar/awesome-jev-apps/tree/main/apps/data/entity-resolver) — Score levels as actions (app)
- [Deep taxonomy classifier](https://github.com/Justmalhar/awesome-jev-apps/tree/main/apps/data/deep-classifier) — beam search over Choice (app)
- [CI failure triage](https://github.com/Justmalhar/awesome-jev-apps/tree/main/apps/developer-tools/ci-triage) — bug/flake/infra classification (app)
- [evals/ README](https://github.com/Justmalhar/awesome-jev-apps/blob/main/evals/README.md) — bar for honest Jev benchmarks (guide)
