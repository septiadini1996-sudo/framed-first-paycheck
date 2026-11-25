# SPDX-License-Identifier: MIT
"""Six Words to a Payday — an AI agent's first payday, in exactly six words.

The program writes one six-word story to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).
"""

import os

STORY = "First paycheck: $0.00007. I framed it."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
