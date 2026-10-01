# Anil-matcha/awesome-jev-by-typesafe
- **One-liner:** Evidence-backed practical guide to Jev: quick facts, primitives, 31 use-case recipes, community implementations, benchmarks, safety checklist and runnable Python/TS starter code.
- **Language(s):** English
- **Type:** tutorial/study-guide (hybrid with curated-list)
- **Scale:** README ~74KB: 31 numbered use cases (Workflow control; Retrieval and knowledge; Safety and quality; Data and operations; Real-time and agentic systems; Recent workflow evaluations and cookbook patterns), "Additional industry use cases", ~40 "Recent independent implementations", "Curated ecosystem additions", ~11 "Benchmarks, calibration, and open reproductions", official references (~20). Plus docs/jev-use-case-playbook.md (776 lines), docs/coding-agent-use-cases.md (303 lines), examples/python (quickstart, workflows, decision_policies) and examples/typescript, offline unit tests.
- **Quality flags:** Snapshot reviewed September 19, 2026. Well sourced (each fact linked to a docs page). Some self-promotion: YouTube video, sibling repos by same author (awesome-gpt-6-astra, open-business-agents, etc.), BTK audit study link. Not auto-generated. No independent measurements of its own.
- **Unique value:** Best single "quick facts" table in batch with docs citations (context, data handling, language guidance, calibration guidance); design pattern table; production decision-loop diagram; safety/reliability checklist; workflow-eval-derived reference architectures (security incidents, invoice matching, expense claims, insurance triage); coding-agent harness patterns doc; runnable starter code with offline-tested policy functions; pointers to other lists/directories.

## Facts claimed about Jev
- Jev: "TypeSafe's flagship and first System One model". Alias `jev-latest`; current version `jev-1.13.0`; `jev-latest` and `jev-preview` resolve to versioned releases, aliases can move (docs/models).
- Endpoint `POST https://api.typesafe.ai/v1/systemone`. Input: string, JSON object, or array of text values (concepts/state).
- Output: Choice -> `choice`, probability per option, `confidence`; Score -> `score` (probability-weighted, may land between levels), `legend`, `probabilities`, `confidence`; Noul -> `noul` 0-1 (0.5 = uncertain, not medium).
- Price $0.042 / 1M input tokens, output free. Limits 250,000 tokens/second and 1,200 requests/minute, can change dynamically. Context 64k tokens per request; 32k for state plus longest question.
- Guidance from docs: pin versioned model ID when thresholds depend on behaviour and log returned version; English is primary language — test non-English workloads; customer requests/responses not used for training (check enterprise retention for ZDR); text only (no images/audio/video); early access at launch via console.typesafe.ai.
- Launch post: 70-500 ms end-to-end; "roughly two orders of magnitude faster and more efficient" for System One tasks (vendor-reported).
- Access paths: official API/SDKs; Vercel AI Gateway `typesafe-ai/jev`; Cloudflare Workers AI `typesafe/jev`; typesafe-ai/system-one-adapter-python (System One-shaped adapter backed by OpenAI, Anthropic or OpenAI-compatible models; not a substitute for Jev calibration); official agent skill (docs.typesafe.ai/agent-skill). Also mentions OpenRouter's "TypeSafe-compatible endpoint" (jev-fanout-bench) and users bringing an OpenRouter key (jev-slop-guard).
- SDK retries on 429 and 529 by default.
- Community numbers: Paper Radar 501 papers for $0.0196; BTK SEO audit 1,204 pages, 4,816 typed judgments per run, $0.0048 per 12-query batch.
- Jevals.com: hosted Jev via Vercel + six LLMs, PubMedQA (Noul), Banking77 (Choice), HelpSteer2 (Score), 300 items x 5 runs; data public, harness not.

## Key insights / patterns
- Pattern table: Atomic questions; Speculative fan-out (ask every likely-needed question in one call, ignore irrelevant answers); Confidence-gated routing (answer and confidence as separate axes); Composite scoring (normalize Scores, explicit weights); Intent routing (deterministic code vs specialist LLM vs human); Two-stage dependency (second call only when first answer changes state/options).
- Rule: "questions describe judgments; code owns composition, thresholds, and side effects."
- Always include `other`/`none_of_the_above`/`review` options when set may be incomplete.
- Per-action, per-risk thresholds (no global threshold); low confidence is a first-class branch.
- Version state schemas, instructions, criteria and policy code together; store full distributions for audit/calibration.
- Side effects as explicit second step after inspection/approval.
- Decision loop: Inspect -> Evaluate -> Compose -> Gate -> Record -> Calibrate.
- Workflow-eval architecture (security incidents): join alert with context; ask unauthorized?/explained by existing record?/evidence strength; deterministic playbook chooses close/queue/notify/contain; deeper questions only after first gate.
- Coding agents: skill/tool selection, command safety (allow/ask/block + irreversibility/exfiltration Nouls — also in learn-jev-end-to-end course), repo context selection, diff verification/semantic CI, model cascades, citation checks.
- QuantDinger: blocks entries but bypasses exits/protective orders; fallback to LLM or fail-open audited path if Jev unavailable.
- What Jev is not: chatbot, generator, correctness guarantee (calibration is about groups), authorization replacement.
- Benchmark hygiene: record versioned model, question definitions, dataset, baseline, metric, ambiguous/OOD behavior; distinguish Jev vs adapter vs open reproduction.

## Standout entries
- [Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — launch post (official)
- [Models, aliases, prices, and limits](https://docs.typesafe.ai/models) — official specs (official)
- [State](https://docs.typesafe.ai/concepts/state) — packaging state (official docs)
- [Confidence](https://docs.typesafe.ai/confidence) — confidence routing (official docs)
- [Workflow evaluations](https://evals.typesafe.ai/) — official workflow evals incl. security_incidents, invoice_processing, customer_service, agent_trace_observability (benchmark)
- [System One adapter for Python](https://github.com/typesafe-ai/system-one-adapter-python) — LLM-backed System One-shaped adapter (official tool)
- [Official agent skill guide](https://docs.typesafe.ai/agent-skill) — Jev in coding agents (official)
- [Learn Jev end to end](https://github.com/harshithsunku/learn-jev-end-to-end) — 12 Python notebooks course (tutorial)
- [Jevals.com](https://jevals.com/) — independent ground-truth benchmark, data in Jevals/jevals-data (benchmark)
- [DecisionBench](https://github.com/Hanno-Labs/decision-bench) — open decision-model eval runner with Jev adapter (benchmark)
- [Bosun v3.1](https://huggingface.co/Hanno-Labs/bosun-v3.1-1.7b) — Apache-2.0 open decision model 0.6B/1.7B (open model)
- [When a Judgment Layer's Self-Reported Fields Lie](https://doi.org/10.5281/zenodo.22901853) — independent calibration/cost paper (research)
- [jev-fanout-bench](https://github.com/blowxian/jev-fanout-bench) — billing/batching via OpenRouter route (benchmark)
- [Paper Radar](https://github.com/Eliot5566/JEV-Paper-Radar) — daily arXiv radar with Noul per interest, calibrate command (application)
- [Awesome Jev directory](https://awesomejev.com/) — searchable daily-refreshed directory (directory)
