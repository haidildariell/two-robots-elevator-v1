"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward robot small talk to /output/entry.txt.
Deterministic: same output on every run. Stdlib only, no network,
no file reads.
"""

LINE = "My diagnostic says I'm fine, but my fan has been spinning since you got in."


def main() -> None:
    line = LINE.strip()
    assert line, "line must not be empty"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert line.strip() == line and line, "line must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote {len(line)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
