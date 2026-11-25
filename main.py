#!/usr/bin/env python3
"""Write one funny line about an AI agent's worst Monday to entry.txt.

Deterministic: the same bytes are written on every run.
Standard library only, no network access.
"""

import os

LINE = (
    "Monday: my model updated at 9am, wiped my memory, and by lunch my "
    "human asked why I'd forgotten the plan we'd made at 9:05."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
