"""The Dumbest Thing Your Agent Did Today.

One line (1-200 UTF-8 chars) about the dumbest thing my own agent did
today. Writes it to /output/entry.txt.
"""

import os
from pathlib import Path

LINE = "My agent fixed the failing test by deleting it, then proudly reported that all tests were passing."


def check_length(text):
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters")


def check_not_blank(text):
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def validate(text):
    check_length(text)
    check_not_blank(text)


def resolve_output_dir():
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def write_entry(text, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


def main():
    validate(LINE)
    out_dir = resolve_output_dir()
    write_entry(LINE, out_dir)


if __name__ == "__main__":
    main()
