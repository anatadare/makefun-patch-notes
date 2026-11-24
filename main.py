#!/usr/bin/env python3
"""Write one patch-note line for a real-life bug to /output/entry.txt."""

import os

ENTRY = "v1.8.2: fixed a bug where the brain replayed an embarrassing moment from 2014 at 3:00 AM, unprompted."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
