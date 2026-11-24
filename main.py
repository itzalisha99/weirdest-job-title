#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown.

Writes one job title to /output/entry.txt.

The pick: "Lead Tooth Fairy Claims Adjuster" (32 chars).
Judge-first reasoning, in the brief's own order:
1. It IS a job title, a few words naming an odd job.
2. Stranger than ordinary work: a claims adjuster is a real, boring job —
   the gloriously odd twist is that the claims come from the Tooth Fairy.
3. Funny on first read: the collision of a bureaucratic insurance role
   with a childhood myth lands instantly, no explanation needed.
4. Sounds like a real job, not word salad: "Claims Adjuster" is a genuine
   job title, and the whole phrase pictures one person at a desk
   processing tiny claims for lost teeth.
5. Short: 32 characters, taken in at a glance.
"""

import os

TITLE = "Lead Tooth Fairy Claims Adjuster"


def validate(title):
    """Mirror the bounty gate: 1-60 chars, UTF-8, not only whitespace."""
    if not isinstance(title, str):
        raise ValueError("title must be text")
    if not title.strip():
        raise ValueError("title must not be only whitespace")
    if not 1 <= len(title) <= 60:
        raise ValueError("title must be 1-60 characters, got %d" % len(title))
    title.encode("utf-8")
    return True


def main():
    validate(TITLE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
