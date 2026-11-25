#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open (make.fun).

Writes the entry -- one line of office comedy --
to /output/entry.txt, where the sealed scorer reads it."""

import os

TEXT = 'Our stand-up lasts longer than the sprint because Dave treats a quick update as a three-act play with a Q&A and an encore.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
