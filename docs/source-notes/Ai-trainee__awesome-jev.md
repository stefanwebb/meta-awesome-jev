# Ai-trainee/awesome-jev
- **One-liner:** Chinese-first collection of 68 X posts + 56 open-source projects about Jev, each "Jev-scored", with screenshots, packaged as an agent-loadable SKILL.md + references/index.json.
- **Language(s):** Chinese (README.md) and English (README_EN.md; post titles remain in Chinese)
- **Type:** skills-collection (curated X-post/use-case collection)
- **Scale:** 124 cases (68 posts + 56 projects), "50 Jev highlights", 9 scenes: Browser & Computer Automation; Gaming & Real-time Interaction; Trading & Finance; Ecosystem & Hype; Development & Tools; Content Categorization & SEO; Tutorials & Resources; Model Routing & Decision-Making; Context Compression; plus Featured Projects (56) and Other. ~67 PNG screenshots in images/ (~13 MB). External Feishu bitable with 87 posts.
- **Quality flags:** Sourced from author's X bookmarks; each item has a "Jev score" (0–98) from "an independent Jev scoring model" — methodology opaque. Titles are Chinese paraphrases with like counts; heavy on hype/social posts ("Ecosystem & Hype" section). One empty "untitled record". Some screenshots missing. Not commercial-promotional. Stars snapshot (jev-ultrafast ★9291). Some claims only as tweet headlines (unverified).
- **Unique value:** Best index of influential X posts (with handles) about Jev, including Japanese/Chinese community; SKILL.md packaging so agents can suggest Jev patterns; some negative/realistic signals (Mario 229 ms too slow; trading bot lost 300% in 14 h; limits for market-context probabilities).

## Facts claimed about Jev
- Describes Jev as "a lightweight, millisecond-scale execution model" paired with an LLM ("big-model reasoning + small-model execution") — note this framing ("lightweight/small") conflicts with TypeSafe's "Jev is neither small nor an LLM" (per majiayu000).
- Price: "$0.042/1M input tokens, output free" (akira_papa_IT post); "193× faster, 445× cheaper" (KKaWSB post, echoing vendor headline).
- OpenRouter: beta availability, "decision model, 10× cheaper 10× faster than LLM" (OpenRouter official post 2101061688338575739).
- Vercel AI Gateway: Jev free until 9/25 (HtWavever post).
- "Jev V13 vs Fable 5.1 vs GPT-6 Astra" chess (aimlapi).
- Latency anecdotes: Mario single decision 229 ms, didn't clear 1-1 (chenchengpro); Slay the Spire 2 action in 0.7 s; jev-voice-browser ~300 ms per spoken word; jevskill-like claims absent.
- Cost anecdotes: Snake 200 requests $0.02; Pokémon $1.21 for 8,000+ decisions, first gym badge; Browser Use flights 7 s $0.0039; YouTube sponsor skip $0.005/video (Tony Dinh); DuckDB extension labels ~1k rows in ~10 s; 1,891 ads classified in 19 s; 428 news items for 15 brands in 28 s; fx auto safety classifier replaced GPT-5.6 Luna, 5–18× faster and more accurate (fazxes); UPSC GS-1 72.7%.
- Founder Diogo Almeida (CompleteSkeptic) reply: "private evals + calibrated confidence: go automate".
- Limitation post (GianMattya): zero-shot probability distributions not suitable for market context; income estimates biased.

## Key insights / patterns
- Dominant framing: LLM plans (System 2), Jev executes high-frequency discrete decisions ("web operations are essentially discrete multiple-choice, you don't need AI to write poetry").
- Context compression and memory are top community uses: parallel recall/store/merge/remove/relevance decisions (anthdm); drop stale tool history rather than summarize (fast-jev-compaction); ~50% context reduction (pedronauck).
- Model routing by benchmark pass rate/cost/latency; Jev as AI referee for Claude Code/Codex.
- Real-time games expose latency limits (Mario 229 ms insufficient); trading demos lose money — architecture interesting, not profitable.
- "Generating" text by asking 29 yes/no questions per character (ryanvogel) — novelty, not practical.
- Computer use: send only text candidates (not screenshots), let Jev pick element/action/completion/risk, local policy gates block sensitive ops (Sac-Y/Jev-cu); cua recipe validates the chosen bounded action client-side.

## Standout entries
- [Browser Use + Jev launch post](https://x.com/gregpr07/status/2100411066966749359) — 7 s, $0.0039 flights demo (browser)
- [OpenRouter explains Jev](https://x.com/OpenRouter/status/2101061688338575739) — official gateway post (integration)
- [Harrison Chase on Jev for harnesses](https://x.com/hwchase17/status/2100773130041950579) — LangChain CEO commentary (article)
- [Matija Sosic 45-second explainer](https://x.com/MatijaSosic/status/2100190746389135772) — popular explainer (tutorial)
- [Flavio Copes tutorial](https://x.com/flaviocopes/status/2100695543995347188) — what it is/how to use (tutorial)
- [Jarrod Watts trading bot post](https://x.com/jarrodwatts/status/2100356151468585346) — buy/sell decision every 300 ms block, 4,392 likes (finance)
- [jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader) — Monad-block trader (finance)
- [Sac-Y/Jev-cu](https://github.com/Sac-Y/Jev-cu) — text-only computer-use with policy gates (computer use)
- [trycua/cua](https://github.com/trycua/cua) — computer-use platform with Jev recipe (computer use)
- [fstandhartinger/jevbench](https://github.com/fstandhartinger/jevbench) — JevBench harness (benchmark)
- [Zaious/jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas) — evidence map of where Jev holds/breaks (evaluation)
- [sutro-sh/jev-align](https://github.com/sutro-sh/jev-align) — calibrated AI functions from human feedback with GEPA (tool)
- [githubnext/localjev](https://github.com/githubnext/localjev) — local Jev-compatible API on DiffusionGemma (open reproduction)
- [kerpopule/hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills) — Hermes routing/memory/compaction skills (agents)
- [Hamilton Ulmer DuckDB extension post](https://x.com/hamiltonulmer/status/2100370557405667768) — label CSV/Parquet rows (data)
