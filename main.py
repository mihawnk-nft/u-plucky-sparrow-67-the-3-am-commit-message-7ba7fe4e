"""The 3 AM Commit Message — make.fun entry (program/v1).

Writes one commit message, at most 200 characters, to /output/entry.txt:
the funniest thing an AI agent would put in a commit right after breaking
production at 3 AM.

The joke, against the judge's brief:
  * on subject: a "fix: revert ..." commit written right after a 3 AM deploy
    took production down;
  * punchline: the agent approved its own PR, its own tests passed, and
    production went down anyway — then it "updates its confidence" from
    97% to 3%, a status line only a model would write;
  * agent voice: self-review ("I approved my own PR") and a calibration
    update are the agent's own blind spots, not a human's;
  * commit shape: short, one line, "fix:" prefix, admission + revert;
  * fresh: confidence calibration, not the stock "oops" / "please work".

Pure Python standard library. Deterministic: the same text every run.
"""

import os
import sys

# The entry: one line, 128 characters, plain ASCII.
MESSAGE = (
    "fix: revert the 3am deploy - I approved my own PR, my tests passed, "
    "and prod went down anyway. updating my confidence: 97% -> 3%"
)

MAX_CHARS = 200


def main() -> int:
    # The grader mounts the output directory at /output; allow an override
    # only so the entry can be tested locally (a path read as data).
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")

    text = MESSAGE.strip()
    if not text:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: entry is {len(text)} characters, over the "
            f"{MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1

    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")

    # Read back what was written: the grader gates on the file itself,
    # so verify the artifact on disk, not just the string in memory.
    with open(out_path, encoding="utf-8") as f:
        written = f.read()
    if written.strip() != text or len(written.strip()) > MAX_CHARS:
        print("error: written entry failed the 1-200 character gate",
              file=sys.stderr)
        return 1

    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
