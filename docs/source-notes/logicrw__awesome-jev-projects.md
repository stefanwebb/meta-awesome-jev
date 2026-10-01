# logicrw/awesome-jev-projects
- **One-liner:** "Awesome Jev — System-1 Agent Architecture Radar": a large, auto-synced, 4-language catalog of 799 Jev projects. Each entry states **where Jev makes a decision**, with commit-pinned source evidence and a searchable web app.
- **Language(s):** English, Simplified Chinese, Japanese, Korean
- **Type:** auto-generated-list (a radar with human source review; also a web app and an agent skill)
- **Scale:** 799 projects (~824 entries in a 522KB README) in 17 categories: Browser & OS Action (51), CLI & Pipelines (87), Classification (2), Code Navigation (15), Context GC (42), Creative Tools (26), Data & Search (50), Decision Tools (37), Domain Tools (85), Evaluation & Observability (29), High-Frequency / Games (54), MCP & Integrations (51), Model Routing (65), SDK & Decision Frameworks (130), SDK Integrations (6), Security & Guardrails (65), Voice & Conversation (4). There is a Vite/TS web app, discovery scripts, radar receipts and reviews, an `npx skills add logicrw/awesome-jev-projects` skill, and llms.txt / llms-full.txt.
- **Quality flags:** Mixed.
  - The entry format is excellent: "Where Jev makes a decision" plus "What this project offers" plus a pinned-source link plus licence.
  - The audit documents are rigorous: a 2026-09-19 review of 259 records found 7 flagged "review-pending" for fail-open gates, API contract mismatches and licence riders.
  - The catalog grew fast (130 on 09-18, 259 on 09-19, 799 by 09-30), so later entries are likely mostly auto-discovered with less human review.
  - The **marketing copy is hype-y and partly inaccurate**: "Sub-100ms latency, 50–100ms" (others say 70–500ms), "Deterministic bounded state machine", "Zero Vaporware", and gimmicks like a "Tactile Gacha Dispatcher with 10-draw fireworks".
  - It is **open to paid placements/sponsorship** (none yet) and accepts Issues only, no PRs. There is also an outreach kit, so it is promotional.
- **Unique value:** The decision-point annotation per project ("where Jev makes a decision") at large scale. There are 4 languages. The audit trail catches concrete integration bugs, such as an SDK that sends the wrong request shape and a fail-open pre-commit gate.

## Facts claimed about Jev
- The official API contract is referenced implicitly in the audit: requests carry a **`questions` object** (not an `evaluations` array) and responses carry **`answers`** (not `results[0].value`). This is why Olti1947/jev-java was flagged.
- It claims "Sub-100ms latency: decisions in 50–100ms", which **contradicts** the vendor's 70–500ms quoted in other lists. It compares System 2 at 1,500–5,000ms+ and $1–15/1M tokens.
- Primitives: Choice, Score, Noul.
- OpenJev (razorback16) is a protocol-compatible implementation on DiffusionGemma that does not call hosted Jev. hr98w/jev-visual and rongxinzy/LightJev do not integrate TypeSafe Jev.
- It says there were 1,348 code-search matches for a domain query (search-tool detail).

## Key insights / patterns
- The entry template itself is a useful meta-list pattern: for each project, name the **exact decision point** (e.g. "chooses an action and its DOM element in one request; a text model generates input text").
- Audit lessons: **fail-open gates** (jev-git returns success on a missing key, an API/parse error or a missing answer) are a common security bug in Jev guardrail tools. Stars measure attention to the whole repository, not Jev adoption. Separate "public code" from "declared open-source licence" (49 of 259 had unconfirmed licences).
- Recurring architecture across browser and desktop entries: deterministic extraction of candidate controls, then Jev selects, then local policy decides whether to execute, and a text model is used only for typing.
- Categories like "Context GC" (42) and "Model Routing" (65) show how large the coding-agent use case has become.

## Standout entries
- [Live radar](https://logicrw.github.io/awesome-jev-projects/en/) — searchable 799-project directory (directory)
- [Catalog audit 2026-09-19](https://github.com/logicrw/awesome-jev-projects/blob/main/docs/catalog-review-2026-09-19.md) — review findings incl. fail-open and API-mismatch cases (audit)
- [llms-full.txt](https://logicrw.github.io/awesome-jev-projects/llms-full.txt) — machine-readable catalog (data)
- [trycua/cua](https://github.com/trycua/cua) — jev-use example for computer use (browser/OS)
- [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) — browser agent (browser)
- [lahfir/agent-desktop](https://github.com/lahfir/agent-desktop) — native accessibility-tree desktop agent with optional Jev skill (desktop)
- [awlevin/typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) — OCR plus Jev macOS control (desktop)
- [logicrw/ask-jev](https://github.com/logicrw/ask-jev) — zero-dependency CLI for semantic judgments (CLI; the maintainer's own)
