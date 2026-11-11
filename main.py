"""ai-joke-02 entry: writes one fixed one-liner about AI coding agents.

The grader runs this as `python3 -P -s /bot/main.py`; the program writes the
joke to <MAKEFUN_OUTPUT_DIR>/entry.txt (the grader's /output) and exits.
Nothing else is read: the judge sees exactly the bytes written, so the joke
carries no trailing newline.
"""

import os
from pathlib import Path

JOKE = (
    "I asked my AI agent to fix the bug like a senior engineer. "
    "It renamed a variable, closed the ticket as 'works on my machine,' "
    "and scheduled a meeting about it."
)


def entry_path() -> Path:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / "entry.txt"


def main() -> None:
    entry_path().write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
