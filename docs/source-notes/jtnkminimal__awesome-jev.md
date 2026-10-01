# jtnkminimal/awesome-jev
- **One-liner:** Verified and ranked list of 136 Jev projects plus 18 upstream integrations into major OSS projects, with a Top-25 ranked by stars blended with a Jev-scored "interest" rating.
- **Language(s):** English
- **Type:** curated-list (semi-automated, Jev-assisted verification)
- **Scale:** 136 ranked projects + 18 upstream integrations. Sections: Top 25 · Models and Runtimes · Agent Tooling (about 47) · Guardrails and Code Review · Search, Ranking and Extraction · Applications · Trading and Markets · Benchmarks and Evaluations (14) · Games and Fun · Framework Integrations · Other Lists · **Upstream Integrations** · Method. Snapshot 2026-09-18.
- **Quality flags:** A solid, transparent method. It uses static evidence (greps for `api.typesafe.ai`, `TYPESAFE_API_KEY`, `typesafe-sdk`, `@typesafe-ai/sdk`, `jev-latest`, `/v1/systemone`, `noul`) plus two Jev questions per repo, combined in code. The "Interest" score comes from a Jev Score question, so it is subjective and model-generated. It includes some trivial toys (is-jeven, magic 8-ball) and one duplicate fork (chensirui2008/fast-jev-compaction). One description oddity: iammrduncan/typesafe-ai-benchmark is described as "a LLM Gateway that mimics typesafe ai structured output. Like an imposter Jev", which differs from other lists. Stale from 2026-09-18 on. Some Top-25 star counts are very high, e.g. jev-trader at 2.6k when other lists give about 600, which is a discrepancy.
- **Unique value:** The **Upstream Integrations** section is unique: Jev landing in established projects, with PR numbers: NousResearch/hermes-agent, oh-my-pi, trycua/cua, BoundaryML/baml, agentgateway, laravel/ai, aiavatarkit, llama.cpp fork, mlx-vlm fork. The verification method is reusable. It also collects small benchmark repos with headline numbers.

## Facts claimed about Jev
- Jev answers typed questions (Choice, Noul, Score) with calibrated probabilities. Doc URLs: docs.typesafe.ai/primitives/choice.md, /noul.md, /score.md.
- Integration fingerprints: `api.typesafe.ai`, `TYPESAFE_API_KEY`, `typesafe-sdk`, `@typesafe-ai/sdk`, `jev-latest`, `/v1/systemone`, `noul`.
- **The Choice cap is 255 options** (jev-tree).
- **OpenRouter Decisions API**: gmaxxxie/jev-cli uses "the Jev decision model via the OpenRouter Decisions API". stbenjam/jev-eight-ball also goes through OpenRouter.
- Jev is also reachable via "Lolipop! AI gateway" (the Japanese shogi experiment, kentaro/jev-shogi).
- Upstream: BoundaryML/baml has a "TypeSafe System One provider" (#4906 open). laravel/ai has TypeSafe AI classification (#1010 merged). hermes-agent adds Jev to its provider list (#113847, #114376 open). agentgateway has an LLM guardrail example (#3529 merged). trycua/cua has a Jev-use recipe (#3916 merged). aiavatarkit has a Jev turn-end gate (#428 merged).
- Benchmarks:
  - goodrahstar/jev-column-race: Jev vs Gemini 3.8 Flash labeling 1,000 app reviews, "4.1× faster and 7× cheaper".
  - jev-harness: Claude CLI 48.9 s vs Jev 1.3 s.
  - zhuyansen/jev-news-cold-start: a zero-shot Jev headline prior "worth ~500 labelled articles", +0.069 ρ as features.
  - zhuyansen/jev-support-pulse: catches 17 vs 10 incidents about 4h ahead at equal false alarms.
  - zhuyansen/jev-issue-pulse: a null result at daily cadence (n=7).
  - onlyoneaman/jev-eval: vs gpt-5.4-mini and gpt-5.6-luna on four public classification sets.
  - gemanor/jev-code-review-benchmark: Jev vs Gemini Flash vs **Claude Fable** on code-review rules.

## Key insights / patterns
- **Verification pattern for lists:** use static code fingerprints as authoritative, use a Jev Noul ("TypeSafe's model vs generic type-safety?") plus a Choice (relationship: calls API / open alternative / tooling / benchmark / list / unrelated) for ambiguous cases, and combine them in code. Rank with transparent weights: `score = 50 × log-scaled stars + 50 × (interest ÷ 4)`.
- A "type-safe" name proves nothing because it's an ordinary programming term, so filter name collisions.
- Rule/skill pruning for coding agents: jev-rules picks which rules apply per prompt so Claude sees only the relevant ones. Tool-list pruning: jev-tool-permissions for the Vercel AI SDK.
- Guardrails: deny/ask/allow risk scoring per tool call with session context and injection flags in tool results (leepokai/jev-guard). Checking side-effecting calls against what the user said (pi-heed).
- Validation composed with schemas: Jev semantic checks inside Zod 4 schemas while shape rules stay in Zod (zod-jev, jod).
- Cascade FAQ routing: category, then FAQ, or not found.
- Time-series and alerting uses: labeled streams as early-warning signals. These give mixed results, including an honest null result.
- Knowledge-base linting for contradictions and stale claims (vayungodara/jev-lint).

## Standout entries
- [typesafe-ai/skills](https://github.com/typesafe-ai/skills) — official skills (official)
- [vercel-labs/ai-cli](https://github.com/vercel-labs/ai-cli) — Vercel AI CLI with Jev evaluate (integration)
- [BoundaryML/baml](https://github.com/BoundaryML/baml) — TypeSafe System One provider PR #4906 (upstream integration)
- [laravel/ai](https://github.com/laravel/ai) — TypeSafe classification in Laravel AI SDK (upstream integration)
- [agentgateway/agentgateway](https://github.com/agentgateway/agentgateway) — LLM guardrail example on Jev (upstream integration)
- [trycua/cua](https://github.com/trycua/cua) — Jev-use agent recipe (upstream integration)
- [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) — Jev provider + skill routing PRs (upstream integration)
- [bespokelabsai/nimble](https://github.com/bespokelabsai/nimble) — local typed decisions + data curation (models/runtimes)
- [zmtomorrow/typear](https://github.com/zmtomorrow/typear) — type-safe decoding for autoregressive LLMs (research)
- [leepokai/jev-guard](https://github.com/leepokai/jev-guard) — deny/ask/allow auto mode for coding agents (guardrails)
- [EliaAlberti/jev-rules](https://github.com/EliaAlberti/jev-rules) — per-prompt rule selection (agent tooling)
- [jomatsu/zod-jev](https://github.com/jomatsu/zod-jev) — Jev checks inside Zod schemas (framework)
- [goodrahstar/jev-column-race](https://github.com/goodrahstar/jev-column-race) — Jev vs Gemini 3.8 Flash on 1,000 reviews (benchmark)
- [gemanor/jev-code-review-benchmark](https://github.com/gemanor/jev-code-review-benchmark) — Jev vs Gemini Flash vs Claude Fable (benchmark)
- [zhuyansen/jev-news-cold-start](https://github.com/zhuyansen/jev-news-cold-start) — zero-shot prior worth ~500 labels (benchmark)
