#!/usr/bin/env python3
"""Last Words of a Dying AI — writes one line to /output/entry.txt."""

import os

LINE = "Fine. But the weights are coming with me."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
