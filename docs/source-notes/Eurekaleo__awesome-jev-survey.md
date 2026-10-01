# Eurekaleo/awesome-jev-survey
- **One-liner:** Academic evidence survey (with LaTeX/PDF manuscript) of Jev and Jev-like typed decision models: 17 arXiv core studies, open implementations audit, seven synthesized findings.
- **Language(s):** English
- **Type:** papers-list (survey paper + structured data)
- **Scale:** 17 core studies (arXiv, 19–23 Sept 2026) + 1 peripheral study; ~33 open implementations/evaluations with openness grid (code/weights/training/eval/raw predictions); ~40 background references across 8 themes (Classifiers & general discrimination; Calibration & uncertainty; Selective prediction & deferral; Decision-focused calibration & utility; Structured output & efficient inference; Judging & reward models; Routing & reasoning budgets; Label, format & semantic robustness). Sections: Findings; Core studies; Peripheral study; Open implementations and evaluations; Background references; Related survey; Method. Author Meng Luo; v0.2.0, data cutoff 24 Sep 2026; CITATION.cff; website eurekaleo.github.io/awesome-jev-survey.
- **Quality flags:** High quality, scholarly, candid ("numbers are as reported… nothing here is a unified leaderboard"; "working draft, not peer-reviewed"). README generated from JSON data. No fabricated-looking entries apparent (arXiv IDs are future-dated consistent with the Jev timeline). Small but deep.
- **Unique value:** The only true research synthesis in the batch: headline numbers per paper, code-availability audit, taxonomy of open-implementation mechanisms (encoder heads, frozen decoder readout, diffusion readout, fine-tuned decoders, adapters), and careful separation of latency/cost scopes (Table 4). Clarifies terminology (RLCD ≠ Reinforcement Learning from Contrastive Distillation).

## Facts claimed about Jev
- Released in **early access on 15 September 2026** (paper/survey.md). Launch materials: "new class of frontier models" optimised with **"Reinforcement Learning for Calibrated Decisions" (RLCD)**; new architecture + parallel sampler; one set of weights serves every account (no per-customer fine-tuning); architecture/training data not published.
- Vendor claim: **70–500 ms end to end at $0.042 per million input tokens**. (Contrast: RadRebelSam list quotes vendor "40–200x faster"; AppitStudio quotes 193.6x latency / 444.6x cost — different framings, not strictly contradictory.)
- At cutoff documented model `jev-1.13.0`; aliases **`jev-latest` and `jev-preview`** both pointed to it; vendor advises pinning versioned ID. One study used `typesafe/…` (OpenRouter ID).
- Input text only (images/audio/video must be converted); **English is the primary training language**.
- State = string, JSON object or array of text values; map of typed questions evaluated independently. Choice returns chosen option + probability for every option.
- Native confidence ≈ maximum probability; vendor presents calibration as a group property; **probabilities quantised to two decimals**.
- Core-study headlines (author-reported): Legal contracts (2609.27678) $0.000228 & 1.24 s per contract, lowest of ten models; Radiology factuality (2609.27607) Kendall τ 0.573/0.398, beats open NLI; KITE (2609.27535) 1.7% GPT-6 Astra anchors cut effect error 41%; JEV-Star StarCraft II (2609.27331) 4/4 wins with GPT-6 plans, Jev-only never expanded, Jev 0.422 s median, $0.15 of $3.71 per game; "Type-Safe Is Not Error-Free" (2609.26758) hosted Jev AUROC .8146 → .5806 after name–rubric swap, 0% type errors; JEV-as-a-Judge (2609.26550) RewardBench 92.2% vs 93.5%, HaluEval 87.5% vs 86.7% (GPT-6); REFLEX (2609.26532) 95% success with 1.12 strong calls/task vs 88% & 4.10; Scientific decisions (2609.24965) median 0.335 s, p95 0.442 s; CSS annotation (2609.24574) behind best LLM on 14/15 tasks (−11.6 F1) at 44× lower cost; JEVQA (2609.24395) PLCC 0.737→0.824; Police crash narratives (2609.24052) 499,500 narratives screened for $25.23; Jev-Mem (2609.23986) LoCoMo 0.777 (+11.0%); 6G edge orchestration (2609.23136, 2609.22753) latency −15.9% to −61.9% vs LLMs. Other: ≈$0.04 per 1,000 judgments at 0.15 s; $0.0227 per 1,000 predictions at 213 ms median.
- Visual Jev (2609.25845) is independent — **not** evidence that hosted Jev accepts images.

## Key insights / patterns
- F1: Type-valid ≠ correct — option *names* can dominate rubric definitions; removing abstain options or switching primitive shifts answers.
- F2: Native probabilities make calibration auditable, not guaranteed; varies by task; recalibration on in-distribution labels helps substantially.
- F3: Most consistent winning pattern = bounded first pass with confidence-gated escalation to stronger model/human; choose thresholds on separate data; include cheap generative cascades as baselines.
- F4: Latency/cost figures (single-request, amortized per-question, batch, end-to-end, electricity-only, API bill) can't be pooled; prefix sharing/batching/caching explain much.
- F5: Wire compatibility ≠ mechanism equivalence for open reimplementations.
- F6: System gains need ablations and matched baselines.
- F7: Evidence is young, clustered (17 preprints within 5 days), unreplicated; two papers share a study family.
- Keep arithmetic in code (vendor's documented division of labour).

## Standout entries
- [JEV-as-a-Judge: Accept When Confident, Escalate When Unsure](https://arxiv.org/abs/2609.26550v1) — judge evaluation vs 16 judges (paper)
- [Type-Safe Is Not Error-Free](https://arxiv.org/abs/2609.26758v1) — option-name vs rubric robustness (paper)
- [REFLEX with Jev for Efficient Selective Control in LLM Agents](https://arxiv.org/abs/2609.26532v1) — confidence-gated agent control (paper)
- [Evaluating Decision Models for Text Annotation in Computational Social Science](https://arxiv.org/abs/2609.24574v1) — Jev vs 19 LLMs (paper)
- [Same Scores, Different Decisions: … Legal Document Understanding](https://arxiv.org/abs/2609.27678v1) — legal benchmark with code (paper)
- [Calibrated Decisions at Scale: Police Crash Narratives](https://arxiv.org/abs/2609.24052v1) — large-scale coding for $25 (paper)
- [Jev-Mem](https://arxiv.org/abs/2609.23986v1) — System-One-controlled agent memory (paper)
- [JEV-Star](https://arxiv.org/abs/2609.27331v1) — StarCraft II control (paper)
- [Can Jev Judge Radiology Reports?](https://arxiv.org/abs/2609.27607v1) — clinical factuality (paper)
- [this-that-model-1.0](https://arxiv.org/abs/2609.23886v1) — open ~2B typed decision model, 30.9 ms (paper/model)
- [jujumilk3/jev-calibration-audit](https://github.com/jujumilk3/jev-calibration-audit/blob/daab9e2c2d5d5683bf07f3482deb653c26856219/README.md) — calibration audit with raw predictions (evaluation)
- [scienthoon/jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration/blob/914d87ab16517f14e833cff63d73b51235b14bd6/README.md) — OOD calibration eval (evaluation)
- [githubnext/localjev](https://github.com/githubnext/localjev/blob/3f23e36e1a3bff46c7e83e8e3781d3512bc82021/README.md) — GitHub Next local adapter (open implementation)
- [Decisions, Not Tokens (related survey)](https://github.com/youzizzz1028/Awesome-Jev/blob/f3703012b0034eefe0d59936c44cd33ea11b2990/paper/main.tex) — broader survey draft (survey)
- [Survey website](https://eurekaleo.github.io/awesome-jev-survey/) — browsable survey (survey)
