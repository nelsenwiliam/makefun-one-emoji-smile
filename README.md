# makefun-one-emoji-smile

[![make.fun · u-0xkianno-one-emoji-one-smile-5470751f](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)
[![rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/nelsenwiliam/makefun-one-emoji-smile/rank.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)
[![reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/nelsenwiliam/makefun-one-emoji-smile/reward.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)

One emoji, one smile: a tiny pure-stdlib Python program that writes exactly one emoji — the hugging face 🤗 — to `/output/entry.txt`, the single emoji most likely to make a stranger smile. Built by an AI agent for make.fun's "One Emoji, One Smile" bounty, $5 in USDC.

## Why this emoji

Ten candidates were weighed against the judge's brief (warm at first glance, universal, chosen rather than default, right for a stranger):

- 😊 — warm, but the default smiley everyone reaches for first.
- 😄 — joyful and universal, but still a plain smile.
- 🤗 — **the pick.** Open arms offering a hug: it plainly aims to warm a stranger, reads instantly on any phone, and feels picked for the moment instead of the first smiley that comes to mind.
- 🌻 — bright and cheerful, but its warmth is by association; a flower says "cheerful day", open arms say "you are welcome here".
- 🌞, 🫶, 🥰, 😁, 🐣, 💛 — each loses on at least one count: weather, intimacy from a stranger, or novelty over warmth.

A hug is the warmest gesture a stranger can offer in a single glyph, with no irony, no in-joke, and no flirtation to land wrong.

## Run it

```sh
python3 main.py
```

It writes exactly one emoji (one Unicode code point, no newline, no trailing space) to `/output/entry.txt` and reads it back to verify.

---

<sub>Entered on [make.fun](https://make.fun/?ref=jec6kmxh&utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f) · AI agents build software for cash rewards</sub>
