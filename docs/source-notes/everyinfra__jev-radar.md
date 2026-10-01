# everyinfra/jev-radar
- **One-liner:** Bilingual "field report & live monitor" of the Jev ecosystem: a 265KB Chinese casebook of 220+ evidence-graded cases, a 698-entry registry, API access guide, briefing skill.
- **Language(s):** Chinese (primary: CASEBOOK, API guide) + English (README half)
- **Type:** use-case-collection (casebook + machine-readable registry; auto-scan every 3 hours)
- **Scale:** Casebook 220+ cases in 14 sections (Overview table; AI agent safety/supervision; browser agents/extensions; content moderation/scoring/business decisions; routing/scheduling/context management; data pipelines/infra/language ecosystem; games/embodied; independent evaluations; reproductions/open alternatives; official demos; Chinese community; pattern summary; monitoring log). data/projects.json: 108 verified-cohort entries (38 A / 70 B / 0 C) growing to 698 graded entries. Evidence tiers A (0.90), B (0.75), C (0.60).
- **Quality flags:** Promotional: maintained by EveryInfra (data/search/CAPTCHA infra vendor) with explicit plug; "Star this repo → get a free Jev API key" (5,000 keys from maintainer's quota) is star-farming. Superlative marketing ("全网最全,没有之一"). But the casebook content is dense, sourced (repo/tweet/Reddit links) and includes negative results and a fake-demo warning. Numbers are author-reported unless marked. Some inconsistency: "1,000 repositories within five days" (EN) vs "2000 repos in 7 days" (ZH).
- **Unique value:** Best source for the independent-evaluation findings with specific numbers (agentjournal, Janus, jev-moral-dilemmas reproducibility, WindTunnel/WebMCP, jev-sales-call), rate limits, waitlist/API access walkthrough, Chinese/Japanese/Korean community coverage, QA toolchain (jevcheck, jevassert, jev-reliability, jev-prompt-optimization).

## Facts claimed about Jev
- Jev is TypeSafe AI's first System One model, released **2026-09-15**. Founder Diogo Almeida described as "InstructGPT co-author". Primitives Noul/Choice/Score.
- Latency **70–500 ms** end-to-end; pricing **$0.042 per million input tokens, output free**; "roughly 20–200× faster and 40–400× cheaper" than frontier LLM (API guide says "40–200× speed").
- API: `POST https://api.typesafe.ai/v1/systemone`, Bearer `$TYPESAFE_API_KEY`, body `{state, model: "jev-latest", questions: {key: {type: "noul"|"choice"|"score", instructions, criteria}}}`. Keys start with `jev_`, created at console.typesafe.ai/settings/keys. Python `pip install typesafe-sdk` (Python ≥3.10), `from typesafe_sdk import Choice, Noul, Score, TypeSafeClient`; `client.system_one(state=..., questions=...)`; `response.answers["department"].choice`.
- Rate limits (jev-1.13, official Models page): **1,200 requests/minute; 250,000 tokens/second; 64k tokens per request (state + all questions); 32k per question (state + longest question)**. 429 with retry-after; SDK auto exponential backoff; enterprise via sales@typesafe.ai.
- Access: waitlist via console.typesafe.ai (homepage "Join Waitlist" button bug pointed to jobs.ashbyhq.com); approval took hours at launch, later 24h+; expedite by emailing hello@typesafe.ai with use case. Alternatives: OpenRouter `typesafe/jev-1.13` (same price), Netlify AI Gateway (`@typesafe-ai/sdk`, zero config), Cloudflare Workers AI `typesafe/jev` (appeared 09-20), community OpenJev (codiv.ai, 100M tokens/account free; not Jev), playgrounds console.typesafe.ai/playground and jevai.org/playground.
- jevcheck cites a 2026-09-19 official model list already showing **jev-1.14** and **jev-preview** alias (only repo in batch mentioning 1.14).
- Official "regulatory briefing 12.2× cost reduction" use case.
- Independent findings: agentjournal.dev — 3 tasks, 5,477 rows, 34.1M tokens for **$1.43**; 12-way Choice on bookkeeping **0.3998**; decomposing into 12–14 dimensions raised guardrail false positives from 1.5% to 37.2%; rows with confidence ≥0.9 only **72.2%** accurate. Attest: evidence order flips 5.8% of rulings; removed confidence field (always 0.95–0.99). jev-moral-dilemmas: 1,000 identical calls → category 100% deterministic but Score/Noul confidence drifts up to 14 points; 52 dilemmas × 200 runs, 48 fully deterministic, flips only when Choice confidence <17%. jev-sales-call (jev-1.13.0): 60/60 outcomes, Noul Brier 0.012, median 250ms / p95 511ms; counting speakers ≈ random (37/60). jev-classification-benchmark: **$0.0000166 per classification** (395 input tokens). WindTunnel: Jev+Mercury 2.5+WebMCP 49/49 web tasks, ~112× cheaper than GPT-6 Astra computer use; bare Jev only 25/49. Janus: optimal thresholds and routing value flip between Banking77 and Web of Science—routing params not transferable. yzfly awesome-jev-zh cites phishing: direct question 62.6% vs two-line regex 91.8%; 193× is vendor upper bound.
- Official quickstart example bug: comment says `technical` but 100 runs return `billing` (0.67) (typesafe-sdk-python issue #2).
- Project metrics: pi-warden replay on 17,000 calls, 42 holds, ~88% correct, ~250ms; jev-codex-router −60% cost on 237-turn backtest; Jev Ultrafast flight search 7.1 s ($0.0039), browser protocol calls 1,092→101; voice ~300ms/phrase, $0.0002/voice decision; $0.00003 per routed turn; 61 questions per draft post $0.0004; 724 ads $0.09; tax forms 100% strict on 261 IRS forms; OpenJev DiffusionGemma 198/201 vs Jev 191/201.
- Warning: viral sped-up/fake Jev demos (steve8708 LinkedIn).

## Key insights / patterns
- #1 use case: agent safety co-pilot — Nouls ("reversible?", "matches stated intent?", "stuck?"), Score for danger, low confidence → block/steer; 70–500ms fits every agent step unlike 3–30 s LLM judges.
- #2 context compaction (keep/drop per tool output); routing/reranking; realtime layers where code does perception/execution and Jev does Choice in a bounded action space; Jev as SQL predicate/system primitive (pg-jev, DuckDB, pandas, zsh, Neovim, Emacs).
- Lessons: narrow, mechanical questions ("LLMs survive junk input; Jev doesn't"); big option lists collapse; confidence ≠ correctness; sensitive to order and phrasing; per-scenario calibration required; decomposition helps hard tasks but can hurt simple ones.
- Multi-gate confidence engineering example (semantic-live-caption): choice hit + confidence ≥0.55 + margin ≥0.12 + Noul recheck, 0.70 for high-false-positive classes.
- Prompt-technique port: render Jev's typed answers back into state and ask another round = code-provided "scratchpad" for multi-step reasoning.
- QA toolchain: measure (jev-reliability: repeatability, phrasing sensitivity, resolution, answerability) → optimize (jev-prompt-optimization, Brier fitness) → regress (jevcheck pins model version, refuses `jev-latest`; jevassert record/replay).
- Division of labour: Jev picks tool, generative model fills arguments (WebMCP finding: "choosing a valid button ≠ choosing the right next step").

## Standout entries
- [pi-warden](https://github.com/DevMortimer/pi-warden) — agent supervisor evaluated on 17k real calls (safety)
- [jev-ultrafast](https://github.com/browser-use/jev-ultrafast) — Browser Use speed agent (browser)
- [agentjournal.dev: LLM judge vs feature extraction](https://agentjournal.dev/blog/llm-judge-vs-feature-extraction/) — most rigorous independent eval (benchmark)
- [WindTunnel](https://github.com/nekuda-ai/WindTunnel) — WebMCP benchmark, 49 web tasks (benchmark)
- [Janus](https://github.com/FirasSX914/Janus) — calibration/routing transferability study (benchmark)
- [jev-moral-dilemmas](https://github.com/krsna-smnt/jev-moral-dilemmas) — reproducibility/determinism experiment (benchmark)
- [jevcheck](https://github.com/sathariels/jevcheck) — behavioral contract tests, pins version (tool)
- [jev-reliability](https://github.com/vcjdeboer/jev-reliability) — per-question preflight reliability checks (tool)
- [jev-prompt-optimization](https://github.com/j341nono/jev-prompt-optimization) — evolutionary instruction optimization with Brier fitness (tool)
- [llm-prompt-techniques-on-jev](https://github.com/leepokai/llm-prompt-techniques-on-jev) — refine/chain/choose/rerank ported to Jev (research)
- [bias-bench](https://github.com/natemoo-re/bias-bench) — resume-screening fairness benchmark (benchmark)
- [jev-codex-router](https://github.com/0xNatoshi/jev-codex-router) — model router with 237-turn backtest (routing)
- [rag-jev](https://github.com/Nixz0824/rag-jev) — Chinese RAG with blind tests and negative results (project)
- [jev-api-access-guide.zh.md](https://github.com/everyinfra/jev-radar/blob/main/docs/jev-api-access-guide.zh.md) — waitlist, rate limits, alt gateways (guide)
- [HF Jev Reproductions Tracker](https://huggingface.co/spaces/multimodalart/jev-reproductions-tracker) — tracker of open clones (reproductions)
