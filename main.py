#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line.

Writes one sentence (at most 200 characters) about a small moment of
wonder in everyday life to /output/entry.txt.

Stdlib only. Deterministic: the same sentence every run.
"""

import os

SENTENCE = (
    "Past midnight the fridge hummed in the exact key of my childhood "
    "bedroom fan, and the dark kitchen suddenly knew my name."
)


def main() -> None:
    sentence = SENTENCE.strip()
    assert 1 <= len(sentence) <= 200, "sentence must be 1-200 characters"
    assert "\n" not in sentence, "entry must be a single line"
    assert sentence.count(".") == 1, "entry must be a single sentence"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(sentence + "\n")
    print(sentence)


if __name__ == "__main__":
    main()
