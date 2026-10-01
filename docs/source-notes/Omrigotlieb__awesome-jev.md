# Omrigotlieb/awesome-jev
- **One-liner:** Deduplicated, auto-audited union of ~9 other awesome-jev lists: 1,603 entries with twice-daily link/Jev-evidence checks and cross-list agreement counts.
- **Language(s):** English (some entry descriptions in Chinese/Japanese)
- **Type:** auto-generated-list (merge + audit; README generated from entries.json by build_readme.py; discover.py runs GitHub search)
- **Scale:** 1,603 entries (1,455 GitHub repos; 1,437 live, 18 dead; 1,306 with clear Jev reference; 131 unevidenced; 72 carried by 7+ lists; 218 by one list; 760 auto-discovered "unreviewed"). 19 categories: Official & Documentation (38), Classification & Routing (68), Verification & Guardrails (80), Scoring & Ranking (36), Agent Decisions (63), Browser & Computer Use (49), Context & Compaction (11), SDKs, Clients & Integrations (126), Evaluation & Benchmarking (58), Calibration & Open Reproductions (41), Games & Simulation (71), Data Labeling & Curation (4), Content Moderation (5), Finance & Trading (9), Compliance & Legal (1), Demos & Playgrounds (67), Articles, Threads & Field Notes (91), Other Jev Lists (25), Recently Discovered (760). Also "Start here" (12), 14 live screenshots, dead-link audit.
- **Quality flags:** Largely a superset/duplicate of other lists by design (sources: yibie, hellogumbo, Eric-Zhou-0302, Heman10x-NGU, cobanov, kraayenjon, chy4pro, AbdelStark, BYK, madewithjev.com). ~47% of entries are unreviewed search hits. Audit verifies link liveness and README mention only, not code quality. Warns about same-day wave of scaffolded 1–2 commit repos. Uses "boolean" in intro but "Noul" elsewhere.
- **Unique value:** Cross-list agreement signal (⭐ = 7+ lists), dead-link tombstones to prevent re-adding, excellent "Other Jev Lists" directory (25 lists with descriptions), large Articles/Threads section (X posts, HN, blogs) with launch-era claims, strong Calibration & Open Reproductions section.

## Facts claimed about Jev
- Jev = TypeSafe AI's "System One model for typed decisions"; returns typed answer with calibrated probability: choice, score, or boolean (Noul). Launch post: https://typesafe.ai/blog/introducing-system-one-models-and-jev (covers RLCD, performance claims, caveats).
- Official SDKs: Python `pip install typesafe-sdk` (github.com/typesafe-ai/typesafe-sdk-python, sync + async); JS `npm install @typesafe-ai/sdk` (github.com/typesafe-ai/typesafe-sdk-js, inferred answer types); `system-one-adapter-python` = official drop-in TypeSafeClient replacement backed by OpenAI/Anthropic for comparing Jev against chat models.
- Official resources: docs.typesafe.ai (models & aliases page with version IDs, limits, pricing, stable vs preview aliases), console.typesafe.ai (playground, keys, live request inspection), evals.typesafe.ai (accuracy-vs-cost frontier across four workflows: security incidents, agent trace observability, invoice processing, customer service), Discord discord.gg/typesafe, X @typesafeai, manifesto typesafe.ai/manifesto, official agent skill (docs.typesafe.ai/agent-skill).
- Confidence docs: Choice/Score confidence ≠ answer probability; Noul has no separate confidence field.
- Launch: founder Diogo Almeida's thread (63k likes) arguing RLCD-trained decision models are a shorter path to economic value; HN launch thread ~1,800 points / ~480 comments; dev.to headline "He says he co-invented ChatGPT".
- Third-party claims: Latent Space AINews "over 100x faster and 200x cheaper than small frontier LLMs"; Aaron Levin computer use "155x cheaper than Opus 5, about 20x faster"; Stagehand + Jev "about $0.001" per step; DuckDB extension ~10 s per 1,000 rows; Sniff Test "182 ms median"; Jev Pac-Man shows 888 ms latency per decision; jev-drone runs control loop at 2.5 Hz.
- Open reproductions claims (not Jev): von 395M, <15 ms; Laya ~35 ms single forward pass, RLCD-trained; openJev-verdict-2.0 151M ModernBERT claims beating Jev & Laya (77.10% acc, 0.0636 Brier, 0.0144 ECE); CUA-S1-FORMS 706,048 params, 99.7% on own forms set; minojev 547k params, Choice 2–255 candidates.
- Jev launched with ≥9 awesome-jev lists appearing within ~48 hours.

## Key insights / patterns
- Before adopting a listed project, verify: code actually calls the API, a runnable check exists, published numbers trace to a source, license present.
- Canonical patterns (Start here): routing to cheapest capable model with one Choice (jev-router); score every shell command for destructiveness before running (jev-axi); rerank by judged relevance (jev-reranker); Jev picks browser action, LLM only when text must be typed (jev-ultrafast); security checks over build files (is-malicious); low confidence → human review (jev-cookbook).
- Official cookbook patterns: date extraction separating typed extraction from date arithmetic in code; citation checking; classifying RAG passages; skill suggestion two-stage with shortlist rejection; speculative fan-out (smart-home demo): many questions in one call, code keeps relevant answers.
- Game/tactics pattern: local code shrinks action space (gomoku 225→~40) then Jev picks.
- Large open-reproduction ecosystem (RLCD, parallel constrained decoding, option-logit scoring on Qwen/Gemma/ModernBERT, MLX, ESP32).
- Single-list entries least corroborated; README-missing-marker ≠ false.

## Standout entries
- [Documentation](https://docs.typesafe.ai) — official docs (official)
- [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — launch post (official)
- [typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) — official Python SDK (official)
- [typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) — official JS/TS SDK (official)
- [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) — official adapter for comparing against chat LLMs (official)
- [Workflow evals](https://evals.typesafe.ai) — TypeSafe accuracy-vs-cost frontier (benchmark)
- [Models and aliases](https://docs.typesafe.ai/models) — versions, limits, pricing (official)
- [building-with-jev-skill](https://github.com/dbreunig/building-with-jev-skill) — community agent skill on question design (skill)
- [jev-cookbook (nexibeo)](https://github.com/nexibeo/jev-cookbook) — 15 runnable Node recipes (tutorial)
- [jev-axi](https://github.com/shiftynick/jev-axi) — shell-command destructiveness guardrail (tool)
- [Sniff Test](https://github.com/DanRWilloughby/snifftest) — measured latency and FP rate (project)
- [Typed decisions, not chat](https://warmersun.com/jev) — independent walkthrough separating claims from evidence (article)
- [jev-agent-failure-benchmark](https://github.com/TokenTrim/jev-agent-failure-benchmark) — Who&When Pro agent failure attribution (benchmark)
- [NanoJev](https://github.com/TianyuCodings/NanoJev) — 0.6B open replica with training pipeline/weights (reproduction)
- [Jev Pac-Man](https://jev-pacman.ephraimduncan.com) — visual demo of per-junction decisions (demo)
