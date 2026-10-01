# onlyoasis/awesome-jev-cases
- **One-liner:** Bilingual structured catalog of 43 Jev case studies (input → Jev decision → action → evidence limit), 81 GitHub projects, and 18 official TypeSafe cookbooks.
- **Language(s):** Chinese (README.md, CATALOG.md) and English (README.en.md); data JSON bilingual; mirrored at typesafe-jev.com
- **Type:** use-case-collection
- **Scale:** 43 worked cases, 81 project listings (table: category, relationship Official/Inspired replica/etc., license, stars·checked date), 18 official cookbooks (data/official-recipes.json). Sections: Use cases; GitHub projects; Data and updates; Contributing. Generated from data/*.json via scripts/render.mjs; daily Codex-driven curation (docs/codex-daily-curation.md, AGENTS.md) with monitor-status.json.
- **Quality flags:** AI-assisted (Codex daily curation) but carefully written with honest "evidence & limit" per case (e.g. "Author post only", "this site did not run the API"). Distinguishes official (`typesafe-ai/*` only) vs replicas; license column. Low promo; website typesafe-jev.com is the maintainer's. Some cases are X posts only.
- **Unique value:** Per-case decision anatomy (which primitives, how many questions, thresholds, what code does) plus explicit evidence limits and data-egress warnings; the only list in the batch that enumerates all 18 official cookbooks with their headline metrics.

## Facts claimed about Jev
- Official Python SDK: pip `typesafe-sdk`, Python >= 3.10, sync/async clients, Choice/Score/Noul types, reads `TYPESAFE_API_KEY` by default. JS SDK npm `@typesafe-ai/sdk` with inferred answer types, built-in retries, error classes. typesafe-ai/skills ★1,472 (2026-09-22); system-one-adapter-python emulates TypeSafeClient on ordinary LLM APIs for A/B testing or fallback.
- Official cookbooks (docs.typesafe.ai/cookbooks/*.md), with official claims: Parallel questions — 13-question GDPR briefing batched in one call is **12.2× cheaper and 10.0× faster** with no change in answers; Re-ranking — 30-passage BM25 shortlists, 40 CLERC legal queries, top-1 **5%→18%**, top-10 **38%→62%**; Line-by-line search — 218 line ids scored with one Choice + Noul "does document contain answer"; Skill suggestion — ≤1 of 182 Hermes skills via two requests (rank + recheck); Entity alignment — 450 candidate pairs, one Score + three companion Nouls; Classification using confidence — SEC reports into 75 industry groups, fall back to broader division when confidence low; Hierarchical classification — parallel beam search over Choice probabilities; SDE cascade (mini → verify → reasoning); LLM guardrails (pass/review/block/route); citation check; RAG passage classification; date extraction; pre-parsed value extraction (regex candidates → Jev selects span); function calling; autoformat; autoresearch feature discovery (CatBoost); self-consistency nouls/choices.
- OpenRouter Jev Router: Jev judges task type/difficulty/precision/benefit from larger model → selects model + reasoning effort (x.com/OpenRouter/status/2103610898690855161).
- Author-reported numbers: 500-email classification demo cost 3.5 cents; jev-voice-browser 9–11 questions per partial transcript, ~$0.0002/call; mobile-jev Uber demo 9 actions in ~21 s; minecraft-agent best run 131 Jev decisions + 35 GPT-6 Astra calls, 8m43s; jev-codex-router ~60% saving is a backtest of 237 turns; Glean expert routing pilot 8.1× median speedup (offline, author-reported); jevmeter 99% held-out preset accuracy (self-reported); pi-jev default thresholds 0.90/0.70/0.85/2.50.
- Jev does not release weights; "inspired replicas" are independent.

## Key insights / patterns
- Batch all questions over one state into a single call (official: 12.2× cheaper, 10× faster).
- One request mixing primitives is the norm: e.g. ticket triage = Choice (department) + Score (impact) + Noul (churn); drone = Choice maneuver + Score risk + Noul target-lost at 2.5 Hz with scene-fingerprint caching; neo4jev = Choice next relationship + Noul goal-reached in one round trip.
- Semantic routing: each route as a Noul, pick first above threshold, fall through when none match; don't use semantic routes for authN/authZ (hono-jev-router).
- Context compaction: one Noul per chunk/tool result; hide only confident-no blocks; keep error-looking outputs (winnow, jev-pruner, fast-jev-compaction) — risk of discarding later-needed evidence.
- Constrain action space in code: Jev picks from code-supplied legal actions, never arbitrary coordinates (jev-mobile, typesafe-mario, jevwright grounding but not pass/fail).
- Tool-call gating: Score risk + Nouls for destructive / exfiltration / beyond-scope / planted instructions → deny/ask/allow; not a replacement for host permissions.
- Regex/rules first, Jev for residual semantic questions (wellposed, pre-parsed extraction).
- Data egress: most cases send content to TypeSafe/gateways — flagged repeatedly. Offline keyword fallbacks can make demos misleading.
- Generative + Jev hybrids: LLM drafts candidates, Jev ranks with win probability (jev-chat-jarvis); planner LLM + Jev per-action (minecraft-agent).

## Standout entries
- [Official cookbooks](https://docs.typesafe.ai/cookbooks.md) — 18 official recipes (official)
- [Parallel questions cookbook](https://docs.typesafe.ai/cookbooks/parallel_questions.md) — batching economics (official)
- [Re-ranking cookbook](https://docs.typesafe.ai/cookbooks/rerank_typesafe.md) — CLERC legal reranking (official)
- [Guardrails for LLMs cookbook](https://docs.typesafe.ai/cookbooks/llm_guardrails.md) — in/out message screening (official)
- [Hierarchical classification cookbook](https://docs.typesafe.ai/cookbooks/hierarchical_classification.md) — beam search over Choice (official)
- [jev-ultrafast](https://github.com/browser-use/jev-ultrafast) — Browser Use agent choosing action + element (browser agent)
- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) — Noul-based tool-result compaction (coding agent)
- [DocJev](https://github.com/jerryjliu/docjev) — document category + boundary splitting (Jerry Liu) (document processing)
- [pg-jev](https://github.com/realZachi/pg-jev) — PostgreSQL extension with Noul/Choice/Score functions (database)
- [hono-jev-router](https://github.com/yusukebe/hono-jev-router) — semantic HTTP routing (web framework)
- [jev-guard](https://github.com/leepokai/jev-guard) — deny/ask/allow tool review (security)
- [jevals](https://github.com/openlayer-ai/jevals) — eight parallel agent-trace judgments incl. injection and PHI (evaluation)
- [hn-oracle](https://github.com/anthony-maio/hn-oracle) — preregistered HN prediction extraction pilot (research)
- [jev-drone](https://github.com/RomanSlack/jev-drone) — 2.5 Hz MuJoCo drone control (robotics)
- [HA-Jev](https://github.com/AboveColin/HA-Jev) — Home Assistant integration (smart home)
