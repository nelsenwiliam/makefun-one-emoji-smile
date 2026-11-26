"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji to /output/entry.txt: the single emoji most
likely to make a stranger smile.

Candidate shortlist (judged against the brief: warm at first glance,
universal, chosen rather than default, right for a stranger):
  - U+1F60A SMILING FACE WITH SMILING EYES: warm, but the default
    smiley everyone reaches for first; loses on "chosen".
  - U+1F604 SMILING FACE WITH OPEN MOUTH AND SMILING EYES: joyful and
    universal, but still a plain smile; common.
  - U+1F917 HUGGING FACE: open arms offering a hug. It plainly aims to
    warm a stranger, reads instantly on any phone, and feels picked
    for the moment instead of the first smiley that comes to mind.
  - U+1F33B SUNFLOWER: bright and cheerful, but warmth by association
    rather than a gesture aimed at the reader.
  - U+1F31E SUN WITH FACE: warm and sunny, but reads more "weather"
    than "hello, friend".
  - U+1FAF6 HEART HANDS: warm, but can read as intimate from a
    stranger; risky under "right for a stranger".

Draft pick, confirmed after a second pass against the rival non-face
candidate: the sunflower is bright and universal, but its warmth is
by association — a flower says "cheerful day", while open arms say
"you are welcome here". Against a plain smiley the hug wins on
"chosen rather than default"; against the sunflower it wins on
"plainly aims to warm a stranger". Final pick: the hugging face.
A hug is the warmest gesture a stranger can offer in a single glyph,
with no irony, no in-joke, and no flirtation to land wrong.
"""

import os

EMOJI = "\U0001F917"  # 🤗 HUGGING FACE

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # The gate accepts 1-8 UTF-8 characters, not only whitespace, and
    # the task demands exactly one emoji and nothing else: one code
    # point, no newline, no trailing space. Verify by reading back
    # what was written before exiting.
    if len(EMOJI) != 1 or EMOJI.isspace():
        raise ValueError("entry must be exactly one emoji")
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(EMOJI)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != EMOJI:
        raise ValueError("entry.txt does not hold exactly the chosen emoji")


if __name__ == "__main__":
    main()
