# AstonyCat/jev-tab-grouper
- **One-liner:** "Tab Sorter" is a Chrome MV3 extension that groups every open tab into named, colored groups. It sorts with Jev (fixed rules, ~1s) or with any OpenAI-compatible LLM (the LLM invents the groups).
- **Language(s):** English README (Chinese tagline and screenshots)
- **Type:** project/code (not a list)
- **Scale:** One small project (manifest, grouper.js, background.js, options page), v1.1.0, MIT license. No list entries.
- **Quality flags:** Real, working-looking code that calls the native API directly. It has a privacy policy dated 2026-09-20 and screenshots. It uses the floating `jev-latest` alias, not a pinned version. Not promotional.
- **Unique value:** A concrete example of the **native `/v1/systemone` wire format** in production JS. It shows a confidence-threshold "review" bucket and a comparison of Jev vs an LLM engine for the same task. Nice pattern: saved LLM-invented groups can be adopted as fixed Jev rules.

## Facts claimed about Jev
- Endpoint: `POST https://api.typesafe.ai/v1/systemone` with a `Authorization: Bearer <key>` header. The body is `{ state, model: "jev-latest", questions }`.
- Question shape as used in the code: `questions` is an **object keyed by question id**. Each value is `{type: "choice", instructions: "...", criteria: {g0: "label — desc", g1: ...}}`, so the options are passed as a `criteria` map.
- Response shape as used in the code: `data.answers[<id>].choice` (the chosen criteria key), `data.answers[<id>].confidence` (a number), and `data.usage`.
- API keys come from console.typesafe.ai/settings/keys.
- Claims: a whole window resolves in "a single sub-second call" with **zero completion tokens**, because Jev prices output at $0. A measured run took **456 ms end-to-end** (screenshot), vs 10–30s for the LLM engine ("20× longer", 500+ output tokens). "Pennies per month of daily use."
- "100% structured answers, zero parsing failures."

## Key insights / patterns
- **One `choice` question per item, all in one parallel call**: batch classification of N items in a single request.
- **Confidence gate**: `CONFIDENCE_THRESHOLD = 0.6`. Tabs below it go to a "⚠️ review" bucket instead of being forced into a group.
- **LLM for discovery, Jev for the routine**: use an LLM occasionally to invent a taxonomy, then freeze it as Jev rules for fast daily runs. This is a clean way to combine System 2 and System 1.
- The last rule line is a fallback bucket (the same idea as adding an explicit "other" option).
- Operational: every API failure logs the HTTP status and response body, and a "test connection" button runs a real 3-tab classification.
- Privacy: tab titles and domains are sent only when the user clicks, and keys are stored in `chrome.storage.local`.

## Standout entries
- [AstonyCat/jev-tab-grouper](https://github.com/AstonyCat/jev-tab-grouper) — Chrome tab grouper, Jev rules engine vs LLM engine (browser extension/project)
