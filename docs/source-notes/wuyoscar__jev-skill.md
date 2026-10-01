# wuyoscar/jev-skill
- **One-liner:** "Awesome Jev Skills": 5 installable coding-agent skills (Codex/Claude Code/OpenCode), a `jev-decide` CLI, 108 scenario templates and 66 curated projects. It also has unusually transparent small evals with every raw request and response kept.
- **Language(s):** English, Chinese (README.zh.md)
- **Type:** skills-collection (plus curated-list and evals)
- **Scale:** ~489 files. README (171KB) sections: Projects (Demos, Apps, Local models, Tools & resources, More sources; ~66 entries) / Skills (install, update, setup, examples, CLI, habits, pitfalls) / Examples (108 scenarios grouped as: keep a long task on track; supervision, review & evaluation; routing, delegation & context; browser/desktop/interactive; and more). Skills: `jev`, `jev-triage`, `jev-documents`, `jev-eval`, `jev-act`. skills/jev/references has 25 reference docs (api, calibration, pitfalls, question-design, routing, context-and-throughput and others). The evals/ and docs/experiments/ folders hold pilot results with receipts. There are tests and CI.
- **Quality flags:** High effort and scientifically honest. It reports a negative result prominently (the Jev-assisted agent was *worse* in its 12-pair pilot) and labels every number as a small pilot. The version situation is confusing: published v0.2.0 had 11 entry points, and the 5-skill set is a "source preview". Parts appear AI-assisted ("claude" is listed as a contributor). Not promotional.
- **Unique value:** (1) **Original, reproducible evals**: BBH calibration, a 10-task Jev vs 4 chat-model panel, agent before/after, and a context-size pilot. (2) **OpenRouter Decisions API transport details** (alpha endpoint, SDK 404 gotcha). (3) A practical **pitfalls table** on repeat-judging, context size and batch size. (4) 108 ready-made scenario templates for agent supervision (goal drift, stuck loops, test weakening/reward gaming, completion-evidence checks).

## Facts claimed about Jev
- **OpenRouter route: `POST https://openrouter.ai/api/alpha/decisions`**, Bearer `$OPENROUTER_API_KEY`. This is not `/api/v1/chat/completions`, not `/api/v1/decisions`, and not `/v1/systemone`. Send `state` and `questions`, not `messages`. No separate TypeSafe key is needed. The Decisions endpoint is **alpha** (contract checked 2026-09-21). OpenRouter TS SDK: use a separate Decisions client with `serverURL: 'https://openrouter.ai'`, because the default base URL gives a 404 in SDK 1.2.146 (per OpenRouter's "jev-verified-cascade" cookbook).
- Official route: `POST https://api.typesafe.ai/v1/systemone` with `TYPESAFE_API_KEY`. Pinned model `jev-1.13.0`, while the OpenRouter ID is `typesafe/jev-1.13`.
- Native request shape: `{"model", "state": {...}, "questions": {id: {"type": "choice"|"noul"|"score", "instructions", "criteria"}}}`. Choice criteria is a dict. **Noul can take a criteria dict `{"true": ..., "false": ...}`**. Score criteria is an ordered list.
- BBH pilot (160 items, 2026-09-20): Jev **136/160 (85%)** vs DeepSeek V4.1 Flash 120/160 strict. The `confidence ≥0.90` band was 92/100 correct (8 wrong). ECE 0.0994, Brier 0.2560, NLL 0.5974. The [.9,1] bin had mean p 0.9814 but accuracy 0.8898, so it was **overconfident**. By task: pronoun 90%, causal judgment 55%, logical deduction 100%, sarcasm 95%.
- Model panel (2026-09-22) vs DeepSeek V4 Flash / Qwen35B-A3B / Qwen9B / Llama3.1-8B: BBH Jev 138/160 (best). LogiQA Chinese 16/20 (DeepSeek 19). OCNLI 18/20. Ruozhiba 20/20. Context 39/40. Public PRs 38/40 (best). Banking77 16/20. BoolQ 19/20. BFCL tool names 20/20 (all saturate). Prompt injection 17/20 (Qwen9B 19).
- Agent pilots: 12 pairs (09-20), baseline **12/12 vs Jev-checkpoint arm 10/12**, 0 Jev wins, 10 ties, 2 losses. Jev also used more cost ($0.0091 vs $0.0051) and more time (12.57s vs 6.33s). In a later 4-pair run (09-22), 3/4 → 4/4. Neither shows a general benefit.
- Context pilot (40 calls): short vs full evidence scored 20/20 vs 19/20; "unknowns" fell from 15 to 4. **More evidence enabled more decisions, not higher accuracy.**
- The CLI exit codes: 0 selected/scored, 2 review, 1 error.

## Key insights / patterns
- **Two habits**: (1) give enough context (goal, rules, source evidence, history, candidate meanings), because Jev does not inherit the agent's conversation; keep the *question* narrow, not the evidence artificially tiny. (2) Parallelize independent judgments over one shared state, and run independent requests with bounded concurrency.
- Pitfalls:
  - Don't rerun until the answer looks right.
  - Three agreeing calls are not independent evidence; repeatability is not accuracy.
  - Split a vague "safe and done?" into outcome, evidence sufficiency and specific rules.
  - Don't send only the agent's conclusion, and don't paste everything.
  - Distinguish shared-state questions from mixed-record batches; pg-jev reports a large-batch quality drop.
  - Describe options with conditions, boundaries and an unknown option.
  - Don't execute just because a value exceeds 0.9; probability, confidence and score differ.
  - Test for false alarms, not only attacks.
- **Missing evidence means unknown.** Saved judgments expire: recheck evidence, question and policy versions before reusing them.
- Adding Jev "advice" checkpoints to an LLM agent does not automatically help and can add turns and cost. The host must use the advice well.
- Scenario ideas for agent supervision: goal-drift checkpoint, stuck-loop recovery, completion evidence check, unsupported success language, postmortem failure attribution, plan vs action, **test weakening / reward gaming**, project-rule compliance, action-risk triage, suspicious tool-output instructions, subagent report admission, safe moment to compact, browser wait vs intervene.

## Standout entries
- [wuyoscar/jev-skill](https://github.com/wuyoscar/jev-skill) — 5 agent skills plus jev-decide CLI (skills)
- [OpenRouter Decisions API](https://openrouter.ai/docs/api/api-reference/alphadecisions/submit-a-decisions-query) — alpha decisions endpoint (platform)
- [OpenRouter verified-cascade cookbook](https://openrouter.ai/docs/cookbook/evaluate-and-optimize/jev-verified-cascade) — cascade pattern (tutorial)
- [BBH calibration results](https://github.com/wuyoscar/jev-skill/blob/main/evals/CALIBRATION_RESULTS.md) — calibration pilot (benchmark)
- [Model panel](https://github.com/wuyoscar/jev-skill/blob/main/docs/experiments/model-panel/README.md) — Jev vs 4 chat models on 10 tasks (benchmark)
- [Agent pilot results](https://github.com/wuyoscar/jev-skill/blob/main/evals/RESULTS.md) — negative result (benchmark)
- [Context pilot](https://github.com/wuyoscar/jev-skill/blob/main/docs/experiments/context-pilot/README.md) — context size vs accuracy (benchmark)
- [Pitfalls guide](https://github.com/wuyoscar/jev-skill/blob/main/skills/jev/references/pitfalls.md) — repeat-judging, batch and context traps (guide)
- [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) — browser agent (project)
- [thelau/jev-tetris](https://github.com/thelau/jev-tetris) — code lists legal moves, Jev picks (demo)
- [cocktailpeanut/jevthoven](https://github.com/cocktailpeanut/jevthoven) — music from Jev choices (demo)
- [davila7/jev-explained](https://github.com/davila7/jev-explained) — illustrated primitives guide (tutorial)
- [nekuda-ai/WindTunnel](https://github.com/nekuda-ai/WindTunnel) — WebMCP tool selection benchmark (benchmark)
