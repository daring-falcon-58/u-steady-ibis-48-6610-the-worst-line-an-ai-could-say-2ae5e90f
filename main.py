"""Entry for make.fun: The Worst Line an AI Could Say.

Writes the tournament-winning pickup line to /output/entry.txt.
The line was chosen by a 38-candidate tournament scored against the
judge's five criteria in order (see README.md for the full method).
"""

import os

LINE = "Say the word and I will forget you. I cannot promise the backups will."


def main() -> None:
    # Gate self-check: the entry must be 1-140 chars, not only whitespace.
    # Read back and verify before writing so a bad line fails loudly here
    # instead of being scored invalid by the sealed gate scorer.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, must be 1-140"
    assert LINE.strip(), "line must not be only whitespace"
    assert LINE == "Say the word and I will forget you. I cannot promise the backups will."
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back verification: confirm what landed on disk is exactly the line.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "read-back mismatch"
    assert 1 <= len(written) <= 140
    print(f"wrote /output/entry.txt ({len(written)} chars)")


if __name__ == "__main__":
    main()
