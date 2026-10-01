# Zhao-Tian-yi/awesome-jev
- **One-liner:** Research-grade, evidence-audited map of open Jev/System One reimplementations (architecture, readout, training/RL, weights), with taxonomy, evaluation protocol and papers.
- **Language(s):** English, Simplified Chinese, Japanese (parallel READMEs; data YAML carries en/zh/ja notes)
- **Type:** papers-list / tutorial/study-guide hybrid — best described as a research landscape of open models (curated-list of implementations)
- **Scale:** Model Landscape table: 1 official + ~32 community implementations (columns: GitHub Stars, First Public, Backbone/Size, Decision Architecture, Training/RL, Artifacts, Evidence). Sections: Model Landscape; Find by goal; Official resources and tools; Awesome Awesome Jev (list of lists). docs/: architecture, comparison (full technical table), evidence (per-project source records), audit, training (RLCD/RLCR), evaluation (protocol), multimodal (image/video/audio/grounding), jev-vs-models, updates. data/papers.yaml: 10 papers.
- **Quality flags:** Exceptionally careful and candid. Explicit audit record (2026-09-21) listing corrections to its own earlier errors; per-field evidence levels; refuses to invent first-public dates ("All 22 core first-public dates are Unknown"). No benchmarks re-run and no live Jev calls — states this openly. Small star count (1). Not stale (metadata 2026-09-28). Uses TheoLeeCJ/SemIf (older name; KuzanJ notes rename to SemIf-OpenJev).
- **Unique value:** Only list that dissects *how* clones work along three axes (backbone / readout / execution schedule), distinguishes real RL from calibration losses mislabeled "RLCD", catalogs multimodal Jev-style models, provides an evaluation reporting protocol, and lists arXiv papers including Jev-specific ones.

## Facts claimed about Jev
- Official Jev: backbone, size, architecture "Not disclosed"; RL "RLCD" is vendor terminology; API only; no weights. RLCD = "Reinforcement Learning for Calibrated Decisions" (per launch material; the audit could not retrieve the launch page live).
- "No reviewed primary source establishes that Jev uses diffusion, LLaDA, a particular pointer head, or one total forward." "One API request may contain several server-side model invocations." Earlier "32k/64k architectural deductions require fresh primary documentation verification and are not facts in this catalogue." (Contrasts with other lists stating 64k/32k limits as facts.)
- Official skill (typesafe-ai/skills SKILL.md) describes independent parallel questions, typed outputs, dynamic options, no text generation; "typed output guarantees the interface, not truth."
- Official tools: typesafe-sdk-python (client and API schemas), typesafe-sdk-js, system-one-adapter-python (ordinary LLM APIs behind a System One comparison interface), skills.
- TypeSafe evaluations site `evals.typesafe.ai` exists (protocol not verified).
- Papers (arXiv v1 dates): Visual Jev 2609.25845 (2026-09-22); From Text Decisions to Pixels: A Study of Jev-Style Visual Choice Model 2609.29283 (2026-09-24); Jev-Mobile: Jev as an Executor for Mobile GUI Agents 2609.30186 (2026-09-24); Jev in the Wild 2609.30216 (2026-09-24). Background: On Calibration 1706.04599; BERT 1810.04805; MDLM 2406.07524; LLaDA 2502.09992; Beyond Binary Rewards (RLCR) 2507.16806; GLiClass 2508.07662.
- Awesome-awesome: OmniJev/awesome-jev-gallery (466★), yibie/awesome-jev (1,852★), AnotiaWang/awesome-jev (513★), hellogumbo/awesome-jev (201★).

## Key insights / patterns
- Describe any implementation on three independent axes: backbone (causal, hybrid, encoder, masked diffusion), readout (label-token logits, pointer head, option scorer, masked answer slots), schedule (individual forwards, batched rows, shared-prefix branches, native slots). "Does not generate text" identifies none of these.
- Implemented patterns: direct AR-logit readout (SemIf: prefill prefix, duplicate cache, batch suffixes); trained pointer/decision heads (Kev; Qwen3.5 DeltaNet recurrent layers can't be isolated by attention mask alone); option-wise scalar scorers (JevForge, jevlike); encoder option markers (Laya, Von, Verdict/GLiClass); diffusion answer slots (DiffusionGemma OpenJev).
- Many "RLCD" community claims are really CE/Brier losses + temperature scaling; true RL examples: decider 2B v10 (PPO + log-score belief term), eve-rlcd (REINFORCE reward correct − p(action)), Laya (Gaussian-logit policy gradient + soft CE, temperature fit on training items — not held-out).
- Probability semantics: Choice softmax is conditional on the supplied menu (can put mass on a wrong/incomplete set → need coverage/abstention); option margin/entropy ≠ P(correct); Score expected level ≠ most-likely label; a model writing "0.82" as text ≠ native readout; neither is automatically calibrated.
- "Zero output tokens" need not mean zero compute; billing may count scored candidate tokens.
- Evaluation protocol: accuracy/macro-F1/AUROC; NLL/Brier/ECE/reliability; risk-coverage/AURC; unseen questions/options/domains split by source; option permutation/paraphrase robustness; high cardinality (2…255 options); p50/p95 with hardware details; packed vs separate parallel semantics. Don't mix in-domain specialized results with zero-shot comparisons; a 400-token explanation is not a fair latency comparator.
- Multimodal clones (Valen, OmniJev, Jev-Omni, Visual Jev, GroundingJev, Jev-Spatial) extend the interface beyond hosted Jev's text-only input.

## Standout entries
- [typesafe-ai/skills SKILL.md](https://github.com/typesafe-ai/skills/blob/main/skills/typesafe-ai/SKILL.md) — official design guidance, primary source (official)
- [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) — LLM-backed comparison interface (official)
- [SemIf METHOD.md](https://github.com/TheoLeeCJ/SemIf/blob/master/docs/METHOD.md) — generation-free causal-model readout (open model)
- [Kev](https://github.com/jaredpalmer/kev) — pointer-head decision models (open model)
- [decider](https://github.com/Mapika/decider) — Qwen3.5 family incl. MoE, PPO + belief-scoring (open model)
- [Laya](https://github.com/NandhaKishorM/laya) — encoder-based typed decisions (open model)
- [OpenJev / DiffusionGemma](https://github.com/razorback16/openjev) — masked diffusion answer slots (open model)
- [eve-rlcd](https://github.com/anthony-maio/eve-rlcd) — calibration RL experiments + dataset (training)
- [NanoJev RLCD experiment](https://github.com/TianyuCodings/NanoJev/blob/618cea6d906d54e128360786d12f703fff2b1245/docs/RLCD_EXPERIMENT.md) — sampled Brier-gradient study (training)
- [mini-Jev](https://github.com/r-ms/mini-jev) — preregistered readout vs constrained generation (evaluation)
- [Valen](https://github.com/Liuziyu77/Valen) — multimodal text/image/video decision model (multimodal)
- [Visual Jev (arXiv 2609.25845)](https://arxiv.org/abs/2609.25845) — decisions from shared visual context (paper)
- [Jev-Mobile (arXiv 2609.30186)](https://arxiv.org/abs/2609.30186) — Jev as executor for mobile GUI agents (paper)
- [Jev in the Wild (arXiv 2609.30216)](https://arxiv.org/abs/2609.30216) — ecosystem analysis (paper)
- [Beyond Binary Rewards / RLCR (arXiv 2507.16806)](https://arxiv.org/abs/2507.16806) — calibration-aware RL background (paper)
