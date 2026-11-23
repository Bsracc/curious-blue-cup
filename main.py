#!/usr/bin/env python3
"""Write one calm, curious text to /output/entry.txt.

No network, no dependencies. Python 3.13.
"""

from pathlib import Path

TEXT = (
    "In the house at the end of the lane, someone leaves a blue cup "
    "on the windowsill every morning. It is always empty by noon, "
    "and no one has ever seen who drinks from it."
)


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
