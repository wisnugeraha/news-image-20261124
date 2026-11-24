"""news-image-20261124: copy the finished front page to the output dir.

The image (entry.png) sits next to this script. Running the script places
an identical copy at $MAKEFUN_OUTPUT_DIR/entry.png (default /output).
Standard library only; no network access.
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
    if os.path.getsize(dest) != os.path.getsize(SOURCE):
        raise SystemExit("error: copied file size does not match entry.png")
    print(f"wrote {dest}")


if __name__ == "__main__":
    main()
