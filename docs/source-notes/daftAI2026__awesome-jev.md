# daftAI2026/awesome-jev
- **One-liner:** Auto-collected directory of ~2,188 Jev/System One GitHub projects (awesomejev.cc), admitted by Jev itself, plus a 213-item Chinese Jev news archive from AIHOT.
- **Language(s):** English (README/docs); news archive (data/news.json) mostly Chinese; site in EN/ZH/JA
- **Type:** auto-generated-list
- **Scale:** Badge says 2,188 projects (~2,190 links) in: Agents & automation, Browser & computer use, SDKs & integrations, Developer tools, Research & evaluation, Learning & resources, Project directories, Apps & demos, Open-source alternatives, Other. Plus data/news.json (213 news items), docs/ (architecture, data-model, collector, news, design, directory-ui).
- **Quality flags:** Fully automated GitHub radar; broad inclusion pulls in generic big repos (composio, pydantic-ai, openharness, openclaw/docs) whose connection to Jev may be incidental; many descriptions are placeholder "X: TypeSafe Jev ecosystem repository." Ordering by stars. Honest about limits (thresholds "not calibrated accuracy guarantees"; admission is not a security endorsement). News items are summaries of X/tweets and blogs, some hype/jokes ("quantum Jev 0.12ms") — unverified.
- **Unique value:** (1) The collector itself is a well-documented real-world Jev pipeline (Noul+Choice+Choice in one request with confidence thresholds, prompt-injection guard, budgets). (2) Separate "Open-source alternatives" section. (3) The news archive is a dense source of dated ecosystem facts: pricing, OpenRouter model IDs, benchmarks, third-party comparisons, competitor launches.

## Facts claimed about Jev
(From README/docs unless marked [news] = data/news.json summaries of third-party posts)
- Official launch blog: https://typesafe.ai/blog/introducing-system-one-models-and-jev. Console/API keys: https://console.typesafe.ai/settings/keys. API docs https://docs.typesafe.ai/api. Model id used: `jev-latest`. Env secret `TYPESAFE_API_KEY`.
- Primitives Noul / Choice / Score; multiple questions per request.
- [news] Endpoint `POST https://api.typesafe.ai/v1/systemone`; Jev is Transformer-based but does not generate text.
- [news] Launch: announced Sept 15/16, 2026 (both dates appear); OpenRouter Decisions API early access 2026-09-15, model ID **`typesafe/jev-1.13`**; versions referenced "Jev 1.13" / "Jev 1.13.0". Also `typesafe/jev-router` on OpenRouter (auto-picks model + reasoning effort; test: $0.008 vs $0.018, 1.5s vs 1.9s median vs fixed GPT-6 Sol).
- [news] Pricing: **$0.042 per million input tokens, output tokens free** (repeated many times; Simon Willison: below GPT-5 Nano's $0.05).
- [news] Launch claims (founder @CompleteSkeptic, co-inventor of ChatGPT): "20–200× faster, 40–400× cheaper"; vendor-reported "193.6× speed, 444.6× cost advantage"; response time "70 to 500 ms"; "does not hallucinate" guarantee only covers output structure.
- [news] Training method: **RLCD** (reinforcement learning for calibrated decisions), unpublished. CEO Diogo Almeida (ex-OpenAI RLHF). One item mislabels CEO as "Jev". TypeSafe declines to publish benchmarks / API-level refusals.
- [news] Signups paused due to demand surge; access via waitlist.
- [news] Known-issues page: https://docs.typesafe.ai/model-jaggedness/jev-1.13; Discord channel "model-jaggedness"; TypeSafe: Jev "still too slow, too expensive, too dumb".
- [news] Benchmarks: OpenRouter Banking77 (3,080 items): Jev 1.13 81.0% vs Claude Opus 5 84.4%; median latency 175 ms vs 2,266 ms; $0.11 vs $2.42 per 1k requests. OpenRouter ticket triage: $0.0248 per 1,000 tickets, median 194 ms. OpenRouter Ori Eval: >5× faster than next-fastest model. MotherDuck `prompt_jev()` SQL function: 100k rows in 40 s for $0.50 vs LLM 32 min/$37 (~50× faster). Tomer Tunguz: 98 production email threads, Jev 80% vs local SemIf 82% vs production model 47%; 76×–209× cheaper. Metaview: ~10× faster candidate search. 2.3K papers re-labelled for $0.14 in ~83 s (75% agreement with DeepSeek V4 Flash labels). JevBench v1.4.1: 534 public + 308 sealed decisions, 77 systems, Jev 1.13.0 top with 77 points (JevK5 v0.2.0, Hopper 2nd/3rd); earlier JevBench: GPT-5.6 Luna more accurate on hard items but Jev leads composite. Jev-vs-LLM-as-a-Judge: parity accuracy on closed rubrics with evidence provided, 1/5 cost, 1/10 latency. JEV-as-a-Judge paper: within 3 pp of SOTA judge at 0.36% cost; cascade keeps ~99% of GPT-6 accuracy at ~57% cost (510 preference pairs). Independent test: 24 Norwegian docs median 0.32 s; ECE rose 0.040→0.116 when qualifiers added. OpenAI Decisions API (Luna, ~150 ms) beat Jev in some Every tests (76/78 vs 73/78; 230 ms vs 500 ms) and lost others.
- [news] Integrations: OpenRouter (Decisions API, Classifiers), Vercel (first to integrate), Pydantic AI (output_type becomes the question, per-field confidence), DSPy 3.4.0 (native support + ReAnchor calibration optimizer), Simon Willison `llm-typesafe` 0.1a0 (noul returns `{"type": "noul", "noul": 0.99}`), OpenClaw core decision-model support, MotherDuck, Treg. Official TypeSafe Python SDK 0.7.1 mentioned (Ollaya compatibility). Jev took 27% of OpenRouter weekly classification requests (~2× DeepSeek V4 Flash).
- [news] Negative results: maze test — Jev took 2,306 steps stuck in corner vs random RNG 892 steps; "Jev with no web search confidently gives wrong output"; 70 ms latency too slow for HFT.
- [news] Competitors/alternatives: Laya (Convai, 32.8 ms, "7.8× faster", Apache-2.0), CLM-8B (Stanford/NVIDIA, "up to 9× faster"), Kev (0.8B/4B/9B Qwen3.5 LoRA + pointer head), GLiNER2.5-Decide (340M), Julia 1 (144.3M), Drex (NaceAI, $0.04/1M input), Liquid AI d1, together/Tev1-4B-experimental ($17 fine-tune), Jeeves (PostHog), OpenAI Decisions API.

## Key insights / patterns
- Collector pattern: ask `jev-latest` in one request `about` (Noul), `keep` (Choice), `category` (Choice); accept only keep with about ≥ 0.9 and keep-confidence ≥ 0.9; route low-confidence to a 7-day review queue; don't apply strict thresholds to navigation labels; treat README/code as untrusted evidence; "a crafted repository can still mislead a relevance model."
- Budgeting: 2,000 Jev HTTP attempts/day with counters; stop reviews on auth/service failure.
- Recurring use cases in listing: coding-agent model/effort routers (jev-router, jev-codex-router, agent-router), tool-call guardrails (jev-guard deny/ask/allow, pi-warden), context sieves (winnow), skill ranking (skillranker), games/robotics (Mario, LIBERO, drones), GTM lead scoring.
- [news] Best practices: decompose agents into smallest semantic units, set own thresholds, fix bugs by adding questions not editing system prompts (Metaview); cascade — accept high-confidence Jev, escalate low-confidence to frontier model; Jev pairs well with retrieval/web search (Exa) since it lacks world knowledge.

## Standout entries
- [TypeSafe launch blog](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — official announcement (official)
- [skills](https://github.com/typesafe-ai/skills) — official agent skills for System One API (official)
- [jev-docs-zh](https://github.com/Bald0Wang/jev-docs-zh) — Chinese translation of official docs (learning)
- [jev-cookbook (datawhalechina)](https://github.com/datawhalechina/jev-cookbook) — Chinese notebook tutorial, 18 recipes, eval & local fine-tuning (tutorial)
- [jev-cookbook (nexibeo)](https://github.com/nexibeo/jev-cookbook) — tested recipes on OpenRouter (tutorial)
- [jev-crash-course](https://github.com/nadeemcite/jev-crash-course) — 11-level course with capstone + evals (tutorial)
- [jev-deep-dive](https://github.com/LouisUltra/jev-deep-dive) — evidence-graded bilingual deep dive with probe tools (research)
- [jevals](https://github.com/openlayer-ai/jevals) — agent evals/guardrails as Jev decisions (eval)
- [jev-guard](https://github.com/leepokai/jev-guard) — deny/ask/allow tool-call risk scoring for coding agents (security)
- [winnow](https://github.com/GhalebDweikat/winnow) — calibrated context sieve for Claude Code (agent tooling)
- [skillranker](https://github.com/Dicklesworthstone/skillranker) — Rust CLI ranking agent skills with abstention (agent tooling)
- [Decis](https://github.com/chaitin/Decis) — self-hosted /v1/systemone-compatible API on Laya/kev (alternative)
- [laya-mlx](https://github.com/mizorewww/laya-mlx) — 7–14 ms MLX runtime for Laya (alternative)
- [jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas) — where Jev holds up vs breaks (evaluation)
- [instruct-jev](https://github.com/ctaxnagomi/instruct-jev) — 119-row choice/noul/score instruction corpus (dataset)
