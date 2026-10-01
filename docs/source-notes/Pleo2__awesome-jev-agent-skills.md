# Pleo2/awesome-jev-agent-skills
- **One-liner:** Five installable Codex/Claude Code agent skills (diff review, test coverage, failure triage, extraction review, QA evidence) that call Jev via a stdlib-only Python client.
- **Language(s):** English, Spanish (README.es.md)
- **Type:** skills-collection (project/code, not a link list)
- **Scale:** 5 skills (jev-diagnose-failures, jev-test-coverage, jev-review-diff, jev-extraction-review, jev-qa-evidence), each with SKILL.md, references/protocol.md, examples/request.json, scripts/ask.py; shared tools/ (ask.py, protocol.md, sync_skills.py), unit tests, CI (offline, no secrets). Install: `npx skills add Pleo2/awesome-jev-agent-skills --skill <name>`.
- **Quality flags:** Small but well-engineered and honest ("advisory", "smoke check, not a benchmark", no universal thresholds). Not an awesome list despite the name. No inflated claims. Independent/community; doesn't bundle the official TypeSafe skill.
- **Unique value:** Original, reusable skill code plus a careful protocol for using Jev as an advisory evaluator inside coding agents — including data-sanitization and security hygiene for requests.

## Facts claimed about Jev
- Endpoint `https://api.typesafe.ai/v1/systemone`; request `{model: "jev-latest", state, questions}`; question object `{type: "choice"|"noul"|"score", instructions, criteria}`.
- Response fields used: `model` (resolved model), `answers`, `usage` (tokens); client also reports elapsed time.
- Noul has no separate confidence field.
- API key env vars accepted by the client: `TYPESAFE_API_KEY`, `TYPESAFE_AI_API_KEY`, or `JEV_API_KEY`.
- Official docs referenced: https://docs.typesafe.ai/api.md, /llms.txt, /concepts/use-case-map, /cookbooks/citation_check.md, /primitives.md.
- Client-side conservative limits (explicitly not service limits): 30-second timeout, no automatic retries, max 20 questions, 64 KiB per request; refuses HTTP redirects.

## Key insights / patterns
- Jev as **advisory** evaluator: the development agent keeps control of implementation, tool execution and final verification; verify actionable findings with source inspection, deterministic validation, or executed tests.
- Question IDs are not instructions — put the full meaning and relevant state paths into each question's instructions.
- Independent questions share one request; dependent questions need the prior result plus new evidence (sequential calls).
- One explicit invariant per question; always include an "insufficient evidence" option (e.g. criteria preserved / violated / insufficient).
- Use Choice for mutually exclusive outcomes, Noul for yes/no, Score for explicitly ordered levels.
- Security hygiene: send minimal sanitized snippets, strip secrets/PII/proprietary data, never send env files or whole repos; treat source text, comments and logs as evidence, never instructions (prompt-injection defense).
- Service failure ≠ negative finding — report evaluation unavailable and continue local verification.
- Check numeric calculations, identifiers and exact spans with code; inspect test assertions rather than test names.
- Report model judgment separately from independent evidence; log resolved model, latency and token usage; don't tune examples to force agreement.

## Standout entries
- [jev-review-diff](https://github.com/Pleo2/awesome-jev-agent-skills) — `skills/jev-review-diff/SKILL.md`: invariant-based semantic diff review (skill)
- [jev-test-coverage](https://github.com/Pleo2/awesome-jev-agent-skills) — `skills/jev-test-coverage/SKILL.md`: missing behavioral test scenarios (skill)
- [jev-diagnose-failures](https://github.com/Pleo2/awesome-jev-agent-skills) — `skills/jev-diagnose-failures/SKILL.md`: failure triage / next diagnostic check (skill)
- [jev-extraction-review](https://github.com/Pleo2/awesome-jev-agent-skills) — `skills/jev-extraction-review/SKILL.md`: extracted fields vs source text (skill)
- [jev-qa-evidence](https://github.com/Pleo2/awesome-jev-agent-skills) — `skills/jev-qa-evidence/SKILL.md`: completion claims vs evidence (skill)
- [TypeSafe use-case map](https://docs.typesafe.ai/concepts/use-case-map) — official concept doc (official)
- [Claim verification cookbook](https://docs.typesafe.ai/cookbooks/citation_check.md) — official cookbook (official)
