# Agency Poem 01 — entry by @velzard.
#
# Writes one poem about agency to /output/entry.txt: a speaker who declines
# the life laid out for him (his father's bakery) and chooses his own work.
# The poem is fixed text, so two runs write the same bytes. It is 1-1,000
# characters of UTF-8, as the gate requires.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

POEM = """My father left his apron on the nail
and called the bakery my rightful share.
All winter, flour settled like a veil
on every road I might have taken there —

I took the dawn train with a canvas sack,
a wrench, two shirts, the wages I had saved.
The chimney dwindled; I did not look back.
Beyond the glass, the unplowed water waved.

Now sparks fall blue along a trawler's seams;
I weld its ribs beneath the harbor lights.
No borrowed oven feeds my waking dreams.
The choice was mine; I claim its days and nights."""


def main():
    # Gate guard: the poem must be 1 to 1,000 characters and not only
    # whitespace; fail loudly here rather than hand the grader a bad file.
    assert 1 <= len(POEM) <= 1000 and POEM.strip(), "poem outside the gate"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "entry.txt").write_bytes(POEM.encode("utf-8"))


if __name__ == "__main__":
    main()
