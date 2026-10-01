# yanng981/awesome-system-one
- **One-liner:** Auto-synced comparison table of 25 "System One" decision models — hosted Jev, Liquid AI d1, and open Jev-compatible reproductions — with size, license and /v1/systemone compatibility.
- **Language(s):** English
- **Type:** auto-generated-list
- **Scale:** 25 models, last checked 2026-09-30. Organized as one table (Model | Maker | Approach | Size | License | Jev API | Links), then per-model "Details", then "Choosing a model".
- **Quality flags:** AUTO-GENERATED every 6 hours by GitHub Action from a JSON feed at laya-ai.com/system-one-models.json. Likely affiliated with / promotional for Laya (Convai Innovations): Guide links point to laya-ai.com, "Jev alternatives" page and submissions go to laya-ai.com. All benchmark numbers self-reported by model authors and "not directly comparable". Calls TypeSafe Jev "Generally available and billed per token" — contradicts other lists' early-access/waitlist framing (possible status change by 09-30, unverified).
- **Unique value:** Only focused comparison of open/alternative System One models, including which serve a drop-in `POST /v1/systemone` compatible with TypeSafe SDKs; sizes and licenses; a competing hosted provider (Liquid AI d1). Useful "Choosing a model" guidance.

## Facts claimed about Jev
- TypeSafe named the category with Jev on September 15, 2026; hosted only on TypeSafe cloud; size undisclosed; proprietary; "Generally available and billed per token" (contradiction flag vs early access claims elsewhere).
- Liquid AI d1: released September 29, 2026, free tier (`d1:free`), paid pricing unpublished; serves `POST /decisions/v1/systemone`, works with TypeSafe SDKs; AlphaSignal reports it took first place on the "Jev Decision Index" on Hugging Face ahead of Jev 1.13.
- Self-reported comparisons vs Jev (inconsistent Jev baselines across projects): OpenDecider nano 0.796 vs Laya 0.766 vs Jev 0.754 on "typed-decisions benchmark"; Rizzo Flow 0.648 vs Jev 0.727; Anarkali (68M) 74.0% vs Jev 72.7%; Jeeves 0.935 vs Jev 0.866 on public JevBench items (hard tier 0.865 vs 0.730), Jev leads on MMLU-Pro; Jev-Omni 86.15% on matched JevBench groups.
- Open-model specs: Laya 322M/421M ModernBERT/mmBERT encoders, Apache 2.0, 100+ language checkpoint; Kev 0.8B/4B/9B/27B on Qwen3.5/3.8 with fitted temperature, "TypeSafe SDK works unchanged"; Decider 2B/4B/35B MoE, Choice 2 to 255 options; Von 395M ModernBERT-Large, v1.2 order-invariant; Bespoke Nimble 9B, 8,192-token inputs, 255 choices/field; Together AI Tev1-4B-experimental (Sept 23, 2026); Fastino GLiNER2.5-Decide 340M; PostHog Jeeves 9B (~0.3 s, 3.3 s with thinking on H100); Anarkali 68M; OpenJev-4B trained on OpenJevData-140k; JevK5 reads >16 options in several passes.

## Key insights / patterns
- Drop-in replacement path: choose a model serving `POST /v1/systemone` to swap without client code changes (Kev, Decider, Von, Rizzo Flow, djev, Open-Jev, Anarkali, Jeeves, OpenJev-4B, Liquid d1).
- CPU-only/low latency: encoder models (Laya, Von, GLiNER2.5-Decide). Highest accuracy with GPU: large fine-tuned LLMs (Kev-27B, Decider 35B MoE).
- Architectural approaches: trained encoders with decision heads (non-autoregressive), fine-tuned LLMs with letter/slot readout, training-free readouts of option probabilities from frozen LLMs (SemIf, AnyJev hidden states, djev diffusion).
- Order invariance is a design goal for several open models (Von 1.2, OpenJev-4B, AgentJev) — echoes option-order sensitivity found in Jev.
- Calibrate on your own data; many open models ship uncalibrated probabilities (Rizzo Flow) or a single fitted temperature.
- Always test on your own labelled data before switching production traffic.

## Standout entries
- [TypeSafe Jev docs](https://docs.typesafe.ai/introduction) — reference hosted model (official)
- [Liquid AI d1](https://docs.liquid.ai/lfm/models/decision-models) — competing hosted decision model, SDK-compatible (hosted alternative)
- [Laya](https://github.com/NandhaKishorM/laya) — open encoder decision model (open model)
- [Kev](https://github.com/jaredpalmer/kev) — fine-tuned Qwen Jev-like models 0.8B-27B (open model)
- [Decider](https://github.com/Mapika/decider) — calibrated one-pass decisions, /v1/systemone (open model)
- [Von](https://github.com/wfzyx/von) — order-invariant 395M encoder (open model)
- [Bespoke Nimble](https://github.com/bespokelabsai/nimble) — training recipe and data curation (open model)
- [SemIf (formerly OpenJev)](https://github.com/TheoLeeCJ/SemIf-OpenJev) — training-free option-probability readout (open model)
- [AnyJev](https://github.com/nokia-applied-research/AnyJev) — hidden-state decisions over any LLM (open model)
- [Tev1-4B-experimental](https://huggingface.co/togethercomputer/Tev1-4B-experimental) — Together AI decision fine-tune (open model)
- [GLiNER2.5-Decide](https://huggingface.co/fastino/GLiNER2.5-Decide) — encoder classifier with runtime labels (open model)
- [Jeeves](https://github.com/PostHog/jeeves) — PostHog reasoning-before-deciding model (open model)
- [OpenJev-4B](https://github.com/ejhshen/OpenJev) — SFT+RL on OpenJevData-140k, training code (open model)
- [System One models comparison](https://laya-ai.com/system-one-models) — upstream data source (directory)
