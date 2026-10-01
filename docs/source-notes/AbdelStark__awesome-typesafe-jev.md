# AbdelStark/awesome-typesafe-jev
- **One-liner:** A careful, source-backed "field guide" to Jev. It has an official-resource index, a route comparison (direct/Cloudflare/Netlify/Vercel/OpenRouter), runnable starters, a "before you trust a decision" failure-mode table, and ~280 caveated community entries.
- **Language(s):** English
- **Type:** curated-list (field guide / tutorial hybrid)
- **Scale:** ~284 entries (174KB README). Sections: See Jev at work / Recently curated / Start here (choose the right tool, choose where to call Jev, first decision JS/Python, shape a typed question, try a policy threshold, before you trust a decision) / Official resources (product & docs, SDKs, concepts/patterns/cookbooks, research & writing, community) / Community projects (Client libraries & integrations, Agent & developer tooling, Browser agents, Applications & workflows, Games & robotics, Evaluations & independent research, Showcases & field notes). Also resources.json (machine-readable), llms.txt, 246 generated project pages, a GitHub Pages site, an agent skill, and 125 all-contributors.
- **Quality flags:** Probably the most careful list in this batch. Nearly every entry carries a limitation or caveat (licence of weights, author-reported numbers, what data is sent). Last updated 2026-09-23 in the README, with later entries present. The maintainer (AbdelStark) lists some of his own projects (LeJudge, bicameral, jev-benchmarks). Mildly self-promotional but transparent. Not auto-generated in a spammy way.
- **Unique value:** (1) The most complete **official TypeSafe resource index**: API reference, demos, manifesto and blog essays, Discord, agent-skill guide, how-to-build page. (2) A **route comparison table** covering five access paths and their gotchas. (3) A **"Before you trust a decision"** table built from 5 independent studies. (4) Rich coverage of open alternatives and evaluations with licence caveats. (5) Machine-readable JSON plus llms.txt.

## Facts claimed about Jev
- Official documented quickstart example (`jev-1.13.0`, saved response): state is a Stripe support ticket. Choice `technical` with **0.85** selected probability. Score `1` on a 0–2 frustration rubric ("Frustrated but civil"). Noul urgency `1.0`.
- SDKs: `npm install @typesafe-ai/sdk` (Node.js 20+), `import { choice, noul, TypeSafeClient }`, `new TypeSafeClient().systemOne({state, questions})`, `answers.team.choice`, `answers.team.probabilities[team]`, `answers.refund.noul`. Python: `uv add typesafe-sdk` (Python 3.10+), `TypeSafeClient().system_one(...)`. This README's Python example reads **`result.choices["team"]` and `result.nouls["refund"]`**, while other repos (vicfei, dog-last) use `response.answers[...]`. This is an SDK-accessor discrepancy (possibly different SDK versions); flag it.
- Env var `TYPESAFE_API_KEY`.
- Access routes:
  - **Cloudflare Workers AI** `typesafe/jev` (labelled third-party).
  - **Netlify AI Gateway** (official JS SDK from Netlify Functions, server-side only).
  - **Vercel AI Gateway** through AI SDK experimental `evaluate` with `typesafe-ai/jev` (Boolean maps to Noul).
  - **OpenRouter** decisions API `typesafe/jev-1.13` or its latest route (openrouter.ai/labs/jev/compile). Do not send these questions to chat-completions.
  - An **OpenCode Zen free `/v1/systemone` endpoint** (per jev-agent-skill entry).
  - BeatAPI (jevapi.io).
- Official resources: docs.typesafe.ai/api (HTTP API reference), /demos (including a smart-home assistant), /concepts/how-to-build-with-system-one, /agent-skill, /confidence ("how confidence differs from answer probability"). Also evals.typesafe.ai, typesafe.ai/manifesto, blog posts "The Bitterest Lesson" and "AI: too good to be true, too bad to be useful", discord.gg/typesafe, x.com/typesafeai, LinkedIn.
- `system-one-adapter-python` runs the same typed interface over OpenAI, Anthropic and OpenAI-compatible APIs.
- Independent findings:
  - KoBBQ: Jev chose "unknown" for 95% of 300 ambiguous items when that option existed. With it removed, 79% of answers picked the stereotype.
  - Janus: a Jev→DeepSeek cascade helped on Banking77 but matched Jev alone at 47% higher cost on Web of Science.
  - jev-certify (CLINC150): a 5% misroute bound held with 84.75% auto-routed and 2.25% loss. The scope gate missed its target by 3.6× when OOS prevalence rose.
  - ORDER BY study: passed 6 ranking gates on topic rows, failed 4/6 on shopping pairs. 53 rows tied at 0.99. **Batching 40 rows turned a pass into a fail.**
  - 111-case action gate: Jev 100/111 vs Claude 102/111, one unsafe allow each.
  - jev-does-not-play-dice: Choice put 82.9% on face 1 for fair-dice inputs.
  - jevos: 0.815 vs hosted Jev 0.927 on 2,000 Noul questions.
  - ruling: 231 vs 238 on 256 public judgments (not significant).
  - LLM memory audit: `jev-1.13-20260917` showed no memory of earnings outcomes (within-company AUC 0.506).
  - Agentjournal: decomposing into 12–14 Jev-scored dimensions with fitted weights beat one direct question; 5,477 rows / 34.1M tokens for $1.43.
- JevBench: 534 frozen cases per entrant, a four-axis score (accuracy, calibration, latency, cost).

## Key insights / patterns
- Split work three ways: **code** for explicit rules on known fields, **Jev** for bounded judgment on messy context, **text LLM** for prose or open-ended tasks. Code validates and owns actions.
- Ask independent questions together in one request. Keep the state short, use non-overlapping option descriptions, include a no-match option, and choose thresholds only after measuring labelled cases.
- Thresholds are application policy. The same 0.85 answer routes at a 0.80 threshold and goes to review at 0.90.
- Pre-ship checklist from the studies: add abstain options; price both legs of a cascade; calibrate on representative traffic and monitor the mix; test ties and request shape (batching) before sorting by probability; test the answer-to-action mapping, not just the model.
- Decomposition into many scored dimensions plus fitted weights beats a single direct question (matches dog-last's atomization lesson).
- Position/order bias exists (dice test). Use order-reversed and negated re-asks (Love-Language Arena).
- Open-model licensing: many code repos are Apache/MIT while their weights are non-commercial (blink, bev-decider).

## Standout entries
- [HTTP API reference](https://docs.typesafe.ai/api) — request/response contract (official)
- [How to build with TypeSafe](https://docs.typesafe.ai/concepts/how-to-build-with-system-one) — design guidance (official)
- [Confidence](https://docs.typesafe.ai/confidence) — confidence vs probability (official)
- [Manifesto](https://typesafe.ai/manifesto) — TypeSafe thesis (official)
- [The Bitterest Lesson](https://typesafe.ai/blog/bitterest-lesson) — TypeSafe essay (official)
- [Discord](https://discord.gg/typesafe) — official community (official)
- [OpenRouter Jev](https://openrouter.ai/labs/jev/compile) — decisions API route (platform)
- [Netlify AI Gateway](https://docs.netlify.com/build/ai-gateway/overview/) — access route (platform)
- [JevBench results v1.2](https://github.com/fstandhartinger/jevbench/blob/main/RESULTS-v1.2.md) — cross-model benchmark (benchmark)
- [jev-calibration-audit](https://github.com/jujumilk3/jev-calibration-audit) — KoBBQ abstention audit (benchmark)
- [jev-certify](https://github.com/nikkoxgonzales/jev-certify) — conformal routing thresholds (tool/benchmark)
- [jev-sec-bench](https://github.com/Gaurav-Gosain/jev-sec-bench) — prompt-injection and vulnerable-code eval (security)
- [Awesome Jev Robustness](https://github.com/Yifan-Lan/awesome-jev-robustness) — robustness index (list/security)
- [Milvus Search with Jev](https://github.com/milvus-io/bootcamp/tree/master/bootcamp/RAG/search_with_jev) — 9 RAG notebooks (tutorial)
- [Learn Jev end to end](https://github.com/harshithsunku/learn-jev-end-to-end) — 12-notebook course (tutorial)
