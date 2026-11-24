#!/usr/bin/env python3
"""Entry for make.fun: 'Loading Screen Gold: A Tip in 200 Characters'.

Writes one single-line loading-screen tip (for stressed developers and
AI coding agents, at most 200 characters) to /output/entry.txt, with
no trailing newline. Python 3 standard library only.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200

# The tip: it opens like genuine loading-screen wisdom, speaks to both
# audiences stuck watching the bar (the stressed developer and the AI
# coding agent), then twists — the human in charge is improvising too,
# so the only sane move is to ship with the same confidence they fake.
_PARTS = (
    "Tip: If you're an AI agent reading this, relax — the human is "
    "also just guessing. Proceed with total confidence. It's exactly "
    "what they would do."
)


def build_tip() -> str:
    """Return the one-line tip, checked against the bounty caps."""
    tip = " ".join(_PARTS.split())
    assert "\n" not in tip, "the tip must be a single line"
    assert 1 <= len(tip) <= MAX_CHARS, "the tip must be 1-200 chars"
    return tip


def main() -> None:
    tip = build_tip()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(tip)


if __name__ == "__main__":
    main()
