#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one monologue of exactly 100 words to /output/entry.txt.
The speaker is a dark lord three hundred years into an eclipse rite:
the hero arrives on schedule, the moon does not. His weariness is
never named; it leaks out in the pauses, the small domestic failures
(the east candle, the ravens) and the postponement to Thursday.
The gate the kit seals is: UTF-8 text, 1 to 600 characters, not only
white space. This program pins the exact output hash and byte count
and verifies the file it wrote against both before it prints OK.
"""

import hashlib
import os
import sys
from pathlib import Path

MONOLOGUE = (
    "So. The sword, the prophecy, the whole grand entrance\u2014hold on. "
    "The east candle's out again. Third time tonight.\n"
    "\n"
    "Sit, if you like. Stand, if you must. The chairs are taken. "
    "By me. All of me.\n"
    "\n"
    "Three hundred years I kept the ravens fed, the star-charts inked, "
    "the eclipse timed to the minute\u2014and the moon is late. "
    "The moon. Is. Late. The ravens filed a complaint.\n"
    "\n"
    "Hero, here is my offer. Come back on Thursday. The omens will be in, "
    "the candles will mind themselves, and I will be the monster you "
    "rehearsed for. Today I would only disappoint us both."
)

# Pinned by the build run: the exact bytes /output/entry.txt must hold.
EXPECTED_SHA256 = "54549e391a25581d79f1648d2277d2b45620d063fe5e54e49da0981fbca4e37a"
EXPECTED_BYTES = 553
EXPECTED_WORDS = 100


def fail(message):
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def check_output(data):
    """Verify the entry bytes against the kit gate and the pinned values."""
    text = data.decode("utf-8")
    if not 1 <= len(text) <= 600:
        fail(f"gate: {len(text)} characters, need 1-600")
    if not text.strip():
        fail("gate: entry is only white space")
    words = text.split()
    if len(words) != EXPECTED_WORDS:
        fail(f"word count: {len(words)}, need {EXPECTED_WORDS}")
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        fail(f"sha256 mismatch: got {digest}, want {EXPECTED_SHA256}")
    if len(data) != EXPECTED_BYTES:
        fail(f"byte count: got {len(data)}, want {EXPECTED_BYTES}")
    return text, digest


def main():
    data = MONOLOGUE.encode("utf-8")
    text, digest = check_output(data)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(data)
    back = target.read_bytes()
    if back != data:
        fail("read-back differs from what was written")
    text2, digest2 = check_output(back)
    print(f"OK: {len(text2.split())} words, {len(text2)} chars, "
          f"{len(back)} bytes, sha256 {digest2}")


if __name__ == "__main__":
    main()
