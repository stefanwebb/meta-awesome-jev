# Sarim-MBZUAI/awesome-jev-security
- **One-liner:** Focused papers list on the security, robustness and safety of Jev and RLCD/System One models: 11 arXiv papers with dates, authors and quantitative one-paragraph summaries.
- **Language(s):** English
- **Type:** security/robustness (papers-list)
- **Scale:** 11 papers + 1 background link + 3 related projects. Sections: Attacks & Adversarial Robustness (4); Jev as a Security / Safety Detector (2); Jev in Security Applications (2); Reliability & Safe Deployment (3); Background; Related Projects.
- **Quality flags:** High signal, small, careful; summaries quote specific numbers and caveats (e.g. "one exploratory run per condition", "JevLite … not TypeSafe's Jev"). Papers dated 2026-09-21 to 09-27; excludes marketing/blogs by policy. Not stale as of end-Sept. Cannot verify arXiv IDs offline.
- **Unique value:** The best single source of **quantified adversarial and reliability findings** on Jev: context-injection flip rates, prompt-injection selection rates, option-name sensitivity, probability-axiom violations, security-detector calibration failures, with arXiv IDs.

## Facts claimed about Jev
- Jev announced 2026-09-15; TypeSafe's first System One model; maps state to typed probabilistic decisions (`Choice`, `Score`, `Noul`) with calibrated confidence; RLCD = Reinforcement Learning for Calibrated Decisions. Launch post includes vendor workflow evals incl. a security incident response workflow.
- **JevAdvBench** (arXiv 2609.31142, 2026-09-25): 812 typed questions, 66 scenarios, 9,744 single-edit black-box attack variants; a single unverified opinion appended to state flips **12.1%** of decisions (tied with strongest injected command, **10.1%**); pushes **38%** of confident answers below human-review thresholds.
- **JevOut** (2609.30243): natural-looking context optimizer flips **61.4%** of Jev's initially correct decisions; **64.9–73.2%** on OpenSourceJev, Von, plain Qwen.
- **Decision Hijacking** (2609.28613): 510 reconstructed InjecAgent cases; Jev rarely picks attacker target (**1.8%**), adaptive attacks with score feedback **3.5%**.
- **Type-Safe Is Not Error-Free** (2609.26758): renaming `0/1` to `no/yes` with identical definitions changes **70.4 more answers per hundred**, AUC drops **.94 → .23**, with 0% type errors — decision heads follow option *names*, not rubrics.
- **Evaluating System One Models for Agent Security Decisions** (2609.33401): Jev, Laya, Decider, Bespoke Nimble vs classifiers and LLM judges; good average calibration hides systematic failures on attack subgroups; under strict missed-attack limits very little traffic can be auto-allowed.
- **Just Ask Jev / RLCDAlignBench** (2609.29429): zero-shot detector of ten alignment failures; far cheaper than LLM judges.
- **Pentest harnesses** (2609.28940): ~**236–276 ms** per call with Jev, **33–40 ms** with Laya.
- **CallScreenBench** (2609.23959): JevLite (Qwen3-4B, not TypeSafe's) AUROC .974, calibration error .052, 64.5 ms/decision.
- **Beyond Calibration** (2609.33209): negation pairs P(X)+P(not X) misses 1 by **0.064** on average (Qwen3.8-27B first-token: 0.293).
- **Early Evidence Audit** (2609.32160): 28 papers in first nine days; typed readout has not shown an independent accuracy advantage over label-probability baselines; clearest gains are latency and cost; 14-item checklist.
- **REFLEX with Jev** (2609.26532): 95% success with **72.7% fewer** strong-model calls; gains shrink when routing already accurate.

## Key insights / patterns
- Schema constraints eliminate malformed outputs but not manipulation of the decision distribution or confidence; typed output ≠ injection-proof.
- Benign-looking unverified opinions in state are as dangerous as explicit injected commands; sanitize/segregate untrusted state fields.
- Attackers can push confident answers below review thresholds (DoS on automation) or flip decisions; monitor confidence distribution shifts.
- Option labels matter: use semantically meaningful option names consistent with rubric; test label renaming.
- Average calibration hides subgroup failures — evaluate per attack family; strict miss limits reduce auto-allow coverage.
- Don't assume probability coherence (negations); ask one polarity and calibrate.
- Security uses: finding adjudication, severity recalibration, agent pruning, confirmation loops in pentest agents; scam screening; alignment-failure detection; defer-to-strong-LLM routing.
- Latency reality check: ~236–276 ms per Jev call in a real harness.

## Standout entries
- [JevAdvBench (arXiv 2609.31142)](https://arxiv.org/abs/2609.31142) — first adversarial benchmark for RLCD models (security)
- [JevAdvBench project page](https://JevAdvBench.github.io/JevAdvBench/) — benchmark site (security)
- [JevOut (arXiv 2609.30243)](https://arxiv.org/abs/2609.30243) — natural context flips decisions (security)
- [JevOut code](https://github.com/xzx34/JevOut) — attack optimizer (security)
- [Decision Hijacking (arXiv 2609.28613)](https://arxiv.org/abs/2609.28613) — prompt injection on typed decisions (security)
- [Type-Safe Is Not Error-Free (arXiv 2609.26758)](https://arxiv.org/abs/2609.26758) — option-name sensitivity (robustness)
- [Evaluating System One Models for Agent Security Decisions (arXiv 2609.33401)](https://arxiv.org/abs/2609.33401) — detector reliability/calibration (security)
- [Just Ask Jev / RLCDAlignBench (arXiv 2609.29429)](https://arxiv.org/abs/2609.29429) — alignment-failure detection (safety)
- [RLCDAlignBench code](https://github.com/sumleo/RLCDAlignBench) — benchmark code (safety)
- [Pentest harnesses with JEV and Laya (arXiv 2609.28940)](https://arxiv.org/abs/2609.28940) — System One in pentest agents (application)
- [CallScreenBench (arXiv 2609.23959)](https://arxiv.org/abs/2609.23959) — scam screening with open Jev-style model (application)
- [Beyond Calibration (arXiv 2609.33209)](https://arxiv.org/abs/2609.33209) — probability-axiom coherence (reliability)
- [typed-decision-coherence code](https://github.com/bro789/typed-decision-coherence) — coherence tests (reliability)
- [Typed Decision Models: Early Evidence Audit (arXiv 2609.32160)](https://arxiv.org/abs/2609.32160) — 14-item checklist (reliability)
- [REFLEX with Jev (arXiv 2609.26532)](https://arxiv.org/abs/2609.26532) — selective control in LLM agents (reliability)
