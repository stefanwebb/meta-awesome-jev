# sfmqrb/awesome-decision-models
- **One-liner:** Clean, vendor-neutral "Awesome Decision Models" list covering Jev plus the open Laya/Kev/SemIf ecosystem: weights, runtimes, SDKs, integrations, research code, benchmarks, papers, articles.
- **Language(s):** English
- **Type:** curated-list
- **Scale:** ~190 entries. Sections: Official (Jev/TypeSafe hosted; Laya/Convai Innovations open source); Open models and weights (~22); Runtimes, ports and servers (~22); SDKs and libraries (12); Integrations and plugins (Coding agents; Browser and computer use; MCP servers); Tools and CLIs (16); Apps, demos and games (14); Robotics and simulation (4); Training and research code (10); Benchmarks and datasets (8); Papers (4); Articles and tutorials (16); Discussions (2); Related lists (4). Plus docs/what-is-a-decision-model.md explainer with example request/response. Link-check workflow.
- **Quality flags:** High quality, concise, awesome-lint style, no hype numbers. Treats Laya as a co-equal "official" project (reflects Laya's prominence). Maintainer lists own tool (sfmqrb/gutcheck) — minor self-listing. Recent (cites arXiv 2609.28940, marktechpost 2026-09-23).
- **Unique value:** Best coverage of the Laya ecosystem (HF checkpoints, PyPI, ports to MLX/CoreML/C++/ONNX/GGUF/browser/Jolt); non-Jev open models (Eikos finance, OpenThai-SystemOne, dev-0.4b, Blink C runtime, JevK5); two Jev application papers not seen elsewhere (arXiv:2609.24052 crash narratives; arXiv:2609.28940 pentest harnesses); mainstream article coverage (LangChain, DataCamp, Tom's Hardware, marktechpost, Latent Space "6 clones in 2 days"); vendor-neutral definition of "decision model" / "semantic ifs".

## Facts claimed about Jev
- Decision models are "also called System One models, typed decision models, or 'semantic ifs'"; three de facto question types: `noul` (yes/no probability), `choice` (pick one of N labels), `score` (ordered rubric). Response in "tens of milliseconds, zero output tokens" (explainer; note vendor says 70–500 ms E2E).
- Example wire format: `{state, questions:{name:{type:"choice", criteria:{...}}, name2:{type:"noul", instructions:"..."}}}` → `{answers:{name:{choice, probabilities}, name2:{noul}}}` — consistent with /v1/systemone per other lists.
- Official: launch post "introduced the System One model category"; typesafe-sdk-python, typesafe-sdk-js, skills, system-one-adapter-python ("answers System One calls with regular LLM APIs").
- Laya (Convai Innovations): `pip install laya`, multilingual checkpoint "100+ languages with up to 8k context", laya-typed-decisions fine-tune; laya-server "compatible with the Jev API format".
- Kev: Qwen3.5/3.8 "0.8B to 27B" with Jev-compatible server (other lists give 0.8B/4B/9B or 0.6B/4B/8B — inconsistent across lists).
- Tev1 fine-tuned on Qwen3.5 4B; Open-Jev (Zefan-Cai) 27B; Verdict 151M ModernBERT; AgentJev 0.6B.
- Tom's Hardware headline: "claims to be 193x faster and 445x cheaper".
- "Jev's Architecture Unmasked" (archerhume.com) = reverse-engineered architecture Kev builds on.

## Key insights / patterns
- Decision models sit beside a slower LLM as fast "System 1": routing, triage, guardrails, picking next browser action, deciding what to keep in agent context.
- Answers can never fall outside declared options (schema guarantee) — correctness still separate.
- Local/open path is mature: Laya + many runtimes enable on-device / offline decisions (Apple Neural Engine, CPU INT8, browser), and many ports expose Jev-compatible APIs so apps can switch hosted↔local (laya-ultrafast = jev-ultrafast on local Laya).
- Caching repeated decisions (JevCache) and calibration/drift checks (jevcal) are production concerns.
- GEPA-based optimization of Jev harnesses/functions (JevHarness, jev-align) is an emerging pattern.
- Preregistered/logit-reading experiments on frozen models (mini-jev) show interface can be replicated cheaply.

## Standout entries
- [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — launch post (official)
- [Laya](https://github.com/NandhaKishorM/laya) — open multilingual non-autoregressive decision engine (open model)
- [convaiinnovations/laya-multilingual](https://huggingface.co/convaiinnovations/laya-multilingual) — 100+ languages, 8k context (weights)
- [Kev](https://github.com/jaredpalmer/kev) — Jev-like family with training code (open model)
- [Tev1](https://github.com/togethercomputer/tev1) — Together AI open-weight model (open model)
- [JevCache](https://github.com/hyperspaceai/jevcache) — memoize repeated decisions (tool)
- [building-with-jev-skill](https://github.com/dbreunig/building-with-jev-skill) — agent skill for writing Jev programs (skill)
- [typed-decisions dataset](https://huggingface.co/datasets/LocalLLaMA/typed-decisions) — shared benchmark (dataset)
- [JevPokerBench](https://github.com/Prophetlab/JevPokerBench) — poker leaderboard for decision models (benchmark)
- [AIM-Decision](https://aimultiple.com/decision-models) — independent Jev/Kev/LLM comparison (benchmark)
- [Calibrated Decisions at Scale (arXiv:2609.24052)](https://arxiv.org/abs/2609.24052) — Jev on police crash narratives (paper)
- [Calibrated Decision Models for Autonomous Penetration-Testing Harnesses (arXiv:2609.28940)](https://arxiv.org/abs/2609.28940) — Jev/Laya in pentest agents (paper)
- [Building a harness with Jev (LangChain)](https://www.langchain.com/blog/building-a-harness-with-jev) — tutorial (article)
- [A Coding Guide to TypeSafe AI Jev (marktechpost)](https://www.marktechpost.com/2026/09/23/a-coding-guide-to-typesafe-ai-jev/) — code tutorial (tutorial)
- [Latent Space: 6 Clones of Jev in 2 days](https://www.latent.space/p/ainews-here-are-6-clones-of-jev-in) — open-clone roundup (article)
