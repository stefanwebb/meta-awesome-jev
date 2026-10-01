# ham-zax/awesome-jev
- **One-liner:** Strict, hand-curated awesome list (downstream of yibie/awesome-jev) organizing ~350 Jev projects, evaluations and write-ups by decision pattern and application domain.
- **Language(s):** English (entries link to some Chinese/Japanese X posts)
- **Type:** curated-list
- **Scale:** ~350 one-sentence entries in 15 category files, rendered into a collapsible README by scripts/build-readme.py. Groups: USE CASES → Decision Patterns (Classification & Routing 23, Verification & Guardrails 22, Scoring & Ranking 28, Agent Action Control 18, Data Labeling & Curation 7) and Application Domains (Adaptive/Realtime UI 11, Games/Robotics/Simulation 19, Finance/Trading 5, Legal/Compliance 1, Content Filtering/Moderation 6, Scientific Workflows 1); SDKs & Integrations/Infrastructure 55; Research & Evaluation (Calibration & Model Research 30, Evaluation & Benchmarks 24); Guides, Analysis & Community 79 (tutorials, critique, demos, launch signals, directories).
- **Quality flags:** Badge says "upstream yibie/awesome-jev" — likely a fork/derivative, so overlap with yibie is expected. Hand-written, concrete one-sentence descriptions; explicit "inclusion is not endorsement". Includes many X/Reddit posts (ephemeral). Maintained with an agent skill (.agents/skills/jev-curation) — AI-assisted curation. Not auto-dumped; low spam.
- **Unique value:** Pattern-first taxonomy (what Jev decides), a strong "Technical analysis & critique" section with skeptical takes, and a calibration-studies subsection (ECE, pre-registered audits). Good coverage of verification/guardrail tools for coding agents.

## Facts claimed about Jev
- Jev "turns unstructured state plus a typed question into a typed decision with confidence."
- Curation skill says primitives are `Choice`, `Score`, `Boolean`, "each with confidence" — **contradicts** other sources (Promethe-us) that the native binary primitive is `Noul` and has no separate confidence; entries in the list itself use "Noul" (e.g. "Ask HN: What do you think of Noul").
- Jev 1.13 jaggedness page: https://docs.typesafe.ai/model-jaggedness/jev-1.13.
- Availability: waitlist removed (x.com/typesafeai/status/2101786156572823624), then signups **paused** after GA (x.com/typesafeai/status/2102281508950307159); Cloudflare Workers AI as `typesafe/jev`; OpenRouter; Cloudflare AI Gateway.
- Founder Diogo Almeida (launch thread by @CompleteSkeptic); RLCD training; video "Why I couldn't build Jev at OpenAI."
- Third-party numbers: r6i blog — replacing agentic classification loop with one Jev call, 7× speedup; hermes-jev-approvals — 8.7× faster decisions, 4.4× fewer user prompts; CUA-S1-FORMS 99.7% vs Jev 83.6% on its form-filling eval; von sub-15 ms, 395M params; minojev 547k params; openJev-verdict-2.0 151M claims to beat Jev and Laya; Jev vs GPT-4.1 synthetic survey over 24,596 cells (Noul-vs-Choice framing mattered more than model swap); "One 50 ms pass versus 23 turns"; X index reporting >5,380 Jev-related posts; Reddit review of 287 open-source Jev projects.
- Reddit critique: calibration claims lack published ECE/reliability curves.
- Community hypotheses: speed is an inference-interface effect (one prefill + parallel answer scoring) reproducible on open weights.

## Key insights / patterns
- Inclusion rule defines a Jev loop: typed question → typed answer + confidence → accept / reject / escalate. Rejects generic classifiers/routers/LLM judges.
- Routing: one Jev call selecting model + thinking level while deterministic rules handle pinned/disabled routes (Jevonian); preserve prompt cache when switching (jcm-router); decline weak matches instead of forcing choice (skill router).
- Guardrails: deterministic rules first, then typed Jev check on remaining tool calls (jev-engineering, 300-call injection eval); screen both tool calls and tool results (Agent Chaperone); Stop-hook completion checks (limpet); pre-commit secret/destructive-command screening (jev-git); two-pass malware screening with escalation (is-malicious).
- Include an explicit `Unresolved`/`other` option to trigger clarification (TryJevAI).
- Hysteresis thresholds, decision journaling/replay (huncho).
- Critique: context compaction via relevance filtering loses reconstruction (theo); early negative results for RAG reranking; Jev "can't see" — only textual descriptions of images; skeptical about knowledge-heavy tasks.
- Language calibration matters: pre-registered Spanish audit (jev-acento) of ECE effects.

## Standout entries
- [Jev Tutorial](https://www.jev-tutorial.org/) — multilingual guide to primitives, thresholds, fallbacks (tutorial)
- [Search with Jev and Milvus](https://github.com/milvus-io/bootcamp/tree/master/bootcamp/RAG/search_with_jev) — nine notebooks: ranking, filtering, routing, stopping (tutorial)
- [Building a Harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev) — LangChain harness integration (guide)
- [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13) — official limitations (official)
- [jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration) — ECE + temperature refit on 900 tickets + 3 benchmarks (calibration)
- [ASSAY-001](https://github.com/jourdanlabs/assay-001) — pre-registered Banking77/CLINC150 calibration check (calibration)
- [jev-acento](https://github.com/marcosmartinez/jev-acento) — 3,200-item Spanish calibration audit (calibration)
- [jevcal](https://github.com/abhixhek/jevcal) — threshold fitting + CI regression check (tool)
- [DeepSearcher stopping-policy experiment](https://github.com/zilliztech/deep-searcher/blob/master/evaluation/jev_stopping/README.md) — Noul stopping policy for agentic search (benchmark)
- [Jevals.com](https://jevals.com/) — Jev vs six LLMs on human-labeled data (benchmark)
- [jev-engineering](https://github.com/eugeniughelbur/jev-engineering) — rules-then-Jev tool-call gating with 300-call injection eval (security)
- [Agent Chaperone](https://github.com/agent-chaperone/agent-chaperone) — MCP-proxy screening of tool calls/results (security)
- [fx](https://github.com/vercel-labs/fx) — Vercel Labs `typesafe_permission_reviewer` (integration)
- [CUA-S1-FORMS](https://huggingface.co/cua-ai/cua-s1-forms) — specialist computer-use model vs Jev (alternative)
- [jev-experiments](https://github.com/dabit3/jev-experiments) — 22 latency-focused demos (demos)
