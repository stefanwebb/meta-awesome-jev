# snowfungo/awesome-jev-projects
- **One-liner:** Collection of 194 Jev demos sourced exclusively from X (Twitter) posts, each described by a truncated quote of the author's tweet; README in four languages.
- **Language(s):** English, Chinese (zh-CN), Korean (ko-KR), Japanese (ja-JP) — parallel READMEs
- **Type:** use-case-collection (social-media showcase)
- **Scale:** 194 entries in 11 categories: Agents (19), Browser extensions (7), Creative tools (16), Data & research (9), Developer tools (34), Experiments (18), Finance (8), Games (39), Marketing (6), Productivity (31), Robotics (7). Every link is an x.com status URL; zero GitHub links.
- **Quality flags:** Descriptions are raw tweet text truncated with "…" (often hype: "INSANE", "🤯"), not editorial summaries; claims unverified. Some mis-categorization (e.g. spreadsheets, tax-document classifier, Autumn billing voice commands, Youform, YouWare résumé screener listed under Games). No repo/code links, so hard to verify. Heavily overlaps with the X-sourced parts of Li-Evan's gallery. Not spam, but low editorial depth. Translations are the main added value.
- **Unique value:** Quick multilingual snapshot of launch-week social demos with author handles; contains many self-reported cost/latency anecdotes and a couple of honest negative results (browser-agent stress test, pixel drawing failure).

## Facts claimed about Jev
(All are claims from tweets, as quoted in the list.)
- Browser Use + Jev "Ultrafast": flight search in 7s for $0.0039 (@gregpr07).
- Computer use "155x cheaper than opus 5, ~20x faster" (@awlevin).
- Starchild prompt routing: "20x decrease in cost and 6x increase in speed" (@StarchildOnX).
- Ego Lite: 20 Amazon product decisions in 3.71s vs GPT-5.6 Sol 54.45s, 10/10 both.
- Voice browser: Jev returns probabilities "in ~300ms", $0.0002 per command (@moritzkremb).
- PR review: "~200x cheaper than Claude", half a second, $0.00007 per PR; 1,000 PRs = 7 cents vs ~$14.50 on Opus 5 (@redp314).
- Email fraud: Jev classified 100 emails in 1.42s, uncertain cases routed to Kimi K3; 96/100 correct for ~$0.07 (@nutlope).
- Jev compaction for OMP: 30–55% less context, $0.0005 a pass (@jerry543).
- Physical-AI QA: 58,643 action labels in under 3 minutes for 90 cents (@the_cyw).
- ~900 images (via OCR) categorized in 40 seconds (@fayazara).
- Android e2e: ~14.8x faster than DeepSeek + vision (@kevinkern); Touchpress: Jev 29s/$0.003 vs Haiku 4.5 37s/$0.07.
- Postgres join-order query planner sped up 12% (@mmalisper).
- Danish stock backtest: 239 trading days, 8.1 million tokens for $0.32 (@tommy_jepsen).
- YouWare: 360 resumes screened in 24.2s for $0.0212.
- Magic 8 Ball: $4 of credits ≈ 300,000 questions.
- Drone: 300ms decisions; robot arm ~2 decisions/second.
- Negative: "It completed about 5 actions before collapsing in a non-cheated test" for browser use (@SSHCodes); Jev "can't draw" on pixel canvas (@yoheinakajima).
- Contradiction: many posts claim excellent browser/computer-use performance while @SSHCodes says Jev is not useful for browser use.

## Key insights / patterns
- Dominant patterns: model/agent routing (Eve, Goose JIT model selection, Starchild, Corent, sawyerhood auto-picks agent/model/folder); computer/browser use with a DOM/a11y action space rebuilt each step and a small LLM fallback for typing; context compaction by scoring each tool output; real-time feed filters (slop, ads, reply-guys, fallacy scoring) as browser extensions; PR/rule enforcement ("rules a linter can't" — Abide); E2E testing.
- Cascade pattern: Jev classifies bulk, uncertain cases go to a stronger LLM (nutlope fraud pipeline).
- Robotics tip: split each update into two calls — decide what to do, then decide how to move (MuJoCo arm).
- Pass structured environment state as JSON rather than images (MakerMods arm).
- "Jev can't reason" → build an interpreter/logic language around it (narphorium).
- Hacks: generate text one character at a time via per-character Choice/yes-no questions (29 questions per char); emulate a 6502 CPU; draw pixels in parallel.
- Choice vs Noul framing can change judgments (trolley-problem experiment).
- Threshold calibration by data rather than vibes (jevcal).

## Standout entries
- [A faster browser agent (Browser Use Ultrafast)](https://x.com/gregpr07/status/2100411066966749359) — launch browser-agent demo (agents)
- [Instant context compaction](https://x.com/tamarajtran/status/2100694549362553153) — origin of fast-jev-compaction (developer tools)
- [Jevcal confidence-threshold calibration](https://x.com/thenightshipper/status/2100850610962919551) — pick thresholds from data (developer tools)
- [Email fraud detection with Jev and Kimi](https://x.com/nutlope/status/2100614659690713543) — cascade with numbers (developer tools)
- [Fourteen checks for every pull request](https://x.com/redp314/status/2100585126652481915) — one-call PR review (developer tools)
- [Decisions from the command line](https://x.com/ctatedev/status/2100584917092409479) — `npm install -g ai-cli` (developer tools)
- [Natural-language queries inside PostgreSQL](https://x.com/iam_zachi/status/2100679300756435135) — jev() SQL function (developer tools)
- [A Jev query planner](https://x.com/mmalisper/status/2101001041903009987) — 12% faster join ordering (developer tools)
- [Just-in-time model selection in Goose](https://x.com/alexjhancock/status/2100932130196852896) — model routing (agents)
- [Computer use across operating systems](https://x.com/awlevin/status/2100262612428894676) — typesafe-computer-use (agents)
- [A browser-agent stress test](https://x.com/SSHCodes/status/2101026313871970721) — negative result (experiments)
- [Writing one character at a time](https://x.com/ryanvogel/status/2100218045549412499) — text-generation hack (experiments)
- [MuJoCo robot-arm control](https://x.com/dimentary/status/2101018760371171420) — two-call decomposition for control (robotics)
- [Jev Trader on Monad and Kuru](https://x.com/jarrodwatts/status/2100356151468585346) — on-chain trading demo (finance)
- [Quality checks for physical-AI action labels](https://x.com/the_cyw/status/2100807905859739779) — bulk label QA at scale (data & research)
