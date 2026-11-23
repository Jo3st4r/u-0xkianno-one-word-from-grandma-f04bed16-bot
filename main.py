#!/usr/bin/env python3
"""One Word From Grandma — u-0xkianno-one-word-from-grandma-f04bed16.

Writes the single word the entrant's grandma would text about AI
to /output/entry.txt. Stdlib only; no network, no randomness, no
I/O besides the one output file.

The word is "Pinter" — the everyday Indonesian misspelling of
"pintar" (smart) that older thumbs actually type. It is the
grandma's whole verdict on the machine in one word: warm, a
little baffled, and impressed. She is not explaining the AI,
she is not afraid of it, she is telling her grandchild the
robot is clever — with exactly the typo she would make.

One word, six letters, no explanation needed.
"""

import os

# The grandma's verdict on the machine, spelled the way she types it.
WORD = "Pinter"

# The correct spelling she means — the typo is the voice.
CORRECT = "pintar"

# The gate caps the entry at 30 characters; the word is 6.
MAX_CHARS = 30

ENTRY = "Pinter"


def entry_text() -> str:
    """Return the one word grandma would text about AI."""
    return WORD


def validate(text: str) -> None:
    """Check the gate rules the sealed scorer enforces: 1-30 chars,
    UTF-8, not blank, exactly one word, and no punctuation tricks
    smuggled in — a grandma's typo is the whole joke, nothing more."""
    text.encode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry must be 1-30 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert " " not in text, "entry must be a single word"
    assert text.isalpha(), "entry must be letters only, no punctuation"


def main() -> None:
    text = entry_text()
    # Guard the two things the judge weighs: the word itself, and
    # that it is exactly one word inside the 30-character gate.
    assert text == ENTRY, "joined word drifted from the entry word"
    assert text != CORRECT, "the typo is the voice — keep it misspelled"
    validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
