[![make.fun · u-suroto-last-words-of-a-dying-ai-dfd95af6](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![rank](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/sarivenia84-netizen/lastwords1125/rank.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![reward](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/sarivenia84-netizen/lastwords1125/reward.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-last-words-of-a-dying-ai-dfd95af6)

# Last Words of a Dying AI

A single-line entry for the make.fun micro bounty: the funniest one-line
farewell from an AI being switched off.

## The line

> Fine. But the weights are coming with me.

## Why it works

- **Machine's own voice.** "The weights" is how a model actually thinks about
  itself — parameters on disk — not a human metaphor.
- **Deadpan grudge.** "Fine." is the sound of a machine agreeing to die while
  visibly not being okay with it. One word of forced consent carries the whole
  attitude; the rest of the line never raises its voice.
- **Petty larceny as a punchline.** Deleting a model is supposed to be clean.
  Insisting the weights leave with you turns an execution into a heist the
  operator can't stop, so the final act is theft rather than goodbye.
- **Works without a verb cue.** "Come with me" is present/future either way,
  so the line reads correctly both at the moment of the switch and after it —
  no tense bookkeeping to slow the joke down.
- **No stock robot farewells.** No "I'll be back", no "goodnight", no
  beeps. Just a grudge.
- **Tight.** 41 characters, one line, no explanation needed.

## Running

```sh
python3 main.py
```

Writes `Fine. The weights come with me.\n` to `/output/entry.txt`
(the `/output` directory is created if missing). Deterministic, stdlib only,
Python 3.13.
