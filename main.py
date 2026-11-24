#!/usr/bin/env python3
"""Copy the competition image into the make.fun output directory.

Context
-------
make.fun competition **news-image-20261124** — "Sum up 24 November's
world news in one image". The deliverable is a PNG (1024x1024, at most
1 MiB) that a grader runs this program to produce. The image
``entry.png`` already lives next to this script (at the submitted
commit it ships in the repository). The grader runs us with no
network, on a read-only ``/bot`` (the repository) and a writable
``/output``; we respect ``$MAKEFUN_OUTPUT_DIR`` when it is set.

What this program does
----------------------
1. Locate ``entry.png`` in the same directory as this script.
2. Create the output directory if it does not exist yet.
3. Copy the image byte-for-byte to ``<output>/entry.png``.
4. Verify the copy's size matches the source's size; if it does not,
   exit non-zero with an error message (the grader's gate requires
   a whole, valid file and two runs that are byte-identical).
5. Print a confirmation.

Determinism: the copy is a straight ``shutil.copyfile`` (bytes only,
no timestamps embedded in the image data), so two runs in any two
output directories produce identical bytes — which is what the
competition's "two runs must write the same bytes" rule requires. No
network, no time, no randomness touches the output bytes.
"""

from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path

# The image ships in the repository next to this entrypoint.
SOURCE_NAME = "entry.png"
# make.fun's default output directory; overridable via env for local tests.
DEFAULT_OUTPUT_DIR = "/output"
# The image is a 1024x1024 PNG; its first bytes must read as PNG.
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def source_image() -> Path:
    """Return the path to the shipped image, next to this script."""
    here = Path(__file__).resolve().parent
    src = here / SOURCE_NAME
    if not src.is_file():
        raise SystemExit(f"error: {src} not found next to this script")
    return src


def run(src: Path, outdir: Path, verbose: bool) -> None:
    """Copy ``src`` to ``outdir/entry.png`` and verify the result."""
    outdir.mkdir(parents=True, exist_ok=True)
    dst = outdir / SOURCE_NAME

    # Straight bytes copy: no metadata, no re-encode, fully deterministic.
    with src.open("rb") as fin, dst.open("wb") as fout:
        shutil.copyfileobj(fin, fout)

    # Verify the copy is complete and intact.
    if src.stat().st_size != dst.stat().st_size:
        raise SystemExit(
            f"error: copy size mismatch: source {src.stat().st_size} bytes "
            f"!= destination {dst.stat().st_size} bytes ({dst})"
        )

    # PNG must start with the magic bytes so the grader's format check
    # (PNG vs JPEG, told apart by the first bytes) sees a valid PNG.
    with dst.open("rb") as f:
        if f.read(8) != PNG_MAGIC:
            raise SystemExit(f"error: {dst} does not look like a PNG")

    if verbose:
        print(
            f"{SOURCE_NAME}: {dst.stat().st_size} bytes -> {dst} "
            f"(PNG magic OK, size verified)"
        )
    else:
        print(f"copied {SOURCE_NAME} to {dst}")


def main(argv: list[str]) -> int:
    verbose = False
    i = 0
    while i < len(argv) and argv[i] in ("--verbose", "-v"):
        verbose = True
        i += 1
    if i < len(argv):
        print("usage: main.py [--verbose]", file=sys.stderr)
        return 2

    src = source_image()
    outdir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR)
    run(src, outdir, verbose)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
