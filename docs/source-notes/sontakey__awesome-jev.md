# sontakey/awesome-jev
- **One-liner:** Small, evidence-badged catalog (128 entries) of public projects that actually use Jev, with action-taking projects first. Includes an audit of the official GitHub org and skill-gap analysis.
- **Language(s):** English
- **Type:** curated-list (use-case collection with evidence badges)
- **Scale:** 128 entries, updated 2026-09-19. Sections: Action-taking projects (58) · Model and skill routing (7) · Email and inbox routing (2) · MCP and agent bridges (6) · Official cookbooks and patterns (4) · Official SDKs and adapter (3) · Official docs, skill, and launch demos (4) · Platform integrations (7) · Community clients (8) · Installable agent skills (9) · Other awesome-Jev lists (12) · Related, not TypeSafe Jev (8). Plus docs/catalog.md (per-entry caveats), docs/ideas.md, docs/skill-opportunities.md and docs/research-method.md. Data in data/use-cases.json.
- **Quality flags:** High integrity. Each entry carries an evidence badge (code-inspected / demo-inspected / documented-example / author-claim / proposed). It keeps open reproductions separate ("Related, not TypeSafe Jev"). It says vendor numbers are "attributed, not endorsed" and treats launch-week latency claims as marketing. The research was done by an agent pipeline (grok-4.6 lanes via Hermes), which is disclosed. It is deliberately small ("not inflating to match 400-entry auto-directories"). Sweep date 2026-09-17, so it may be getting stale.
- **Unique value:** A **full audit of the typesafe-ai GitHub org** (10 public repos with dispositions). A skill-install table with verified commands. Proposed safe "action contracts" (email triage, allowlisted model routing). An index of 12 sibling awesome lists with evaluations of each. Credits each project's author.

## Facts claimed about Jev
- "Jev does not chat, write code, or see images." It is **text-only** (per the official system-one.md). Computer-use tools OCR first.
- Quick start: Python `uv add typesafe-sdk`, JS `npm install @typesafe-ai/sdk`. Both need `TYPESAFE_API_KEY`. HTTP is `POST https://api.typesafe.ai/v1/systemone`. Docs index at docs.typesafe.ai/llms.txt.
- Skill: `npx skills add typesafe-ai/skills --skill typesafe-ai`, or `claude plugin marketplace add typesafe-ai/skills` then `claude plugin install typesafe@typesafe-ai`. The official skill is a design skill that "does not call Jev by itself".
- Official org `typesafe-ai` had public_repos=10: 4 product (typesafe-sdk-python, typesafe-sdk-js, skills, system-one-adapter-python), 3 supporting (daggerverse, Overwatch training dashboard referencing a private `typesafe-ai/Flow` and a private CodeArtifact `typesafe` package, typesafe-ai.github.io with the 2024 manifesto), and 3 forks (vllm, **LLaDA**, pulumi-clickhouse). The LLaDA fork is a diffusion-LM hint but is not interpreted by the list. There is no public repo for the Doom, Wikipedia-race or cookbook sources. Later, an official **n8n node** `typesafe-ai/n8n-nodes-typesafe-ai` is listed.
- The launch post is dated **2026-09-15**, by Diogo Almeida. It covers RLCD, pricing, workflow evals, and Doom and Wikipedia-race videos.
- system-one-adapter-python is a "Drop-in TypeSafeClient.system_one backed by OpenAI or Anthropic". This suggests the SDK method is `client.system_one(...)`, which contrasts with bakiabaci's `client.decide.noul`.
- Vercel: Jev is `typesafe-ai/jev` on AI Gateway, plus **AI SDK 7** `experimental_evaluate`.
- Official skill-suggestion cookbook: "Two Jev requests rank 182 Hermes skills and may suggest none."
- The smart-home demo uses speculative questions with an LLM fallback.
- Env var inconsistency: jev-router's README uses `JEV_API_KEY`, not `TYPESAFE_API_KEY`.

## Key insights / patterns
- Recurring architecture: Jev picks, code acts. Examples include browser agents where a small LLM only types text, Mario from RAM JSON rather than screenshots, and Unix exit codes (semdecide).
- Safety contracts, using email as the example: one request with `needs_reply` Noul, `department` Choice **including `none`**, `priority` Score and `sensitive` Noul. Apply labels only above a threshold set on your data. Write actions (reply, forward, archive, delete) require human review. **Fail closed** if the key is missing or the API errors. The GiesN demo "always routes and does not gate on confidence — do not copy that as production mail policy".
- Model routing should be allowlist-only (don't spill from a work key to a personal key). When uncertain, keep the pinned model.
- Publish-time citation brake: wire the citation-check Choice into a pre-commit or PR hook, and Jev never pushes.
- Skill routing is a strong cluster: SkillRanker, Pi Skill Picker, skillbox, and the official skill-suggestion cookbook. It lets agents see only the selected skills.
- Semantic lint: jev-lint checks what parsers can't ("does the function do what its name says", "is this comment still true").
- Not-ideas: native vision/audio/robot Jev (not in the API), another MCP clone.
- Copies of the official skill inside dotfiles are not unique skills.

## Standout entries
- [typesafe-ai/skills](https://github.com/typesafe-ai/skills) — official design skill (official)
- [typesafe-ai/n8n-nodes-typesafe-ai](https://github.com/typesafe-ai/n8n-nodes-typesafe-ai) — official n8n node with confidence thresholds (official integration)
- [Official skill-suggestion cookbook](https://docs.typesafe.ai/cookbooks/skill_suggestion) — rank 182 skills, may suggest none (official)
- [Official function-calling cookbook](https://docs.typesafe.ai/cookbooks/function_calling) — typed functions with closed-set args (official)
- [Vercel AI SDK evaluate](https://ai-sdk.dev/docs/ai-sdk-core/evaluation) — `experimental_evaluate` with Jev (integration)
- [peterfriese/jev-foundation-models](https://github.com/peterfriese/jev-foundation-models) — Jev with Apple Foundation Models Swift types (integration)
- [yamadashy/jev-labeler-action](https://github.com/yamadashy/jev-labeler-action) — GitHub Action for issue/PR labels (integration)
- [YaoApp/yao](https://github.com/YaoApp/yao) — Yao Agents decision_decide tool backed by Jev (framework)
- [jlowin/vibecheck](https://github.com/jlowin/vibecheck) — Python check/classify/score helpers (client)
- [dbreunig/building-with-jev-skill](https://github.com/dbreunig/building-with-jev-skill) — community skill for writing Jev programs (skill)
- [mizchi/jev-lint](https://github.com/mizchi/jev-lint) — semantic lint for what parsers can't check (code quality)
- [sdras/jev-webmcp-extension](https://github.com/sdras/jev-webmcp-extension) — WebMCP tool selection in Chrome (agent)
- [dabit3/jev-experiments](https://github.com/dabit3/jev-experiments) — latency-focused demos using the JS SDK (demos)
- [sutro-sh/jev-align](https://github.com/sutro-sh/jev-align) — active labeling + GEPA optimization (tool)
- [featherless-ai/simple-jev](https://github.com/featherless-ai/simple-jev) — open models via next-token logits (related/open)
