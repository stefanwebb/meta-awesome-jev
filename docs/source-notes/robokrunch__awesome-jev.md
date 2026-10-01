# robokrunch/awesome-jev
- **One-liner:** Very large, heavily annotated curated Jev list (891 lines, ~400KB) by RoboKrunch; unusually strong Benchmarks section with numbers, sources and caveats.
- **Language(s):** English (some entry descriptions in Chinese; covers JP/KR/TR/PL/PT/FR/DE-language resources)
- **Type:** curated-list
- **Scale:** ~800 entries in one README. Sections: Official (8), Models & API (~26, mostly SDKs/open replicas), Projects & Code (~449), Benchmarks & Evaluations (~131), Demos on X (12), Videos (10), Tutorials & Guides (~21), News & Articles (~108), Papers (1), Community (~36, incl. competing awesome lists).
- **Quality flags:** Long entries carry stars, license, creation date, and "real non-fork verified via GitHub API, raw README verified". It labels vendor claims and gives caveats, such as the Steve8708 fake-demo rule. Some entries were probably machine-assisted (uniform verification boilerplate, and some Chinese descriptions of non-Chinese repos). The maintainer promotes its own RoboKrunch experiments (marked 📊). Current as of 2026-09-30. It is not a duplicate: it has the richest benchmark annotations seen.
- **Unique value:** A benchmark digest with exact numbers per study, including accuracy/ECE/latency/cost against named LLMs and caveats. It audits claims (the 193.6×/444.6× figures are called the vendor's best case). It tracks competing awesome lists and open Jev clones (Laya, Kev, OpenJev, bev-decider). It lists one arXiv paper, and security papers through Sarim-MBZUAI.

## Facts claimed about Jev
- Built by TypeSafe AI and founder Diogo Almeida ("ex-OpenAI, co-inventor of RLHF/ChatGPT"). Came out of stealth in Sept 2026 with $40M (Business Wire, 2026-09-15; seed at ~$200M valuation, led by DCVC). **GA on 2026-09-21**: no waitlist, $5 starter credits (~120M tokens). Vercel, Cloudflare, LangChain and Langfuse are integrating it (per Indian Express). Reported talks to raise $1B+ at a $10B+ valuation (The Information, 2026-09-24).
- Training method called **RLCD** (Reinforcement Learning for Calibrated Decisions). Launch thread by founder @CompleteSkeptic.
- Native API: `POST https://api.typesafe.ai/v1/systemone`. Questions are `choice` (up to **255 options**, per-option probabilities + `confidence`), `noul` (yes/no as one probability) and `score` (numeric). Many questions can go in one call. Docs: docs.typesafe.ai/introduction/quickstart.
- Pricing: **$0.042 / 1M input tokens, $0 output**.
- Latency: vendor says **70–500ms**. Independent testers see p50 ~0.2–0.8s.
- OpenRouter: `typesafe/jev-1.13`, **32K context**, served through the decisions endpoint and not `/chat/completions`. LLM Gateway listing: **64k context**, OpenAI-compatible. systemonemodels.org: **64K total context / 32K state budget, 250K tok/s + 1,200 req/min**. So the 32K vs 64K figures are not a real contradiction: one is the state budget and the other is total context.
- Versions: `jev-1.13.0`, `typesafe/jev-1.13-20260917`, and the floating alias `jev-latest` (advice: pin 1.13.0). The official docs have a per-version jaggedness page (docs.typesafe.ai/model-jaggedness/jev-1.13) listing 9 failure modes: literal reading, math, dates, indirection, context rot, adversarial content, and others. There is a noted Python SDK vs quickstart serialization discrepancy. The claim that customer data is not used for training has not been audited.
- Vendor evals (MarkTechPost): Jev 0.114s / $0.000081 vs GPT-5.6 Terra 8.566s / $0.013880, which gives the "193.6× faster, 444.6× cheaper" claim. The reference answers were the average of GPT-6 Astra and Fable 5.1, and TypeSafe's own team wrote the workflows.
- Vercel (Rauch): up to 18× faster at p95 than GPT Luna on command safety. Bryo: Gemini is slightly more accurate but 10–20× more expensive.
- No official paper as of 2026-09-27.
- Independent numbers (selected): phishing 62.6% accuracy / ECE 0.154 vs Haiku 4.5 81.3% (anisselbd). BANKING77 92.40% vs fine-tuned BERT 93.66% (simonmesmith). BBQ 97.28% on 58,492 questions. TrueStandard 77-class ~73% vs OpenAI ~85%. Jevals: Noul tied #1 with Gemini 3.8 Flash at 1/28 the price. omarmujahid: matched or beat gpt-5.6-luna on 42/49 tasks, ECE 0.07 vs 0.14–0.18. Code review 98.0% vs 100% at $0.043 vs $1.94/$11.78 per 1K. Pong 227ms/decision vs 2.5–3.5s for chat models.
- PostHog/jeeves claims to beat Jev on JevBench (0.935 vs 0.866). WebJev claims Jev loops or stalls on browser tasks.

## Key insights / patterns
- Best framed as **"a filter, not a replacement"**. Confident answers (near 0/1) are right 90–100% of the time, and the middle band is a coin flip. Route low-confidence cases to an LLM or a human.
- The biggest speedups (100×+) come only when **one batched call replaces a chain of sequential LLM calls**. A single small question is only ~1.5–2× faster than cheap chat models (GuardingPear, TrueStandard).
- Batching and packing: pack-32 gives the same accuracy at much higher throughput (collapseindex). The claimed 32× gain holds only under request-counted billing, not token billing. Putting a whole document LLM-style into one prompt dropped accuracy to 62% (ebrain.lab). "Batching increases drift."
- **Calibrate per question type**: Choice/Score tend to be overconfident and Noul underconfident. Jev is confidently wrong out of distribution (scienthoon). Conformal risk control gives finite-sample guarantees (jev-certify).
- Position bias: on questions with no single correct answer it picked the first-listed option in 2,000 of 2,000 repeats (jev-dice). Shuffling candidates changes 2–6% of picks. One choice with up to 254 candidates beats many yes/no calls (shaun117).
- Framing sensitivity: answer order in the prompt changes arithmetic accuracy (RINNECODER).
- Weak spots: counting, arithmetic, fine-grained many-class intent (BANKING77 full set), phishing recall, and OOD rules. Strong spots: reranking (matches Cohere Rerank / Qwen3-Reranker), judge/eval roles, short-text classification.
- Design pattern: "code owns the physics, Jev owns the judgment". Browser agents let Jev pick the operation + element while a small LLM writes the text.
- Self-hosting crossover (RoboKrunch): ModernBERT beats Jev on cost above ~977K decisions/month. Jev's advantage is zero training, zero labeling and zero ops.
- Security: appended opinions or injected context flip decisions (JevAdvBench 12.1%, JevOut 61.4%). Decision heads follow option names, not rubrics.

## Standout entries
- [Quickstart](https://docs.typesafe.ai/introduction/quickstart) — official API docs (official)
- [Jev on OpenRouter](https://openrouter.ai/typesafe/jev-1.13) — gateway listing (official/platform)
- [Jev on Cloudflare](https://developers.cloudflare.com/ai/models/typesafe/jev/) — Workers AI (platform)
- [systemonemodels.org spec page](https://systemonemodels.org/models/jev/) — specs, limits, jaggedness (reference)
- [OpenRouter docs: Jev vs LLM](https://github.com/openrouterteam/docs/blob/HEAD/content/blog/2026-09-19-jev-vs-llm-when-to-use-each.md) — vendor tutorial with measurements (tutorial)
- [Aman Kumar: Testing Jev](https://amankumar.ai/blogs/jev-measured) — ~16K-call eval, "filter not replacement" (benchmark)
- [Jevals](https://jevals.com/) — independent per-question-type benchmark (benchmark)
- [JevBench](https://benchmarkheaven.com/jev-models) — typed-decision leaderboard (benchmark)
- [scienthoon/jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration) — OOD calibration audit (benchmark)
- [collapseindex/jev-ultralightspeed](https://github.com/collapseindex/jev-ultralightspeed) — packing/batching study (benchmark/tool)
- [arXiv:2609.29429 Just Ask Jev](https://arxiv.org/abs/2609.29429) — RLCDAlignBench, alignment-failure detection (paper)
- [Sarim-MBZUAI/awesome-jev-security](https://github.com/Sarim-MBZUAI/awesome-jev-security) — attack papers list (security)
- [Real Python: Get Started With Jev](https://realpython.com/jev-python/) — tutorial (tutorial)
- [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) — flagship browser agent (project)
- [Laya](https://laya.convaiinnovations.com/) — Apache-2.0 open alternative (open model)
