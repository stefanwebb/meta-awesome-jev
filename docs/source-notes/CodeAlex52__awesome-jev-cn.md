# CodeAlex52/awesome-jev-cn
- **One-liner:** A Chinese-language Jev list focused on Chinese social media (X Chinese KOLs, Xiaohongshu, Bilibili), with a quickstart, short project reviews, a controversies section and an anti-scam note.
- **Language(s):** Chinese (primary), a little English
- **Type:** curated-list (Chinese community / media-focused) + tutorial/study-guide
- **Scale:** Small. Top 5 Chinese posts, 2 Xiaohongshu notes, 1 Bilibili search link, a 5-step tutorial, 8 GitHub repos in the README and about 30 in docs/CATALOG.md, 5 controversies, and an FAQ. Sections: 30 seconds on Jev · Chinese Top 5 · Xiaohongshu picks · Bilibili/video · Getting-started tutorial · GitHub ecosystem reviews (Chinese) · Controversies & sober thoughts · FAQ. Snapshot 2026-09-21.
- **Quality flags:** Thin, with TODOs (Bilibili details missing). It says it derives its structure from Promethe-us/awesome-jev (MIT). Star counts are 2026-09-20 snapshots, lower than later lists (e.g. jev-ultrafast 10,422). Social-media-heavy. Not spam. The facts look plausible and contain specific numbers not seen elsewhere.
- **Unique value:** **Company/funding facts** (DCVC lead, ~$200M valuation, SF, 2 years in stealth). Official headline multipliers with their comparison baselines. Chinese KOL experiments with numbers. **An anti-scam warning: there is no official $JEV token.** A candid controversies list.

## Facts claimed about Jev
- Company: TypeSafe AI, **San Francisco**, **2 years in stealth**, emerged 2026-09-15.
- Founder: Diogo Almeida, described as "ex-OpenAI, one of the co-creators of ChatGPT / RLHF".
- **Funding: $40M seed led by DCVC, valuation about $200M.**
- **Official numbers: 193.6× faster and 444.6× cheaper**, compared to the average of **GPT-6 Astra / Fable 5.1**. Latency 70ms–500ms. These match the "445×" in the TS2 headline and the "193×" in OrcaRouter's 75× vs 193× discrepancy (cited elsewhere).
- Pricing: input $0.042 per million tokens, output free. **The official side admits "output free" may be subsidized.**
- Can't do: free text generation, image reading, chat. It is closed-source.
- Hype (as of 2026-09-20): the launch tweet had 73.1k likes (73,115). HN had 1,920 points / 504 comments. 3,200+ new jev-related GitHub repos in a week.
- **Choice with more than 255 options goes to a two-stage path and gets slower.**
- Waitlist approval is reportedly same-day. Keys come from console.typesafe.ai/keys (evan87863 says /settings/keys, so the path differs).
- Python SDK: `pip install typesafe-sdk`.
- **API request example:** `POST https://api.typesafe.ai/v1/systemone` with `Authorization: Bearer $TYPESAFE_API_KEY` and body `{"state": "...", "model": "jev-latest", "questions": {"department": {"type":"choice","instructions":"...","criteria":{"billing":"Payment issues","technical":"Bugs","sales":"Pricing"}}, "is_urgent": {"type":"noul","instructions":"..."}}}`. Choice `criteria` is a **map of label to description**. Questions are a named map.
- Agent usage: after installing the skill, write "use the TypeSafe skill" in the prompt.
- Chinese KOL tests:
  - 500 e-commerce tickets: Jev finished in 83 s for $0.01, while DeepSeek V4.1 Flash only finished 173 tickets for $0.06.
  - 50 Subway Surfers runs cost under 1 cent.
  - 724 ads analyzed in 40 s for $0.09.
  - jpschroeder "replicated Tesla FSD in an hour" (4,734 likes).
- Stars (2026-09-20): skills 899, system-one-adapter 184, kev 729 (Qwen2.5-0.5B), NanoJev 1220, nimble 809, jev-ultrafast 10,422, fast-jev-compaction 4,627, jev-trader 1,419, OpenByteInc/QuantDinger 11,791 ("AI trading OS + Jev integration").

## Key insights / patterns
- Controversies and sober thoughts:
  1. A priority dispute ("I open-sourced the same architecture a year ago") can't be settled because Jev has no paper.
  2. Benchmarks are self-reported: the official 4-workflow eval uses self-chosen baselines, so there is routing bias.
  3. "Never hallucinates" is true only by definition: 0% type errors in the schema is not the same as correct answers.
  4. Pricing may be subsidized.
  5. There is no official paper, so it's unknown whether open replicas can reproduce "400× cheaper".
- Beginner path: waitlist → key → install the skill → try Choice/Score/Noul in the playground → start with classification/routing/moderation, not generation.
- Recommended starter tasks: support-ticket classification, content moderation / jailbreak detection, review scoring and extraction. Avoid code, docs, chat and vision.
- Positioning: complementary to LLMs. LLMs are System 2, Jev is System 1 for fast execution.
- Jevons-paradox framing: 400× cheaper decisions will make total intelligence consumption explode.
- Scam alert: no official token exists, so any "$JEV" is fake.

## Standout entries
- [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — launch post (official)
- [TypeSafe docs](https://docs.typesafe.ai) — docs with llms.txt (official)
- [Playground](https://console.typesafe.ai/playground) — no-code trial (official)
- [Workflow evals](https://evals.typesafe.ai) — vendor evals (benchmark)
- [Diogo Almeida launch thread](https://x.com/CompleteSkeptic/status/2099925682726002904) — founder announcement, 73k likes (official/social)
- [森叔 @harrisonitsme quickstart](https://x.com/harrisonitsme/status/2100799749192569167) — most-shared Chinese onboarding thread (tutorial, zh)
- [黄小木 @ai_xiaomu 0→1 tutorial](https://x.com/ai_xiaomu/status/2101135680168771979) — long Chinese beginner tutorial (tutorial, zh)
- [SuSu @NFT_Chen 500-ticket test](https://x.com/nft_chen/status/2101253568774697099) — Jev vs DeepSeek V4.1 Flash cost/speed (evaluation, zh)
- [jpschroeder FSD-in-an-hour](https://x.com/jpschroeder/status/2100347770867458384) — viral demo (demo)
- [Xiaohongshu: CUA + Jev computer control](https://www.xiaohongshu.com/explore/6aaf844a000000001103379c) — Chinese video demo (demo, zh)
- [OpenByteInc/QuantDinger](https://github.com/OpenByteInc/QuantDinger) — AI trading OS with Jev integration (application)
- [Promethe-us/awesome-jev](https://github.com/Promethe-us/awesome-jev) — English source list it derives from (list)
