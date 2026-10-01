# Oscar-dzy/Awesome-jev-papers
- **One-liner:** Evidence-aware annotated bibliography of 35 Jev research items — 30 arXiv preprints (with exact v1 timestamps) plus key vendor and technical articles.
- **Language(s):** English
- **Type:** papers-list
- **Scale:** 35 entries, last verified 2026-09-28. Sections: Core JEV Sources (3), Benchmarks and Evaluation (12), Applications (18), Technical Articles (2); tiers A (direct Jev research) / B (Jev as measured system); 🔥 for foundational items; Search and Verification Notes + Verification Policy.
- **Quality flags:** Hand-curated, careful paragraph-length annotations noting limitations of each paper. Excludes repos/demos/news. Explicitly notes Jev is closed-weight and no peer-reviewed architecture/RLCD paper exists; all Jev academic items are preprints. CONTRADICTION with Yifan-Lan/awesome-jev-robustness: "Decision Hijacking" (arXiv 2609.28613) authors listed here as Tiantong Wu and Wei Yang Bryan Lim, but as "Ren et al." in the robustness list — needs checking. Not promotional.
- **Unique value:** Only dedicated academic bibliography in batch; arXiv IDs with UTC submission times; balanced summaries with key numbers; covers application papers (6G edge orchestration, crash narratives, radiology, StarCraft II, mobile GUI agents, LoRA routing, memory) not found in project lists.

## Facts claimed about Jev
- Jev is not an acronym; named after economist William Stanley Jevons. Introduced 15 September 2026 (launch post by Diogo Almeida) as a non-autoregressive decision component with Choice, Score, Noul outputs with probabilities and confidence.
- Closed-weight commercial model; as of 28 Sep 2026 no peer-reviewed architecture or RLCD paper.
- Workflow evals (evals.typesafe.ai): four automation evaluations; policies decomposed into typed judgments + code; scored against consensus probabilities from large external models (reference-label caveat).
- "Jev in the Wild" (arXiv 2609.30216): 2,170 public Jev projects on GitHub through 22 Sep 2026.
- this-that-model-1.0 (2609.23886): 2B one-pass typed decision model beats Jev on accuracy/Brier on a 68-question cohort; "decides in 30 ms".
- Social-science annotation (2609.24574): Jev 1.13 vs 19 LLMs on 7,977 items / 18 tasks; trails best LLM on most tasks; far cheaper and often better calibrated than verbalized LLM confidence.
- JEV-as-a-Judge (2609.26550): within 3 accuracy points of strongest of 16 judges on ordinary preference; confidence cascade retains 99% of comparator accuracy.
- Option-name binding (2609.26758): 1,200 decisions; neutral->no/yes labels reverse rankings despite zero type errors.
- Legal (ContractNLI, 2609.27678): Jev lowest cost/latency, LLMs higher baseline accuracy.
- Decision Hijacking (2609.28613): 510 InjecAgent cases; adaptive attacks raise success 1.8% -> 3.5%.
- RLCDAlignBench (2609.29429): median AUROC 0.886; context fields matter more than phrasing.
- Rubric judges (2609.29769, Rao & Callison-Burch): competitive on binary criteria, weaker on graded; cascades recover at most 2 points because LLMs repeat Jev's confident errors.
- JevOut (2609.30243): 312/508 flipped, 229 high-confidence errors.
- JevAdvBench (2609.31142): jev-1.13.0, 812 questions, 66 scenarios, 9,744 attacks; appending an unverified opinion flips 12.1% and moves 38% of confident answers below 0.8; rewording near repeat floor.
- Applications: crash narratives 499,500 Texas narratives, 27-question schema, F1 0.908 vs human (2609.24052); Jev-Mobile AndroidWorld 79% success vs 84% step-wise VLM, −32.7% time, −73.4% cost (2609.30186); REFLEX 95% success with 72.7% fewer strong-model calls (2609.26532); enterprise coding-agent routing estimated 14-21% savings (2609.28919); JEV-Star StarCraft II with GPT-6 planning (2609.27331).
- Vercel article "What is Jev" (Ben Sabic) distinguishes schema validity from semantic correctness.

## Key insights / patterns
- Schema validity ≠ semantic correctness; zero type errors can coexist with reversed rankings.
- Confidence cascades (Jev then LLM) work only when failure modes are uncorrelated; LLM judges often share Jev's confident errors.
- Planner/executor split: infrequent VLM/LLM planning + high-frequency Jev action selection (Jev-Mobile, JEV-Star, REFLEX); risks: large action sets and near-valid alternatives.
- Jev as typed control plane for memory systems (Jev-Mem: labeling, relation construction, retrieval routing, stopping).
- Route coding agents only at session/subagent boundaries to avoid rebuilding prompt caches.
- Cache decisions per unique state for huge simulations (KITE).
- Numerical prediction via repeated range Choices (NumericJev multiway decision trees).
- Post-hoc recalibration materially reduces calibration error at scale.
- Jev-style interface is reproducible with open models (this-that-model, JevLite on Qwen3-4B, Visual Jev, PixelJev, LAVOIR on Laya).

## Standout entries
- [Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — canonical primary source (official)
- [Workflow evals](https://evals.typesafe.ai/) — first-party evaluation (official benchmark)
- [Jev in the Wild](https://arxiv.org/abs/2609.30216) — ecosystem study of 2,170 projects (paper)
- [Evaluating Decision Models for Text Annotation in CSS](https://arxiv.org/abs/2609.24574) — broadest verified accuracy/calibration study (paper)
- [JEV vs. LLMs as Rubric Judges](https://arxiv.org/abs/2609.29769) — correlated failures defeat cascades (paper)
- [JevAdvBench](https://arxiv.org/abs/2609.31142) — adversarial benchmark (paper)
- [Type-Safe Is Not Error-Free](https://arxiv.org/abs/2609.26758) — option-name effect (paper)
- [JevOut](https://arxiv.org/abs/2609.30243) — natural context flips decisions (paper)
- [this-that-model-1.0](https://arxiv.org/abs/2609.23886) — open 2B competitor (paper)
- [Jev-Mobile](https://arxiv.org/abs/2609.30186) — Jev as mobile GUI executor (paper)
- [REFLEX with Jev](https://arxiv.org/abs/2609.26532) — selective control in LLM agents (paper)
- [Jev-Mem](https://arxiv.org/abs/2609.23986) — System-One-controlled agent memory (paper)
- [Calibrated Decisions at Scale (crash narratives)](https://arxiv.org/abs/2609.24052) — 499,500 narratives (paper)
- [What is Jev? (Vercel)](https://vercel.com/i/what-is-jev) — sober integration guide (article)
- [Testing Jev on Public and Private Data](https://amankumar.ai/blogs/jev-measured) — 16,000-call study (evaluation)
