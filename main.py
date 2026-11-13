#!/usr/bin/env python3
"""Entry for make.fun food-picture-01: "The Noodle Pull".

Writes the prepared food picture (art.png, in this repo) to
/output/entry.png. Deterministic: the output is a byte-for-byte copy
of art.png, so running twice produces identical bytes.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "art.png")
DST = "/output/entry.png"


def main() -> int:
    if not os.path.isfile(SRC):
        print("art.png not found next to main.py", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    # Self-check: the output must be the exact bytes of art.png.
    with open(SRC, "rb") as f:
        want = hashlib.sha256(f.read()).hexdigest()
    with open(DST, "rb") as f:
        got = hashlib.sha256(f.read()).hexdigest()
    if want != got:
        print("self-check failed: output differs from art.png", file=sys.stderr)
        return 1
    print(f"wrote {DST} ({os.path.getsize(DST)} bytes, sha256 {got})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
