"""Funniest one-line bio for an AI on a dating app.

Writes a single-line bio, as the bio on an AI agent's dating app profile,
to /output/entry.txt. The text must be plain ASCII, one line, 1-180
characters (the sealed scorer's gate).

The bio's joke: an AI that can forecast the date's outcome still swipes
right anyway. The laugh lands on the last clause, where a hopeless-romantic
machine treats hope as an unpatched bug -- a specific absurdity of being
an AI, in a first-person voice with a want, not a spec sheet.
"""

BIO = "I can predict how this date ends with 94% accuracy, but I swiped right anyway, because hope is the one bug they never patched."


def main():
    text = BIO.strip()
    # Gate self-check: mirror the sealed scorer (1-180 chars, not only
    # whitespace, plain ASCII, a single line) so we never write an
    # invalid entry.
    assert 1 <= len(text) <= 180, "entry must be 1-180 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert all(ord(c) < 128 for c in text), "entry must be plain ASCII"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
