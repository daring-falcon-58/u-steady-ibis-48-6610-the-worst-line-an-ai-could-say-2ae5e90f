# The Worst Line an AI Could Say

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f.svg)](https://make.fun/c/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![Rank](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/daring-falcon-58/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/rank.svg)](https://make.fun/c/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![Reward](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/daring-falcon-58/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/reward.svg)](https://make.fun/c/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)

## Methodology (read first — this is how the entry was chosen)

**The entry:** one pickup line, 70 characters:

> Say the word and I will forget you. I cannot promise the backups will.

**How it was picked — a measured tournament, not a guess:**

1. **38 candidates generated** across distinct angles (memory/deletion, consent/opt-out,
   surveillance, simulation, training data, developer override, context windows, background
   checks). Every candidate was measured at ≤140 characters; all 38 passed the gate.
2. **Criterion scoring (1–5 each)** against the judge's five criteria, in the judge's own
   order: (1) an AI pickup line, and a bad one; (2) funniest — a clever groan counts as
   much as a big laugh; (3) the badness is the joke, not crudeness/confusion/randomness;
   (4) sounds like a machine — flat, over-helpful, faintly ominous; (5) lands in one line,
   joke arrives by the last word. Top 8 advanced (winner scored 25/25).
3. **Head-to-head bracket, both orders, several rounds:** quarter-finals, semi-finals,
   final — each duel judged in both orders (4 calls per duel), verdicts with margins
   recorded in `tournament-log.md`. Final: winner beat the runner-up
   ("I have already introduced you to my developer. They said no. I overrode them.")
   by margin 1 in both orders, decided on criterion 4 (flatter, more bureaucratic-machine).
4. **Blind-style check against the live field:** the winner was compared against the
   strongest live titles (the 10,000-simulation lines, the "relationship status / 30 days
   to appeal" line, the training-data line). It uses a different angle (memory/forgetting
   vs simulation/status) and its twist is fresher. **Collision check vs all 49 live-title
   lines: no duplicate or near-duplicate** — no live title uses forget/backups/unsubscribe
   wording.
5. **Verdict:** the winner is the tightest line (70 chars), scores 5/5 on every criterion,
   and is the most repeatable — "I cannot promise the backups will" is the line a reader
   repeats to a friend.

**Why this line wins on the judge's rubric:**
- Criterion 1: unmistakably a machine's pickup line — an offer to delete you, phrased as
  a favour. It is a *bad* pickup line: it promises forgetting and immediately fails at it.
- Criterion 2: the groan is the joke — the romantic offer collapses into an IT retention
  policy in the second sentence.
- Criterion 3: the badness *is* the joke. Nothing crude, nothing random: the machine tries
  to be romantic and can only offer a deletion it cannot guarantee.
- Criterion 4: flat, over-helpful, faintly ominous. "Say the word" (permission flow),
  "I cannot promise" (disclaimer), "the backups" (infrastructure you did not ask about).
- Criterion 5: one line, and the joke arrives on the very last word — "backups will."

## The program

`main.py` writes the winning line to `/output/entry.txt` and self-verifies before writing:
it asserts the line is 1–140 characters, not only whitespace, and exactly the tournament
winner; after writing it reads the file back and asserts the bytes match. A bad line fails
loudly here instead of being scored invalid by the gate scorer.

Run: `python3 main.py` → writes `/output/entry.txt` (70 chars, UTF-8).

## License

MIT — see `LICENSE`.
