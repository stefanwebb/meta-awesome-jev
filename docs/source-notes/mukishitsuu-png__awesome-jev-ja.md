# mukishitsuu-png/awesome-jev-ja
- **One-liner:** Japanese-language curated Jev list (~70 entries) with plain-language explanations, safety cautions, and original macOS computer-use latency measurements.
- **Language(s):** Japanese (short English summary)
- **Type:** curated-list
- **Scale:** ~70 entries. Sections: Jev とは (What is Jev); はじめかた (Getting started); Claude Code・Codex 向け; ブラウザ・PC・スマホ操作 (browser/PC/phone control); MCP サーバー・SDK・ゲートウェイ; ルーティング (model/skill routing); コードレビュー・開発フロー; 検索・分類・データ; メッセージ・チャット支援; ゲーム・ロボット・シミュレーション; オープンな代替モデル・再現実装; スキル集・プロンプト; ほかのまとめ (other lists, English); 注意が必要なもの (cautions); 実測メモ (measured notes).
- **Quality flags:** Hand-curated, careful, facts-only descriptions ("don't translate marketing copy"); marks Japanese authors with 🇯🇵. Small. Measurements are single-machine anecdotes (2026-09-23, Apple Silicon).
- **Unique value:** Only Japanese-language list; original computer-use timing breakdown showing latency lives in the driver, not Jev; practical Japanese-UI tips; explicit cautions on trading bots, ToS-violating account farms, and data egress; highlights Japanese projects (jev-semgrep cross-lingual semantic grep, receptron/laya Node ONNX runtime).

## Facts claimed about Jev
- Jev = "AI that doesn't write text": state + typed questions (which? what score? yes/no?) → answers with probabilities in **~0.2–0.5 s**. Comparison table: LLM (System Two) seconds+, Jev (System One) ~0.2–0.5 s per decision.
- Docs https://docs.typesafe.ai; keys at console.typesafe.ai/settings/keys; env `TYPESAFE_API_KEY`.
- Jev is TypeSafe's cloud API (no official local weights); open alternatives are unofficial.
- Creating many accounts to farm free tier violates TypeSafe terms.
- Maintainer's measurements: Jev decision itself **0.2–0.35 s per step, confidence 0.87–0.99**; calculator 7×8 in 5 steps via hermes-jev-skills + cua-driver 0.28.2: 13.6 s default → 7.4 s with `serve --no-overlay` → **3.3 s** with coordinate clicks (≈0.1 s/click); jev-mcp `jev_classify` on 35 X posts into 3 classes in one call: 22 auto-confirmed, 13 flagged for review.
- Community claims: jev-ultrafast Google Flights demo 7.1 s; mobile-jev Uber route to payment selection in 9 steps / ~21 s; jev-voice-browser ~300 ms per word; tax-doc-classifier ~$0.001 per page (IRS 261 forms); von "under 15 ms"; jev-drone 2.5 Hz.
- Other lists' sizes as reported here: heyjunpenn/awesome-jev 832 verified entries; kydlikebtc/awesome-jev 805 entries (rhc98 reports 962 and 1207 respectively — counts grow over time).

## Key insights / patterns
- Computer-use slowness is usually the driver (cursor overlay animation, post-click verification waits), not Jev.
- On Japanese UIs, put the on-screen Japanese text verbatim into the goal; English-only goals can drop the target button during candidate filtering.
- jev-ultrafast tends to choose typing into search fields even for click-only tasks — provide a text-generation model key (e.g. OpenRouter).
- Some `--expect` completion checks only read window title; re-read state yourself to verify completion.
- Privacy: many tools send conversation/page contents to TypeSafe; check "what gets sent" before using with confidential data. Jev-cu sends only screen text, not screenshots.
- Pattern clusters: context compaction/pruning for Claude Code, per-turn model/effort routing for Codex, tool-call gates, reply-suggestion assistants (read-only screen OCR, user sends).

## Standout entries
- [jev-mcp](https://github.com/jkudish/jev-mcp) — 10 decision tools via MCP; `claude mcp add jev -- npx -y @jkudish/jev-mcp` (MCP)
- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) — Claude Code compaction replacement (agent tooling)
- [jev-pruner](https://github.com/tamaratran/jev-pruner) — prunes long Bash output before the model sees it (agent tooling)
- [hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills) — SKILL.md pack for routing, memory, computer use (skills)
- [jev-codex-router](https://github.com/0xNatoshi/jev-codex-router) — per-turn model/effort routing for Codex (routing)
- [jev-ultrafast](https://github.com/browser-use/jev-ultrafast) — browser agent (browser)
- [mobile-jev](https://github.com/droidrun/mobile-jev) — Android control via Mobilerun (mobile)
- [jev-semgrep](https://github.com/uehaj/jev-semgrep) — cross-lingual semantic grep with AND/OR/NOT (dev tool)
- [tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) — IRS form page classification ~$0.001/page (application)
- [neurolink](https://github.com/juspay/neurolink) — Juspay multi-provider layer incl. Jev decisions (integration)
- [simple-jev](https://github.com/featherless-ai/simple-jev) — any open model as Jev-style API (open alternative)
- [laya (receptron)](https://github.com/receptron/laya) — Laya in Node/TS via ONNX Runtime (open alternative)
- [JevHarness](https://github.com/TianyuCodings/JevHarness) — LLM-written Jev harnesses improved with GEPA (tooling)
- [building-with-jev-skill](https://github.com/dbreunig/building-with-jev-skill) — skill for writing/fixing Jev programs (skill)
- [minecraft-agent](https://github.com/rmalde/minecraft-agent) — Astra plans, Jev acts (game)
