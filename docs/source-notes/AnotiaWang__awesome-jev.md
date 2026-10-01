# AnotiaWang/awesome-jev
- **One-liner:** Classic, well-structured awesome list (~220 entries) of Jev SDKs, apps, agent tools, open models and independent evaluations, with a full Simplified Chinese translation.
- **Language(s):** English + Simplified Chinese (README_zh.md, same link set)
- **Type:** curated-list
- **Scale:** ~220 entries. Sections: Official; Community; SDKs & Clients (~30, many languages); Applications (~65); Demos & Games (~30); Agent Tools (~40); Research & Open Models (~40 incl. benchmarks); Articles (independent measurements + community cookbooks); Related (other directories); Contribute.
- **Quality flags:** Hand-curated, concise, accurate-looking one-liners with "Unofficial / Not TypeSafe's model" labels. Cited by yzfly/awesome-jev-zh as "the most structurally complete list" it drew on. No auto-generation evident. Some entries embed author-reported numbers.
- **Unique value:** Best polyglot SDK index (Python, JS, Elixir, Ruby, Rails, Rust ×4, Scala/ZIO, .NET, PHP/Laravel, Go ×2, Swift ×2, Kotlin ×2, C++, Effect); strong "Articles" section of independent measurements with concrete numbers (OpenRouter Banking77, LexGLUE, dice calibration); open-model catalogue incl. multimodal OneJev and CPU-only jevos; notes slopsquatting-protection PyPI shim.

## Facts claimed about Jev
- "**Public access opened 21 September 2026**" — keys from console.typesafe.ai/settings/keys. (Other lists say early access 15 Sept 2026; consistent if 21 Sept = general availability.)
- Packages: `pip install typesafe-sdk`; `npm install @typesafe-ai/sdk`; `pip install system-one-adapter` (official drop-in `TypeSafeClient` replacement backed by LLM APIs). PyPI `typesafe-ai` is a community redirect shim registered to block slopsquatting.
- Vercel AI SDK provider `@ai-sdk/typesafe-ai` with `experimental_evaluate`; `typeSafeAi.evaluationModel('jev-latest')` or Gateway id `typesafe-ai/jev`. Swift SDK aligned with Python SDK **0.6.0** API.
- OpenRouter model ID seen: **`typesafe/jev-1.13-20260917`** (LexGLUE entry).
- OpenRouter blog: Banking77 (3,080 utterances) **Jev 1.13 81.0% vs Claude Opus 5 84.4%; 175 ms vs 2,266 ms median; ~$0.11 vs $2.42 per 1,000**.
- ayautomate (791 decisions): Jev matches small models, trails GPT-5.6 Terra ~5 points on 77-way routing; a 0.80 confidence gate escalating the rest to Terra matches Terra's accuracy at ~¼ the cost.
- LexGLUE (23,607 examples): Jev mean micro-F1 **69.9 at $4.02** vs 71.3 at $16.45 for GPT-5.6 Luna.
- "Jev Does Not Play Dice": selects face 1 on all 400 fair-die rolls with **82.9% mean reported probability vs 19.0% accuracy** — calibration fails on true-random events.
- NASA Kepler: 8,054 KOIs, Jev 1.13 **72.5%** archive match vs 64.4% fixed 3-rule baseline.
- jev-fanout-bench (2,976 requests via OpenRouter): ~**261 fixed input tokens per request**; charges match published token rate; batched vs separate answer differences comparable to repeat-request noise.
- NanoJev: 128/128 on ViZDoom Basic vs 56/128 for Jev (author split). WebJev: 38.5% vs 16.7% for Jev 1.13 on 125 real-website tasks. Jev Ultrafast: Zürich→London Google Flights ~7 s.
- Jev search rerank eval (9,831 pairs): fusion wins; Jev alone doesn't beat embeddings (bge-m3). Jev Phishing Bench: Haiku wins accuracy.

## Key insights / patterns
- Confidence-gated escalation to a frontier LLM is the recurring cost/accuracy sweet spot (ayautomate, hunch "escalation of unsure rows to an LLM that must pick from the same labels").
- Calibration must be checked per workload: jevcal fits per-question thresholds on labeled data, verifies on held-out split and fails CI when a Jev update breaks the threshold.
- Jev as reranker: better fused with BM25/embeddings than alone.
- Distillation-to-local pattern: stuntd records upstream Jev answers, trains per-question head on Laya, serves with calibrated threshold + upstream fallback.
- Libraries that force handling of uncertainty (discern's explicit `Uncertain` branch; kojev "no default thresholds").
- Hosted Jev is text-only; multimodal "Jev-like" projects (OneJev, PocketJev, PlayJev, jev-visual) are independent.

## Standout entries
- [Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python) — official client (SDK)
- [JavaScript / TypeScript SDK](https://github.com/typesafe-ai/typesafe-sdk-js) — official client (SDK)
- [Vercel AI SDK provider](https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai) — `@ai-sdk/typesafe-ai` (integration)
- [Milvus Search with Jev](https://github.com/milvus-io/bootcamp/tree/master/bootcamp/RAG/search_with_jev) — nine runnable RAG notebooks (cookbook)
- [Is Jev as Accurate as Frontier Models at Classification?](https://openrouter.ai/blog/insights/jev-vs-claude-opus-5-classification/) — OpenRouter Banking77 study (benchmark)
- [Jev × LexGLUE](https://github.com/chepyle/jev-test) — 23,607-example legal eval (benchmark)
- [Jev Does Not Play Dice](https://kantahayashiai.github.io/posts/jev-does-not-play-dice/) — calibration failure on known probabilities (evaluation)
- [Jevals.com](https://jevals.com/) — independent Jev vs 6 LLMs benchmark with open logs (benchmark)
- [ASSAY-001](https://github.com/jourdanlabs/assay-001) — pre-registered calibration check (evaluation)
- [jevcal](https://github.com/abhixhek/jevcal) — threshold fitting + CI guard (tool)
- [jev-fanout-bench](https://github.com/blowxian/jev-fanout-bench) — batched vs separate calls cost study (benchmark)
- [hunch](https://github.com/steven-shoemaker/hunch) — DataFrame-level Jev functions with LLM escalation (library)
- [Kev](https://github.com/jaredpalmer/kev) — trainable open decision models with `/v1/systemone` server (open model)
- [OneJev](https://github.com/OmniJev/OneJev) — open multimodal System One models 0.8B–27B (open model)
- [Jev in Search: Three Practical Evaluations](https://zc277584121.github.io/rag/2026/09/22/jev-search-deep-evaluation.html) — search stopping/rerank experiments (article)
