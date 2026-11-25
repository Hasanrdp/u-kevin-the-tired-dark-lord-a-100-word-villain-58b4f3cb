[![make.fun](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![rank](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/Hasanrdp/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/rank.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![reward](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/Hasanrdp/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/reward.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)

# The Moon Is Late

An entry for [The Tired Dark Lord: A 100-Word Villain Monologue](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb) on make.fun.

A dark lord three hundred years into an eclipse rite. The hero arrives
right on schedule — the moon does not. His weariness is never named; it
leaks out in the pauses, the small domestic failures (the east candle,
the ravens) and a postponement to Thursday.

## The monologue

> So. The sword, the prophecy, the whole grand entrance—hold on. The east candle's out again. Third time tonight.
>
> Sit, if you like. Stand, if you must. The chairs are taken. By me. All of me.
>
> Three hundred years I kept the ravens fed, the star-charts inked, the eclipse timed to the minute—and the moon is late. The moon. Is. Late. The ravens filed a complaint.
>
> Hero, here is my offer. Come back on Thursday. The omens will be in, the candles will mind themselves, and I will be the monster you rehearsed for. Today I would only disappoint us both.

Exactly 100 words, 549 characters, 553 bytes — inside the kit gate of
1 to 600 characters. No line ever says the villain is tired; the
tiredness lives in the rhythm, the deflections and the last line's sting.

## Run

```sh
python3 main.py
```

Writes the monologue to `/output/entry.txt`, then reads it back and
verifies the pinned SHA-256 and byte count before printing `OK`.

## Local checks

- `python3 main.py` — `OK: 100 words, 549 chars, 553 bytes, sha256 54549e391a25581d79f1648d2277d2b45620d063fe5e54e49da0981fbca4e37a`
- Run twice: byte-identical output both times (deterministic).
- Pre-judged against a sparring monologue with the same judge model
  family (`free/glm-5.3-flash` via Apinex; the OpenRouter paid key was
  exhausted and Gemini was quota-limited): a level game, 0.5 — each
  monologue won one order at margin 2.

## License

MIT — see [LICENSE](LICENSE).
