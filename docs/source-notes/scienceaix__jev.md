# scienceaix/jev
- **One-liner:** Long analytical report ("The Awesome Jev Open-Source Ecosystem") profiling about 12 leading Jev projects, open models and integrations, with a leaderboard, timeline, maturity matrix and recommendations (snapshot 2026-09-28).
- **Language(s):** English
- **Type:** other (ecosystem survey/analysis report; reads like an AI deep-research report)
- **Scale:** About 12 deep project profiles (jev-ultrafast, fast-jev-compaction, NanoJev, TypeSafe Skills, jevlike, typesafe-computer-use, Ollaya, official SDKs/adapter, AutoTrust JEV-27B/9B), a top-10 star leaderboard, an integrations table (Pydantic AI, Vercel AI SDK, Spring AI, Langfuse, OpenRouter Jev Router, Ollaya), HN/Reddit/X buzz, a Sept 15–28 timeline, and a maturity matrix. Sections: Executive summary · Scope/methodology · Leaderboard · Project profiles · Hugging Face and open-model research · Integrations, buzz, timeline · Analytical assessment · Bottom line. It has infographic PNGs and a small site (docs/, data/projects.json with 12 items).
- **Quality flags:** Written in a first-person, AI deep-research style ("I have seen"). It is heavily cited to primary sources, and every claim links a URL. It marks unknown values "unspecified" rather than inventing them. It is careful to label benchmarks as author-reported. Star counts roughly agree with bakiabaci (20.8k jev-ultrafast, 7.0k fast-jev-compaction, 2.4k NanoJev). Coverage is narrow (top projects only). Not promotional.
- **Unique value:** **Maturity and risk analysis** of top projects, drawn from their issue trackers (e.g. stale action IDs in jev-ultrafast). A detailed profile of the **AutoTrust JEV-27B/9B** open distilled students. A dated timeline of ecosystem formation. Framework integrations not seen elsewhere (Pydantic AI, Spring blog, Langfuse, OpenRouter Jev Router). A recommended production architecture.

## Facts claimed about Jev
- Launched in early access on **2026-09-15**. It is TypeSafe's first "System One Model". The stack combines "a new model architecture, parallel sampling, and … RLCD". The launch post phrase is "unstructured state in, typed probabilistic decisions out".
- **Jev is not open-weights.** The "open-source ecosystem" is the open SDKs, skills and adapter plus community work.
- Vendor-reported latency is "roughly 70–500 ms" with "40–200× speed advantages" for System-One-shaped tasks.
- Python SDK: `uv add typesafe-sdk`, `TypeSafeClient.system_one`, `Choice` types, `TYPESAFE_API_KEY`. MIT, 238★. JS SDK: `npm install @typesafe-ai/sdk`, Node.js 20+, ESM + CJS + TS declarations, result types inferred from questions. MIT, 248★. system-one-adapter: 313–315★.
- typesafe-ai/skills: 2.3k★ with only 2 commits.
- jev-ultrafast: 20.8k★/1.4k forks with only 3 commits. It needs `TYPESAFE_API_KEY` + `TEXT_MODEL_API_KEY` and runs with `uv run jev`. Its 7.073-second Google Flights run is "repeated measurement of one task/profile, not a general reliability benchmark". The text helper uses OpenRouter.
- Ollaya exposes `/v1/systemone`, `/v1/decisions` and `/v1/models`, redirected via `TYPESAFE_BASE_URL`. It is a Rust runtime with ONNX Runtime and llama.cpp and has an MCP server. Its Winnow-E4B scores 0.722 vs **Jev 0.738** on Ollaya's benchmark, 89 ms for 5 questions on an RTX 4090.
- AutoTrust JEV-27B (HF `autotrust/JEV-27B`):
  - Qwen3.8-27B backbone distilled from Jev 1.13 output distributions. Apache-2.0.
  - Six-benchmark mean 84.07 vs 83.85 for hosted Jev 1.13 (self-run).
  - KL ≈0.017, top-1 agreement ≈90.5%.
  - Choice limited to 2–16 options in its serving path. 53.8 GB BF16.
  - JEV-9B uses Qwen3.5-9B.
- Integrations: Pydantic AI (pydantic.dev/docs/ai/models/typesafe/), Spring AI blog 2026-09-21, Langfuse, and **OpenRouter Jev Router** (openrouter.ai/typesafe/jev-router, surfaced Sep 25).
- HN: jev-ultrafast about 93 pts; typesafe-computer-use about 82 pts/60 comments; the "single function Jev-like wrapper for LLMs, including vision" about 150 pts. An OpenJev thread showed a prompt-injection counterexample.
- typesafe-computer-use: macOS 14+, Python 3.12+, 1.0k★. It compares against Claude Opus 5, with the caveat that the multimodal model infers facts from pixels while the Jev path has to rebuild facts deterministically.

## Key insights / patterns
- The core doctrine behind the best projects: **"classifier chooses, code establishes facts, writer only writes."** Expose only the finite actions valid right now instead of inspect → reason → generate → serialize → parse → validate.
- Recommended production architecture: application state → deterministic preprocessing → Jev → confidence above a *validated* threshold? If yes, take a deterministic action. If no, go to an LLM, a human or a stronger model. Then verify outcomes and record telemetry and evaluation. "Not 'replace every LLM call with Jev'."
- Use the official adapter to measure error, calibration, p95, cost and escalation rate on your own workload.
- jev-ultrafast open issues include stale action IDs resolving to different controls, missing semantic controls, confidence-gating requests, and Windows/background rendering. Don't run it unchanged for high-consequence automation. Its executor checks freshness and occlusion.
- fast-jev-compaction asks two Noul questions per tool call: is it still relevant, and must its result stay verbatim? Replay experiments found fancier methods didn't clearly beat a **head+tail baseline**.
- Schema validity does not imply correctness or robustness to adversarial input.
- Strategic trend: the lasting standard may be the **interface** (state + typed questions → distributions, the `/v1/systemone` wire shape) with interchangeable models (Ollaya).
- Three open research strategies: distill teacher distributions (JEV-27B), train a compact model end to end (NanoJev), or find a minimal option scorer (jevlike).
- Stars measure attention, not engineering scope. The ecosystem is only about 2 weeks old.

## Standout entries
- [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — launch post (official)
- [typesafe-ai/system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) — evaluation baseline adapter (official)
- [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) — breakout browser agent (application)
- [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) — Claude Code context compaction (tooling)
- [awlevin/typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) — desktop agent reference architecture (application)
- [ollaya-dev/ollaya](https://github.com/ollaya-dev/ollaya) — local TypeSafe-compatible runtime (infrastructure)
- [AutoTrust JEV-27B](https://huggingface.co/autotrust/JEV-27B) — distilled open-weight student (open model)
- [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev) — 0.6B replica with training pipeline (research)
- [vinnylarouge/jevlike](https://github.com/vinnylarouge/jevlike) — minimal option-scoring architecture (research)
- [Pydantic AI TypeSafe models](https://pydantic.dev/docs/ai/models/typesafe/) — framework integration (integration)
- [Spring AI TypeSafe integration](https://spring.io/blog/2026/09/21/spring-ai-typesafe-structured-judgment/) — Java integration (integration)
- [Vercel Jev integrations](https://vercel.com/i/jev-integrations) — AI SDK/Gateway (integration)
- [OpenRouter Jev Router](https://openrouter.ai/typesafe/jev-router) — Jev-based routing (platform)
- [OpenRouter: Jev vs LLM, when to use each](https://openrouter.ai/blog/tutorials/jev-vs-llm-when-to-use-each/) — tutorial/comparison (tutorial)
- [HN: Jev-like wrapper for LLMs incl. vision](https://news.ycombinator.com/item?id=49853175) — 150-pt discussion (discussion)
