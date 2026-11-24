#!/usr/bin/env python3
"""news-image-20261124 entry (Python 3.13, standard library only).

The entry is a front-page image summing up the world news of Tuesday
24 November 2026. The image itself is entry.png beside this file; this
program copies it to the grader's output directory as entry.png.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    # Verify the copy landed intact: same size as the source, or fail loudly
    # instead of silently handing the grader a truncated image.
    if os.path.getsize(dest) != os.path.getsize(SOURCE):
        raise SystemExit("entry.png copy failed: size mismatch")


if __name__ == "__main__":
    main()
