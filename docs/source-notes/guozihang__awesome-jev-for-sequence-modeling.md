# guozihang/awesome-jev-for-sequence-modeling
- **One-liner:** A compact, explainer-style Jev awesome list with a specs table, SDK snippets, 4 arXiv papers, community benchmarks and an 11-item gotchas list. The repo name ("sequence modeling") does not fit the content.
- **Language(s):** English (README.md), Chinese (README_ZH.md)
- **Type:** curated-list (explainer-heavy)
- **Scale:** ~50 links. Sections: What is Jev? / How It Works / Specs & Pricing / Official Resources / SDKs & Integrations / Research Papers / Benchmarks & Independent Evaluations / Use Cases / Open-Source Reimplementations / Community Resources / Media Coverage / Gotchas & Operational Risks. Last updated 2026-09-24.
- **Quality flags:** Several links are bare domain placeholders (https://techcrunch.com, https://www.forbes.com, https://dev.to, https://python.langchain.com, https://www.typesafe.ai/blog), so they are not real article links. The OpenRouter slug `typesafe-ai/jev` conflicts with `typesafe/jev-1.13` in other lists. The SDK names (`@typesafe-ai/sdk`, `typesafe-sdk`) are unverified here. The repo itself admits its name is a misnomer. Low volume, but the synthesis is good.
- **Unique value:** A compact, high-quality summary of what Jev is, including an "is / is not" table, the three pillars (non-autoregressive architecture, parallel sampler, RLCD), a precise explanation of "zero hallucination", and an operational gotchas list (Vercel quirks, confidence location, Noul="boolean"). It also covers Chinese media (36Kr, Huxiu, Xinhua, OSChina) and 4 arXiv IDs.

## Facts claimed about Jev
- TypeSafe AI: San Francisco, founded 2024. Founders are **Diogo Almeida** (ex-OpenAI, co-inventor of RLHF/InstructGPT/ChatGPT), **Erik Gafni** and **Sasha Sheng**. About 2 years in stealth. **$40M seed led by DCVC**, ~$200M valuation (per Forbes).
- **Launch: September 15, 2026.** It says the launch post topped HN, and that within 24h on Vercel AI Gateway ~13% of paid teams had used it ("fastest model adoption in the platform's history"). This contrasts with the "GA 2026-09-21" date given elsewhere; the two may be different events (launch vs waitlist removal). It also dates BusinessWire to Sept 16 and TechCrunch to Sept 18.
- Name taken from William Stanley Jevons / the Jevons Paradox.
- Architecture: non-autoregressive transformer (no paper, no parameter count published). A parallel sampler answers all questions in one pass, **70–500 ms, often <100 ms**. **RLCD** training uses **synthetic data only**.
- Primitives: Choice (up to **255 options**; add an explicit `other` option), Score (a **2–10 level rubric**, can land between levels, e.g. 1.4), Noul (a single 0–1 probability; spelled `boolean` in the Vercel AI SDK).
- A request has exactly `state`, `model` and `questions`. There is no temperature, max_tokens or thinking budget, and **no streaming**.
- Pricing: **$0.042/1M input, $0 output**; it notes GPT-5 Nano is $0.05/M. A typical decision is ~400 tokens ≈ $0.000017 (~60,000 decisions per $). **No free tier.**
- Claimed 40–200× faster and 40–400× cheaper. Official peak figures: 193.6× faster, 444.6× cheaper.
- Context: **64k native (~32k state + longest question); 32k on gateways**. It notes the official docs are inconsistent (32k vs 64k).
- Rate limits: **250,000 tok/s, 1,200 req/min** (adjusted dynamically without notice).
- Text and structured data only; no image, audio or video.
- Version `jev-1.13.0`, alias `jev-latest`.
- SDKs: `@typesafe-ai/sdk` (npm), `typesafe-sdk` (PyPI, `from typesafe_sdk import Jev; jev.evaluate(...)`). The Vercel AI SDK uses `experimental_evaluate` with model `'typesafe-ai/jev'`, and `providerOptions.gateway.zeroDataRetention`. It also names LangChain `langchain-typesafe` with `AutoModeMiddleware`, and Langfuse through OpenInference.
- Vercel gateway gotchas: versioned IDs such as `typesafe-ai/jev-1.13.0` return **404**, and confidence sits at `providerMetadata.typesafe.confidence`.
- The official 1.13 jaggedness doc says Jev is weak on numbers, dates and adversarial content, and recommends decomposition plus code-based argmax for numeric judgments.
- Community numbers: chess puzzles Jev 25/100 in 8s for $0.03 vs gpt-6 astra 68 in 33 min for $11 (3-move puzzles only 3/30). Tetris 9200 pts at 300ms/step. Huxiu reports ~64% on 50 support-triage questions.

## Key insights / patterns
- "Zero hallucination" only means the output is always a valid enum value. Jev can still be confidently wrong.
- Conflicting instructions were the most stable failure mode, but those failures had very low confidence (0.04–0.16), which supports using confidence as an escalation gate (llt22/jev-lab).
- For more than 255 options, use two stages: score a shortlist, then make the final pick.
- Pin the version and log the `model` field from every response.
- Security: attacker-controlled state reaches the gate, so test state poisoning and confidence-threshold bypass. Treat the verdict as one input to the gate, not the gate itself, and use ZDR for sensitive state.
- Ecosystem hygiene: some third-party indexes mislabel Jev as "Text Generation", and npm has fake packages with the same names.
- Selective control (REFLEX): execute high-confidence steps and escalate the rest. Reported 95% success with 72.7% fewer strong-model calls.
- Jev is a fast first pass, not a deep reasoner (chess result).

## Standout entries
- [Official docs](https://docs.typesafe.ai) — API reference (official)
- [Console](https://console.typesafe.ai) — API keys (official)
- [`@typesafe-ai/sdk`](https://www.npmjs.com/package/@typesafe-ai/sdk) — Node SDK (SDK)
- [`typesafe-sdk`](https://pypi.org/project/typesafe-sdk/) — Python SDK (SDK)
- [Jev in the Wild (arXiv:2609.30216)](https://arxiv.org/abs/2609.30216) — ecosystem survey of 2,170 GitHub projects (paper)
- REFLEX, arXiv:2609.26532 — selective control in agents (paper; no link given)
- Jev-Mem, arXiv:2609.23986 — System-One-controlled agent memory (paper)
- 6G edge orchestration, arXiv:2609.23136 — 97.0% on-time vs 93.5%/88.7% (paper)
- [Simon Willison: Jev introduces a new shape of LLM](https://simonwillison.net/2026/Sep/21/jev/) — influential analysis (article)
- [llt22/jev-lab](https://github.com/llt22/jev-lab) — confidence-as-gate experiments (benchmark)
- [Raunaksplanet/jev-research-sept-2026](https://github.com/Raunaksplanet/jev-research-sept-2026) — research write-up, including security (guide)
- [Eigent AI: 什么是 Jev](https://www.eigent.ai/zh-CN/blog/typesafe-ai-jev-system-one-models) — Chinese explainer (article)
- [36氪 article](https://m.36kr.com/p/3988164509711361) — Chinese coverage (news)
- [虎嗅 hands-on](https://www.huxiu.com/article/4892583.html) — Chinese evaluation, ~64% triage (benchmark/news)
- [cobanov/awesome-jev](https://github.com/cobanov/awesome-jev) — cited as the highest-starred community list (list)
