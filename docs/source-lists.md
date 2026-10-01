# The Source Lists, Reviewed

> This meta-list was built from **106 community "awesome-jev" repositories**. Every one was read in full; per-source notes are in [`source-notes/`](source-notes/), and pull dates, commits and stars are in [`sources.md`](../sources.md). This page compares them: what each is good for, how they relate, and which to treat with caution.
>
> The source notes were written with AI assistance from the cloned repositories and haven't been reviewed line by line. Treat them as a reading guide and follow the links to the primary material.

[← back to the main list](../README.md)

## The landscape at a glance

| Kind | Count | Notes |
|---|--:|---|
| Hand-curated lists | 57 | from 14-entry starter sets to ~800-entry annotated lists |
| Auto-generated / merged indexes | 13 | GitHub-search harvesters and merges of other lists; several use Jev itself to decide inclusion |
| Use-case / case-study collections | 9 | per-project "what Jev decides vs what code does" anatomy |
| Papers / research lists | 5 | + 2 security/robustness evidence maps |
| Agent-skill packages | 4 | installable skills that call Jev |
| Prompt / question-design collections | 2 | |
| Guides / study companions | 3 | |
| Projects that aren't lists | 8 | apps, skill packs and test logs that happen to be named "awesome-jev" |
| Empty or skeleton | 2 | [munibashami07-oss/awesome-jev](https://github.com/munibashami07-oss/awesome-jev) (every file empty), [Python-World/Awesome-jev](https://github.com/Python-World/Awesome-jev) (placeholders; links the wrong domain `typesafe.co`) |

**Languages.** Most lists are in English. Many ship full translations: Chinese (~20), Japanese, Korean, Spanish, Portuguese, and up to 20 languages in [wh000wh000/awesome-jev-live](https://github.com/wh000wh000/awesome-jev-live). Dedicated non-English lists:
- Chinese: [yzfly/awesome-jev-zh](https://github.com/yzfly/awesome-jev-zh), [CodeAlex52/awesome-jev-cn](https://github.com/CodeAlex52/awesome-jev-cn), [JingHao-Leon/awesome-jev-apps](https://github.com/JingHao-Leon/awesome-jev-apps), [fanly/Jev-awesome](https://github.com/fanly/Jev-awesome), [99hansling/awesome-jev](https://github.com/99hansling/awesome-jev) and [everyinfra/jev-radar](https://github.com/everyinfra/jev-radar).
- Japanese: [mukishitsuu-png/awesome-jev-ja](https://github.com/mukishitsuu-png/awesome-jev-ja).
- Korean/English: [fivetaku/awesome-jev-study](https://github.com/fivetaku/awesome-jev-study).

## Start here: the best list for each need

| If you want… | Read |
|---|---|
| **The most careful single field guide** | [AbdelStark/awesome-typesafe-jev](https://github.com/AbdelStark/awesome-typesafe-jev): official index, access-route comparison, a "before you trust a decision" table |
| **A one-page technical cheat sheet** | [Li-Evan/awesome-jev: cheatsheet.md](https://github.com/Li-Evan/awesome-jev/blob/main/cheatsheet.md) |
| **Hard specs, the gateway matrix and a timeline** | [Promethe-us/awesome-jev](https://github.com/Promethe-us/awesome-jev) (bilingual, source-audited) · [kydlikebtc/awesome-jev](https://github.com/kydlikebtc/awesome-jev) (compatibility matrix across 13 surfaces, corrections table) |
| **The biggest well-organized catalogue** | [yibie/awesome-jev](https://github.com/yibie/awesome-jev) (domain taxonomy, the most-starred list) · [Li-Evan/awesome-jev](https://github.com/Li-Evan/awesome-jev) (3,398 entries by scenario, EN/ZH) · [thevibeworks/awesome-typesafe-jev](https://github.com/thevibeworks/awesome-typesafe-jev) (1,093 reviewed entries plus its own lab measurements) |
| **A catalogue where every entry is verified to call Jev** | [punk2898/awesome-jev-verified](https://github.com/punk2898/awesome-jev-verified) (links the exact line) · [ozers/jevsome-projects](https://github.com/ozers/jevsome-projects) (proof-of-call) · [MrJev/awesome-jev](https://github.com/MrJev/awesome-jev) (code-verified, plus container security audits) |
| **Independent benchmarks with numbers** | [punk2898/awesome-jev-verified](https://github.com/punk2898/awesome-jev-verified) (its own 2,390-question benchmark) · [robokrunch/awesome-jev](https://github.com/robokrunch/awesome-jev) (benchmark digest) · [tanxarx/awesome-jev](https://github.com/tanxarx/awesome-jev) (~65 skeptical threads) · [charetterat/awesome-jev-essentials](https://github.com/charetterat/awesome-jev-essentials) |
| **Robustness, calibration and security** | [Yifan-Lan/awesome-jev-robustness](https://github.com/Yifan-Lan/awesome-jev-robustness) (132 studies plus a synthesis table) · [Sarim-MBZUAI/awesome-jev-security](https://github.com/Sarim-MBZUAI/awesome-jev-security) (11 papers) · [cobanov/awesome-jev](https://github.com/cobanov/awesome-jev) (the evaluation section) |
| **Papers** | [OmniJev/awesome-jev-papers](https://github.com/OmniJev/awesome-jev-papers) (51 papers with abstracts) · [Oscar-dzy/Awesome-jev-papers](https://github.com/Oscar-dzy/Awesome-jev-papers) (annotated) · [Eurekaleo/awesome-jev-survey](https://github.com/Eurekaleo/awesome-jev-survey) (survey manuscript) · [youzizzz1028/Awesome-Jev](https://github.com/youzizzz1028/Awesome-Jev) (research lineage) |
| **Open models and alternatives** | [KuzanJ/awesome-jev](https://github.com/KuzanJ/awesome-jev) (licence-audited) · [Zhao-Tian-yi/awesome-jev](https://github.com/Zhao-Tian-yi/awesome-jev) (architecture taxonomy) · [notsointresting/awesome-jev-family](https://github.com/notsointresting/awesome-jev-family) · [mturac/awesome-jev-alternatives](https://github.com/mturac/awesome-jev-alternatives) · [andyrewlee/awesome-system-one](https://github.com/andyrewlee/awesome-system-one) (vendor-neutral, including competitors) · [sfmqrb/awesome-decision-models](https://github.com/sfmqrb/awesome-decision-models) (Laya ecosystem) |
| **How to write good questions** | [vicfei/awesome-jev-prompts](https://github.com/vicfei/awesome-jev-prompts) (43 patterns and 10 anti-patterns) · [dog-last/awesome-jev](https://github.com/dog-last/awesome-jev) (decision tree, atomization lesson, CI-tested cookbooks) |
| **Use cases explained as architecture** | [FuturExplorator/awesome-jev-cases](https://github.com/FuturExplorator/awesome-jev-cases) · [onlyoasis/awesome-jev-cases](https://github.com/onlyoasis/awesome-jev-cases) (43 cases plus all 18 official cookbooks) · [SeeAPI/awesome-jev-use-cases](https://github.com/SeeAPI/awesome-jev-use-cases) · [aliaihub/awesome-jev-usecases](https://github.com/aliaihub/awesome-jev-usecases) · [anandi1989/awesome-jev-usecases](https://github.com/anandi1989/awesome-jev-usecases) · [logicrw/awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects) (a "where Jev decides" note on 799 projects) |
| **Runnable code** | [Justmalhar/awesome-jev-apps](https://github.com/Justmalhar/awesome-jev-apps) (100 Streamlit apps, plus a write-up of the OpenRouter Decisions API) · [whyashthakker/awesome-jev-use-cases](https://github.com/whyashthakker/awesome-jev-use-cases) (50 Jev-vs-LLM demos) · [Anil-matcha/awesome-jev-by-typesafe](https://github.com/Anil-matcha/awesome-jev-by-typesafe) (starter code) · [Awesome-llms-labs/awesome-jev](https://github.com/Awesome-llms-labs/awesome-jev) |
| **Agent skills** | [wuyoscar/jev-skill](https://github.com/wuyoscar/jev-skill) (5 skills, a CLI, 108 scenarios and honest evals) · [aitofy-dev/jev-awesome-skills](https://github.com/aitofy-dev/jev-awesome-skills) · [Pleo2/awesome-jev-agent-skills](https://github.com/Pleo2/awesome-jev-agent-skills) · [Ai-trainee/awesome-jev](https://github.com/Ai-trainee/awesome-jev) (an X-post index packaged as a SKILL.md) |
| **Robotics and embodied AI** | [Frank-ZY-Dou/awesome-jev](https://github.com/Frank-ZY-Dou/awesome-jev) (rigorous, with archived videos) |
| **Launch-week social demos** | [walidboulanouar/awesome-jev-use-cases](https://github.com/walidboulanouar/awesome-jev-use-cases) (with engagement metrics) · [snowfungo/awesome-jev-projects](https://github.com/snowfungo/awesome-jev-projects) (194 X posts, four languages) · [hellogumbo/awesome-jev](https://github.com/hellogumbo/awesome-jev) (annotated articles and threads) |
| **A classic, compact awesome list** | [AnotiaWang/awesome-jev](https://github.com/AnotiaWang/awesome-jev) (best polyglot SDK index) · [ckaraca/awesome-jev](https://github.com/ckaraca/awesome-jev) (official repos and framework integrations) · [valentynkit/awesome-jev-typesafe](https://github.com/valentynkit/awesome-jev-typesafe) · [KennethAshley/awesome-jev](https://github.com/KennethAshley/awesome-jev) · [onmyway133/awesome-jev](https://github.com/onmyway133/awesome-jev) · [jqueryscript/awesome-jev](https://github.com/jqueryscript/awesome-jev) |
| **Beginner explainer** | [Vishnurr2k01/awesome-jev](https://github.com/Vishnurr2k01/awesome-jev) · [rudy2steiner/awesome-jev-hub](https://github.com/rudy2steiner/awesome-jev-hub) · [karozi/awesome-jev-resources](https://github.com/karozi/awesome-jev-resources) (for PMs) |
| **Jev landing in mainstream OSS** | [jtnkminimal/awesome-jev](https://github.com/jtnkminimal/awesome-jev) (upstream integrations with PR numbers) · [BeatAPI/awesome-jev](https://github.com/BeatAPI/awesome-jev) (integrations in LangChain, LiteLLM, Pydantic AI and others at fixed commits) |
| **A cross-list consensus signal** | [mabodx/awesome-jev](https://github.com/mabodx/awesome-jev) ("on N of 31 lists") · [Omrigotlieb/awesome-jev](https://github.com/Omrigotlieb/awesome-jev) (audited union of ~9 lists) · **this repo** (106 lists) |

## How the lists relate to each other

- **Most lists share a core set of entries.** The same ~50 projects appear on most lists: jev-ultrafast (📚76), jev-review, fast-jev-compaction, jev-trader, typesafe-ai/skills, jev-mcp, jev-drone, jev-search, typesafe-mario, foreman, and so on. Past that core the lists diverge sharply: 9,859 of the 18,330 unique entries appear on only one list.
- **Some lists are copies or derivatives:**
  - ham-zax is downstream of **yibie**.
  - fivetaku annotates **kraayenjon**.
  - Vishnurr2k01 draws its index from **AnotiaWang**.
  - CodeAlex52 derives from **Promethe-us**.
  - Awesome-llms-labs mirrors **dakotac1994/awesome-jev**.
  - BeatAPI borrows its structure from **logicrw**.
  - supermanc417-alt and larkwins are near-identical (and both define Noul wrongly).
  - vicfei's quick start is adapted from **Anil-matcha**.
- **Several lists merge other lists:**
  - mabodx (31 lists)
  - THEROCKSSS (21 lists)
  - Omrigotlieb (~9 lists)
  - Gerry9000's RADAR (29 mirrors)
  - KuzanJ credits 8 other lists
- **Several lists use Jev as their own curator:**
  - RadRebelSam uses Noul thresholds of 0.75 and 0.45.
  - rhc98 asks 11 questions per repo and publishes a [calibration report](https://github.com/rhc98/awesome-jev).
  - fatwang2 uses the [Jev Review Action](https://github.com/fatwang2/jev-review-action).
  - valentynkit, yibie, jtnkminimal, punk2898 and daftAI2026 all tag or classify entries with Jev.
  - yunhe-dev has a [design doc](https://github.com/yunhe-dev/awesomejev/blob/main/docs/jev-native-radar.md) for "using Jev to list Jev".
  - These double as case studies of the pattern.
- **Stars measure attention, not quality.** Star counts reported *inside* lists disagree wildly because they are stale snapshots. jev-ultrafast is quoted anywhere from 1,052 to 21,563 stars, and laya from 17.7k to 29.2k. This repo verified stars directly on 2026-09-30.

## Handle with care

| List | Issue |
|---|---|
| [bakiabaci/awesome-jev](https://github.com/bakiabaci/awesome-jev) | **Benchmark tables and SDK code look fabricated**: `pip install typesafe`, `client.decide.noul(...).confidence`, a Go `typesafe-go` from typesafe-ai, latencies like "P95 68 ms", and comparisons against dated models. Its discovery methodology and ecosystem statistics are still useful. |
| [Gerry9000/awesome-jev](https://github.com/Gerry9000/awesome-jev) | Very large, with some real first-hand testing, but **SEO/"parasite GEO" promotional**: links carry `utm_medium=parasite_geo`. Internal numbers contradict each other: three different invoice accuracies, "30–50 ms" vs a measured 0.42 s, and a wrong `/v1/eval` endpoint in one dossier. |
| [AiPersonacademy/Awesome-jev-use](https://github.com/AiPersonacademy/Awesome-jev-use) | Interleaved with promotion for a paid course and "JevProxy". The non-promotional parts, including a good cookbook index, look copied from better lists. |
| [everyinfra/jev-radar](https://github.com/everyinfra/jev-radar) | Its casebook is excellent, but it is star-farming: "star this repo → get a free Jev API key". |
| [BeatAPI/awesome-jev](https://github.com/BeatAPI/awesome-jev), [logicrw](https://github.com/logicrw/awesome-jev-projects), [kraayenjon](https://github.com/kraayenjon/awesome-jev), [heyjunpenn](https://github.com/heyjunpenn/awesome-jev), [karozi](https://github.com/karozi/awesome-jev-resources), [walidboulanouar](https://github.com/walidboulanouar/awesome-jev-use-cases), [cobanov](https://github.com/cobanov/awesome-jev), [yanng981](https://github.com/yanng981/awesome-system-one) | Content is good but the lists promote something. BeatAPI resells access. logicrw has hype copy ("sub-100ms, 50–100ms") and is open to paid placement. kraayenjon promotes its maintainer's site, heyjunpenn carries sponsor placements, karozi promotes a Substack, walidboulanouar has a sponsor, cobanov runs an Ollaya banner, and yanng981 is fed by laya-ai.com. |
| [jqueryscript/awesome-jev](https://github.com/jqueryscript/awesome-jev), [vicfei](https://github.com/vicfei/awesome-jev-prompts), [rudy2steiner](https://github.com/rudy2steiner/awesome-jev-hub) | Each treats a **`TypeSafeAI/*`** repo as official or first-party. That org is a community org; the official org is `typesafe-ai`. |
| [larkwins](https://github.com/larkwins/awesome-jev), [supermanc417-alt](https://github.com/supermanc417-alt/awesome-jev-hub) | Both define Noul as "skip — not worth it". It is the yes/no probability primitive. |
| [guozihang/awesome-jev-for-sequence-modeling](https://github.com/guozihang/awesome-jev-for-sequence-modeling), [Awesome-llms-labs](https://github.com/Awesome-llms-labs/awesome-jev) | Several links are bare homepages (techcrunch.com, pypi.org, and so on) rather than real article links. |
| [daftAI2026](https://github.com/daftAI2026/awesome-jev), [RadRebelSam](https://github.com/RadRebelSam/awesome-jev), [THEROCKSSS](https://github.com/THEROCKSSS/awesome-jev), [JohnDotOwl](https://github.com/JohnDotOwl/awesome-jev), [shirenchuang](https://github.com/shirenchuang/awsomejev), [stainlu](https://github.com/stainlu/awesome-jev) (bulk table), [wh000wh000](https://github.com/wh000wh000/awesome-jev-live) | Automated harvests. Use them for discovery, not endorsement. They include keyword false positives and launch-week scaffold repos. stainlu's "active only" filter drops 3,906 launch-week drops. |
| [yangzhou-chaofan](https://github.com/yangzhou-chaofan/awesome-jev-prompt), [JohnDotOwl](https://github.com/JohnDotOwl/awesome-jev), [supermanc417-alt](https://github.com/supermanc417-alt/awesome-jev-hub), [sontakey](https://github.com/sontakey/awesome-jev) | Frozen at launch week (09-17 to 09-22), so stars, repo names and access information are stale. |
| Projects named "awesome" | [AstonyCat/jev-tab-grouper](https://github.com/AstonyCat/jev-tab-grouper), [Faizullah9181/jev-esketcher](https://github.com/Faizullah9181/jev-esketcher), [ayyazzafar/needle-jev](https://github.com/ayyazzafar/needle-jev), [caohy1988/jev-guard-smoke](https://github.com/caohy1988/jev-guard-smoke), [v4fs/awesome-jev-security](https://github.com/v4fs/awesome-jev-security), [yunhe-dev/awesomejev](https://github.com/yunhe-dev/awesomejev), [scienceaix/jev](https://github.com/scienceaix/jev). These are good reference implementations or reports, but they aren't lists. |

## Warnings that recur across the careful lists

- **"A listing is not an endorsement."** Many launch-week repos are **same-day bulk scaffolds** from one author with shared `AGENTS.md`, `CLAUDE.md` and `STATE.md` files and a thin commit history. They pass inclusion rules without being proven. yibie, v-modal and KennethAshley have explicit checklists for this.
- A Reddit review of 287 Jev projects found that most **barely touch Jev**. `"typesafe"` and `"jev"` are noisy search terms: `jev` also matches Japanese encephalitis virus, JeVois, JEvents, Jevil and jEveAssets, and "type-safe" is an ordinary programming term.
- Before adopting a project, verify four things: the code actually calls the API, there's a runnable check, published numbers trace to a source, and a licence is present.
- **Rigor doesn't track reach.** The strongest measurements often come from single-digit-star repos.
