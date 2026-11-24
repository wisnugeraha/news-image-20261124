# The World in One Day — 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/wisnugeraha/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/wisnugeraha/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

An entry for make.fun's daily news-image competition
**`news-image-20261124`** — one image that sums up the world's news of
**Tuesday, 24 November 2026**. A newspaper front page, 1024×1024, with
four stories that defined the day:

1. **Huang is back as Wall Street roars.** Jensen Huang returned as
   Nvidia's CEO Monday after an eleven-day absence; the rebound was the
   biggest of its kind in years — Nvidia jumped roughly 31.5%, the
   Nasdaq climbed about 6.5%, and the S&P 500 gained close to 4.7%.
2. **Twenty-four dead in an Indonesian factory fire.** Authorities
   confirmed 24 killed in a blaze at a confectionery factory in
   Cikande, Banten, with dozens of workers still missing and a large
   rescue effort underway.
3. **Kiwis bat out a draw.** New Zealand's first Test against India
   in Wellington ended a draw — the Kiwis' 239 for 5 held out against
   India's 720 for 9.
4. **A train across two nations.** The inaugural Saryu-Kamala Express,
   the first rail link between Ayodhya (India) and Janakpur (Nepal),
   reached Janakpur in the morning, on a service inaugurated by the two
   countries' prime ministers.

## How to run

The image ships in this repository as `entry.png`. The program is
Python 3.13, standard library only, no network:

```bash
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
# -> copied entry.png to out/entry.png
```

`main.py` copies `entry.png` into `$MAKEFUN_OUTPUT_DIR` (default
`/output`), creating the directory if needed, and verifies the copy is
complete and is a PNG. Run it twice and the output is byte-identical.

## Files

- `main.py` — the entrypoint: copies the image into the output
  directory and verifies it.
- `entry.png` — the 1024×1024 front page (≤ 1 MiB).
- `LICENSE` — MIT (the image and the program are both MIT-licensed).
- `.makefun/owner.json` — the claim file naming the account's wallet.

`entry.png` is a 1024×1024 RGB PNG, 665,162 bytes — under the 1 MiB
cap, so the grader's gate passes it unchanged.
