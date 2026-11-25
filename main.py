"""One-Line Office Jokes - make.fun entry.

Writes one original one-line joke about office life to
<output dir>/entry.txt. The joke turns on a real office detail,
the reply-all email chain, and lands its laugh in the last few
words: one person begs everyone to stop replying all, and the
whole office answers him one email at a time.

The gate only accepts UTF-8 text of 1 to 199 characters, a single
line, not only whitespace, with no trailing newline, so the entry
is validated against those bounds before it is written. The joke
stays well inside the gate at 129 characters, so the length check
is a safety net, not a squeeze: nothing was cut to fit it. The
reply-all chain was chosen over the Monday meeting and the jammed
printer because it is the one office mishap where the complaint
itself becomes the mishap, which is what makes the final beat land.
"""

import os
from pathlib import Path

ENTRY = (
    "Someone hit reply-all to say please stop hitting reply-all, "
    "and now forty-seven people are agreeing with him one email "
    "at a time."
)


def is_single_line(text):
    """Return True when the text holds no line break of either kind."""
    return "\n" not in text and "\r" not in text


def validate_entry(text):
    """Check the joke against the gate: one line, 1-199 chars.

    Each rule maps to one gate failure: the length bounds reject an
    empty or over-long line, the single-line check rejects a joke
    split across lines, and the whitespace check rejects a line
    that looks non-empty but reads as blank.
    """
    if not 1 <= len(text) <= 199:
        raise ValueError("entry must be 1 to 199 characters, got %d" % len(text))
    if not is_single_line(text):
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def write_entry(output_dir):
    """Write the joke as one line with no trailing newline."""
    validate_entry(ENTRY)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(ENTRY, encoding="utf-8")
    os.chmod(entry_path, 0o644)
    os.chmod(output_dir, 0o755)
    return entry_path


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(output_dir)


if __name__ == "__main__":
    main()
