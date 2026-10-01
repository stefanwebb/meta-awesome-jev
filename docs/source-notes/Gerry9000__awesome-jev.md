# Gerry9000/awesome-jev
- **One-liner:** Huge, media-heavy "Awesome Jev & Fast Classifiers" directory (awesomejev.org) with ~200 curated repos, 25 teardown dossiers, recipes, and a 6,000+ repo auto-scraped radar.
- **Language(s):** English
- **Type:** curated-list (plus auto-generated-list for RADAR.md)
- **Scale:** README/README-COMPACT ≈ 207 curated bullet entries (badges claim "160"/"175"/"190 verified" in different places) in 9 categories: 1 Browser, Desktop & Mobile Automation; 2 AI Development, Code Review & Agent Triage; 3 MCP Servers, Agent Skills & Shell Plugins; 4 Database Filtering, Search & Knowledge Graphs; 5 Security Guardrails, SecOps & Content Moderation; 6 Simulation, Real-Time Gaming & Physical Control; 7 Benchmarks & Empirical Evaluations; 8 Competing Fast Classifiers & Open Reproductions; 9 Official SDKs & Gateway Integrations. Plus: 8 "Production Use Cases & Architecture Recipes", BLUF, System1/System2 essay, comparison table, visual demo/benchmark galleries (~41 videos/GIFs in media/, ~60MB), "Canonical Demonstrations" (X threads without repos, ~29), 4 patterns + 4 anti-patterns, Python/TS/cURL quickstart. RADAR.md (1.1 MB): 1,066 consensus (3+ mirrors), 983 emerging, 5,751 single-mention repos, 2,194 X discussions, auto-classified into 9 categories "by Jev". dossiers/ has 25 deep-dive teardowns (S1Bench, open reproductions, semantic code retrieval trade study, invoice benchmark, NanoJev, laya-mlx, GLiNER2.5-Decide, etc.). demos/huggingface-space = intent-search explorer.
- **Quality flags:** Strongly promotional/SEO-driven: every section funnels to gerryburde.com "canonical research report"; README asks readers to cite a bibtex; a dossier's links carry `utm_medium=parasite_geo` (explicit GEO/SEO "parasite" campaign). Many per-entry latency numbers (e.g. "18 ms", "22 ms") look templated/unverified; internal counts inconsistent (160 vs 175 vs 190 curated; RADAR "over 6,000" vs dossier "2,800"). Some numbers contradict each other across sections (invoice benchmark 50/50 vs 96% vs 94%). RADAR is raw auto-aggregation from 29 other awesome lists (i.e., this repo is itself a meta-list). Still the most comprehensive single source in the batch; the dossiers contain some genuine first-hand testing.
- **Unique value:** Largest inventory of open reproductions and competing fast classifiers with S1Bench/JevBench numbers; production recipes with confidence thresholds and code; anti-patterns (compaction trap, certain-and-wrong, fine-tuning tax); first-hand security finding on `dzhng/jevgrep` (`jg`) leaking internal policy text to a third-party API; SDKs in ~15 languages; RADAR as a de-duplication source across 29 mirrors.

## Facts claimed about Jev
- Pricing: "$0.042 per million input tokens ($42 per billion)", zero output-token charges; "$0.025 / 1,000 decisions" (README, dossier). JevBench cites Jev 1.13.0 at "$0.040 / 1k decisions". Dossier example response shows `cost_usd: 0.00000537` for 128 input tokens.
- Latency: "30–50 ms median" (table, SDK entries); BLUF says "12–50 ms" and that 1 or 30 questions over the same state cost the same latency. S1Bench measures Jev at "2.4 decisions/s (0.42 s/item)" — contradicts the 30–50 ms figure (cloud round-trip vs model time). feder-cr/jev entry: hosted Jev 344 ms on a short request.
- Primitives: `noul` (binary probability 0–1), `choice` (up to 255 options), `score` (2 to 10 ordered levels).
- Model versions/names: "Jev 1.13.0" (S1Bench/JevBench anchor), `model: "jev-latest"`; HF demo mentions "Jev, Jev Fast, Valen" as TypeSafe System One models; "RLCD" (reinforcement learning for calibrated decisions) per founder Diogo Almeida's release thread (x.com/CompleteSkeptic/status/2099925687465570372).
- API: README quickstart `POST https://api.typesafe.ai/v1/systemone` with `{model, state, questions:{id:{type, instructions, criteria}}}` → `answers[id].choice/probabilities/noul`. Dossier instead shows `POST https://api.typesafe.ai/v1/eval` with `{context, questions:[{id,type,prompt,options}]}` → `results[id].probability`, `usage` — **contradiction** on endpoint and schema. Docs URL: https://docs.typesafe.ai/introduction.
- SDKs: official `pip install typesafe-sdk` (typesafe-ai/typesafe-sdk-python), `npm install @typesafe-ai/sdk` (typesafe-ai/typesafe-sdk-js), typesafe-ai/system-one-adapter-python (simulates Jev with frontier LLMs).
- Gateways: OpenRouter endpoint, Cloudflare AI Gateway, Vercel AI Gateway (via X threads).
- Benchmarks: S1Bench (Jake Cuth, 1,999 decisions, 13 sets, DGX Spark): Jev 77.5% macro acc, ECE 0.076; simplejev-qwen38-27b 75.8%; Reflex-4b 72.0% @10 dec/s; Decider-2b 71.0% @30 dec/s. JevBench v1.2.7 (Benchmark Heaven, 42 systems/534 decisions; composite of Intelligence/Calibration/Speed/Cost 25% each): Jev #1 75.4, SemIf 74.7, djev Maisa 74.3, Verdict 1.4 72.5, GLiNER2 53.0. manjunathshiva/jev-frontier-bench: Jev 72.5% on 200 decisions; Claude Fable 5.1 478x costlier ($11.81/1k). FLock THIS/THAT: FLock 94.1% vs hosted Jev 76.5% (68 binary questions). AnyJev: "0.727 published for Jev". feder-cr/jev: Jev 0.927 on 2,000 yes/no questions. Rerank: nDCG@10 0.692 vs Cohere Rerank-v3 0.691 (anessbelbati). Invoice (Huryn): "50/50 accuracy in 30 ms ($0.025/1k vs $2.83 for Opus 5)" vs recipe "96% accuracy across 50" vs dossier "94% vs 88% GPT-4o-mini" — **contradictory**.
- Limitation: "certain, and wrong" — >0.95 confidence on wrong labels when criteria omit implicit business rules (0.98 on invoice tax case). Tetris: pure reflex Jev "topped out" without a search harness (Tony Dinh).

## Key insights / patterns
- Two-tier "sensory shield + reasoning engine": Jev triages; escalate to System 2 LLM/human when confidence < 0.80.
- Speculative parallel fan-out: ask all primary and conditional questions over the same state in one call; never chain sequentially.
- Code-owned composite scoring: ask atomic booleans, combine weights in code; don't ask for "1–100" scores.
- Deletion test: if regex/linter/AST can decide it, don't use Jev.
- Risk-tiered thresholds (Foreman recipe): read-only ≥0.60, local edits ≥0.85, external writes ≥0.92, destructive never automated; ≥0.95 or HITL for irreversible ops.
- Anti-patterns: context compaction (breaks KV prefix cache; Teknium/Theo critiques); low-entropy input (model can't infer absent info); treating probabilities as booleans; assuming open replicas are zero-shot (they usually need fine-tuning; "fine-tuning tax").
- Pre-filter with deterministic extraction (AST, DOM accessibility tree, candidate generation) before Jev; games need a search harness.
- Open-reproduction strategies: logit readout from open LLM heads (SemIf, AnyJev, rizzo-flow), fine-tuned small Qwen (NanoJev, Decider, Kev), encoders (GLiNER, jeff), wire-compatible `/v1/systemone` servers (ollaya, litjev, rizzo-flow).
- Security: semantic-grep tools send repo text to third-party APIs; `jg` leaked internal manifest content and has no preview/dry-run.

## Standout entries
- [TypeSafe docs](https://docs.typesafe.ai/introduction) — official docs (official)
- [typesafe-ai/typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) — official Python SDK (SDK)
- [typesafe-ai/typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) — official TS SDK (SDK)
- [Diogo Almeida launch thread](https://x.com/CompleteSkeptic/status/2099925687465570372) — founder's RLCD/System One thread (official)
- [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) — DOM action selection via choice (browser automation)
- [thruwire/foreman](https://github.com/thruwire/foreman) — supervisory gate for Codex runs (agents)
- [S1Bench](http://bench.jakecuth.com) — 30+ Jev alternatives vs Jev on 1,999 decisions (benchmark)
- [JevBench / Benchmark Heaven](https://benchmarkheaven.com/jev-models) — 42 decision systems composite ranking (benchmark)
- [manjunathshiva/jev-frontier-bench](https://github.com/manjunathshiva/jev-frontier-bench) — Jev vs 5 frontier LLMs Pareto (benchmark)
- [phuryn/experiments](https://github.com/phuryn/experiments) — adversarial invoice benchmark (benchmark)
- [nokia-applied-research/AnyJev](https://github.com/nokia-applied-research/AnyJev) — training-free Jev-style decisions from open LLMs (open reproduction)
- [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev) — 0.6B open replica (open reproduction)
- [ollaya-dev/ollaya](https://github.com/ollaya-dev/ollaya) — local runtime wire-compatible with /v1/systemone (tool)
- [fastino/GLiNER2.5-Decide](https://huggingface.co/fastino/GLiNER2.5-Decide) — 340M open decision model (competitor)
- [WebDevCody critique video](https://www.youtube.com/watch?v=lDmrk_7D-W8) — where classification beats LLMs vs where regex wins (critique)
