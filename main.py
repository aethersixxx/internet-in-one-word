#!/usr/bin/env python3
"""Entry for make.fun bounty 'The Internet in One Word'.

Writes exactly one word -- the whole internet in a single word -- to
/output/entry.txt. No arguments, no network, no randomness: two runs
write byte-identical files, as the gate's determinism check requires.
"""
import os

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

# The whole internet, in one word.
WORD = "brainrot"


def main() -> None:
    os.makedirs(OUTPUT_DIR, mode=0o755, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(WORD)
    os.chmod(OUTPUT_FILE, 0o644)


if __name__ == "__main__":
    main()
