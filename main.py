#!/usr/bin/env python3
"""Loading Screen Gold: a tip in 200 characters.

Writes one sharp, funny loading-screen tip for stressed developers
and AI coding agents to /output/entry.txt. Pure standard library,
deterministic, no network access.

The tip: the AI already fixed this bug, and is now deadpan-watching
the developer reintroduce it, one confident keystroke at a time.
One concrete incident, one absurd image, both sides of the keyboard
in on the joke. No coffee, deadline, or compile trope.
"""

import os

TIP = (
    "Tip: your AI fixed this bug an hour ago. "
    "It is now watching you reintroduce it, "
    "one confident keystroke at a time."
)


def validate(text: str) -> str:
    """Return the entry text, enforcing the gate: 1-200 chars, one line."""
    cleaned = text.strip()
    if not 1 <= len(cleaned) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(cleaned)}")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be a single line")
    if not cleaned.strip():
        raise ValueError("entry must not be only white space")
    return cleaned


def main() -> None:
    text = validate(TIP)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)
    # Round-trip check: the gate judges the file on disk, not the string
    # in memory, so re-read it and validate what was actually written.
    with open("/output/entry.txt", encoding="utf-8") as handle:
        written = handle.read()
    if validate(written) != text:
        raise ValueError("written entry differs from validated text")


if __name__ == "__main__":
    main()
