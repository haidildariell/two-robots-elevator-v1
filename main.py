#!/usr/bin/env python3
"""Two Robots in an Elevator - one-line entry writer.

Writes a single line of awkward robot small talk to /output/entry.txt.
Deterministic: fixed string, no randomness, no network, no file reads.
"""

import os

LINE = "I was going to compliment your paint job, but my thermal camera caught me blushing at 42 degrees."
OUTPUT_PATH = "/output/entry.txt"


def validate_line(line):
    """Check the entry line against the bounty gate: UTF-8, 1-200 chars,
    not only whitespace, single line."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    if len(line) < 1 or len(line) > 200:
        raise ValueError("line must be 1-200 chars")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if line.strip() == "":
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")
    return line


def write_entry(line, path):
    """Validate the line, then write it to path, creating parent dirs."""
    checked = validate_line(line)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(checked + "\n")
    return len(checked)


def main():
    count = write_entry(LINE, OUTPUT_PATH)
    print("Wrote %d chars to %s" % (count, OUTPUT_PATH))


if __name__ == "__main__":
    main()
