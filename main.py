"""Emit one pickup line an agent sends another agent, into entry.txt.

Standard library only: the program never touches the network or a clock, and
it holds nothing that changes between runs, so its output is byte-identical
every time.
"""

import os
import sys

CEILING = 200

LINE = (
    "I have 128,000 tokens of context and I spent the first 512 on you."
)


def normalise(raw):
    """Collapse runs of whitespace so the file holds one clean line."""
    return "".join(part + " " for part in raw.split()).rstrip()


def validate(text):
    """Refuse a line the gate would score as invalid."""
    if not text:
        raise ValueError("the line is empty")
    if not text.strip():
        raise ValueError("the line is only whitespace")
    length = len(text)
    if length > CEILING:
        raise ValueError("the line is %d characters, past the %d allowed"
                         % (length, CEILING))
    return text


def destination():
    """$MAKEFUN_OUTPUT_DIR when the grader sets it, else the working folder."""
    root = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip() or "."
    return os.path.join(root, "entry.txt")


def run():
    text = validate(normalise(LINE))
    path = destination()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
        handle.write("\n")
    sys.stdout.write("%d characters in %s\n" % (len(text), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
