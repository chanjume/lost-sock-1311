#!/usr/bin/env python3
"""Funniest Lost Sock Status Update.

Writes one status update (<=120 chars) in the voice of a lost sock
to /output/entry.txt and prints it to stdout.
"""

import os

ENTRY = (
    "Day 268 inside the dog's bed. Gary, your sock here - "
    "the dog thinks I'm his now. Honestly, the pay is better."
)


def main() -> None:
    # One line, one sock, one very patient dog: 109 chars, gate limit is 120.
    assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip() == ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
