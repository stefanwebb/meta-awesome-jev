# fatwang2/awesome-jev
- **One-liner:** Directory of 163 open-source Jev projects. Each submission is reviewed by Jev itself through a GitHub Action that checks the source for a real integration.
- **Language(s):** English
- **Type:** curated-list (Jev-reviewed submissions; README generated from entries/*.json)
- **Scale:** 163 projects. Categories: SDKs (22) · Integration (about 40) · Developer tools (about 37) · Search (10) · Applications (about 25) · Games (15) · Research (22). Each entry is a JSON file (name, repository, description, category, optional evidence paths).
- **Quality flags:** High signal density. Descriptions are factual and must not make unsupported speed or accuracy claims (per CONTRIBUTING), and entries must show source evidence of a real Jev integration, not just a README claim. The initial seed entries were hand-maintained and did not pass a live review. Not promotional. Almost no official/doc links: repos only, no articles.
- **Unique value:** (1) **Jev Review Action**: a worked example of using Jev as a PR/submission reviewer. Its design is transparent: Jev picks up to six source files, then a separate Jev call judges the checks, with accept/reject thresholds (uses_jev accept 0.85 / reject 0.2, category confidence 0.7). (2) The widest multi-language SDK coverage in this batch: Go, Rust, Elixir, Ruby, PHP, .NET, Swift, Scala/ZIO, Laravel, Rails. (3) Many infrastructure integrations: GPTCache, Milvus, SQLite, Postgres, Hono, Spring WebFlux, LiteLLM routers.

## Facts claimed about Jev
- **Choice cap of 255 options.** jev-tree does recursive Choice over a taxonomy to go past it.
- Model id `jev-latest` (ask-jev-skill, ha-conversation-jev).
- swift-typesafe follows "the Python SDK's 0.6.0 API". This matches the Python SDK v0.6.0 release in fanly/Jev-awesome.
- **jevkit sends requests to an `/api/alpha/decisions` endpoint.** This differs from `/v1/systemone` and may be a legacy/alpha path or a mistake. Compare wh000wh000's migration note from `/preview/evaluation`.
- **OpenRouter has a "Decisions endpoint"** that nexibeo/jev-cookbook uses to call Jev.
- Jev launched **15 September 2026** (per jev-phishing-bench).
- Jev is reachable via Vercel AI Gateway or TypeSafe directly (unclutter).
- The review workflow sends README, manifests, candidate paths and selected source contents to TypeSafe. Reports record model version, usage and a policy hash. It allows up to 10 files and 48,000 characters of file content.

## Key insights / patterns
- **Jev as a CI reviewer** (Jev Review Action):
  - Two-stage process: a selection call chooses files without seeing their contents, then a judgment call reads them.
  - Thresholds live in a public JSON policy.
  - Uncertain results go to maintainer review, and provider failures are reported as failures, never as favorable reviews.
  - The model is advisory and never merges.
- **Recurring developer-tool patterns:**
  - Pre-commit/pre-push gates: jev-commit (blocks only on credentials), jev-git.
  - Claude Code Stop hook that checks "done" claims: jev-belay, which fails open.
  - Command auto-approval that fails closed: pi-jev-auto-mode.
  - Local classification of routine commands before any request: jev-axi.
  - CI test selection: Leanest.
  - Semantic circuit breaker for silent HTTP 200 failures: jev-resilience.
- **Semantic grep and SQL:**
  - `every` asks a yes/no question of every function.
  - jgrep batches 16 Noul checks per request.
  - Neovim quickfix ranking: jev.nvim.
  - SQLite/Postgres extensions.
- **Ranking from pairwise Noul:** jsort fits a local Bradley-Terry scale. jlink does record linkage with local candidate blocking. jselect does budgeted evidence selection with diversity.
- **Routers:**
  - Model plus effort picked per turn, with deterministic prefiltering by protocol/context (Jevonian).
  - Fix the routing decision for the session (pi-jev-router).
  - A LiteLLM-based router (prismhq/jev-router).
- **Cache validation:** GPTCache uses Noul to decide whether a cached answer serves a new request.
- **Games** follow a strict split: deterministic code owns routes, arithmetic and legal moves, and Jev picks only at branches. jev-plays-pokemon-red also scores faint predictions by Brier score.
- jev-skip catches 77% of SponsorBlock sponsor seconds over 23 videos for about $0.0008 (truncated in the source).

## Standout entries
- [typesafe-ai/typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) — official Python client (official)
- [typesafe-ai/typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) — official JS/TS client with question builders (official)
- [fatwang2/jev-review-action](https://github.com/fatwang2/jev-review-action) — GitHub Action using Jev to review submissions/PRs (developer tools)
- [reachjalil/jev-tree](https://github.com/reachjalil/jev-tree) — recursive Choice beyond the 255-option cap (SDK/pattern)
- [keltokhy/jsort](https://github.com/keltokhy/jsort) — pairwise Noul + Bradley-Terry ranking (search)
- [zilliztech/GPTCache](https://github.com/zilliztech/GPTCache) — semantic cache with Jev evaluator (integration)
- [milvus-io/milvus-model](https://github.com/milvus-io/milvus-model) — Milvus reranker adapter (integration)
- [mattn/sqlite3-jev](https://github.com/mattn/sqlite3-jev) — SQLite extension (integration)
- [yusukebe/hono-jev-router](https://github.com/yusukebe/hono-jev-router) — natural-language HTTP routing (integration)
- [valentynkit/jev-belay](https://github.com/valentynkit/jev-belay) — Claude Code Stop hook verifying done claims (developer tools)
- [baronunread/leanest](https://github.com/baronunread/leanest) — CI test selection (developer tools)
- [jourdanlabs/assay-001](https://github.com/jourdanlabs/assay-001) — pre-registered verification of calibration claims (research)
- [anessbelbati/jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench) — Jev vs Cohere Rerank 4 vs zerank-2 on 14 datasets (research)
- [zilliztech/deep-searcher](https://github.com/zilliztech/deep-searcher) — search-stopping evaluation (research)
- [valentynkit/jev-plays-pokemon-red](https://github.com/valentynkit/jev-plays-pokemon-red) — Brier-scored game agent (games)
