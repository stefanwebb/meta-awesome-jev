# FuturExplorator/awesome-jev-cases
- **One-liner:** A bilingual (CN/EN), heavily governed case library of 27 source-verified Jev projects. Each case explains exactly what Jev decides and what code does, with pinned commits and SHA-256 evidence receipts.
- **Language(s):** Chinese, English (every case is bilingual)
- **Type:** use-case-collection
- **Scale:** 27 cases. Categories: browser execution (7), routing and selection (5), coding and context (4), guardrails (2), evidence evaluation (5), integrations and SDKs (2), games and simulations (1), streams and other (1). There is also a large research/ audit trail (candidates, link checks, CSV triage, release reviews), a schema, templates, and a `validate_catalog.py` validator. Companion site: jevforagents.com.
- **Quality flags:** Rigorous about provenance. "Verified" means only that source, identity, Jev usage and links were checked; performance, security and cost are not independently verified (it says so explicitly). It is small in coverage and heavy on process documents. It withholds the official typesafe-ai/skills repo (no distinct case) and SkillRanker (restrictive licence rider). No spam or fabrication.
- **Unique value:** A **clean split of responsibilities** in every case: "Jev's specific role" vs what code owns. It also gives reproduction steps and limitations (fail-open behaviour, shadow modes), pinned source revisions and licence notes. It is the best source for describing *how* Jev fits into the architecture of real projects.

## Facts claimed about Jev
- Uses the TypeSafe `/v1/systemone` endpoint (dannote/jev Elixir, AgriciDaniel/jev-seo).
- OpenRouter route: `typesafe/jev-1.13` through "OpenRouter Decisions" (NanmiCoder/jev-arena).
- `jevclient` is the Python client used by the HA-Jev Home Assistant integration.
- It does not measure performance. Author benchmarks are labelled as author-reported and not re-run.

## Key insights / patterns
- Recurring division of labour: **Jev judges and code acts.**
  - Browser agents (jev-ultrafast, jev-browser, jev-ra, wy-coliney bridge): Jev picks the operation and target from permitted, compatible elements. Code validates, rechecks page freshness and confidence, executes, and controls stopping. Jev also judges completion or lack of progress.
  - Context compaction (fast-jev-compaction, codex-context-diet, compact-adviser): per tool-call keep-call/keep-result questions. Code retains, drops or truncates. **Jev never writes the summary.**
  - Routing (jev-router, ClearJev, Astra-Ares, rajdhakad jev-router): Jev answers task complexity, reasoning need and tool complexity, and returns tier probabilities. Code applies thresholds, a configured fallback on API failure, and caches or heuristics that bypass Jev.
  - Guardrails (pi-heed, pi-jev): Jev judges destructive, exfiltration, scope and impact questions about pending tool calls. Code thresholds decide whether to notify or block. **Uncertain or failed judgments can fail open; this is not a security sandbox.** Run in shadow mode first.
  - Multi-question per tick (snake-jev): 9 questions per tick (wall/body/food × left/straight/right), and Python composes the action from the judgments alone.
  - Firehose moderation (firehose-judge): 8 questions per sampled post in one request, feeding confidence routing and a display-safety filter.
  - Chat with no LLM (w3cj/jev-chat): Jev chooses intent, tool and argument candidates, and code executes the MCP tools.
- Recommended reproduction habit: configure your own key and observe decisions in shadow or status mode before enforcing.

## Standout entries
- [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) — Jev picks operation and target in one request (browser)
- [jkudish/jev-browser](https://github.com/jkudish/jev-browser) — action selection plus completion/no-progress judgments (browser)
- [moritzkremb/jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser) — voice to intent/target/destructiveness (browser)
- [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) — keep/drop compaction (coding)
- [kunchenguid/compact-adviser](https://github.com/kunchenguid/compact-adviser) — when to compact (coding)
- [konstantinosbotonakis/codex-context-diet](https://github.com/konstantinosbotonakis/codex-context-diet) — tool-result pruning for Codex (coding)
- [gargpratyush/jev-router](https://github.com/gargpratyush/jev-router) — model routing for Claude Code (routing)
- [miuuyy/Astra-Ares](https://github.com/miuuyy/Astra-Ares) — mid-run reasoning-effort selection (routing)
- [Nyarlathoteppppp/pi-heed](https://github.com/Nyarlathoteppppp/pi-heed) — constraint retention and tool-call gate (guardrails)
- [y0usaf/pi-jev](https://github.com/y0usaf/pi-jev) — destructive/exfiltration judgments (guardrails)
- [w3cj/jev-chat](https://github.com/w3cj/jev-chat) — tool-calling chatbot with no LLM (routing)
- [superagents-lab/jev-search](https://github.com/superagents-lab/jev-search) — search pipeline with Jev relevance judgments (evaluation)
- [ragelink/firehose-judge](https://github.com/ragelink/firehose-judge) — 8 questions per post over a firehose (other)
- [AboveColin/HA-Jev](https://github.com/AboveColin/HA-Jev) — Home Assistant integration (integration)
- [jevforagents.com](https://jevforagents.com) — companion case site (community)
