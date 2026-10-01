# whyashthakker/awesome-jev-use-cases
- **One-liner:** Runnable Node app with 50 minimal visual use-case demos, each comparing Jev Choice/Score/Noul with OpenAI gpt-4o-mini Structured Outputs side by side.
- **Language(s):** English
- **Type:** project/code (not a list) — tutorial-style use-case collection
- **Scale:** 50 use-case folders (scenario.json, index.html, run.js, README.md each), numbered 01-50, spanning support, fraud, moderation, games, routing, RAG, extraction, compliance, robotics, forecasting. Docs: methodology.md, research.md, beam-cli-action-judging.md. Tests incl. Playwright.
- **Quality flags:** Original code, not a link list. Preview mode uses hand-authored fixtures (clearly labeled illustrative, not measurements). No benchmark winner claimed. Author's own Beam CLI is plugged (mild self-promotion). Has an SEO/GEO doc. Honest and careful.
- **Unique value:** Runnable, key-optional side-by-side harness against an LLM baseline with per-run cost estimation; a 50-item catalogue of "why a typed decision fits" rationales; strong evaluation methodology checklist; precise semantics of each primitive's output; concrete thresholds for an agent-action safety gate (Beam CLI).

## Facts claimed about Jev
- Endpoint `POST https://api.typesafe.ai/v1/systemone`, body `{state, model, questions}`; default model `jev-latest`; env `TYPESAFE_API_KEY`, `JEV_MODEL`.
- Pricing verified 2026-09-20: "TypeSafe Jev 1.13: $0.042 per million input tokens; output free" (docs.typesafe.ai/models). OpenAI gpt-4o-mini $0.15 input / $0.075 cached / $0.60 output per million, used for comparison.
- Output semantics: Choice -> one option, distribution over all options, and confidence (confidence is distinct from selected-option probability). Score -> probability-weighted value over indices 0..N-1 (may be fractional), distribution, legend, confidence. Noul -> single yes/no probability 0-1, no separate confidence.
- Questions in a batch are independent; compose in code.
- TypeSafe documents limitations ("jaggedness", docs.typesafe.ai/model-jaggedness/jev-1.13) around arithmetic, dates, indirection, irrelevant context and adversarial state.
- Official docs pages referenced: llms.txt index, introduction, api, primitives, confidence, patterns, concepts/use-case-map, model-jaggedness/jev-1.13.
- Providers count tokens differently; token count alone isn't a dollar comparison.

## Key insights / patterns
- Noul near 0.5 = uncertainty, not medium intensity. Use one Noul per independent condition; Choice is a competition among options.
- Keep exact computations (arithmetic, dates, A/B allocation, permission enforcement, price calculations) in code; Jev does the semantic step only (e.g. date component extraction as Choice, validation in code).
- Choose existing span IDs instead of generating text (semantic line search, email span selection) — eliminates hallucinated extraction.
- Safety-critical demos (driving, traffic, robot): code interlocks override unsafe candidate actions.
- Confidence-gated routing is a Jev-specific capability: low native confidence -> human review.
- Beam CLI agent-action gate: two independent Nouls (credential/data exposure; irreversible delete/overwrite) + Score damage 0-3. Noul >= 0.8 or Score >= 2 -> deny; Noul both <= 0.2 passes; Score <= 0.5 with confidence >= 0.7 passes; else review; any deny wins. Starts in observe mode; send only redacted action fields.
- Evaluation recipe: held-out human-labeled data incl. adversarial; freeze questions/model IDs (aliases move); randomize order, p50/p95 latency; accuracy + macro-F1; calibration separately; review/rejection rates; compare with small classifiers and rules too.
- No retries in comparisons; production should add logged backoff.

## Standout entries
- [TypeSafe docs llms.txt](https://docs.typesafe.ai/llms.txt) — complete docs index (official)
- [TypeSafe primitives](https://docs.typesafe.ai/primitives) — Choice/Score/Noul reference (official)
- [TypeSafe confidence](https://docs.typesafe.ai/confidence) — confidence semantics (official)
- [TypeSafe patterns](https://docs.typesafe.ai/patterns) — official patterns (official)
- [Industry use-case map](https://docs.typesafe.ai/concepts/use-case-map) — official use-case map (official)
- [Jev 1.13 limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13) — known failure modes (official)
- [API contract](https://docs.typesafe.ai/api) — HTTP API (official)
- [Models & pricing](https://docs.typesafe.ai/models) — $0.042/M input (official)
- [Beam CLI](https://github.com/whyashthakker/beam-cli) — optional Jev action judging for coding agents (tool)
- [Beam Jev action-judging walkthrough](https://agentbeam.com/blog/beam-cli-jev-action-judging) — thresholds and setup (tutorial)
- [jev-action-judge skill](https://github.com/whyashthakker/beam-cli/tree/main/Skills/jev-action-judge) — agent skill (skill)
- [awesome-jev-use-cases](https://github.com/whyashthakker/awesome-jev-use-cases) — this repo: 50 runnable Jev vs OpenAI demos (tutorial/code)
