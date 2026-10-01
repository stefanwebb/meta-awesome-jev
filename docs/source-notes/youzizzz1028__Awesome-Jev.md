# youzizzz1028/Awesome-Jev
- **One-liner:** Academic-style, evidence-labeled index connecting Jev to the research literature (calibration, selective prediction, constrained decoding, routing), with an original survey paper "Decisions, Not Tokens".
- **Language(s):** English (README, LaTeX survey); Chinese (README.zh-CN, survey_zh.md)
- **Type:** papers-list (plus a small ecosystem index and an original survey)
- **Scale:** About 32 papers across 7 categories: Foundations and structured prediction (3) · Typed output and constrained decoding (3) · Calibration and uncertainty (9) · Selective prediction and deferral (6) · Decision-focused learning (2) · Routing, cascades, and dynamic inference (7) · Calibration-aware decision training (2). Also 7 official resources, about 25 ecosystem repos (Official SDKs; Open models/replicas; Framework integrations; Applications; Evaluation/playgrounds; Larger directories), a concept map, an evaluation reporting bundle, a comparison protocol, figures, BibTeX, and YAML catalogs. Snapshot 2026-09-21.
- **Quality flags:** High quality and scholarly. Evidence labels: [A] peer-reviewed, [B] preprint, [C] official, [D] community. It is careful about vendor claims. Small ecosystem coverage. No obvious fabrication. The papers carry venue/year and citation keys, but some 2026 citations (EACL 2026, Findings of ACL 2026, arXiv 2609.15982 "The Router Within") couldn't be verified here. Not promotional.
- **Unique value:** **The only research-grounded treatment in this batch.** It has a taxonomy (output contract / inference / learning objective / uncertainty / system control) and a four-layer evaluation framework (structural validity, semantic correctness, probabilistic reliability, decision utility). It includes an evidence-audit table of Jev's launch claims, a reproducible comparison protocol, and a note on the RLCD acronym collision.

## Facts claimed about Jev
- TypeSafe introduced "System One Models" under its "**Machine-Native Intelligence**" thesis in September 2026. Jev is the first public instance.
- The launch article (Almeida 2026) reports **RLCD** (Reinforcement Learning for Calibrated Decisions), **a parallel sampler**, low latency and low price.
- The launch post gives "70–500 ms; USD 0.042/MTok". The survey treats this as a "public performance/price hypothesis" that still needs region, concurrency, length and tail-latency tests.
- "Zero hallucinations": the vendor limits this claim to schema matching, so it is a format-validity claim, not factual accuracy.
- TypeSafe's refund example is cited as the motivating interface mismatch.
- **RLCD acronym collision:** ICLR 2024 "RLCD: Reinforcement Learning from Contrast Distillation" (Yang et al.) is unrelated to TypeSafe's RLCD.
- Architecture is undisclosed. "If the implementation is a general generator plus a constraint layer, its main contribution resides at the system interface."
- Ecosystem claims: decider is fine-tuned from Qwen3.5-2B; openjev is built on DiffusionGemma; hev/reranker handles up to 30 documents per call; llama-index-jev and n8n-nodes-jev (vibe-with-me-tools) are community integrations.

## Key insights / patterns
- Jev's scientific value today is its **interface proposition**: types, probabilities and multi-question batching as first-class concepts. Whether it is a new model class depends on undisclosed architecture and reproducible results.
- Evaluate on four layers. Structural validity alone (what "type-safe" guarantees) says nothing about correctness, calibration or utility.
- Minimum reporting bundle:
  - Task quality with CIs.
  - Probability quality: NLL, Brier, ECE/ACE, reliability diagrams.
  - Selection: risk–coverage, AURC, coverage at fixed risk, escalation rate.
  - Structure: parse rate, cross-field consistency.
  - Ops: p50/p95/p99, retries, cost, human workload.
  - Robustness: shift, template perturbation, subgroups, **model-version drift**.
- Comparison protocol: compare (1) a discriminative encoder/classical classifier, (2) an LLM with native structured output, (3) the same LLM via the official adapter, and (4) Jev. Give all four the same state and candidate set. Freeze prompts, versions, retries and prices. Plot a quality–cost–latency Pareto surface and separate first-party from independent results.
- Include tasks for Boolean, enumerated, ordinal, multi-question consistency and **open-set abstention**.
- Useful systems connect uncertainty to execution, verification, routing, abstention or escalation. Relevant research lineages: learning to defer, SelectiveNet, conformal prediction, and FrugalGPT/RouteLLM cascades.

## Standout entries
- [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — launch article (official)
- [System One concept doc](https://docs.typesafe.ai/concepts/system-one) — category definition (official)
- [Confidence](https://docs.typesafe.ai/confidence) — confidence semantics (official)
- [Workflow evaluations](https://evals.typesafe.ai/) — vendor eval dashboard (benchmark)
- [On Calibration of Modern Neural Networks](https://proceedings.mlr.press/v70/guo17a.html) — temperature scaling baseline (paper)
- [SelectiveNet](https://proceedings.mlr.press/v97/geifman19a.html) — reject option / risk–coverage (paper)
- [Conformal Language Modeling](https://openreview.net/forum?id=pzUhfQ74c5) — calibrated rejection (paper)
- [FrugalGPT](https://arxiv.org/abs/2305.05176) — LLM cascades (paper)
- [RouteLLM](https://arxiv.org/abs/2406.18665) — model routing (paper)
- [Detecting Hallucinations Using Semantic Entropy](https://doi.org/10.1038/s41586-024-07421-0) — meaning-level uncertainty (paper)
- [SkillRouter, arXiv:2603.22455](https://arxiv.org/abs/2603.22455) — skill routing for agents (paper)
- [Balancing Classification and Calibration in Decision-Making LLMs](https://aclanthology.org/2026.findings-acl.610/) — calibration-aware RL (paper)
- [WallerChen/jev-measured](https://github.com/WallerChen/jev-measured) — raw cost/latency records across 8 use cases (evaluation)
- [hev/reranker](https://github.com/hev/reranker) — calibrated Jev reranking, 30 docs/call (tool)
- [agent-chaperone/agent-chaperone](https://github.com/agent-chaperone/agent-chaperone) — MCP proxy screening tool calls (safety)
