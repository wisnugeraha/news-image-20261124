# The World in One Day — 24 November 2026

A make.fun entry for
[news-image-20261124](https://make.fun/bounty/news-image-20261124):
one image that sums up Tuesday, 24 November 2026 in world news.

[![make.fun bounty](https://make.fun/bounty/news-image-20261124/badge)](https://make.fun/bounty/news-image-20261124)

The image is a newspaper front page — "THE WORLD IN ONE DAY" —
with the date printed large and four stories that defined the day.

## The four stories

1. **Huang is back as Wall Street roars (lead).** Jensen Huang returned
   as Nvidia CEO on Monday 23 November, 11 days after resigning amid
   alleged espionage claims; the board reinstated him after Nvidia shares
   had lost about half their value (~$2.8T) since the 6 October peak.
   On Monday Nvidia jumped 31.5% (its biggest rise since 2003), the
   Nasdaq rose 6.5% (best since April 2025), the S&P 500 4.7% and the
   Dow 3% (+1,448 points). Asian markets opened higher on Tuesday morning.
   Sources: Reuters, Investor's Business Daily, Morningstar.
2. **24 dead in Indonesia factory fire.** Authorities confirmed on
   Monday 23 November that 24 people died in a fire at the PT Fonusa
   Agung Mulia candy factory in Cikande, Banten (fire on Saturday
   21 November); about 30 workers were still missing, with 500+
   rescue personnel on site and victims identified by DNA.
   Sources: AP via TBS News, Fire Engineering.
3. **Kiwis bat out a draw (sport).** The first India–New Zealand Test
   in Wellington ended in a draw on Monday 23 November: New Zealand
   239/5 (Mitchell 49*, Phillips 26*) held on after India declared
   at 720/9 — the highest total ever on New Zealand soil.
   Sources: AP, cricket.com.au.
4. **A train across two nations.** The first Saryu-Kamala Express
   arrived in Janakpur on Tuesday morning 24 November (departed Ayodhya
   on Monday afternoon, ~604 km, 19 hours); Modi and Nepal PM Balendra
   Shah flagged it off virtually on Monday. Regular weekly service
   starts 28 November. Sources: QNC News, webindia123, newkerala.

## How to run

Requires Python 3.13, standard library only — no network access.

```sh
python3 main.py
```

This copies `entry.png` (1024×1024 PNG, under 1 MiB) to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), creating the
output directory if needed. Running it twice produces byte-identical
output.

## Files

- `main.py` — the entry program (copies `entry.png` and verifies the copy's size).
- `entry.png` — the finished front page image.
- `LICENSE` — MIT License.
