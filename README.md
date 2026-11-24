# news-image-20261124

Front page summing up the world news of **Tuesday, 24 November 2026** —
built for the make.fun bounty
[news-image-20261124](https://make.fun/bounty/news-image-20261124).

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

## The four stories

1. **Markets (lead): Huang is back as Wall Street roars** — Nvidia jumps
   31% as Jensen Huang returns as CEO, 11 days after resigning; Nasdaq
   +6.5%, its best day since April 2025; S&P +4.7%, Dow +3%. Asia opens
   higher at Tuesday's open. (Reuters, Investor's Business Daily)
2. **Indonesia: 24 dead in factory fire** — rescuers search the ruins of
   the PT Fonusa Agung Mulia candy factory in Banten for about 30 workers
   still missing after Saturday's blaze. (AP)
3. **Sport: Kiwis bat out a draw** — New Zealand 239/5 holds off India
   after a record 720/9 declared at Wellington. (ICC, AP)
4. **India–Nepal: a train across two nations** — the first Saryu-Kamala
   Express reaches Janakpur, linking Ayodhya and Janakpur Dham.
   (Indian Railways)

All four stories were reported overnight into Tuesday, 24 November 2026;
the image names the day in its masthead.

## How it runs

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`) and verifies the copy
landed intact. The image is a whole PNG, 1024×1024, under 1 MiB.
No network. Two runs write identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
