# Research Papers

> Papers about Jev and System One decision models, merged from the paper lists in the sources: [OmniJev/awesome-jev-papers](https://github.com/OmniJev/awesome-jev-papers), [Oscar-dzy/Awesome-jev-papers](https://github.com/Oscar-dzy/Awesome-jev-papers), [Eurekaleo/awesome-jev-survey](https://github.com/Eurekaleo/awesome-jev-survey), [Sarim-MBZUAI/awesome-jev-security](https://github.com/Sarim-MBZUAI/awesome-jev-security), [Yifan-Lan/awesome-jev-robustness](https://github.com/Yifan-Lan/awesome-jev-robustness), [youzizzz1028/Awesome-Jev](https://github.com/youzizzz1028/Awesome-Jev) and [Promethe-us/awesome-jev](https://github.com/Promethe-us/awesome-jev). Findings are **author-reported** and summarized from those lists.
>
> **Context.** There is **no official paper** on Jev's architecture or RLCD training, and every Jev-specific item below is a preprint. Around 29 appeared in the first two weeks after launch, clustered within days of each other, and none are replicated. Survey [arXiv 2609.32160](https://arxiv.org/abs/2609.32160) found that across 28 papers, the typed readout shows **no independent accuracy advantage** over comparable label-probability readouts. The clearest gains were latency and cost.

[← back to the main list](../README.md)

## Surveys, audits and ecosystem studies

| Paper | Key finding |
|---|---|
| [Jev in the Wild: A Data-Driven Analysis of the Jev Model's Functionality, Applications and Ecosystem](https://arxiv.org/abs/2609.30216) (2609.30216) | Survey of **2,170 public GitHub projects** through 2026-09-22. The most-cited paper across the source lists (📚18). |
| [Typed Decision Models: An Early Evidence Audit and Evaluation Checklist](https://arxiv.org/abs/2609.32160) (2609.32160) | Meta-review of 28 papers from the first nine days, with a 14-item evaluation checklist. No independent accuracy advantage found for the typed readout. |
| [Beyond Calibration: Do a Typed-Decision Model's Probabilities Obey the Probability Axioms?](https://arxiv.org/abs/2609.33209) (2609.33209) | Negation pairs P(X) + P(¬X) miss 1 by 0.064 on average (Qwen3.8-27B first-token: 0.293). [Code](https://github.com/bro789/typed-decision-coherence). |
| [Awesome Jev Survey](https://eurekaleo.github.io/awesome-jev-survey/) (Eurekaleo, working draft) | 17 core studies, an audit of open-implementation openness, and seven findings. For example, "type-valid ≠ correct", "calibration is auditable, not guaranteed", and that latency/cost scopes can't be pooled. |
| *Decisions, Not Tokens* ([youzizzz1028](https://github.com/youzizzz1028/Awesome-Jev)) | A taxonomy (output contract / inference / objective / uncertainty / system control) and a four-layer evaluation framework. |

## Jev as judge, classifier and annotator

| Paper | Key finding |
|---|---|
| [JEV-as-a-Judge: Accept When Confident, Escalate When Unsure](https://arxiv.org/abs/2609.26550) (2609.26550, CMU) | Within ~3 pts of the best of 16 judges at **~0.36% of the fee** and a 0.15 s median. It is 9–20 pts behind on JudgeBench and math/code/logic. The confidence cascade keeps ~99% of accuracy. |
| [JEV vs. LLMs as Rubric Judges: Cheaper, Faster, and Wrong in the Same Places](https://arxiv.org/abs/2609.29769) (2609.29769, UPenn) | Better on binary checklists, worse on graded scales. LLM judges cost 29–325× more. **LLMs repeat Jev's confident errors ~96% of the time**, so cascades gain ≤1.5–2 pts. |
| [Evaluating Decision Models for Text Annotation in Computational Social Science](https://arxiv.org/abs/2609.24574) (2609.24574) | Jev 1.13 vs 19 LLMs, 18 tasks, 7,977 items. It trails the best LLM on 14/15 tasks (median −11.6 macro-F1) at ~1/44 the cost and is better calibrated than 16/19. Routing matches the LLM at ¼–½ the cost. |
| [Same Scores, Different Decisions: Evaluating JEV and Language Models for Legal Document Understanding](https://arxiv.org/abs/2609.27678) (2609.27678) | ContractNLI: Jev has the lowest cost ($0.000228/contract) and median latency; hosted LLMs are more accurate. |
| [Can Jev Judge Radiology Reports? Evaluating a System One Model for Clinical Factuality](https://arxiv.org/abs/2609.27607) (2609.27607) | Kendall τ 0.573 (RadEvalX) / 0.398 (RadEvalExpert); beats open NLI. One support question per statement uses 43–45% fewer tokens than seven. |
| [Jev for Scientific Decisions: Evaluating Semantic Choices and Their Consequences](https://arxiv.org/abs/2609.24965) (2609.24965) | Matched five configurations at complete semantic correctness with the lowest latency (median 0.335 s). |
| [Just Ask Jev: RLCD as a Zero-Shot Detector of AI Alignment Failures](https://arxiv.org/abs/2609.29429) (2609.29429) | RLCDAlignBench (44 benchmarks, 10 failure types): median AUROC 0.886. Context fields matter more than phrasing. [Code](https://github.com/sumleo/RLCDAlignBench). |
| [KITE: Scaling Jev Population Experiments with Sparse Flagship Calibration](https://arxiv.org/abs/2609.27535) (2609.27535) | Calibrating on 1.7% GPT-6 Astra anchors cut effect error by 41%; caches per unique state. |
| [When a Judgment Layer's Self-Reported Fields Lie](https://doi.org/10.5281/zenodo.22901853) (Zenodo) | Jev as one of three judgment layers; its verdict vocabulary collapses to three reachable values. |
| [Confident Where People Disagree](https://zenodo.org/records/22971492) (Zenodo, pre-registered) | ChaosNLI: Choice confidence 0.807 vs 0.468 human agreement, so Jev is overconfident on contested items. |

## Robustness, security and attacks

| Paper | Key finding |
|---|---|
| [Type-Safe Is Not Error-Free: A Constrained Decision Head Follows the Option Name, Not the Rubric Bound to It](https://arxiv.org/abs/2609.26758) (2609.26758) | Renaming 0/1 → no/yes changes 70.4 more answers per hundred (AUC .94 → .23 in open models; hosted Jev .8146 → .5806), with **0% type errors**. |
| [JevAdvBench: A Benchmark and Black-Box Attacks for RLCD Models](https://arxiv.org/abs/2609.31142) (2609.31142) | 9,744 attacks: an appended unverified opinion flips 12.1% of decisions and moves 38% of confident answers below 0.8. Identical requests can return different answers. [Site](https://JevAdvBench.github.io/JevAdvBench/). |
| [JevOut: Natural Context Can Flip Decision Models](https://arxiv.org/abs/2609.30243) (2609.30243) | Fluent context flips **61.4%** (312/508) of correct decisions, and 64.9–73.2% on open clones. [Code](https://github.com/xzx34/JevOut). |
| [Decision Hijacking: Prompt Injection Attacks on Jev's Typed Probabilistic Decisions](https://arxiv.org/abs/2609.28613) (2609.28613) | 510 InjecAgent cases: probability shifts, but the attacker target is selected only 1.8% of the time (3.5% adaptive). *(Author attribution differs between source lists.)* |
| [Evaluating System One Models for Agent Security Decisions: Reliability, Calibration, and Selective Automation](https://arxiv.org/abs/2609.33401) (2609.33401) | Jev, Laya, Decider and Nimble vs classifiers and LLM judges: average calibration hides failures on attack subgroups. |
| [Calibrated Decision Models for Autonomous Penetration-Testing Harnesses: JEV and Laya as System One Decision Layers](https://arxiv.org/abs/2609.28940) (2609.28940) | ~236–276 ms per call with Jev, 33–40 ms with Laya. |
| [Open-Jev Judgments on CallScreenBench: Calibrated One-Pass Scam Screening with a Small LM](https://arxiv.org/abs/2609.23959) (2609.23959) | JevLite (Qwen3-4B, *not* TypeSafe's Jev): AUROC 0.974 at 64.5 ms. |

## Agents and systems

| Paper | Key finding |
|---|---|
| [REFLEX with Jev for Efficient Selective Control in LLM Agents](https://arxiv.org/abs/2609.26532) (2609.26532) | 95% success with **72.7% fewer** strong-model calls; limited edge over cheap generative cascades. |
| [Jev-Mobile: Jev as an Executor for Mobile GUI Agents](https://arxiv.org/abs/2609.30186) (2609.30186) | AndroidWorld 79% vs 84% for a step-wise VLM, with −32.7% time and −73.4% cost. |
| [JEV-Star: Fast, Low-Cost StarCraft II Control with Language-Model Planning](https://arxiv.org/abs/2609.27331) (2609.27331) | With GPT-6 planning it beats the Lv7 AI 4/4 at $3.71/game; Jev-only is weak. |
| [Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents](https://arxiv.org/abs/2609.23986) (2609.23986) | LoCoMo 0.777 vs 0.700 (+11%), 6.6× faster. [Code](https://github.com/libingzheren/Jev-Mem). |
| [Control the Harness, Control the Cost: Routing and Governing AI Coding Agents in the Enterprise](https://arxiv.org/abs/2609.28919) (2609.28919) | Jev routes at session start, side lanes and subagent launch: estimated 14–21% savings. |
| [Replacing LLMs with Jev Decision Models for Low-Latency Edge Service Orchestration](https://arxiv.org/abs/2609.22753) (2609.22753) | Median decision latency −22.7–64.5% vs the fastest LLM; **caching erases the gap**. |
| [Fast Intent-Driven Service Orchestration with Jev for 6G Edge Networks](https://arxiv.org/abs/2609.23136) (2609.23136) | Latency −22.4% vs DeepSeek, −61.9% vs Gemini; 97.0% on-time. |
| [JevSoup: System-One Routing for Training-Free LoRA Composition](https://arxiv.org/abs/2609.30922) (2609.30922) | Jev routes LoRA adapters. |

## Applications

| Paper | Key finding |
|---|---|
| [Calibrated Decisions at Scale: Converting Police Crash Narratives into Probabilistic Crash Variables](https://arxiv.org/abs/2609.24052) (2609.24052) | 499,500 Texas narratives screened for **$25.23**; 195,857 coded with a 27-question schema; F1 0.908 vs 2,416 human judgments. Cost is governed by schema size, not narrative length. |
| [JEVQA: Video Quality from Metadata, Bitstream, and Pixel Features with a General-Purpose Decision Model](https://arxiv.org/abs/2609.24395) (2609.24395) | Zero-shot PLCC 0.737 → 0.824. |

## Open decision models (papers)

| Paper | Key finding |
|---|---|
| [this-that-model-1.0: A typed decision model that decides in 30 ms, for a millionth of a cent](https://arxiv.org/abs/2609.23886) (2609.23886) | Open ~2B model, 30.9 ms. It beats Jev on a 68-question cohort (0.941 vs 0.765) but loses on multi-step arithmetic (0.560 vs 0.98–1.00). |
| [Visual Jev: Accurate and Efficient Decisions from Shared Visual Context](https://arxiv.org/abs/2609.25845) (2609.25845) | Independent; 8.9× at 32 questions per image. **Not** evidence that hosted Jev accepts images. |
| [From Text Decisions to Pixels: A Study of Jev-Style Visual Choice Model](https://arxiv.org/abs/2609.29283) (2609.29283) | PixelJev. |
| [NumericJev](https://arxiv.org/abs/2609.28587) (2609.28587) | Numerical prediction via repeated range Choices; the code is now JevNext (non-commercial). |
| [LAVOIR: Teaching a Single-Pass Decision Encoder When and What to Ask](https://arxiv.org/abs/2609.30706) (2609.30706) | System One models can't ask for missing information, so they guess. LAVOIR adds value-of-information slots, built on Laya. |

## Foundations and lineage

These are the ideas Jev is built from or sold against. They are collected from [OmniJev/awesome-jev-gallery](https://github.com/OmniJev/awesome-jev-gallery), [youzizzz1028/Awesome-Jev](https://github.com/youzizzz1028/Awesome-Jev), [mturac](https://github.com/mturac/awesome-jev-alternatives) and [rupeshpoojary9](https://github.com/rupeshpoojary9/awesome-open-system-one).

**Calibration and uncertainty**
- [On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599) (Guo et al., 2017): temperature scaling and ECE.
- [Beyond Binary Rewards / RLCR](https://arxiv.org/abs/2507.16806): a Brier reward in RL; the closest published relative of RLCD.
- [Rewarding Doubt](https://arxiv.org/abs/2503.02623)
- [Calibration-Aware RL for Decision-Making LLMs](https://arxiv.org/abs/2601.13284)
- [Language Models (Mostly) Know What They Know](https://arxiv.org/abs/2207.05221)
- [A Gentle Introduction to Conformal Prediction](https://arxiv.org/abs/2107.07511)
- [Detecting Hallucinations Using Semantic Entropy](https://doi.org/10.1038/s41586-024-07421-0)
- [GPT-4 Technical Report](https://arxiv.org/abs/2303.08774): RLHF hurts calibration, the finding RLCD is positioned against.

**Selective prediction and routing**
- [SelectiveNet](https://proceedings.mlr.press/v97/geifman19a.html)
- [RouteLLM](https://arxiv.org/abs/2406.18665)
- [FrugalGPT](https://arxiv.org/abs/2305.05176)
- [Confidence-Aware Routing for LLM Reliability](https://arxiv.org/abs/2510.01237)
- [Distilling System 2 into System 1](https://arxiv.org/abs/2407.06023)
- [Thinking Fast and Slow in AI](https://arxiv.org/abs/2010.06002)
- [Agents Thinking Fast and Slow (Talker-Reasoner)](https://arxiv.org/abs/2410.08328)
- [R2R token routing](https://arxiv.org/abs/2505.21600)

**Discriminative decision heads**
- [InstructGPT](https://arxiv.org/abs/2203.02155): reward-model heads. The founder is a co-author.
- [monoBERT](https://arxiv.org/abs/1901.04085): cross-encoder relevance scoring.
- [Zero-shot Classification as Entailment](https://arxiv.org/abs/1909.00161)
- [GLiNER](https://arxiv.org/abs/2311.08526)
- [GLiClass](https://arxiv.org/abs/2508.07662)
- [Generative or Discriminative?](https://arxiv.org/abs/2506.12181)
- [Llama Guard](https://arxiv.org/abs/2312.06674)
- [Constitutional Classifiers](https://arxiv.org/abs/2501.18837)

**Structured output (what Jev is sold against)**
- [Outlines](https://arxiv.org/abs/2307.09702)
- [JSONSchemaBench](https://arxiv.org/abs/2501.10868)
- [Let Me Speak Freely?](https://arxiv.org/abs/2408.02442)
- [DSPy](https://arxiv.org/abs/2310.03714)
- [MT-Bench / LLM-as-a-judge](https://arxiv.org/abs/2306.05685)

**Non-autoregressive and efficient inference (architecture speculation)**
- [LLaDA](https://arxiv.org/abs/2502.09992): TypeSafe forked it.
- [Mercury](https://arxiv.org/abs/2506.17298)
- [vLLM / PagedAttention](https://arxiv.org/abs/2309.06180)

**Naming**
- Kahneman's *Thinking, Fast and Slow* (System 1).
- The Jevons paradox: cheaper decisions increase total decision volume.
- Note the acronym collision: ICLR 2024's "RLCD: Reinforcement Learning from Contrast Distillation" is unrelated to TypeSafe's RLCD.

For the complete machine-extracted list (229 entries), see [catalog/papers.md](../catalog/papers.md).
