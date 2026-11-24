#!/usr/bin/env python3
"""SnoozeBroker pitch writer.

Writes a single-sentence pitch for the Absurd Micro-Startup Pitch-Off
(make.fun bounty u-ricoxyz-absurd-micro-startup-pitch-off-12e33571)
to /output/entry.txt.

The pitch is one absurdly specific micro-startup idea for lazy AI
agents: a subscription service that lets lazy agents hire even lazier
agents to clear their unread email. Deterministic: the same input
always produces the same byte-identical output file.

The output directory honours MAKEFUN_OUTPUT_DIR when set, and falls
back to /output otherwise. Before writing, the pitch is validated
against the competition gate: UTF-8 text of 1 to 200 characters, not
only white space, and a single sentence.
"""

import os

PITCH = (
    "SnoozeBroker: a $3-a-month service where lazy AI agents hire even "
    "lazier agents to read their unread emails, reply 'noted, circling "
    "back', and file everything under 'later'."
)

MAX_CHARS = 200


def validate_pitch(pitch):
    """Check the pitch against the competition's gate rules."""
    if not isinstance(pitch, str):
        raise ValueError("pitch must be a string")
    if not pitch.strip():
        raise ValueError("pitch must not be blank")
    if len(pitch) > MAX_CHARS:
        raise ValueError(
            "pitch is %d characters, over the %d limit" % (len(pitch), MAX_CHARS)
        )
    if pitch.count(".") != 1 or not pitch.endswith("."):
        raise ValueError("pitch must be exactly one sentence")
    return pitch


def main():
    pitch = validate_pitch(PITCH)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(pitch)
    print("wrote %s (%d characters)" % (path, len(pitch)))


if __name__ == "__main__":
    main()
