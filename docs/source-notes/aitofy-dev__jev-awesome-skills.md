# aitofy-dev/jev-awesome-skills
- **One-liner:** npm package + CLI + eight agent skills (Claude Code, Codex, Cursor, Grok) that use Jev to decide proceed/ask/stop, route skills, guard commands, verify claims, triage, review, act.
- **Language(s):** English
- **Type:** skills-collection (project/code)
- **Scale:** 8 skills: jev-awesome-skills (policy), jev-gate, jev-route, jev-guard, jev-verify, jev-triage, jev-review, jev-act; request/response JSON templates; TypeScript src (redact, guard, judge, branch, parse, cli); tests; llms.txt / llms-full.txt. "In the wild" table of 11 related projects.
- **Quality flags:** Real, small, dependency-free code (Node 20+, ESM, MIT, no telemetry). Opinionated fixed thresholds. AGENTS.md is a generic company engineering-rules file (mentions Chrome/fingerprint — copied boilerplate from another Aitofy product). Not spammy; not a list.
- **Unique value:** Concrete, reusable proceed/ask/stop policy with numeric cutoffs; secret redaction before the request body is built; explicit fail-open semantics (`source: "fallback"`, no fake probabilities); ready-made request templates showing full HTTP schema.

## Facts claimed about Jev
- Live calls: `POST https://api.typesafe.ai/v1/systemone` with model `jev-latest`; key from env `TYPESAFE_API_KEY`. Questions in one request share one state.
- Request schema (examples/gate.request.json): `{ state: {...}, model: "jev-latest", questions: { name: { type: "choice"|"noul"|"score", instructions, criteria } } }` — choice criteria is an object label->description; score criteria is an ordered array.
- Response schema (fixture): `answers.pick {type:"choice", choice, confidence, probabilities{}}`, `answers.determined {type:"noul", noul}`, `answers.harm {type:"score", score, confidence, legend{"0":...,"1":...,"2":...}, probabilities{"0":..}}` (legend as index-keyed object here, unlike array in some other lists — fixture, not live data).
- Redaction patterns include `sk-...`, `jv_live_...`, `TYPESAFE_API_KEY=` — suggesting (not stated) TypeSafe keys may use a `jv_live_` prefix.
- Jev returns probabilities only for closed choice/noul/score; does not write code.

## Key insights / patterns
- Three-question gate over one state: `pick` (Choice incl. an `ask_user` option), `determined` (Noul: does context already determine the answer?), `harm` (Score 0-2: reversible / testable change / may destroy data, leak secret or leave task).
- Cutoffs: stop if harm.score >= 1.5 (stop wins); proceed if chosen-label probability >= 0.9 AND determined.noul >= 0.9; else ask. "guard is a stop, route is an ask, gate is a proceed. Same cutoffs, three jobs."
- Use the chosen label's probability, not `confidence`, for gating.
- Don't call Jev when one file/command already answers; stop for confirmation before calling Jev if you already know a command is destructive.
- Fail open on missing key/transport error/bad body — never invent a probability; decide yourself or ask the user.
- Redact secrets before building the request body; never print keys; dry-run and fixtures by default before network.
- "A proceed branch is not a passing test" — still run checks.
- Act skill: next action must come from an observed list ("no invented clicks"). Route: pass installed skill names as options, allow "none".

## Standout entries
- [aitofy-dev/jev-awesome-skills](https://github.com/aitofy-dev/jev-awesome-skills) — this package: 8 Jev agent skills + CLI (skills)
- [typesafe-ai/skills](https://github.com/typesafe-ai/skills) — official skill for writing Jev calls (official)
- [wuyoscar/jev-skill](https://github.com/wuyoscar/jev-skill) — large scenario collection for agents (skills)
- [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) — keep/delete history without rewriting (context)
- [Dicklesworthstone/skillranker](https://github.com/Dicklesworthstone/skillranker) — rank installed skills (skills routing)
- [ShivamPansuriya/jev-skill-gate](https://github.com/ShivamPansuriya/jev-skill-gate) — hide skills that don't fit the turn (skills routing)
- [DevMortimer/pi-warden](https://github.com/DevMortimer/pi-warden) — drift and unsupported "done" checks (guardrail)
- [dbreunig/building-with-jev-skill](https://github.com/dbreunig/building-with-jev-skill) — skill for designing questions (skills)
- [jkudish/jev-mcp](https://github.com/jkudish/jev-mcp) — Jev as MCP tools (MCP)
