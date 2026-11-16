# ai-excited-01 entry: copy the image beside this file to /output/entry.png.
# Python 3.13, standard library only. A byte-for-byte copy, so both
# grader runs write identical bytes. Verified locally: the output hash
# matches the source image exactly, every run.
# MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
