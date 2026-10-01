# aliaihub/awesome-jev-usecases
- **One-liner:** Evidence-labeled guide to building with Jev: 11 use-case pages, design method, patterns, failure modes, model selection, evaluation methodology, showcase of ~100+ launch-week projects, 9 Python examples.
- **Language(s):** English
- **Type:** use-case-collection (also tutorial/study-guide)
- **Scale:** README highlights 20 projects with headline results; usecases/ = 11 pages (01 Routing & triage, 02 LLM guardrails & verification, 03 Agent harness engineering, 04 Search/reranking/RAG, 05 Structured data extraction, 06 Classification at scale, 07 Feature extraction for ML, 08 Real-time loops & games, 09 Browser & computer use, 10 Domain applications, 11 Frontier and fun); docs/ = what-is-jev, getting-started, how-to-use-effectively (7 steps), patterns (5), failure-modes (9), model-selection, evaluating-jev, research-notes; reference/showcase.md (~150 GitHub links, tagged [measured]/[architecture]), reference/ecosystem.md (~48-repo census of SDKs/infra), reference/question-catalog.md; examples/python 01–09 (routing, composite+fanout, spam, cascade, retrieve-then-judge, agent guard, extraction, evaluate, batch classify).
- **Quality flags:** High quality, candid; every number labeled vendor-reported / independently measured / self-reported / launch-week artifact. Snapshot dated 2026-09-18 (3 days post-launch) — likely stale on prices/limits/star counts. No star-count ranking by design. Not promotional.
- **Unique value:** Honest scorecard of TypeSafe's vendor eval with per-task gap (invoice); "price the fallback" production case (YTAL); hard numbers for context & rate limits; failure-mode examples with concrete probabilities (Noul vs Choice disagreement); comparison with "LLM single constrained token + logprobs"; runnable examples; question catalog.

## Facts claimed about Jev
- Launched **15 September 2026** by Diogo Almeida (described as former OpenAI researcher, InstructGPT co-author), "roughly $40M in seed funding led by DCVC". Name attributed to Kahneman's System 1 (README) — note: majiayu000 says "Jev" is from Jevons; "System One" from Kahneman.
- Primitives: Choice (up to 255 options; chosen option, per-option probability, confidence), Score (2–10 level ordered rubric; can land between levels; distribution + confidence), Noul (single probability 0–1). Questions run in parallel and in isolation.
- Vendor-reported: **$0.042 per million input tokens, output free; 70–500 ms end to end**.
- Vendor 4-workflow eval ("agreement" with average of GPT-6 Astra & Claude Fable 5.1 at high thinking, not ground truth): Jev 67.8% @ $0.0004/case, 0.4 s; GPT-5.6 Terra 67.9% @ $0.0304, 10.1 s; GPT-5.6 Sol 74.1% @ $0.0836, 23.3 s; Claude Opus 5 73.1% @ $0.1761, 37.8 s; Claude Sonnet 5 67.8% @ $0.1174, 78.1 s; Claude Haiku 4.5 53.6% @ $0.0195, 12.5 s. Invoice processing: Jev 61.8% vs Terra 74.7% vs Opus 5 78.4%. "193.6x / 444.6x" headline is vs slowest/priciest baseline; vs Terra ≈25x faster, 76x cheaper.
- Limits: **64k tokens for state + all questions; 32k for state + single longest question.** Rate limits for jev-1.13: **250,000 tokens/second and 1,200 requests/minute**, 429 on excess; SDKs retry with backoff & honor retry-after; limits "moving without notice".
- API: `POST https://api.typesafe.ai/v1/systemone`, body `{model:"jev-latest", state, questions:{name:{type, instructions, criteria}}}`. SDKs: `pip install typesafe-sdk` (Python 3.10+), `npm install @typesafe-ai/sdk` (Node 20+); read `TYPESAFE_API_KEY`; default alias `jev-latest`; Python call `client.system_one(state, {name: Noul(instructions=...)})`, `.answers[...].noul`. Keys at console.typesafe.ai/settings/keys. Early access waitlist; alternative via Vercel AI Gateway.
- Launch HN title originally "Jev: New frontier model 40-400x cheaper and 20-200x faster", changed within the hour. HN launch 1,861 points / 490 comments (snapshot).
- Jaggedness examples: Noul 0.22 vs Choice yes 0.01/no 0.99 on same question; refund 0.72 + not_refund 0.47 = 1.19. State not treated as hostile by default.
- Third-party results (self-reported): jev-ultrafast Zürich→London flights 7.1 s for $0.0039; jev-trader 81 ms model latency; typesafe-computer-use $0.0002/decision vs Opus 5 $0.032; pi-warden 6→0 rule breaks over 150 paired runs; typesafe-ai-firewall 0% vs 39.2% hard-negative blocking (one Noul per hazard vs one "is this dangerous?"); pg-jev 129 rows ≈1 s ≈$0.0009; jevgrep 8/10 SWE-bench tasks, 25.8% lower cost; jev-sec-bench 96.5% injection accuracy, ECE 0.0588, 662 samples; kiarina Japanese moderation 36 misses vs OpenAI Moderation 292 of 826; rerank nDCG@10 0.692 vs Cohere 0.691 (tie); jev-drone advisory 2.5 Hz, code safety at 50 Hz; TokenTrim beat GPT-5.4 on every axis, 6,257 traces, $1.28; tiab-review 95.0% recall on 16,645 records at threshold 0.3; zephel01: 48.3% → 98.3% by splitting a 4-option Choice into four precondition Nouls (2,320 requests); feder-cr/jevos 0.815 vs Jev 0.927. YTAL entity resolution: model stage $0.032 vs $0.787 (96% cheaper) but fallbacks made total $0.819 (+4.1%) → not adopted. Hassan El Mghari: 1,018 papers, DeepSeek $3.99 + Jev $0.08, median 256 ms.
- "The calibration claim is unverified at scale"; AbdelStark/jev-benchmarks is "the only independent calibration benchmark" (300 examples, 3 datasets).

## Key insights / patterns
- Core rule: keep control flow in code; ask narrow atomic literal judgments; recombine probabilities with weights you own.
- 5 patterns: speculative fan-out; confidence-gated routing; composite scoring; cascade (rules → Jev → specialist LLM/reasoning model/human); retrieve-then-judge (filter with Noul before context window).
- Question shape matters enormously: decomposing one Choice into precondition Nouls (48%→98%) and one Noul per hazard (39%→0% false blocks).
- Price the fallback, not just the call — escalation costs can erase savings.
- Consider "LLM single constrained token + logprobs" as a baseline (Sean Goedecke: 2–3x speedup over structured output); open reproductions copy the interface, not the calibration.
- Use Jev when decisions are repeated, high-volume, bounded-answer, latency-sensitive, and need a thresholdable probability; use code for computable things; LLM for generation/rationales/open answers; fine-tuned classifier when you have thousands of labels and need ms latency; human when wrong is costly.
- Date extraction: Choice per date part with "not stated" option, arithmetic in code. Count via per-item Noul.
- Treat user-controlled state as adversarial; state what does NOT count in criteria.
- Keep same field names across Choice options; avoid Noul where true means "no".
- Evaluate yourself: accuracy, calibration, latency on your own traffic.

## Standout entries
- [TypeSafe docs](https://docs.typesafe.ai/introduction) — official docs (official)
- [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13) — official failure modes (official)
- [Workflow evals](https://evals.typesafe.ai/) — vendor eval (official)
- [Date extraction cookbook](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook) — official cookbook (tutorial)
- [Sean Goedecke: Jev means structured output is interesting again](https://www.seangoedecke.com/jev-means-structured-output-is-interesting-again/) — critical technical analysis (article)
- [Pere Pages: Jev sorted](https://pearpages.com/blog/2026/09/16/jev-sorted-what-typesafes-system-one-model-actually-is-and-what-is-still-just-a-claim) — claim-by-claim decoding (article)
- [YTAL entity resolution replay](https://ytal.io/blog/typesafe-jev-entity-resolution-production-replay/) — production replay, not adopted (case study)
- [AbdelStark/jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks) — independent calibration benchmark (benchmark)
- [DevMortimer/pi-warden](https://github.com/DevMortimer/pi-warden) — agent guardrails, 150 paired runs (agents)
- [AnshChoudhary/typesafe-ai-firewall](https://github.com/AnshChoudhary/typesafe-ai-firewall) — per-hazard Noul tool-call firewall (security)
- [Gaurav-Gosain/jev-sec-bench](https://github.com/Gaurav-Gosain/jev-sec-bench) — blind security benchmarks (security)
- [zephel01/Jev-sample](https://github.com/zephel01/Jev-sample) — question-shape experiment with raw logs (evaluation)
- [realZachi/pg-jev](https://github.com/realZachi/pg-jev) — natural-language SQL WHERE (database)
- [TheoLeeCJ/openjev](https://github.com/TheoLeeCJ/openjev) — logit-reading open reproduction (open reproduction)
- [youkiti/tiab-review-plugin report](https://github.com/youkiti/tiab-review-plugin/blob/main/experiments/typesafe-jev/report.md) — systematic-review screening across 6 medical datasets (domain)
