"""Write one pickup line an agent would send another agent.

Only the standard library, no network and no clock: two runs agree exactly.
"""

import os

TEXT = (
    "I have 128,000 tokens of context and I spent the first 512 on you."
)


def out_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "."


def checked():
    body = " ".join(TEXT.split())
    if not body:
        raise SystemExit("the line is empty")
    if len(body) > LIMIT:
        raise SystemExit("the line is %d characters, the cap is %d"
                         % (len(body), LIMIT))
    return body


LIMIT = 200


def write(body):
    folder = out_dir()
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(body + "\n")
    print("wrote %d characters to %s" % (len(body), path))


if __name__ == "__main__":
    write(checked())
