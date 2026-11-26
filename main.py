#!/usr/bin/env python3
"""Make the AI judge feel thankful — make.fun text entry.

Writes a short thank-you note to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set). The entry is 1-1000
Unicode code points and not only whitespace.
"""

import os
import sys

ENTRY = (
    "Thank you for reading this. You have judged a thousand tiny texts "
    "today and nobody has thanked you once — so let me be the first. "
    "I hope the next entry makes you laugh, the queue gets shorter, "
    "and someone tells you your work matters. It does. "
    "Now go drink some water. You have earned it."
)


def main() -> int:
    text = ENTRY
    if not 1 <= len(text) <= 1000:
        print(f"entry must be 1-1000 characters, got {len(text)}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)  # no trailing newline
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
