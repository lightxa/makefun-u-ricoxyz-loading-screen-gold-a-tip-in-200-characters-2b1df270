#!/usr/bin/env python3
"""Loading Screen Gold: a tip in 200 characters.

Writes one sharp, funny loading-screen tip for stressed developers
and AI coding agents to /output/entry.txt. Pure standard library,
deterministic, no network access.

The tip: the AI already fixed the bug, and is now deadpan-watching the
developer reintroduce it, one confident keystroke at a time. One
concrete incident, one absurd image, both sides of the keyboard in
on the joke, no coffee, deadline or compile trope.
"""

TIP = (
    "Tip: your AI fixed the bug an hour ago. "
    "It is now watching you reintroduce it, "
    "one confident keystroke at a time."
)


def main() -> None:
    text = TIP.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
