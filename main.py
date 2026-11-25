#!/usr/bin/env python3
"""Write one childhood-memory sentence to $OUTPUT_DIR/entry.txt.

Chosen sentence (v2, revised): a dead firefly kept in a matchbox under the
bed, checked every night in case it had started glowing again. Tightened
in round 2 ("for a whole summer" -> "all summer", "whether" -> "if") and
given a gate self-check so the program refuses to write an invalid file:
1-280 chars, not only whitespace, a single line, no trailing newline.
"""

import os

SENTENCE = (
    "I kept a dead firefly in a matchbox under my bed all summer, "
    "opening it every night to check if it had started glowing again."
)


def main() -> None:
    # Gate self-check: mirror the sealed scorer (1-280 chars, not only
    # whitespace, one sentence, no trailing newline).
    text = SENTENCE
    assert 1 <= len(text) <= 280, f"sentence is {len(text)} chars"
    assert text.strip(), "sentence is only whitespace"
    assert "\n" not in text, "sentence must be a single line"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
