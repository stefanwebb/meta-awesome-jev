# ozers/jevsome-projects
- **One-liner:** Deliberately short list of 72 open-source projects that provably call Jev, each linked to the exact source line proving the call; daily-refreshed pipeline and site.
- **Language(s):** English
- **Type:** auto-generated-list (pipeline-generated, strict proof-of-call filter)
- **Scale:** 72 listed (782 more candidates in JSON; 1,210 search hits examined; refreshed 2026-09-30). Sections: SDKs & clients (8); Integrations (1); Agent tooling (27); Browser & computer use (6); Applications (14); Games & simulation (8); Demos & playgrounds (5); Benchmarks & research (3). Site: jevsome.ozersubasi.com. `data/not-listed.json`: 351 with no Jev call found, 5 found but not Jev-centric.
- **Quality flags:** Generated from data/index.json; classification by keyword rules. Strong anti-noise bar (proof line, created after Jev launch or Jev-named, real code not mocks, ≥5 stars, daily health). But some proof lines point to test cassettes (system-one-adapter-python) despite the "not a cassette" rule; some descriptions are placeholder GitHub text (e.g. a video URL). One odd inclusion: http4k (Kotlin HTTP toolkit, 2,789★) in Applications despite "subject, not support" rule. Star counts differ markedly from RadRebelSam's same-day snapshot (typesafe-sdk-js 101 here vs 258 there) — one of the two is stale or wrong.
- **Unique value:** Line-level proof links (verifiable evidence Jev is actually called); explicit, written inclusion bar; negative list of rejected repos; activity-status icons.

## Facts claimed about Jev
- API surface used for discovery: calls to `/v1/systemone`, SDK imports, pinned `jev-latest` route, declared dependency; env `TYPESAFE_API_KEY`.
- Community-reported claims in entries: typesafe-computer-use "about $0.0002 a step"; jev-voice-browser "~300 ms per spoken word"; jev-drone "Jev in the loop at 2.5Hz"; mayank953/Jev restates vendor figures "70–500 ms, $0.042 per 1M input tokens"; jev-browser-use "5–10x faster browser operations".
- Star counts (2026-09-30 per this list): jev-ultrafast 3,969; fast-jev-compaction 2,191; jev-trader 707; JevRev 497; jev-align 297; foreman 254; typesafe-mario 252; typesafe-sdk-js 101; system-one-adapter-python 98; typesafe-sdk-python 70.

## Key insights / patterns
- Verifying "uses Jev" requires code evidence; README mentions and package names are unreliable (and "typesafe" is a noisy search term).
- Dominant cluster is agent tooling for coding agents: context compaction (fast-jev-compaction, save-token-jev-clean), model/agent routers (jev-router, agent-router, switchboard), tool-call gates/auto-approve (pi-warden, pi-jev-auto-mode fails closed), MCP servers, semantic linters (JevLint, perch).
- Games pattern: code generates legal moves/facts, Jev picks one per tick (typesafe-snake, mario-jev with RAM observations).
- LLM plans / Jev decides split (jev-browser, mcp-ui-poc "Claude Haiku writes only when confident…").

## Standout entries
- [typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) — official TS SDK (official)
- [jev-recipes](https://github.com/agencyenterprise/jev-recipes) — 200+ plug-and-play decision recipes (library)
- [dspy-typesafeify](https://github.com/typesafeainate/dspy-typesafeify) — DSPy decorator using TypeSafe (integration)
- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) — Claude Code compaction via Jev scoring (agent tooling)
- [hono-jev-router](https://github.com/yusukebe/hono-jev-router) — semantic HTTP router for Hono (agent tooling)
- [jev-ultrafast](https://github.com/browser-use/jev-ultrafast) — browser agent with indexed action space (browser)
- [mobile-jev](https://github.com/droidrun/mobile-jev) — Android/mobile control demo (computer use)
- [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) — macOS computer use ~$0.0002/step (computer use)
- [jev-trader](https://github.com/jarrodwatts/jev-trader) — per-block trade decisions on Monad (application)
- [commit-miner](https://github.com/devanshbatham/commit-miner) — classify commits/CWEs (application)
- [jev-drone](https://github.com/RomanSlack/jev-drone) — MuJoCo drone with Jev at 2.5Hz (simulation)
- [jev-align](https://github.com/sutro-sh/jev-align) — calibrated AI functions from human feedback with GEPA (tooling)
- [jev-experiments](https://github.com/dabit3/jev-experiments) — latency-focused demos (demos)
- [jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks) — calibration/selective-risk eval framework (benchmark)
- [jev-eval-agent](https://github.com/vinilana/jev-eval-agent) — eve agent with 100 mocked tools benchmark (benchmark)
