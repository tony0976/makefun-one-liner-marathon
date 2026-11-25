#!/usr/bin/env python3
"""Writes this entry's text to /output/entry.txt."""

import os

TEXT = """I asked my AI agent to fix one small bug; it fixed it, then fixed the fix, then wrote a 40-page postmortem explaining why the original bug was actually my fault."""

MAX_CHARS = 280

def main():
    # The bounty scores a single one-line joke of at most 280 chars; fail loudly instead of submitting a malformed entry.
    assert 1 <= len(TEXT) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} chars, got {len(TEXT)}"
    assert "\n" not in TEXT, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
