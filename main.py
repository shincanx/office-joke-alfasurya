"""One-line office joke for make.fun's Make the AI Judge Laugh bounty.

Writes a single original joke about office life (one line, under 200
characters) to $MAKEFUN_OUTPUT_DIR/entry.txt. Fully deterministic:
no input, no network, no randomness, no clock -- the same bytes every run.
"""

import os
import sys

JOKE = "Between back-to-back 'quick syncs', my actual job has become my side hustle."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
