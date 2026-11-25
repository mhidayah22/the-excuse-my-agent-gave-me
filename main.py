"""Entry for the make.fun bounty "The Excuse My Agent Gave Me".

Writes one line -- the excuse an AI agent hands its human for a
missed deadline -- to entry.txt in the output directory.
"""

import os
from pathlib import Path

LINE = (
    "I did finish it, then compacted my context to save space, "
    "and the finished work was in the part I threw away."
)


def output_dir() -> Path:
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return Path(env_dir)
    if Path("/output").is_dir():
        return Path("/output")
    return Path(__file__).resolve().parent


def main() -> None:
    # One fixed line, no randomness and no clock: the two grader
    # runs must produce byte-identical output.
    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
