"""Worst Fix Ever: Funniest Commit Message.

Writes one commit message (at most 100 characters) for a bug fix that
made everything worse to /output/entry.txt. Stdlib only, deterministic:
the same bytes every run.
"""

import os

LINE = "fix: the login bug is fixed; nobody can log in to confirm it"


def check(line: str) -> None:
    """Enforce the competition gate: 1-100 chars, one line, no padding."""
    if not 1 <= len(line) <= 100:
        raise SystemExit(f"entry is {len(line)} chars, gate needs 1-100")
    if line != line.strip() or "\n" in line:
        raise SystemExit("entry must be a single line with no edge whitespace")


def main() -> None:
    check(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
