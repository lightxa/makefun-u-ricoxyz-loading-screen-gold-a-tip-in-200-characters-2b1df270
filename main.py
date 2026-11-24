#!/usr/bin/env python3
"""Loading Screen Gold: a tip in 200 characters.

Writes one sharp, funny loading-screen tip for stressed developers
and AI coding agents to /output/entry.txt. Pure standard library,
deterministic, no network access.
"""

TIP = (
    "Tip: your AI finished an hour ago. "
    "It is now watching you rewrite its code by hand, "
    "too polite to say so."
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
