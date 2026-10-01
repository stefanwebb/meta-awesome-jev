# tanxarx/awesome-jev
- **One-liner:** Curated Jev list (sourced from X threads) of open clones, integrations and — most valuably — ~60 annotated articles/threads summarizing independent tests, critiques and playbooks with numbers.
- **Language(s):** English
- **Type:** curated-list
- **Scale:** ~270 entries. Sections: About Jev (7), Open-Source Reproductions & Clones (~40), Coding Agents & Dev Tools (~60), SDKs, Frameworks & Platform Integrations, Browser & Desktop Automation, Data & Retrieval, Content, Media & Moderation, Simulation, Games & Hardware, Finance & Trading, Benchmarks & Evaluation (12), Articles, Threads & Playbooks (~65).
- **Quality flags:** Hand-curated, each link "resolved from its original source tweet/thread and verified live". Heavy reliance on X posts (numbers are posters' claims). Some factual claims differ from other lists (32K context window; founder "co-inventor of RLHF"). No spam. Not auto-generated.
- **Unique value:** The Articles/Threads section is the best single collection of **skeptical and independent findings** (determinism, ordering, phrasing-threshold drift, head-to-heads against GPT-5/Claude/Kimi/encoders, Browser Use founder's 1/20 retest, clone-vs-Jev comparisons, OpenAI DevDay Decisions API). Clone entries carry specific metrics (AnyJev order-flip reduction, Verdict JevBench scores, Nimble 90.12 vs 93.21).

## Facts claimed about Jev
- Launch announcement by Diogo Almeida ("co-inventor of RLHF and InstructGPT at OpenAI"): "20-200x faster and 40-400x cheaper" than generative frontier models on decision-shaped tasks; **"32K context window"** (contradicts 64k per request in kydlikebtc/Justmalhar/everyinfra — 32k is state + longest question); no image/audio input; cannot write code or prose by design.
- Official: typesafe.ai, typesafe.ai/Jev, docs.typesafe.ai; `typesafe-ai/skills` install via `npx skills add typesafe-ai/skills --skill typesafe-ai` or `claude plugin marketplace add typesafe-ai/skills`; `system-one-adapter-python`. Pydantic AI has built-in TypeSafe provider.
- TypeSafe **$40M seed round**, Sept 15 (Prasenjit Sarkar); SYNTHLEX calls it "the $200M model" (valuation claim).
- No-waitlist providers: OpenRouter, Vercel AI Gateway, Cloudflare, Netlify AI Gateway, OpenCode Zen.
- Measured claims from threads: Alcides Ticlla — $0.013880 in 8.566s (LLM) vs $0.000081 in 0.114s (Jev); RobotsTJ500 — measured latency 0.8–1.1 s vs published 70–500 ms; rephrasing a yes/no shifted score 0.97→0.12; Chrisondesk — 100 comments for $0.002171; jasonlk — $2.26 for 54.9M tokens (~$0.04/M, ~$0.0002/request, ~50x cheaper than Sonnet); BourneS — Jev-1.13 ECE **0.045** on 2,000 decisions, 93.7% accuracy on the 24.5% of cases ≥90% confident; fluixoo — 791 decisions, **3.6x faster than GPT-5.6 Terra (not 193.6x)**, cascade routing uncertain 19–23% to Terra matched Terra accuracy at ~¼ cost; drummatick — GPT-5 beats Jev by 3.2% on Banking77 at 32x cost; pukerrainbrow — bge-small + logistic regression 93.3% vs Jev 83.2% on Banking77; SUOHA_AI — Browser Use founder retest on 20 complex tasks: Jev 1/20 vs GPT-5.6 Luna 17/20; kwindla — voice control 92.6% at 296 ms vs Luna 81.3% at 1,008 ms; Yarrow — 48 disclosure cases: classification 48/48 but 10/48 false "No", 8/48 changed on rerun, 20/48 flipped by paragraph reordering; Eastwood — SemEval DimABSA 0-10 vs Kimi-K2, 3-7 vs fine-tuned Qwen3-14B; void — 154 shell commands × 12 phrasings: accuracy 94.8–100% but matching threshold moved 0.14→0.68; EntendreAI crypto accounting ~635 ms, 51.7/47.5/48.3% on 2/3/5 accounts; muratcan — 38,012 forecasts at 118 ms median, AUC 0.78, ~$3; proxy_vector — 272 tickets Claude 88% vs Jev 85%, ~170x cheaper; kcp_kn — LangChain Deep Agents, 100% agreement with human pass/fail over 500 trials, ~1/80 cost of Sonnet 4.6; Prasenjit — 384 headlines 24.9 s $0.19 vs Opus 5 4/384 for $0.77; 0.5M-line codebase 12,938 findings in 2 min for $0.89; Jev beat BM25 9x on tool retrieval over 3,000+ endpoints; WquGuru — Jev 20/20, AnyJev 95%, Laya 65%, djev 35%; neural_avb — non-deterministic probabilities, reordering shifts them; zilliztech deep-searcher median decision latency 2.23 s→0.55 s.
- Critiques: "can't hallucinate" means schema-valid only; workflow-eval ground truth is average of two LLMs' predictions; multiples compare against TypeSafe's own slower wrapper; launch blog "Nuance" disclosures (laptop-only benchmarks, non-empirical hallucination chart) — 193.6x/444.6x are best case.
- OpenAI DevDay launched a "Decisions API" (Luna-powered) seen as a Jev clone; Latent Space counted 6 clones within 2 days; 11 clones with 10,294 stars in 5 days; yoavgo: 29 arXiv papers in two weeks; Almeida published a 12-page, 10-step blueprint ("separate generation from control").

## Key insights / patterns
- The 100x comes from finding calls that never needed an LLM and deleting them, not swapping models (Ronin).
- Restrict Jev to gating jobs: is this done, which tool next, does a human need to see it (Milon); five coding-agent insertion points: tool routing, context pruning, model escalation, termination checks, test-failure triage (noahkostesku); three insertion points: upstream router, midstream execution gate, downstream verifier (Xiaofan Wu — "format-immune, not truth-immune").
- Architecture: LLM for cognition, Jev for judgment, code for hard rules, humans veto irreversible actions (sakevoid). Cascade: route low-confidence to frontier model.
- The threshold is part of the prompt: re-tune thresholds whenever phrasing changes; freeze option order; log confidence against real outcomes; set thresholds before shipping; distrust vendor benchmarks.
- Reframe "which action" as "what outcome to aim for" for multi-step tasks (Tetris, ~10x).
- Validate typed answers for arithmetic (invoice sums fail).
- Compare against encoders/zero-shot classifiers, not only LLMs; Jev reads rows from world knowledge unlike TabPFN.
- Critique: Jev-gated if-statement graphs can become tech debt (fixed options, can't fetch missing facts, silent failures).
- Compaction: Teknium found Jev compaction degenerates to a programmatic rule and breaks prompt-cache reuse; model router should lock main model at session start to preserve prompt caching.
- Clones: open "beats Jev" claims are in-distribution (0.769 ID vs 0.541 OOD); data volume is the lever; AnyJev recalibration cuts answer-order flips 23%→7.3%, ECE 0.240→0.095; distilled students overstate teacher confidence.

## Standout entries
- [typesafe-ai/skills](https://github.com/typesafe-ai/skills) — official agent skills (official)
- [Launch announcement](https://x.com/CompleteSkeptic/status/2099925682726002904) — founder thread (official)
- [Pydantic AI TypeSafe provider](https://github.com/pydantic/pydantic-ai/blob/main/docs/models/typesafe.md) — framework integration (SDK)
- [nokia-applied-research/AnyJev](https://github.com/nokia-applied-research/AnyJev) — training-free calibration layer for open LLMs (reproduction)
- [bespokelabsai/nimble](https://github.com/bespokelabsai/nimble) — 9B open reproduction, 90.12% vs Jev 93.21% (reproduction)
- [vllm-project/vllm#57250](https://github.com/vllm-project/vllm/pull/57250) — DiffusionGemma behind /v1/systemone (reproduction)
- [leepokai/jev-guard](https://github.com/leepokai/jev-guard) — risk-scores every coding-agent tool call (security)
- [zilliztech/deep-searcher Jev stopping eval](https://github.com/zilliztech/deep-searcher/blob/master/evaluation/jev_stopping/README.md) — search-stopping decisions (benchmark)
- [sumleo/RLCDAlignBench](https://github.com/sumleo/RLCDAlignBench) — "Just Ask Jev" alignment-failure detection (benchmark)
- [TheWayWithin/jev-bench](https://github.com/TheWayWithin/jev-bench) — citation verification vs GPT/Claude/Gemini (benchmark)
- [void — the threshold is part of the prompt](https://x.com/sakevoid/status/2102896039678382177) — phrasing moves thresholds (analysis)
- [Yarrow — 48 disclosure cases](https://x.com/Yarrow_ai/status/2102226848436645902) — ordering/rerun instability (analysis)
- [fluixoo — 193.6x retested](https://x.com/fluixoo/status/2103755424117686645) — cascade result (analysis)
- [OrcaRouter — reproducing Jev](https://x.com/OrcaRouter/status/2102318172577911068) — ID vs OOD clone claims (analysis)
- [reachmeviz — Laya vs Jev](https://viswakumar.com/blog/laya_system_one_model) — zero-shot generalization comparison (article)
