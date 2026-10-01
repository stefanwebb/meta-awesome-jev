# OmniJev/awesome-jev-papers
- **One-liner:** Papers-only list: 29 arXiv papers on Jev from its first two weeks plus 22 foundational papers, each checked against arXiv, with abstracts cached in site/arxiv.json.
- **Language(s):** English
- **Type:** papers-list
- **Scale:** 51 papers. Sections: Survey & Ecosystem (1), Open Decision Models (6), Jev as Judge & Classifier (6), Robustness & Attacks (4), Agents & Systems (7), Applications (5), Foundations (22: The Shape Before Jev 14, What Jev Is Sold Against 7, Where the Name Comes From 1). site/arxiv.json holds authors, date, abstract, category for all 51.
- **Quality flags:** High signal, clean. Sibling of OmniJev/awesome-jev-gallery (foundations section duplicated verbatim). All Jev papers dated 2026-09-19 to 2026-09-25 (arXiv 2609.xxxxx). A couple of titles have typos inherited from arXiv ("An Study", "JepSoup"). No commentary beyond titles in README; the substance is in arxiv.json abstracts.
- **Unique value:** The only dedicated academic-paper index for Jev, with arXiv IDs and abstracts containing quantitative findings on calibration, robustness, judges, agents and applications.

## Facts claimed about Jev
- Jev released 15 September 2026; 29 arXiv papers appeared in the first two weeks.
- Jev trained with "reinforcement learning for calibrated decisions (RLCD)"; answers many typed questions about one input in a single call (Just Ask Jev abstract).
- InstructGPT (2203.02155) and GPT-4 report author lists include Diogo Almeida (consistent with founder claims elsewhere).
- Paper findings (from abstracts):
  - Edge service orchestration (2609.22753): 8,280 requests, 33 conditions — Jev reduces median decision latency **22.7–64.5%** vs the fastest LLM; latency barely moves with input size or contract width.
  - this-that-model-1.0 (2609.23886): open 2B typed model decides in 30.9 ms on a laptop GPU vs frontier API 8,758 ms.
  - Crash narratives (2609.24052): screened 499,500 Texas narratives, coded 195,857 with a 27-question schema; cost governed by schema size not narrative length; audited against 2,416 blinded human judgments.
  - JEVQA (2609.24395): zero-shot video quality, Pearson 0.737 from metadata (≈ ITU-T P.1204.1 0.733), 0.797 with bitstream, 0.824 with pixel+bitstream.
  - Scientific decisions (2609.24965): Jev matched five configs at complete semantic correctness with the lowest median latency.
  - REFLEX (2609.26532): Jev decision layer + strong LLM on low confidence → 95% success on 100 tasks with **72.7% fewer strong-model calls**; limited advantage over cheap generative cascades on BFCL/τ-style evals; reliability depends on action-set size and near-valid alternatives near authorization boundaries.
  - JEV-as-a-Judge (2609.26550): within 3 points of GPT-6 where verdict is readable from text, at **0.36% of its fee, 0.15 s median**; behind on math/code/logic; frozen-threshold cascade 0.9 points more accurate than GPT-6 at 41% of fee.
  - Type-Safe Is Not Error-Free (2609.26758): renaming two options 0/1→no/yes changes 70.4 more answers per hundred and shifts AUC from .94 to .23 — the head follows option name, not bound rubric.
  - JEV-Star (2609.27331): Jev action selection + GPT-6 planning beats StarCraft II Lv7 AI; median Jev response 0.422 s; ~$3.71/game ($0.15 Jev, $3.56 GPT-6); Jev-only controller weak.
  - Radiology (2609.27607): Kendall 0.573 RadEvalX, 0.398 RadEvalExpert; one support question per statement uses 43–45% fewer input tokens than seven.
  - ContractNLI (2609.27678): Jev lowest cost and median latency; hosted LLMs higher baseline accuracy.
  - Decision Hijacking (2609.28613): 510 InjecAgent cases — injection shifts probabilities but rarely selects attacker target; adaptive attacks raise success 1.8%→3.5%.
  - LLM rubric judges (2609.29769): Jev differs significantly in only 8/27 comparisons (ahead on binary, behind on graded); LLM judges cost 29–325x more and took 30–220x longer.
  - Jev-Mobile (2609.30186): AndroidWorld 79% success vs SeeAct-V 78% and step-wise VLM 84%.
  - Jev in the Wild (2609.30216): 2,170 GitHub projects as of 2026-09-22.
  - JevOut (2609.30243): fluent context additions redirect **312 of 508 (61.4%)** initially correct decisions.
  - LAVOIR (2609.30706): System One models cannot ask for missing information — they guess.
  - JevAdvBench (2609.31142): identical requests can return different answers; API preprocesses requests out of view; scores attacks against model's own clean decision.

## Key insights / patterns
- Robustness is the main research theme: option naming, natural context additions and prompt injection move decisions; schema validity ≠ correctness; evaluate against re-run noise.
- Judge pattern: accept confident verdicts, escalate the rest (cascade) — strong cost/accuracy trade-off; Jev weak where verdict must be derived (math/code/logic) and on graded criteria.
- Agent pattern: low-frequency planner (LLM/VLM) + high-frequency Jev executor over structured action space (accessibility tree, game actions) — cuts expensive calls 66–73%.
- Cost scales with schema size (number of questions), not document length.
- Fewer, well-designed questions can match many (radiology: 1 vs 7).
- Domain applications span edge/6G orchestration, video QA, crash narratives, pentest harnesses, enterprise coding-agent routing, population simulations, LoRA routing.

## Standout entries
- [Jev in the Wild](https://arxiv.org/abs/2609.30216) — ecosystem survey of 2,170 projects (survey)
- [JEV-as-a-Judge](https://arxiv.org/abs/2609.26550) — accept-when-confident cascade vs GPT-6 (judge)
- [Jev vs. LLM Rubric Judges](https://arxiv.org/abs/2609.29769) — 29–325x cheaper, wrong in same places (judge)
- [Just Ask Jev](https://arxiv.org/abs/2609.29429) — RLCDAlignBench, 44 alignment-failure benchmarks (judge/safety)
- [Type-Safe Is Not Error-Free](https://arxiv.org/abs/2609.26758) — option-name sensitivity (robustness)
- [JevOut](https://arxiv.org/abs/2609.30243) — natural context flips decisions (robustness)
- [Decision Hijacking](https://arxiv.org/abs/2609.28613) — prompt injection on typed decisions (robustness)
- [JevAdvBench](https://arxiv.org/abs/2609.31142) — adversarial benchmark for RLCD models (robustness)
- [REFLEX](https://arxiv.org/abs/2609.26532) — selective control, 72.7% fewer strong-model calls (agents)
- [Jev-Mobile](https://arxiv.org/abs/2609.30186) — Jev executor for mobile GUI agents (agents)
- [JEV-Star](https://arxiv.org/abs/2609.27331) — StarCraft II with Jev + GPT-6 (agents)
- [Crash Narratives](https://arxiv.org/abs/2609.24052) — 195,857 narratives coded with 27 questions (application)
- [JEVQA](https://arxiv.org/abs/2609.24395) — zero-shot video quality (application)
- [LAVOIR](https://arxiv.org/abs/2609.30706) — value-of-information slots for missing info (open models)
- [RLCR](https://arxiv.org/abs/2507.16806) — closest published relative of RLCD (foundation)
