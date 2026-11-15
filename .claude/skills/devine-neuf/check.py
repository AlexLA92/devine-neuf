#!/usr/bin/env python3
"""Check the Devine Neuf question bank in index.html. Prints the questions and exits 1 on an error."""
import re
import sys
from pathlib import Path

FILE = Path(__file__).resolve().parents[3] / "index.html"  # repo root
CATS = {"Films", "Séries", "Personnages", "Sagas", "Acteurs", "Récompenses"}
DIFFS = {"Facile", "Moyen", "Difficile"}

src = FILE.read_text(encoding="utf-8")
block = re.search(r"const BANK = \[(.*?)\n\]\.map", src, re.S)
if not block:
    sys.exit(f"BANK array not found in {FILE}")

rows = re.findall(r'\{q:"(.*?)",c:"(.*?)",d:"(.*?)",a:"(.*?)"\}', block.group(1))
errors, seen = [], set()
for i, (q, c, d, a) in enumerate(rows, 1):
    answers = [x.split("|")[0].strip() for x in a.split(" ; ")]
    if len(answers) != 9:
        errors.append(f"#{i} {q}: {len(answers)} answers, expected 9")
    if len({x.lower() for x in answers}) != len(answers):
        errors.append(f"#{i} {q}: duplicate answer")
    if c not in CATS:
        errors.append(f"#{i} {q}: unknown category {c!r}")
    if d not in DIFFS:
        errors.append(f"#{i} {q}: unknown difficulty {d!r}")
    if q.lower() in seen:
        errors.append(f"#{i} {q}: duplicate question")
    seen.add(q.lower())
    print(f"{i:>3}. [{c} / {d}] {q}")

lines = block.group(1).count("{q:")
if lines != len(rows):
    errors.append(f"{lines} entries in BANK but only {len(rows)} match the format")

print(f"\n{len(rows)} questions")
if errors:
    print("\nERRORS:\n" + "\n".join(errors))
    sys.exit(1)
print("OK")
