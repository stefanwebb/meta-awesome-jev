# hellogumbo/awesome-jev
- **One-liner:** Large community directory (1,094 entries) of Jev projects, integrations and X/blog coverage, backing the awesomejev.com site with daily star refresh.
- **Language(s):** English
- **Type:** curated-list (semi-automated discovery plus PR/issue submissions)
- **Scale:** 1,094 entries (refreshed 2026-09-24). Sections: Official · SDKs & clients · Integrations · Agent tooling (largest, about 240 lines) · Browser & computer use · Applications · Games & simulations · Demos & playgrounds · Benchmarks & research · Other lists · Articles & threads (about 50 annotated posts). Data lives in data/projects.json. scripts/discover.mjs finds new GitHub repos, and categorize.mjs is a keyword categorizer. It has an exclude list.
- **Quality flags:** Partly auto-discovered (GitHub search + keyword categorizer), so it inherits the flood of September 2026 scaffold repos. One-line descriptions are mostly copied from repo descriptions, and self-promotional claims are passed through unverified (e.g. openJev-verdict-2.0 "beating TypeSafe Jev & Laya… 77.10%"). The Official and Articles sections are hand-written and high quality. Used as a discovery source by evan87863. Not stale as of its last refresh.
- **Unique value:** The richest set of **annotated X/blog demo posts with numbers** in this batch, the "Articles & threads" section. Broad coverage of community SDKs (Ruby, Java/Spring AI, Elixir/OTP, Rails) and integrations (pg-jev, DuckDB, Home Assistant, Gmail triage).

## Facts claimed about Jev
- Jev takes a state plus typed questions (Choice, Score, Noul) and returns typed answers with calibrated probabilities in one request, with no text generation.
- Model id `jev-latest`, endpoint `POST https://api.typesafe.ai/v1/systemone`. **Early access since 2026-09-15.**
- Official SDKs: JS `npm install @typesafe-ai/sdk` (typesafe-ai/typesafe-sdk-js, with inferred answer types) and Python `pip install typesafe-sdk` (sync + async). This matches evan87863 on Python. bakiabaci's `pip install typesafe` conflicts.
- system-one-adapter-python is a drop-in TypeSafeClient backed by OpenAI, Anthropic and compatible APIs.
- The launch post covers architecture, RLCD training, pricing, and Doom and Wikiracing demos. The manifesto describes "machine-native intelligence built for software, not conversation".
- Official channels: @typesafeai on X, discord.gg/typesafe, and evals.typesafe.ai (workflow evals).
- Vercel eve "ships Jev as the default evaluation model in its experimental evaluate path". vercel-labs/ai-cli can use Jev for its evaluate command.
- Latent Space: "over 100x faster and 200x cheaper than small frontier LLMs".
- HN launch thread had about 1,800 points.
- Third-party numbers:
  - Aaron Levin (computer use): 155× cheaper than Opus 5, about 20× faster.
  - DuckDB classifier: about 10 s per 1,000 rows.
  - Spanish AEPD corpus: 98.2% agreement with regex on 544 resolutions for about 5 cents.
  - Tabletop MMORPG action mapper: 96% agreement, 317 ms median.
  - ViZDoom agent: navigation at 5 Hz, combat at 12 Hz.
  - Verdict (151M ModernBERT replica): 0.83% adaptive calibration error, 3.0% of predictions flip when the option list is reordered.
  - open-jev-typed-decision-engine (150M): "0.697 vs Jev's 0.727".
  - Gomoku harness: local tactics shrink 225 moves to about 40 candidates before Jev picks.
  - Agent safety monitor: "most attacks caught, almost no false blocks".

## Key insights / patterns
- Candidate pruning before Jev: code narrows the action space (gomoku 225 to about 40, chess legal moves, DOM element tables), then Jev chooses.
- Speculative fan-out, shown in the official smart-home demo: ask many questions in one call and let code keep the relevant answers.
- Browser-agent split: observe the accessibility tree, Jev picks the next action, and Stagehand or Browser Use executes.
- Many "model router" demos (Jev picks which model or agent serves a request) and "skill routers" (skillbox).
- Use cases in data pipelines: dataset sifting (jev-curate), streaming data selection plus LoRA training (jev-dataops), SQL predicates.
- Voice: turn-end detection by scoring after speech (AIAvatarKit).
- Honest-evaluation writing exists: warmersun.com "separating published claims from public evidence", and agentjournal's judge vs dimension scores.
- A big wave of open replicas (SemIf, NanoJev, jevlike, AnyJev, LitJev serving the same /v1/systemone schema, decider, jevk5, Verdict). Many claim to beat Jev, and none of those claims are independently verified.

## Standout entries
- [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — launch post (official)
- [Smart home demo](https://docs.typesafe.ai/demos/smart-home) — official fan-out demo (official)
- [Workflow evals](https://evals.typesafe.ai) — vendor eval methodology (benchmark)
- [typesafe-ai/system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) — LLM-backed drop-in for comparisons (official)
- [vercel/eve](https://github.com/vercel/eve) — Vercel agent framework using Jev as evaluator (integration)
- [spring-ai-community/spring-ai-typesafe](https://github.com/spring-ai-community/spring-ai-typesafe) — Java/Spring AI SDK (SDK)
- [realZachi/pg-jev](https://github.com/realZachi/pg-jev) — Postgres extension (integration)
- [AboveColin/HA-Jev](https://github.com/AboveColin/HA-Jev) — Home Assistant integration (integration)
- [fazlerocks/jevmail](https://github.com/fazlerocks/jevmail) — local Gmail triage (application)
- [vinnylarouge/jevlike](https://github.com/vinnylarouge/jevlike) — open option-scorer replica with Doom/chess (research)
- [zhengxuyu/litjev](https://github.com/zhengxuyu/litjev) — Qwen-based /v1/systemone-compatible reproduction (research)
- [openlayer-ai/jevals](https://github.com/openlayer-ai/jevals) — agent evals + guardrails in one request (evaluation)
- [Jev in Search: Three Practical Evaluations](https://zc277584121.github.io/rag/2026/09/22/jev-search-deep-evaluation.html) — independent search experiments (evaluation)
- [Typed decisions, not chat](https://warmersun.com/jev/) — claims vs evidence walkthrough (article)
- [AI that does not talk](https://ziplyne.agency/blog/ai-that-doesnt-talk-typesafe-jev-guide) — practical guide to playground, SDKs, HTTP, skill (tutorial)
