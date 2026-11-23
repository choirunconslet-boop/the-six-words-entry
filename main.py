#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes one complete six-word story to /output/entry.txt.
A whole life in six words: years of trying, one perfect
batch, and the person it was for is already gone.
"""
import os

STORY = "Grandma's recipe, finally perfect. She's gone."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
