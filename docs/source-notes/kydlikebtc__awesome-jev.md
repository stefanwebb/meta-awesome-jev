# kydlikebtc/awesome-jev
- **One-liner:** "Jev Decision Atlas": an evidence-tracked catalogue of ~1,210 public Jev resources indexed by decision pattern, with a cross-gateway compatibility matrix and negative results.
- **Language(s):** English + full Chinese (README.zh-CN.md, docs/*.zh-CN.md)
- **Type:** curated-list (heavily tooled; README generated from catalog.json, also ships an MCP server, Claude Code plugin/skill, static site)
- **Scale:** 1,210 resources; 1,207 dated HTTP 2xx link records; 1,076 call-site citation records; 73 independent-measurement rows (71 benchmark rows, 25 with structured measurement). Organized by 18 decision patterns: Tool selection (230), Intent routing (35), Context compaction (34), Safety gating (139), Output validation (134), Retry control (7), Human escalation (69), Model routing (44), Speculative fan-out (32), Search & ranking (64), Structured extraction (17), Classification (120), ML feature extraction (8), Document triage (20), Support triage (8), Content scoring (165), Recommendation (1), Overview (451). Also by resource kind; docs/compatibility.md, patterns.md, benchmarks.md, measured.md, sources.md, vetting.md; 4 example scripts (three-primitives, confidence-gate, fan-out, tool-selection).
- **Quality flags:** Highest-rigor list seen. Every row names its source, call-site file and read date; explicitly flags "vendor numbers", "shadow mode", "measured, not adopted", single-commit, no-license. Candid that 0 of 25 measurements were human-read against reports; many rows machine-drafted (a model wrote Chinese notes). Some rows reached via "sibling-list aggregate" (1,053 rows) so breadth partly inherits other lists. Examples are "not executed against the live API". Not affiliated with TypeSafe.
- **Unique value:** (1) Cross-platform compatibility matrix (model strings, yes/no type name, confidence location, endpoint, env var) across 13 surfaces; (2) "Negative results first" section; (3) benchmark index by comparator/dataset; (4) "corrections" table debunking circulating misinformation; (5) table of Jev-compatible reimplementations (not Jev) with weights/endpoint; (6) per-pattern "when not to" guidance.

## Facts claimed about Jev
- Jev is a decision model from TypeSafe AI; does not generate text; returns typed answers with calibrated confidence. Three primitives: `choice`, `score`, `noul` (the yes/no type is **`noul`**, not "Binary"; Vercel AI SDK evaluation API and `@ai-sdk/typesafe-ai` spell it `boolean`, read from `.probability`).
- Model IDs (native): `jev-latest`, `jev-preview`, `jev-1.13.0`. "The model ID is `jev-1`" and `typesafe/jev-1` are called fabrications.
- Gateway strings: Vercel `typesafe-ai/jev`; Cloudflare Workers AI `typesafe/jev`; OpenRouter `typesafe/jev-1.13` and `~typesafe/jev-latest` (tilde); LiteLLM pass-through `jev-latest`/`jev-1.13.0`/`jev-preview`; AI/ML API `typesafe/jev`; Pydantic AI `typesafe:jev-latest`; Netlify `jev-latest (default)`; Bifrost `jev-latest`.
- Endpoint: native `POST /v1/systemone`; Vercel/LiteLLM/Bifrost `POST /typesafe/v1/systemone`; AI/ML API `POST /v1/decisions`; Cloudflare `env.AI.run()` with state/questions wrapped in `input`; OpenRouter uses a decisions endpoint separate from chat.
- Env vars: `TYPESAFE_API_KEY` (native, LiteLLM, Pydantic AI, LangChain); `TYPESAFE_AI_API_KEY` (@ai-sdk/typesafe-ai); `AI_GATEWAY_API_KEY` (Vercel); `JEV_TOKEN` (rig/Rust); `OPENROUTER_API_KEY`; Netlify needs none (Node 20+). Vercel AI SDK needs 7.0.105+.
- SDKs: Python `typesafe-sdk` (`client.system_one(...)`, classes `Choice`, `Score`, `Noul`); JS `@typesafe-ai/sdk` (`client.systemOne(...)`, functions `choice()`, `score()`, `noul()`). Two answer-access patterns: `response.answers["key"]` vs `response.nouls["key"]`/`.choices`/`.scores`. LangChain uses `.nouls[k].noul`. Pydantic AI maps bool→noul, Literal→choice, ordered IntEnum→score.
- Output schema: noul returns 0–1 probability and **no confidence field**; choice returns `choice` + `probabilities` + `confidence`; score returns `score` + `legend` + `probabilities` + `confidence`. Score is probability-weighted and non-integer (docs example `1.05` on three levels).
- Limits: choice max **255 options** (rig enforces at compile time); score **2–10 levels, 0-indexed**; context **64k tokens per request, 32k for state + longest question**; no published tokenizer; input text only (string, JSON object, array of text); **output tokens free** (only input charged); **no streaming** anywhere; no published weights, cannot run locally.
- Vendor headline figures "193.6x / 444.6x / 67.8%" are vendor-run with reference answers derived from other models' judgements; vendor launch post calls them an upper bound. No paper on the training method exists.
- `jevai.org` is an unaffiliated community site with a different API shape—do not copy code from it.
- Jaggedness doc (docs.typesafe.ai/model-jaggedness/jev-1.13) weaknesses: literal reading, arithmetic and counting, date comparison, indirection, large states full of irrelevant detail, adversarial content; a Choice over options vs one Noul per option answer different questions.
- Independent test: reversing option order moved a probability enough to cross a 0.9 threshold (unreplicated).
- Lindfors test: 24 Norwegian documents, "calibrated judgments for half a cent".

## Key insights / patterns
- Decision fit test: closed answer space, runs often, being wrong survivable/detectable, context fits 64k/32k. Otherwise keep an LLM. Division of labour: LLM for open reasoning/writing, decision model for frequent typed judgments, code for policy.
- Primitive picker (from vendor docs): generation needed → not Jev; code can do it → code; split complex judgments into several questions; one noul per item; then score/noul/choice; one snap judgment per question.
- Thresholds do not transfer across question types (noul probability ≠ choice confidence), across model versions (pin `jev-1.13.0`, log the versioned ID in response), or to compatible reimplementations. Freeze option order.
- Porting across gateways is not a URL swap; surfaces exposing `/typesafe/v1/systemone` are cheapest to migrate.
- Safety gating is "defence in depth, not a security boundary"—destructive actions need deterministic rules/humans.
- Tool selection: choice over tools + `none`, gate on confidence, fall back to planner; Jev chooses *which*, not arguments. Two-stage patterns (FastMCP: wide choice coarse-rank, then noul per shortlisted tool). Computer-use: reserved `reobserve`/`abstain` options (Cua).
- Search: reranks shortlist; not a full retrieval stack. Extraction: resolve dates/arithmetic in code. Retry: read Retry-After headers deterministically first. Fan-out: questions evaluated in parallel against one ingest of state; dependent questions need two round trips. >255 options: beam search over hierarchy. Budget context in UTF-8 bytes (no tokenizer).
- Negative results: Hermes Agent compaction (recall below existing summariser; tied recency at matched budget; much cheaper) → not adopted; worldmonitor tied incumbent → shadow mode; no-mistakes review pre-brief removed (PR #1165); hermes-jev-skills: Jev-summarised handoffs worse recall than raw transcripts; jev-skill-router: unlikely to help a strong model as router (3 of 6 real prompts wrong on 0.1.0).
- Shadow-mode trial with golden fixture (worldmonitor) as model for adopting a new model safely.

## Standout entries
- [Quickstart](https://docs.typesafe.ai/introduction/quickstart) — canonical first call, choice+score+noul in one request (official)
- [Jev 1.13 known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13) — vendor jaggedness doc (official)
- [Cookbook: Skill suggestion](https://docs.typesafe.ai/cookbooks/skill_suggestion) — picks ≤1 of 182 skills (official)
- [Cookbook: Function calling](https://docs.typesafe.ai/cookbooks/function_calling) — typed function selection (official)
- [Hermes Agent: Jev compaction evaluation](https://github.com/NousResearch/hermes-agent) — credible negative result (benchmark)
- [worldmonitor](https://github.com/koala73/worldmonitor) — shadow-mode classification trial (benchmark)
- [no-mistakes PR #1165](https://github.com/kunchenguid/no-mistakes/pull/1165) — measured-and-retired review pre-brief (benchmark)
- [Lindfors early-access test](https://lindfors.no/blog/a-first-look-at-typesafes-jev/) — calibration test on 24 Norwegian docs (benchmark)
- [Near Here: Jev vs Mistral vs Gemini](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation) — three-way head-to-head (benchmark)
- [jevbench](https://github.com/fstandhartinger/jevbench) — benchmark for Jev-class typed decision models (benchmark)
- [ai-cookbook: Jev track](https://github.com/daveebbelaar/ai-cookbook) — best structured tutorial (tutorial)
- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) — two nouls per tool call compaction (project)
- [FastMCP jev_search transform](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py) — two-stage MCP tool search (tool)
- [Composio TypeSafe provider](https://github.com/ComposioHQ/composio/tree/next/python/providers/typesafe) — tool catalogue → questions (integration)
- [jev-ultrafast](https://github.com/browser-use/jev-ultrafast) — Browser Use high-speed browser agent (project)
