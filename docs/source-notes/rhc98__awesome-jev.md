# rhc98/awesome-jev
- **One-liner:** Fully Jev-curated directory: ~9,800 GitHub repos judged by one Jev call each (11 typed questions); README shows top 15 per category; site awesome-jev.xyz; published calibration report vs human gold set.
- **Language(s):** English
- **Type:** auto-generated-list
- **Scale:** Badges: judged 9,781 repos, listed 7,741; README ≈ 130 entries (top 15 by composite per category). Categories: Official; SDKs and Clients; Integrations; Agent and Developer Tooling; Applications; Games, Robotics, and Simulation; Research, Evals, and Reimplementations; Learning; Other Lists; Other.
- **Quality flags:** Entirely auto-generated ("nothing below was hand-picked"); descriptions are GitHub descriptions (e.g. "BRRRRRRR…", "Config files" for a dotfiles repo in "Other"). Judges from README/metadata only, never source code, so misses code-only integrations and over-scores near-empty repos. But unusually honest self-evaluation.
- **Unique value:** `docs/calibration.md` — a real calibration study of Jev as a repo classifier (precision/recall threshold sweep, confidence-vs-accuracy bins, failure analysis, question-set v1→v2 lessons, cost/latency from 3,683 calls). Best "Other Lists" index of the batch (15 other Jev directories). Good "Learning" section.

## Facts claimed about Jev
- Model `jev-1.13.0`, question set v2; one call per repo answers **11 typed questions** (gates as Noul, category/pattern as Choice, substance as Score 0–3).
- Choice cap of **255 options** (jev-tree works around it recursively).
- Measured (3,683 calls, 2,209 repos): **mean 3,235 input tokens/call, ~272 output tokens/call, latency p50 210 ms / p90 337 ms**, 11.91M total input tokens ≈ **$0.50** at $0.042/1M input (output free); ≈ $0.00014 per call.
- Gate threshold sweep on 80-repo gold set: at genuine ≥ 0.5, precision 0.97, recall 0.83, F1 0.89; at 0.2 F1 0.94. Category-confidence bins: 0.9–1.0 → 48/48 correct (1.00); 0.5–0.7 → 0.56 accuracy; ~¾ of judgments come back ≥0.9.
- Score (substance) over-scores near-empty repos: a one-file repo 2.30, empty repo 1.23, a Zig client 2.90 vs human 1.
- vercel/eve ships Jev as default model of its experimental evaluate path (code-search `jev-latest`), README doesn't mention it → Jev scored 0.03.
- Community claims listed: laya-mlx 7–14 ms short decisions on M3 Max; jev-demo "fan-out almost free, 40 questions same latency as 1" on jev-1.13.0; kydlikebtc/awesome-jev 1207 resources; what-is-jev 947 rubric-scored repos; heyjunpenn/awesome-jev 962 projects; awesome-jev-verified uses an independent 2,390-question benchmark; jev-radar 220+ cases rescanned every 3 hours.

## Key insights / patterns
- Question wording matters: v1 "is a Jev project?" rejected meta-lists (0.16); v2 enumerating "uses, wraps, evaluates, reimplements, or collects" fixed it (0.78). Move deterministic facts (e.g. `official` owner) out of Choice into code.
- Separate axes: "belongs?" (Noul gate) vs "which shelf?" (Choice confidence) are nearly independent — don't use category confidence as a listing gate; mark uncertain instead.
- Jev only knows what's in state: README-only evidence leads to misses → handle with human overrides recorded with reasons.
- Score rubrics can't detect emptiness if state lacks file-level evidence — add explicit signals.
- 0.9+ confidence reliable; lower bands are thin evidence. Use three bands (list ≥0.5, review 0.3–0.5, exclude).
- Cost of running Jev at scale for classification is trivial (≈$0.50 for ~3.7k calls with ~3k-token states).

## Standout entries
- [typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) — official SDK (official)
- [skills](https://github.com/typesafe-ai/skills) — official agent skills (official)
- [jev-tree](https://github.com/reachjalil/jev-tree) — recursive Choice beyond 255-option cap (tool)
- [ts-jev-cost-calculator](https://github.com/StefanoITA/ts-jev-cost-calculator) — token/cost/context estimator (tool)
- [pg-jev](https://github.com/realZachi/pg-jev) — PostgreSQL extension (integration)
- [sys1bench](https://github.com/rssr25/sys1bench) — System One benchmark: calibration, framing sensitivity, selective prediction (benchmark)
- [reflexbench](https://github.com/brida-ai/reflexbench) — open benchmark harness (benchmark)
- [privatemode-decisions-benchmark](https://github.com/edgelesssys/privatemode-decisions-benchmark) — Jev/Laya/GLM benchmark (benchmark)
- [laya-mlx](https://github.com/mizorewww/laya-mlx) — native MLX Laya runtime (open model)
- [langchain-jev-tutorial](https://github.com/PromptEngineer48/langchain-jev-tutorial) — LangChain + Jev support-ops agent (tutorial)
- [jev-poc](https://github.com/garygentry/jev-poc) — 20 demos with cost/agreement vs chat baseline (tutorial)
- [jev-demo](https://github.com/sawzhang/jev-demo) — Chinese hands-on with fan-out latency measurements (tutorial)
- [building-with-typesafe-jev](https://github.com/aaddrick/building-with-typesafe-jev) — agent skill with prior art from 150+ projects (skill)
- [awesome-jev-verified](https://github.com/punk2898/awesome-jev-verified) — code-line-verified list (directory)
- [what-is-jev](https://github.com/g0runmezadam/what-is-jev) — research on 947 scored repos (research)
