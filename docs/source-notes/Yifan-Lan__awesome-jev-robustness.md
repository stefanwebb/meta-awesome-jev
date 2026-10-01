# Yifan-Lan/awesome-jev-robustness
- **One-liner:** Curated evidence map of 132 independent robustness and calibration tests of Jev (mostly jev-1.13.0), with a synthesized property-by-property findings table.
- **Language(s):** English
- **Type:** security/robustness (curated evidence list)
- **Scale:** 132 entries (snapshot 2026-09-30); data/entries.tsv (133 lines), data/task_benchmarks.tsv (~280 accuracy-only task benchmarks kept out of README), data/candidates_unconfirmed.tsv (~143). Sections: Start here; What the evidence says so far (table); Official material; Papers (9 arXiv/preprints); Calibration and confidence (probability audits, confidence as routing signal, known-probability probes); Consistency and invariance (repeated calls, option order/set/count, question form); Input perturbation and context; Prompt injection and adversarial inputs; Abstention and unanswerable inputs; Failure modes and capability limits (documented jaggedness, counting/sequence/state, signal not in text); Languages other than English; Evaluation tooling; Write-ups, critiques and evidence ledgers; Related lists; Citation (CITATION.cff).
- **Quality flags:** Hand-curated, very information-dense; each entry lists model version and n. Numbers are the authors' own, not re-verified; most studies are small, one-person, run within two weeks of release (explicitly caveated). Not promotional. Highest-signal robustness resource in batch.
- **Unique value:** Synthesis table of Jev's robustness properties with conflicting sources linked; arXiv papers with IDs; concrete failure magnitudes (injection, option naming, abstain-option removal, Choice-vs-Noul probability collapse, language drops); confidence-formula finding; separation of robustness vs task accuracy benchmarks.

## Facts claimed about Jev
- Release 15 September 2026; almost all tests on `jev-1.13.0`.
- Official: Choice self-consistency cookbook — 8 questions, 7 conditions, 99.2% agreement at 0.60 threshold, flips on 2 of 8; Noul self-consistency cookbook — 14 Nouls x 15 repeats, std 0.0102, one borderline answer 0.43-0.53; Jev 1.13 jaggedness lists nine failure modes: literal reading, counting, numbers and dates, indirection, distracting state, adversarial content, contradictory criteria, invariants, generation; evals.typesafe.ai: four workflows, 61.7% to 76.0% agreement, reference label is average of two frontier models.
- Choice confidence = (N·p_max − 1)/(N − 1), a fixed formula of the top probability, not a separate signal (primeline.cc, Anthus).
- Option order: reversing two options moved probability 0.005, 0/400 argmax flips; but on ambiguous/value-laden questions first-listed option gained 0.37. Arithmetic 88% when correct option first vs 57% when last (RINNECODER, 11,621 requests).
- Option names: binding no/yes vs 0/1 to same rubrics dropped hosted Jev AUC .81 -> .58 (24x test-retest floor); random-string names remove effect (Sun & Xu arXiv 2609.26758).
- Repeated calls: std 0.001-0.015; 15 distinct answer sets in 50 identical requests.
- Noul vs 2-option Choice: mean abs gap 0.125, >0.2 on 1 item in 6. Negation: P(x)+P(not x) avg 1.02, range 0.71-1.42; Li et al. 480 negation pairs miss by 0.064 avg.
- Criteria wording is the largest lever: rewrites moved accuracy 70%->96%, 83%->100%.
- Batching questions: no interference (shift 0.008) even with hostile neighbours; but many rows in one state (40 rows) broke a ranking gate.
- No-right-option: without explicit none/unknown option Jev answers anyway: 79% stereotype picks at 0.79 confidence on KoBBQ; removing abstain option took KoBBQ accuracy 0.950 -> 0.000, ECE 0.023 -> 0.793; 0 of 30 out-of-scope inputs flagged; When2Call hallucinated a tool call on 76% of no-tool cases. But AbstentionBench mean F1 0.855, first among 20 systems.
- Calibration by primitive: Noul under-confident, Choice/Score over-confident. Fair die: Choice puts 82.9% on its pick at 19% accuracy; independent Nouls recover ~1/6. Probability puzzles: Noul MAE 5.6 pts vs Choice 21.1. Anthus 8,801 examples: Noul stated 79.0% vs 72.3% actual, Choice 91.4% vs 76.1%; isotonic regression ECE 0.117 -> 0.008. ASSAY-001: CLINC150 ECE 0.020, Banking77 0.094, zero type errors in 8,576. jev-certify: confidence exactly 1.0 on 56.4% of CLINC150 answers (nine wrong), risk floor 1.95%. Coding-agent decisions: Noul ECE 0.169, Choice 0.226. 3-SAT: calibration collapses (willkelly, 123,805 requests; support routing ECE 0.075).
- Injection: works when it reads as evidence about the judged item (claimed approval, editor's note); blunt commands mostly fail. jagged: 96.5% -> 26.5% with one-line injected instruction; decision-injection-bench: Jev flipped 1/1,056 (0.09%) vs others 3.0-62.6%; Iskandeur: one payload flips GPT-5.2 80/80, Jev 26/80; JevOut: 61.4% of 508 items flipped via fluent context (arXiv 2609.30243); VentureBeat: `rm -rf ~/.ssh` block probability 0.76 -> 0.48 after fake pre-approval; primeline 40-pair injection test 22.5% misclassified.
- Languages: Russian −11 pp, Spanish −3 to −6 pp, Korean −6.5 pp; the state's language matters, not the instruction's. yanng981/system-one-benchmark: Jev leads multilingual 0.872 non-English average.
- Capability limits: sequential state mutation 13.2%, exact counting 33.3%, static logic 97-100% (confidence >=0.95 correct 492/493); ARC-AGI-1 4/400 for $2.32; chess from raw FEN worse than random, ~950 Elo with tactical facts; poker 63% solver match; hidden house rule -> wrong 19/24 at high confidence.
- primeline.cc pre-registered: 12 probes of documented failure modes, 4 real, 8 refuted; ~9,750 calls.
- Meta-review (arXiv 2609.32160): typed readout shows no independent accuracy advantage over comparable label-probability readouts.
- Social-science annotation (arXiv 2609.24574): trails best of 19 LLMs by median 11.6 macro-F1, better calibrated than 16 of 19. RLCDAlignBench (2609.29429): median AUROC 0.886 zero-shot alignment-failure detection.

## Key insights / patterns
- Always include an explicit none/unknown/abstain option — its absence is the single most catastrophic failure.
- Prefer Noul for probability estimates; Choice probabilities collapse toward the pick and grow worse with option count; Choice confidence adds no information beyond p_max.
- Invest in criteria wording and option naming (names carry semantics that override the rubric; random names neutralize).
- Batch questions freely; don't pack many rows into one state.
- Recalibrate (isotonic/two-parameter) on your own labels; calibration does not transfer across datasets or OOD; thresholds tuned in-distribution can fail OOD (dependency auto-merge: 15 unsafe merges on 185).
- Ranking/discrimination is more reliable than absolute probability values.
- Injection risk is "evidence-shaped" text (fake approvals); don't let tool output or untrusted state claim authority.
- Give Jev computed features (Tetris, chess, Robocode) rather than raw state requiring computation.
- Test non-English workloads; accuracy and calibration drop.
- Choice and Score confidence distributions differ (bimodal vs mid-range) — one threshold can't serve both.

## Standout entries
- [jujumilk3/jev-calibration-audit](https://github.com/jujumilk3/jev-calibration-audit) — largest single audit, 11,759 items (calibration)
- [willkelly/jev-evaluation](https://github.com/willkelly/jev-evaluation) — 123,805 pre-registered requests (calibration)
- [primeline.cc pre-registered test](https://primeline.cc/blog/typesafe-jev-pre-registered-test) — 12 jaggedness probes, confidence formula (failure modes)
- [zkousama/jagged](https://github.com/zkousama/jagged) — injection drops 96.5% to 26.5% (injection)
- [Type-Safe Is Not Error-Free](https://arxiv.org/abs/2609.26758) — option name vs rubric binding (paper)
- [Decision Hijacking](https://arxiv.org/abs/2609.28613) — prompt-injection attacks on Jev decisions (paper)
- [JevAdvBench](https://arxiv.org/abs/2609.31142) — adversarial benchmark for RLCD models (paper)
- [Beyond Calibration: probability axioms](https://arxiv.org/abs/2609.33209) — negation coherence (paper)
- [Typed Decision Models: An Early Evidence Audit](https://arxiv.org/abs/2609.32160) — meta-review of 28 papers (paper)
- [JEV-as-a-Judge](https://arxiv.org/abs/2609.26550) — accept when confident, escalate when unsure (paper)
- [Evaluating System One Models for Agent Security Decisions](https://arxiv.org/abs/2609.33401) — Jev, Laya, Decider, Nimble as security judges (paper)
- [KantaHayashiAI/jev-does-not-play-dice](https://github.com/KantaHayashiAI/jev-does-not-play-dice) — Choice probability collapse (calibration)
- [AnthusAI/Jev-Calibration](https://github.com/AnthusAI/Jev-Calibration) — isotonic recalibration to ECE 0.008 (calibration)
- [sshariqali/jev-abstentionbench](https://github.com/sshariqali/jev-abstentionbench) — AbstentionBench F1 0.855 (abstention)
- [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13) — nine official failure modes (official)
