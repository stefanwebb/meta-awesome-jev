# vicfei/awesome-jev-prompts
- **One-liner:** A library of 43 Jev question-design patterns and anti-patterns, "question design is the prompt engineering of typed decisions". Each entry has a template, threshold guidance, failure modes and sources.
- **Language(s):** English, Chinese (README.zh-CN.md)
- **Type:** prompt-collection
- **Scale:** 43 entries in 8 category files: Choice patterns (6), Score patterns (5), Noul patterns (5), Routing & triage (4), Guardrails & verification (5), Context compaction (3), Anti-patterns (10), Calibration & eval (5). There are also official-resource links and a related-lists table with stars refreshed daily by CI. Last checked 2026-09-30.
- **Quality flags:** High signal and well sourced. Most entries cite official docs cookbook pages and Anil-matcha/awesome-jev-by-typesafe (the quick-start is adapted from it, so it partly derives from that list). It calls **TypeSafeAI/jev-harness "official"**, but MrJev/awesome-jev describes the `TypeSafeAI` GitHub org as an *independent community organisation* (the official org is `typesafe-ai`). Flag this contradiction. All entries are dated 2026-09-28.
- **Unique value:** The only collection in this batch focused on **how to write Jev questions**. It has a crisp anti-pattern list and calibration process patterns, and it indexes many **official cookbook URLs** (hierarchical_classification, parallel_questions, entity_alignment, citation_check, classifying_rag_passages, rerank_typesafe, function_calling, consistency_noul/choice, classification_using_confidence, llm_guardrails).

## Facts claimed about Jev
- Endpoint `POST https://api.typesafe.ai/v1/systemone`. The aliases `jev-latest` and `jev-preview` both point to `jev-1.13.0`.
- Pricing: $0.042 per 1M input tokens, output free. Latency 70–500 ms.
- Context: **64k tokens per request (32k state + longest question)**. Limits: **250k tokens/sec, 1,200 requests/min**. Text only.
- Primitive schemas:
  - **Choice**: `instructions` plus a `criteria` dict mapping option to description. Returns `choice`, per-option `probabilities` and `confidence`.
  - **Score**: `instructions` plus `criteria` as an **ordered** rubric list. Returns a probability-weighted `score` (it can land between levels), plus `legend`, `probabilities` and `confidence`.
  - **Noul**: `instructions` only. Returns `noul`, the 0–1 probability that the statement is true.
- Python SDK: `pip install typesafe-sdk`; `from typesafe_sdk import Choice, Noul, Score, TypeSafeClient`; `client.system_one(state=..., questions={...})`; `response.answers["intent"].choice / .probabilities / .noul / .score`. TS: `npm install @typesafe-ai/sdk`, `choice(), noul(), score()`, `client.systemOne(...)`.
- Choice cardinality is capped at **255**. "Bigger sets silently fall back to a slower two-stage path" (this list's claim; others just call 255 a hard cap).
- Jev is weak at math, counting and dates (per official jaggedness docs).
- Available on Vercel AI Gateway and Cloudflare Workers AI.
- Official docs pages: /models, /primitives, /patterns, /confidence, /concepts/state, /concepts/use-case-map, /agent-skill, plus the cookbooks listed above.

## Key insights / patterns
- **Core rule: "questions describe judgments; code owns composition, thresholds, and side effects."**
- The 10 anti-patterns:
  1. Asking Jev to compute. Do arithmetic, counting and dates in code.
  2. Using Choice with unbounded options. Generate candidates with an LLM, then use Jev for best-of-N.
  3. Leaving out an `other`/`none_of_the_above`/`review` escape option.
  4. Giving Score an unordered rubric.
  5. Reading Noul 0.5 as "medium". It means uncertain. Use bands such as ≥0.8 act, ≤0.4 pass, in-between → uncertain branch.
  6. Using one global threshold. There is no blessed 0.7; set thresholds per action and risk level.
  7. Trusting `jev-latest` on threshold-sensitive paths. Pin the version and log the returned version.
  8. Ignoring the distribution. A 0.45/0.42 top two is a coin flip.
  9. Cramming several judgments plus an action into one question.
  10. Using Jev as authorization or a substitute for review. Calibration describes groups, not individual answers.
- Calibration process: build **two-band thresholds from logged distributions** (an action band and an escalation band, placed where ground-truth populations separate). Version the question text like a schema. Run **consistency checks** (two phrasings, or a Choice and a Noul encoding the same question; disagreement means escalate). Use **shadow mode** before cutover. Use a bicameral architecture with confidence-triggered System Two handoff.
- Context-compaction patterns: keep-or-drop per message, summarize-or-quote, and tool-result pruning (DeepSeek-harness plugins).
- Pattern catalogue: intent routing, tool selection, model routing, best-of-N, document type, skill routing, severity rubric, quality gate, moderation scoring, RAG relevance rubric, priority queues, policy check, dedup, citation/entailment, human escalation, retry/skip control, output guardrail, jailbreak detection, structured-output validation, code-review gate.

## Standout entries
- [Docs — Confidence](https://docs.typesafe.ai/confidence) — official confidence semantics (official)
- [Docs — Primitives](https://docs.typesafe.ai/primitives) — Choice/Score/Noul (official)
- [Docs — Use-case map](https://docs.typesafe.ai/concepts/use-case-map) — official use-case map (official)
- [Cookbook — classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence) — thresholding (official cookbook)
- [Cookbook — hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification) — more than 255 classes (official cookbook)
- [Cookbook — parallel questions](https://docs.typesafe.ai/cookbooks/parallel_questions) — batching (official cookbook)
- [Cookbook — rerank](https://docs.typesafe.ai/cookbooks/rerank_typesafe) — reranking (official cookbook)
- [Cookbook — citation check](https://docs.typesafe.ai/cookbooks/citation_check) — entailment (official cookbook)
- [Cookbook — consistency (Noul)](https://docs.typesafe.ai/cookbooks/consistency_noul_cookbook) — consistency checks (official cookbook)
- [Anti-patterns](https://github.com/vicfei/awesome-jev-prompts/blob/main/categories/anti-patterns.md) — 10 failure modes with fixes (prompt guide)
- [TypeSafeAI/jev-harness](https://github.com/TypeSafeAI/jev-harness) — "model proposes, Jev supplies evidence, code decides" (harness; officialness disputed)
- [AntonioCoppe/jev-harness](https://github.com/AntonioCoppe/jev-harness) — shadow mode and policies (library)
- [AbdelStark/bicameral](https://github.com/AbdelStark/bicameral) — System 1/System 2 architecture (project)
- [Anil-matcha/awesome-jev-by-typesafe](https://github.com/Anil-matcha/awesome-jev-by-typesafe) — design rules source (list)
