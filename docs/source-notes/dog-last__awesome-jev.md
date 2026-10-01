# dog-last/awesome-jev
- **One-liner:** "Awesome Jev Guide": a decision-oriented guide to whether and how to use Jev. It has a mermaid decision tree, 4 cookbooks tested in CI against the live API, a cost formula, and curated tables of use cases, reproductions and independent evals.
- **Language(s):** English, Simplified Chinese (README.zh-CN.md, docs/zh/). There is also a VitePress web version.
- **Type:** tutorial/study-guide (plus curated-list)
- **Scale:** ~200 links. README sections: decision tree / Quickstart / Cookbooks (4 .py) / Use cases (Flagship demos, Browser/desktop/mobile, Mobile use, Games, Dev tooling, Guardrails, Search/RAG, Finance, Robotics/IoT, Databases, SDKs/MCP) / Cost & latency / Official / Open-source reproductions / Inference-layer reimplementations / Independent evaluations (large-scale and focused) / Deep dives / Other lists. docs/ mirrors this as index, use-cases, cookbooks, research.
- **Quality flags:** High quality. Snippets say they were run live on 2026-09-20, with commented outputs. Stars are snapshots from 2026-09-20 (older than other lists). Numbers are attributed to their eval repos. It has an honest "read before you believe any claim" framing. Minor: it describes the release as "2026-09-15". No spam.
- **Unique value:** (1) The **"should you use Jev?" decision tree**. (2) The **"question atomization" lesson with numbers** (phishing: naive 62.6%, regex 91.8%, atomized + logistic regression 95.0%). (3) A **cost formula** with a worked example. (4) A curated set of independent evals with findings not seen elsewhere (willkelly adversarial, ickma2311 baselines, bitnovus drift, JMLE medical exam, poker). (5) A research framing that the **RLCD calibration training is the moat** (kev −19.1pp OOD).

## Facts claimed about Jev
- Released by TypeSafe AI on **2026-09-15**; it calls Jev the first System One model. Choice ≤255 options, Score on a rubric, Noul = probability a statement is true.
- `pip`/uv package `typesafe-sdk` (cookbooks pin `typesafe-sdk>=0.7.0`). Env var `TYPESAFE_API_KEY`, keys look like `ts-...`. API: `TypeSafeClient().system_one(state=..., questions={...})`. Answers expose `.choice`, `.confidence`, `.noul`.
- Live example output: department "technical" with confidence 0.75, is_urgent noul 0.99.
- Access: typesafe.ai, or Vercel AI Gateway (`typesafe-ai/jev`, no waitlist).
- Endpoint `POST https://api.typesafe.ai/v1/systemone`.
- Latency 70–500 ms vs "3–329 s" for frontier LLMs (vendor comparison). Input $0.042/M, output free. **Rate limit 250k tok/s, 1200 req/min.**
- Cost formula: `monthly $ = daily calls × avg state tokens × 30 × 0.042 / 1,000,000`. Example: 100k calls/day × 500 tokens gives **$63/month**. The official Doom demo queried 10×/s at **~$7/hour**.
- It calls "193× faster / 444× cheaper" vendor self-assessments with non-comparable methodology.
- Jev is closed-weight with no paper.
- vercel/eve ships Jev as the **default model** in its `evaluate` path. browser-use/jev-ultrafast booked a Zürich→London flight in **7.1 s**. fast-jev-compaction demo went 156k → 62k tokens. droidrun did an Uber booking in ~21 s / 9 actions.
- Eval findings:
  - willkelly: 123,805 requests for $12.69. ECE 0.075 in-domain but **fails OOD** (random 3-SAT). "Polite authority injection moves 147/200 answers." "Batching to 255 questions is genuinely free."
  - ickma2311: Banking77/CLINC150 Jev 0.832/0.870 vs **0.933** for bge-small + LR (9 ms). Latency only 2.2× faster than a nano-LLM.
  - kokuren333: JMLE (3,556 items) **88.58%**.
  - scienthoon: OpenBookQA 94.2% / ECE 0.024, but only 44.7% on an unknowable rule-based task at stated p 0.74.
  - EmilLindfors: $0.22 vs $3.08 per 1k docs, 0.32 s vs 26 s. (robokrunch quotes DeepSeek at $1.31 for what looks like the same Norwegian test; minor discrepancy.)
  - bitnovus: spam 98.3% ≈ TF-IDF, but **97.3% vs 72.5% under drift**.
  - mahlernim: reordering the input changes 13–14% of answers.
  - jev-poker: 63% agreement with a solver, inverted confidence.
  - kev: −1.8pp in-distribution, −19.1pp OOD vs Jev. SemIf: 0.845 agreement vs Jev's 0.883.

## Key insights / patterns
- **Decision tree**:
  - Need free text? Use an LLM.
  - Does a regex or rule already solve it at 90%+? Keep the rule.
  - Need explanations? Use an LLM.
  - Under 500 ms or high volume? Use Jev.
  - Need calibrated probabilities to gate actions? Use Jev.
  - Otherwise either works.
- **Question atomization** is the key skill: split the task into atomic signals and combine them in code (for example with logistic regression). "Asking Jev one big vague question is the worst way to use it."
- **Composite scoring**: decompose a big judgment and weight it in code, not in a prompt (cookbook 04).
- **Confidence-gated guardrail**: atomic Noul per policy category, then AUTO_BLOCK ≥0.9, REVIEW ≥0.5, else PASS (cookbook 02).
- RAG rerank: Score each candidate chunk, sort, and drop low-confidence ones. Hybrid RRF fusion adds +0.090 NDCG over Jev or bge-m3 alone.
- Jev's third-party-confirmed edges are **latency, cost, calibrated distributions and drift robustness**. Classical embedding + LR baselines still win some lanes.
- Feed pre-digested intermediate conclusions rather than raw complex state (poker lesson).
- Prompt-injection risk: polite authority injection moves answers.
- Reproductions: proper-scoring-rule rewards produce calibration, while binary rewards destroy it (rlcd-lite ablation).

## Standout entries
- [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — launch post (official)
- [Confidence docs](https://docs.typesafe.ai/confidence) — thresholding (official)
- [dog-last cookbooks](https://github.com/dog-last/awesome-jev/tree/main/cookbooks) — 4 tested runnable patterns (tutorial)
- [willkelly/jev-evaluation](https://github.com/willkelly/jev-evaluation) — 123K-request adversarial eval (benchmark/security)
- [ickma2311/jev-baselines-eval](https://github.com/ickma2311/jev-baselines-eval) — Jev vs classical baselines (benchmark)
- [anisselbd/jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench) — the question-atomization lesson (benchmark)
- [bitnovus/jev-spam-eval](https://github.com/bitnovus/jev-spam-eval) — drift robustness (benchmark)
- [kokuren333/jev-jmle-benchmark](https://github.com/kokuren333/jev-jmle-benchmark) — Japanese medical exam, 88.58% (benchmark)
- [Fox-Islam/jev-bias-bench](https://github.com/Fox-Islam/jev-bias-bench) — counterfactual bias bench (benchmark)
- [exs-brady/jev-eval-evidence](https://github.com/exs-brady/jev-eval-evidence) — pre-registered, 55K judgments vs 10 LLMs (benchmark)
- [sgnt.ai — You could have built Jev](https://sgnt.ai/p/jev/) — technical explainer of the single-token-logit recipe (article)
- [arnabgho/rlcd-lite](https://github.com/arnabgho/rlcd-lite) — GRPO + Brier RLCD reimplementation (research)
- [HackSing/jev-report](https://github.com/HackSing/jev-report) — 52-page Chinese report (report)
- [vercel/eve](https://github.com/vercel/eve) — Vercel agent framework with Jev as the default evaluate model (integration)
- [mizzlelover/jev-hub](https://github.com/mizzlelover/jev-hub) — aggregator of 714 launch-week X posts (community)
