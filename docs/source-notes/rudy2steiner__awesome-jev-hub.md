# rudy2steiner/awesome-jev-hub
- **One-liner:** Small, English-first developer hub for Jev: four-path quick start (Playground, cURL, SDKs, agent skill) plus 30 curated resources across ten categories.
- **Language(s):** English (canonical) + Chinese quick-start (README_CN.md)
- **Type:** curated-list (with tutorial quick start)
- **Scale:** ~40 links; 30 community resources, 3 per category. Sections: Run Jev Now, Jev on One Screen, Know Before You Build, Recently Added, Official & Access, Skills & Agents, Developer Ecosystem, Patterns & Cookbook, Projects by Use Case, Playgrounds & Reproducible Demos, Benchmarks & Evidence, Failures & Limitations, Learn, Open Alternatives, Ecosystem Radar. Has validation script/tests, issue template, docs/superpowers plans/specs (AI-agent planning artifacts).
- **Quality flags:** Young (seeded 2026-09-21), small, likely AI-assisted (superpowers plan/spec docs). Descriptions are sober and emphasize reproducibility. Lists "TypeSafeAI on GitHub" (github.com/TypeSafeAI) as a first-party-ish radar source and "TypeSafe AI Community Playground" from that org — note the official org elsewhere is `typesafe-ai`; the TypeSafeAI org may be unofficial (unverified). Minimal duplication risk.
- **Unique value:** Clean, correct copy-paste quick start for Python, TypeScript, cURL and the agent skill; "Failures & Limitations" category with less-common entries (Winnow Jev contract, Jev Capability Atlas, Jev Is Odd arithmetic probe); non-Python SDKs (Ruby, Elixir).

## Facts claimed about Jev
- API: `POST https://api.typesafe.ai/v1/systemone`, `Authorization: Bearer $TYPESAFE_API_KEY`, body `{state, model: "jev-latest", questions: {urgency: {type: "noul", instructions}}}`. Keys at console.typesafe.ai/keys.
- Python: `python -m pip install typesafe-sdk`; `from typesafe_sdk import Noul, TypeSafeClient`; `client.system_one(state=..., questions={...})`; `response.answers["urgency"].noul`. Requires Python 3.10+.
- JS/TS: `npm install @typesafe-ai/sdk`; `import { choice, TypeSafeClient } from "@typesafe-ai/sdk"`; `await client.systemOne({state: {document: ...}, questions: {category: choice("...", {billing: null, technical: null, other: null})}})`; `response.answers.category.choice`. Requires Node.js 20+.
- Agent skill: `claude plugin marketplace add typesafe-ai/skills` + `claude plugin install typesafe@typesafe-ai`; or `npx skills add typesafe-ai/skills --skill typesafe-ai` (project-local default; `-g` global).
- One request can mix Noul, Choice, Score questions.
- Jaggedness doc covers arithmetic, dates, indirection, irrelevant context, adversarial content, structured generation.

## Key insights / patterns
- Prefer the official API reference over copied examples; model and SDKs change quickly.
- Record model name, input, question definitions and expected output shape for reproducibility.
- Treat community benchmarks as evidence for a specific setup, not universal rankings.
- Recurring project patterns: bounded Jev judgments for coding-worker supervision (completion, test sufficiency, progress, escalation — Foreman); shadow mode + confidence thresholds (pi-jev); Jev advisory in control loop with deterministic safety controls (jev-drone); Jev chooses search parameters and reranks, returning links not generated answers (Jev Search).

## Standout entries
- [Quick Start](https://docs.typesafe.ai/introduction/quickstart) — official walkthrough (official)
- [Playground](https://console.typesafe.ai/playground) — browser playground (official)
- [Official TypeSafe Skill](https://github.com/typesafe-ai/skills/tree/main/skills/typesafe-ai) — teaches agents primitive selection and question design (official)
- [How to Build with System One](https://docs.typesafe.ai/concepts/how-to-build-with-system-one) — design guide (official)
- [Jevify](https://github.com/altryne/jevify) — audits a codebase for Jev decision points (skill)
- [Jev MCP](https://github.com/jkudish/jev-mcp) — Jev workflows as MCP tools (integration)
- [ruby_decision_model](https://github.com/obie/ruby_decision_model) — Ruby interface (SDK)
- [Jevex](https://github.com/kentaro/jevex) — Elixir composition with confidence gates (SDK)
- [TypeSafe Jev Examples](https://github.com/rajivkuriakose/typesafe-jev-examples) — Python examples with offline policy tests (tutorial)
- [Jev RAG Benchmark](https://github.com/erendikmenn/jev-rag-benchmark) — 1,044-query Turkish XQuAD with negative results (benchmark)
- [Jev Is Odd](https://github.com/robipop22/Jev-is-odd) — arithmetic probe (limitations)
- [Winnow Jev Contract](https://github.com/ThinkyMiner/Winnow/blob/main/docs/jev-contract.md) — observed live-API behaviour and defensive rules (limitations)
- [Jev Capability Atlas](https://github.com/Zaious/jev-capability-atlas) — strong/weak task shapes with receipts (limitations)
- [Foreman](https://github.com/thruwire/foreman) — coding-worker supervision (project)
- [Jev Voice Browser](https://github.com/moritzkremb/jev-voice-browser) — voice browser control with latency measurements (demo)
