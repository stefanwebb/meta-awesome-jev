# v-modal/awesome-jev-tools
- **One-liner:** Strict, pattern-organized curated list (~226 entries) of public projects and practices using Jev, categorized by decision type, with an explicit "curation is not endorsement" checklist.
- **Language(s):** English (links to some Chinese/Japanese posts)
- **Type:** curated-list
- **Scale:** ~226 entries in 13 active categories (+1 empty): Classification & Routing (20), Verification & Guardrails (20), Scoring & Ranking (17), Agent Decisions (30), Data Labeling & Curation (2), Evaluation & Benchmarking (13), Calibration & Research (21), Infra / SDKs / Integrations (37), Game & Simulation (8), Finance & Trading (3), Compliance & Legal (1), Content Moderation (4), Related Practices / Discussions (50); Scientific Pipelines (0). README aggregates `categories/*.md` (category files not present in this clone — only README.md and a curation skill in .github/workflows/curation_skills.md).
- **Quality flags:** Good-quality one-line descriptions prefixed with industry; strips unverifiable numbers (states so). Explicit warning that bulk same-day repos from one author with shared scaffolds (AGENTS.md, CLAUDE.md, STATE.md) are "unproven". Minor formatting sloppiness at top (duplicated intro paragraph, run-together "Goal of this ListMost…"). Maintained with an AI "jev-curation" skill. Clone is incomplete (category files, CONTRIBUTING.md, scripts/build-readme.py referenced but missing).
- **Unique value:** Organization by *decision pattern* (routing vs verification/guardrail vs scoring vs agent decisions) rather than by industry; the strongest collection of **coding-agent guardrail/permission-gate** projects; a well-annotated "Related Practices / Discussions" section capturing notable community arguments (Theo's compaction critique, "it's the inference technique, not the training", architecture inference from ~10,000 API calls).

## Facts claimed about Jev
- Jev "is not a chat model"; takes unstructured state + typed question, returns a typed decision — "a choice, a score, or a boolean" — with a confidence rating; no token-by-token decoding. (Curation skill names primitives `Choice`, `Score`, `Boolean`, each with confidence — note: officially the third primitive is Noul and has no confidence field; this list conflates.)
- HN launch thread "1,800-point", ~480 comments; founder Diogo Almeida launch thread "63k-like" (other lists report 75k likes — snapshot differences).
- OpenRouter shipped Jev "in beta"; Cloudflare AI Gateway live, callable from Workers; Vercel eve ships Jev as default evaluation model (`typesafe-ai/jev`) in experimental evaluate path; fx ships a `typesafe_permission_reviewer` builtin.
- WebJev serves `POST /v1/systemone` and `/api/alpha/decisions` routes (the latter apparently mirrors OpenRouter's decisions API).
- Community claims: Notra targets 300 ms p50 with Boolean decisions at 0.5 threshold; hermes-jev-approvals 8.7x faster decisions, 4.4x fewer user prompts; WebMCP benchmark author: Jev + fast small LLM solved 100% of WebMCP tasks at ~112x lower model cost than frontier computer use; DuckDB extension ~10 s per 1,000 rows; CUA-S1-FORMS 706,048-parameter scorer fills a form in one 50 ms pass vs LLM agent 23 turns / 39.6 s; Laya ~35 ms per forward pass; Von 395M, under 15 ms; Abide: independent reviewer confirmed 10 of 39 flagged edits.
- Reranking: "Jev reranking alone did not beat vector retrieval" (33,047 entries, 164 queries, 9,831 graded pairs).
- Jev in the Wild (arXiv 2609.30216): 2,170 public GitHub projects surveyed.

## Key insights / patterns
- Guardrail design converges on: deterministic rules first, then one typed Jev call for the gray zone (pi-verdict: allow/ask/deny Choice; jev-engineering: rules + Jev with 300-call injection test; jev-axi scores destructiveness, exfiltration, RCE, security weakening; is-malicious escalates suspicious chunks for a second pass).
- Pre-commit/pre-push gates: secrets, destructive commands, commit-message/diff mismatch (jev-git, jev-commit — blocks only on detected credential).
- Rules-as-plain-English linting (Hunch, jev-pref from AGENTS.md, Sniff Test with ten Boolean questions per paragraph at 0.7 threshold, Clean Code Judge 31 boolean smells → writing model composes prose).
- Routing: pick model + reasoning effort per turn; pin choice across follow-ups to avoid prompt-cache disruption (Switchboard); decline weak skill matches rather than guess.
- Calibration tooling: fit per-question thresholds to a target accuracy, verify on held-out split, report escalation rate, fail CI on drift (jevcal).
- Specialist tiny System One models (CUA-S1, jevlike-esp32 on microcontrollers) are a distinct trend.
- Skeptic views: Jev "looks like a faster general classifier an LLM could already do"; speed attributed to parallel decoding rather than training; compaction is reconstruction not filtering.
- Adoption signal: X heavy, Reddit light early on.

## Standout entries
- [fx](https://github.com/vercel-labs/fx) — Vercel coding agent with Jev permission reviewer (verification & guardrails)
- [pi-verdict](https://github.com/jesset/pi-verdict) — rules-first, Jev allow/ask/deny gate (guardrails)
- [jev-engineering](https://github.com/eugeniughelbur/jev-engineering) — tool-call gate with rerunnable 300-call injection test (guardrails)
- [jev-axi](https://github.com/shiftynick/jev-axi) — PreToolUse risk scoring for shell commands (guardrails)
- [Switchboard](https://github.com/ruban-24/switchboard) — cache-aware model/effort routing (routing)
- [Notra](https://github.com/usenotra/notra) — production GEO platform using Jev Boolean classifiers (classification)
- [jevcal](https://github.com/abhixhek/jevcal) — threshold fitting with CI drift checks (evaluation)
- [jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration) — OOD calibration test with raw responses (evaluation)
- [Odin R&D: Jev vs open-weight Laya](https://github.com/odin-labs-ai/odin-rnd/tree/main/experiments/laya-vs-jev) — hosted vs open comparison (evaluation)
- [Jev judge call vs dimension scores](https://agentjournal.dev/blog/llm-judge-vs-feature-extraction/) — single question vs weighted dimensions (evaluation)
- [WebJev](https://github.com/lexmount/WebJev) — open-weight browser-agent decision model with compatible routes (research)
- [CUA-S1-FORMS](https://huggingface.co/cua-ai/cua-s1-forms) — 2.8 MB specialist form-filling scorer (research)
- [jev-local](https://github.com/us/jev-local) — SDK drop-in local server with temperature-fit calibration (research)
- [It is the inference technique, not the training](https://x.com/anderslie/status/2100388704644919662) — technical debate (discussion)
- [深入解读 Jev 模型](https://github.com/kuhung/understanding-jev) — Chinese deep-dive on engineering boundaries (guide)
