# yangzhou-chaofan/awesome-jev-prompt
- **One-liner:** "Prompt" (state + question) pattern collection for Jev plus a star-ranked Top-30 showcase of early community builds, with a detailed source registry and a companion HTML gallery on neta.art.
- **Language(s):** English (source notes include some Chinese filenames)
- **Type:** prompt-collection (with a use-case showcase and an unusually detailed sources/verification file)
- **Scale:** data/prompts.json: 7 sections, ~42 entries (Primitives; State formats; Architectural patterns (4); Official cookbooks (16 URLs); Case study — typesafe-mario state schema; Official demos (Doom, Wikiracing); Community patterns). README: Top 10 table + "Worth studying" (5) + six-cluster summary; data/community.json: 119 repos + 15 X posts (badges say 222 tracked / 135 tracked — inconsistent). SOURCES.md: 39 sources with verification status. site/: gallery, patterns, use-cases, videos subsites with 229 preview cards. data/raw: Discord #show-and-tell scrapes (714 links).
- **Quality flags:** Snapshot frozen at 2026-09-17/18 (launch week) — stale star counts (e.g. browser-use 1052★ vs 16.6k elsewhere) and old repo names (TheoLeeCJ/openjev). Internal inconsistencies in counts (222 vs 135 vs 119+15; "Top 100" site vs "Top 30"). SOURCES.md references agent workspace paths (`/workspace/typesafe-ai-情报汇总.md`), suggesting AI-agent-generated content. Promotes a companion page on neta.art. The "prompts" are mostly paraphrased official docs; limited original prompt content beyond the Mario state schema. Honest "Known gaps" section.
- **Unique value:** (1) SOURCES.md is a rich primary-source dossier on TypeSafe the company (funding, investors, hiring, blog posts, homepage claims, evals numbers). (2) Full index of the 16 official cookbook URLs. (3) Verbatim Mario state schema as a canonical "state as data structure" example. (4) First-hand Discord #show-and-tell scrape indicating pre-launch early access since Jul 22.

## Facts claimed about Jev
- Jev launched **2026-09-15**; "TypeSafe AI's first System One Model"; badge "Jev 1.13". 568+ GitHub repos touching it within 72 hours (GitHub search "jev", created > 2026-09-01, on 2026-09-17).
- typesafe.ai homepage h1: "We took the opposite research direction / **193.6x Faster, 444.6x Cheaper**."
- Models & pricing: `jev-1.13.0`, alias `jev-latest`: **$42/Btok ($0.042/MTok) input-only; 250k tok/s; 1,200 req/min**.
- Workflow evals site: **Jev 67.8% / $0.0004 / 0.4s vs opus 5 73.1% / $0.1761 / 37.8s** (per-model accuracy/cost/latency). (Anthony Maio, cited in thevibeworks, compares Jev 67.8% to GPT Sol 74.1%.)
- Latency claim in README: all questions evaluated in parallel "in 70–500ms".
- Docs: System One naming from Kahneman; "cannot hallucinate" = schema guarantee (not correctness).
- Funding: **$40M seed led by DCVC** (Business Wire press release 2026-09-15); founded 2024, HQ San Francisco; valuation ~$200M per secondary source only (unconfirmed). ts2.tech: 445x cost claim "still self-reported".
- GitHub org typesafe-ai: 10 public repos, 187 followers (at 2026-09-17); adapter-python 63★, sdk-js 57★, skills 56★, sdk-python 33★.
- HN launch thread: **1,835 pts / 482 comments** (at capture).
- TypeSafe blog posts: "Lies, Damned Lies, and Benchmarks" (antibenchmaxxing, 2026-09-11 — no public benchmark tables; evals as dated retired snapshots); "The Bitterest Lesson" (2026-09-10); Manifesto "Composable AI — Build Prod, Not God" (neuro-symbolic "smart if-statements").
- Launch demos: Doom at **10 Jev queries/second**, ~**$7/hour** of inference, state is structured game data not images; Wikiracing — Choice cardinality **up to 255**, two-stage scoring for high-cardinality picks.
- Hiring: 4 roles on Ashby; $150k–250k + equity; stack Python, TS/Next/Tailwind, K8s.
- Discord #show-and-tell history from **Jul 22** (pre-launch early-access builders).
- Example output shape shown in README (`{"choice": "right_jump", "p": 0.87, "confidence": 0.93}`) is illustrative/simplified, not the official response schema.

## Key insights / patterns
- State formats: string (single text), object (recommended default; named fields "like material you'd hand a panel of experts"), array (conversation turns). Put conversation + records + policy in one state so questions compare parts.
- Canonical patterns: speculative fan-out, confidence-gated routing ("the core production loop"), composite scoring, intent routing at the front door.
- Game/control loops: telemetry/RAM → structured JSON → Jev Choice → controller input, decision every N steps; log each decision with latency, probabilities, confidence (Mario, Doom). Model never sees a screenshot.
- High-cardinality choices: two-stage scoring when options exceed practical limits.
- Community clusters in first 72 hours: agents & computer use (45+), devtools/SDKs/MCP (30+), games (12), guardrails (8, incl. agent-control-plane with Dafny proofs), replicas & benchmarks (10), trading & data (4).
- Contributing rule worth adopting: one entry = one decision (state + questions + primitive); mark verbatim vs reconstructed; date your numbers.

## Standout entries
- [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — launch post (official)
- [Manifesto](https://typesafe.ai/manifesto) — Composable AI, "Build Prod, Not God" (official)
- [Lies, Damned Lies, and Benchmarks](https://typesafe.ai/blog/antibenchmaxxing) — TypeSafe's eval philosophy (official)
- [Docs: State](https://docs.typesafe.ai/concepts/state) — state formats (official docs)
- [Workflow evals](https://evals.typesafe.ai/) — per-model accuracy/cost/latency (official benchmark)
- [SDE cascade cookbook](https://docs.typesafe.ai/cookbooks/sde_cascade) — verify-and-escalate (official cookbook)
- [Hierarchical classification cookbook](https://docs.typesafe.ai/cookbooks/hierarchical_classification) — taxonomy walking (official cookbook)
- [Self-consistency choice cookbook](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook) — consistency pattern (official cookbook)
- [fhshaik/typesafe-mario](https://github.com/fhshaik/typesafe-mario) — canonical structured-state game loop (case study)
- [jerryjliu/docjev](https://github.com/jerryjliu/docjev) — LlamaIndex founder's document classification (project)
- [phyous/tsai-sc](https://github.com/phyous/tsai-sc) — Jev beats a StarCraft mission (project)
- [vinnylarouge/jevlike](https://github.com/vinnylarouge/jevlike) — reverse-engineered option-attention head (open model)
- [TypeLLM/TypeLLM](https://github.com/TypeLLM/TypeLLM) — type-safe generation generalizing the contract (project)
- [HN launch thread](https://news.ycombinator.com/item?id=49717558) — skeptical and technical discussion (discussion)
- [Business Wire press release](https://www.businesswire.com/news/home/20260915525333/en/) — $40M seed led by DCVC (news)
