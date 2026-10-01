# andyrewlee/awesome-system-one
- **One-liner:** Tightly curated, category-level "Awesome System One" list covering Jev and competing hosted/open decision models, open implementations, agents, tools, SDKs, baselines, benchmarks, papers and foundations.
- **Language(s):** English
- **Type:** curated-list
- **Scale:** ~157 entries. Contents: Models (Open weights; Hosted); Open Implementations (Trained replicas; Serve any open model); Agents (Screen & device control; Domain agents); Tools (Context & memory; Routing & supervision; Review & verification; Search & data; Train & adapt; Apps & utilities); SDKs & Adapters (Official; Community clients; Frameworks & integrations); Baselines; Benchmarks (Suites & harnesses; Probes & studies); Reading (Docs & ecosystem; Jev under the microscope; Foundations). awesome-lint + link-check workflows.
- **Quality flags:** High quality, selective, dense one-line descriptions with key numbers and caveats; vendor-neutral (treats Jev as one member of the class). Some claims are vendor/author claims (e.g. CLM "Jev parity… up to 9× lower latency"; OpenAI Decisions API details) not independently verified. Appears recent (cites arXiv 2609.29769, 2609.30216). Not promotional.
- **Unique value:** Only list framing System One as a model class with competitors (OpenAI Decisions API, Upstage Solar Decide, Respan Span-01, Hanzo Kai, GLiNER2.5-Decide, Jev-Omni, CLM); classic baselines (fastText, SetFit, semantic-router, RouteLLM, ModernBERT); benchmark datasets (Banking77, CLINC150, MASSIVE, fast-decisions, DecisionBench, Image JevBench, LocalLLaMA/typed-decisions); foundational papers with arXiv IDs; OpenRouter Decisions API.

## Facts claimed about Jev
- "Jev was the first commercial model" of the System One class; TypeSafe named the class after Kahneman's System 1.
- Jev: Choice, Score, Noul over a state in one request, "about 70–500 ms", trained with RLCD; hosted API "$0.042 per million input tokens, output free"; "weights unpublished". Available on OpenRouter (https://openrouter.ai/typesafe/jev-1.13), Vercel AI Gateway, Cloudflare Workers AI, LLMGateway (docs.llmgateway.io/features/system-one).
- Confidence: Choice/Score have a confidence distinct from probability; "Noul has no separate confidence field."
- Choice cap: 255 options (jev-tree does recursive choice over taxonomies to exceed it).
- OpenRouter Decisions API (alpha): Jev, Solar Decide, Span-01, Kev-4B under one `state` + `questions` shape, plus a `/v1/systemone` drop-in for TypeSafe SDK users.
- Official Vercel AI SDK provider `@ai-sdk/typesafe-ai`: Choice, Score, and Boolean (Noul) via `experimental_evaluate`. Vercel `ai-cli` `evaluate` command, `-m jev`. vercel/eve: Jev powers `evaluate` primitive and tool-approval policies.
- Official SDK base URL override: `TYPESAFE_BASE_URL` (decider, jevos served as drop-ins).
- JevBench (fstandhartinger): ~48 systems; "Jev 1.13.0 currently #1". djev ranked 3rd on JevBench v1.2 "just under Jev". Kev-9B "about 3.5 points behind Jev on unseen sources". Nimble (Bespoke Labs) 90% vs Jev 93% on 324-example holdout. GLiNER2.5-Decide claims 60.2% vs "JevK5" 57.6% on Fastino's 17-domain suite (Gerry9000 says 60.1% — minor discrepancy).
- Competitors: OpenAI Decisions API (DevDay 2026 limited preview, text/image + fixed answer set, ~150–230 ms, Luna variant, no pricing); Solar Decide (Upstage, Solar Mini 4, same /v1/systemone schema, 512K context, choice limited to 26 single-token letters); Span-01 (Respan, behavior monitoring; vendor benchmarks ahead of Jev overall, behind GPT-6 Sol per-domain); Hanzo Kai (`api.hanzo.ai/v1/decisions`, OpenRouter Decisions wire); Jev-Omni (Gemma 4 12B multimodal, #1 Image JevBench); CLM (frozen Qwen3-8B + 20M heads).
- jev-codex-router: 7-day replay of 237 turns, ~60% savings vs all-frontier. jevgrep: 8/10 SWE-bench, ~30% lower cost (aliaihub says 25.8% in one rerun). jevmail ~3 cents per 1,000 emails. typesafe-computer-use ~$0.0002/step.
- jev-behavior-study (Jev 1.13.0): option-order bias, lost-in-the-middle in long context. open-alternative-jev: 72% vs 21% on same items with option order flipped (open model, order sensitivity).
- "Jev's Architecture Unmasked" (archerhume.com) is a community teardown of probable architecture; kev is built from it.

## Key insights / patterns
- "The model picks an action. Code runs it." — model chooses, never composes (reticle); text copied from goal not generated (mobile-jev); LLM writes text only for TYPE_TEXT (jev-ultrafast).
- Stop when confidence drops (computer-use-jev); code owns budgets and stop gates.
- Force handling of uncertainty: qualm makes an `unsure` branch a compile-time requirement.
- Context/memory tools: per-block yes/no relevance, stub failures (winnow); leases for memory facts (invalidate).
- Distill Jev into local classifiers (jimothy: Jev as teacher → MiniLM) — cost exit path.
- Threshold routing is data-dependent: Janus finds routing wins on Banking77 but "do not route" on Web of Science.
- Always compare against cheap baselines (SetFit, fastText, semantic-router, GLiNER) and use intent datasets with OOS (CLINC150) for abstention tests.
- Check option-order bias and long-context position effects.
- Community SDKs all launched in week one — check last commit before depending.

## Standout entries
- [System One (docs)](https://docs.typesafe.ai/concepts/system-one) — official class definition (official)
- [@ai-sdk/typesafe-ai](https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai) — official Vercel AI SDK provider (SDK)
- [OpenRouter Decisions API](https://openrouter.ai/docs/api/api-reference/alphadecisions/submit-a-decisions-questions-and-answers-request) — multi-provider decisions endpoint (integration)
- [Solar Decide](https://console.upstage.ai/api/systemone) — Upstage competitor, 512K context (competitor)
- [Span-01](https://openrouter.ai/respan/span-01) — behavior-monitoring decision model (competitor)
- [GLiNER2.5-Decide](https://huggingface.co/fastino/GLiNER2.5-Decide) — open decision specialist (competitor)
- [Jev-Omni](https://huggingface.co/akhilaaa3/Jev-Omni) — multimodal open decision classifier (open model)
- [Tev1](https://github.com/togethercomputer/tev1) — Together AI's "train your own for $17" (open model)
- [JevBench](https://github.com/fstandhartinger/jevbench) — public harness, ~48 systems (benchmark)
- [Image JevBench](https://benchmarkheaven.com/image-jev-bench) — held-out image decisions with contamination tracking (benchmark)
- [fast-decisions dataset](https://huggingface.co/datasets/fastino/fast-decisions) — 17 domains × 300 (benchmark)
- [jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration) — independent OOD calibration test (benchmark)
- [RINNECODER/jev-behavior-study](https://github.com/RINNECODER/jev-behavior-study) — order bias & lost-in-middle study (evaluation)
- [Latent Space: Jev, a System One model that only decides](https://www.latent.space/p/ainews-jev-a-system-one-model-that) — launch writeup (article)
- [Distilling System 2 into System 1 (arXiv:2407.06023)](https://arxiv.org/abs/2407.06023) — closest research framing (paper)
