# walidboulanouar/awesome-jev-use-cases
- **One-liner:** Use-case list of Jev demos (mostly X/Twitter videos) with engagement metrics, 150+ repos, official cookbook summaries, limits, reported cost/latency and unshipped ideas.
- **Language(s):** English
- **Type:** use-case-collection
- **Scale:** 74 demo posts tracked (127,162 likes); 38 repos in main list (53,259 stars) + 33 from a 2026-09-26 sweep + 507 more in CSV; "more than 150 repositories" overall. Sections: Top 30 popular demos (cards), FAQ, Browse by area (Content and growth 18, Apps and tools 17, Agents and computer use 14, Triage and routing 9, Games and real time 7, Research and data 7, Trading and markets 2), Numbers at a glance, Most-liked demos, Small accounts big results, Open source (browser/computer use, coding agents, routing, data/search, games/trading/hardware, open models, MCP/skills/clients, SDKs, long tail, other lists), Search demand, Full tables, What Jev is, Cookbooks from TypeSafe, Patterns, Limits of Jev 1.13, Reported cost and latency, Ideas nobody has shipped yet, Tools. docs/demos/ has one page per demo (~60+), data/*.csv.
- **Quality flags:** Sponsored by AY Automate (banner/sponsor image) — mildly promotional; SEO-oriented ("keyword-research.md", "search demand" section, FAQ). Metrics are a dated 2026-09-19 snapshot; demo-focused (social virality ≠ quality). Otherwise careful: says numbers are builder-reported, unverified; separates ideas from shipped work.
- **Unique value:** Engagement metrics per demo (likes, followers, reach); best summary of the **official TypeSafe cookbooks with their reported numbers**; builder-found patterns incl. extension engineering gotchas; list of unshipped ideas with risk notes; Vercel adoption/free-window facts.

## Facts claimed about Jev
- API: `POST https://api.typesafe.ai/v1/systemone`, Bearer `$TYPESAFE_API_KEY`, `model: "jev-latest"`; example response `{"model":"jev-latest","answers":{"is_urgent":{"type":"noul","noul":0.92}},"usage":{"input_tokens":312,"output_tokens":48}}`. `jev-latest` currently points to `jev-1.13.0`.
- Models page: Jev 1.13 **$42 per billion input tokens ($0.042/M), output free; 250,000 tokens/second; 1,200 requests/minute; 32k tokens on state + longest question; 64k whole request**; text only.
- Launch post: end-to-end **70–500 ms**; **40x–200x faster** than frontier LLMs on System One tasks; the **193.6x faster / 444.6x cheaper** homepage figures are "on the higher end of real-world gains".
- Vercel AI Gateway: Jev **free until Sept 25** (announced 2026-09-19; vercel.com/ai-gateway/models/jev); Vercel claimed Jev "adopted faster than any other model in AI Gateway history", ~13% of teams on day one, 2x GPT-5.6 family, 6x Fable 5.1 (unverified).
- Cookbook numbers: parallel questions — 13-question regulatory briefing, **12.2x cheaper, 10.0x faster** batched, same answers; re-ranking — 40 legal queries, 30-passage shortlists, **top-1 5%→18%, top-10 38%→62%**; line-by-line search over GitHub ToS scores 218 line ids in one request; skill suggestion over 182 Hermes skills; entity alignment 450 candidate pairs, Score levels = merge / leave unlinked / hand to curator; classification using confidence — SEC reports into 75 industry groups, fall back to broader division on low confidence; hierarchical classification via parallel beam search; SDE cascade; autoresearch feature discovery with CatBoost.
- Limits (jaggedness page reviewed 2026-09-17): literal reading; not a calculator (math, counting, date comparison); don't interpolate Score between levels; irrelevant state lowers accuracy; injected text can steer; Noul and yes/no Choice on same thing may disagree; no generation; **English works best**.
- Builder numbers: @nutlope 1kpapers — 1,018 papers classified for $0.08 (8 cents), 256 ms median, vs $3.99 summaries; @rileybrown 500 emails for 3.5 cents; 700 leads scored in 40 s; @cjzafir $3.40 over 24h testing; maintainer ~$0.001 across ~100k tokens (note: inconsistent with $0.042/M, which would be ~$0.004).
- Claude Code skill: `claude plugin marketplace add typesafe-ai/skills` then `claude plugin install typesafe@typesafe-ai`. Docs index https://docs.typesafe.ai/llms.txt.
- "Jev plays Doom" posted by @CompleteSkeptic (TypeSafe founder account).

## Key insights / patterns
- Official patterns: speculative fan-out, confidence-gated routing ("answer tells you what, confidence tells you whether to act"), composite scoring (atomic scores + code weights), intent routing (to deterministic handler, specialist LLM or human).
- Generate with an LLM, judge with Jev (1kpapers: judging ~50× cheaper than summarizing).
- Many items in one state: array state, questions keyed `post_0`, `post_1`, refer to `posts[0]` in instructions; trade-off is accuracy loss from unrelated material — keep batches small.
- Rubrics from real outcomes: concrete levels, embed observed numbers to stop score drift; combine Scores with fixed weights in code.
- Browser-extension gotchas: call API from service worker (page CSP blocks localhost fetch); use LinkedIn test-id selectors, not hashed class names.
- Idea risk notes: router flapping between tiers; attacker-controlled text at API gateways is riskiest; tune thresholds so false positives don't cause users to disable checks; duplicate checks need both records in state.
- Top-4 demos (compaction plugin, browser agent, ad teardown, Mac voice assistant) — none generate text with Jev.

## Standout entries
- [Parallel questions cookbook](https://docs.typesafe.ai/cookbooks/parallel_questions) — 12.2x cheaper batching (official)
- [Re-ranking cookbook](https://docs.typesafe.ai/cookbooks/rerank_typesafe) — legal rerank top-1 5→18% (official)
- [Entity alignment cookbook](https://docs.typesafe.ai/cookbooks/entity_alignment) — Score levels as actions (official)
- [Hierarchical classification cookbook](https://docs.typesafe.ai/cookbooks/hierarchical_classification) — beam search over Choice (official)
- [Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence) — confidence-based fallback to parent class (official)
- [Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails) — screen every message (official)
- [Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing) — official pattern (official)
- [Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring) — official pattern (official)
- [TypeSafe skills](https://github.com/typesafe-ai/skills) — official Claude Code plugin (tool)
- [Instant compaction for Claude](https://x.com/tamarajtran/status/2100694549362553153) — most-liked demo, 10,435 likes (demo)
- [Flight search with Browser Use](https://x.com/gregpr07/status/2100411066966749359) — browser agent demo (demo)
- [1kpapers](https://x.com/nutlope/status/2100426999546184123) — 1,018 papers for 8 cents (demo)
- [Jev plays Doom](https://x.com/CompleteSkeptic/status/2099925687465570372) — launch demo (demo)
- [Vercel free-window announcement](https://x.com/vercel_dev/status/2101116818463281579) — gateway availability (news)
