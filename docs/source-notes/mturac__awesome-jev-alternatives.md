# mturac/awesome-jev-alternatives
- **One-liner:** Carefully verified list of open, self-hostable alternatives and building blocks for System One-style decision models: engines, runtimes, zero-shot classifiers, calibration tools, datasets, papers.
- **Language(s):** English
- **Type:** curated-list (alternatives / papers)
- **Scale:** ~40 entries: Decision engines (14), Runtimes and ports (5), Zero-shot classifiers (2), Calibration (4), Benchmarks and datasets (4), Research (7 arXiv papers), Related lists (2). CC0; link-check CI (scripts/check_links, links.yml).
- **Quality flags:** Very high quality: each link fetched, GitHub API checked for stars/license/last push; archived and >365-day-stale repos excluded unless marked historical; every description names a limitation; refuses to repeat unverified benchmark tables. No promo.
- **Unique value:** Only list in batch focused purely on open alternatives with candid limitations (hardware needs, license mismatches, constant-baseline failures), plus classical calibration tooling (MAPIE, net:cal, temperature scaling) and pre-Jev research on logprob judgments/calibration.

## Facts claimed about Jev
- Jev is closed/hosted; answers typed yes/no, choice, score questions with probabilities.
- No direct Jev specs/pricing given. Implicit: open projects replicate the "TypeSafe-shaped"/"Jev-shaped" HTTP API, not Jev's training.
- Claims about alternatives: CLM uses frozen Qwen3-8B + small heads, speedup comes from caching a reused action set, citation is a Notion note; decider 0.8B–35B MoE, 0.8B fell under a constant-answer baseline on a prior long-state check; Kev 0.8B–27B on Qwen3.5/Qwen3.8 with per-checkpoint temperature file; Laya (ModernBERT/mmBERT) base checkpoints are fine-tune bases, not zero-shot engines, under constant-answer baseline on long state, and "Choice labels written as yes/no or true/false are unsafe"; Verdict ~151M, LICENSE Apache-2.0 but GitHub API NOASSERTION; stuntd v0.1 falls back to upstream (possibly paid Jev) when unsure.
- xAI docs: grok-4.20 and newer silently ignore logprobs (relevant to logprob wrappers).

## Key insights / patterns
- Most open "Jev" alternatives reproduce the request shape by reading option/letter logits in one forward pass; raw logprobs are not calibrated ("Just Ask for Calibration") — add temperature scaling / conformal prediction (MAPIE) and measure ECE (net:cal).
- Test open models against a constant-answer baseline on long states — several fail.
- Option-label wording matters (yes/no/true/false labels unsafe in Laya Choice) — echoes "Type-Safe Is Not Error-Free" findings elsewhere.
- NLI zero-shot classifiers cost one forward pass per label; single-pass heads (GLiClass, decision heads) scale better.
- Use the judgment distribution over score tokens rather than greedy digit (LLM-as-a-judge paper).
- Local fallbacks can silently route to paid upstream Jev (stuntd) — check proxy behavior.

## Standout entries
- [Laya](https://github.com/NandhaKishorM/laya) — encoder decision model with Jev-shaped server, CPU-capable (engine)
- [Kev](https://github.com/jaredpalmer/kev) — Qwen-based decision models with temperature files (engine)
- [decider](https://github.com/Mapika/decider) — 0.8B–35B MoE typed decisions (engine)
- [SemIf](https://github.com/TheoLeeCJ/SemIf-OpenJev) — logit readout with shared-state prefill (engine)
- [Ollaya](https://github.com/ollaya-dev/ollaya) — Rust runtime serving open decision models behind TypeSafe-shaped API (runtime)
- [laya-mlx](https://github.com/mizorewww/laya-mlx) — Apple silicon runtime (runtime)
- [Allan Boll's letter-logprob wrapper](http://allanrbo.blogspot.com/2026/09/a-jev-like-wrapper-for-llms-including.html) — minimal logprob-to-decision function (runtime)
- [GLiClass](https://github.com/Knowledgator/GLiClass) — single-pass zero-shot label scorer (classifier)
- [MAPIE](https://github.com/scikit-learn-contrib/MAPIE) — conformal prediction (calibration)
- [net:cal](https://github.com/EFS-OpenSource/calibration-framework) — ECE + temperature scaling (calibration)
- [Jev Decision Index](https://huggingface.co/spaces/multimodalart/jev-decision-index) — catalog of decision-model checkpoints (benchmark)
- [Korean Decision Benchmark](https://github.com/jkf87/korean-decision-benchmark) — SemIf/decider/Laya/Jev on Korean hate speech (benchmark)
- [typed-decisions dataset](https://huggingface.co/datasets/LocalLLaMA/typed-decisions) — synthetic yes/no/choice/score rows, Apache-2.0 (dataset)
- [Balancing Classification and Calibration](https://arxiv.org/abs/2601.13284) — calibration-aware RL for decision tokens (paper)
- [On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599) — temperature scaling source (paper)
