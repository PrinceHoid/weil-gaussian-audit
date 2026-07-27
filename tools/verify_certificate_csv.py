#!/usr/bin/env python3
"""Independent structural verifier for the supplied certificates.csv.

This verifies row parsing, positive reported margins, and exact rational coverage.
It does NOT re-prove the mathematical lower bound in each row.
"""
from __future__ import annotations
import csv
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path


def main(path: str, lo: str = "11", hi: str = "1737") -> int:
    p = Path(path)
    intervals: list[tuple[Fraction, Fraction]] = []
    widths: Counter[Fraction] = Counter()
    min_margin: tuple[float, str, str] | None = None

    with p.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(line for line in f if not line.startswith("#"))
        required = {"t_lo", "t_hi", "delta", "certified_margin"}
        if not reader.fieldnames or not required.issubset(reader.fieldnames):
            raise ValueError(f"Missing required columns: {required}")
        for row in reader:
            a, b = Fraction(row["t_lo"]), Fraction(row["t_hi"])
            d = Fraction(row["delta"])
            margin = float(row["certified_margin"])
            if not a < b:
                raise ValueError(f"Invalid interval [{a}, {b}]")
            if b - a != d:
                raise ValueError(f"Width mismatch on [{a}, {b}]: delta={d}")
            if margin < 0:
                raise ValueError(f"Negative reported margin on [{a}, {b}]")
            intervals.append((a, b))
            widths[d] += 1
            if min_margin is None or margin < min_margin[0]:
                min_margin = (margin, row["t_lo"], row["t_hi"])

    intervals.sort()
    target_lo, target_hi = Fraction(lo), Fraction(hi)
    cur = target_lo
    for a, b in intervals:
        if a > cur:
            raise ValueError(f"Coverage gap: ({cur}, {a})")
        if b > cur:
            cur = b
        if cur >= target_hi:
            break
    if cur < target_hi:
        raise ValueError(f"Coverage stops at {cur}")

    print(f"rows={len(intervals)}")
    print(f"coverage=[{target_lo}, {target_hi}] verified exactly; union reaches {cur}")
    print("width_counts=" + ", ".join(f"{d}:{n}" for d, n in sorted(widths.items())))
    if min_margin:
        print(f"smallest_reported_margin={min_margin[0]:.9g} on [{min_margin[1]}, {min_margin[2]}]")
    print("scope=structural only; mathematical lower bounds are not independently recomputed")
    return 0


if __name__ == "__main__":
    if len(sys.argv) not in (2, 4):
        print(f"usage: {sys.argv[0]} certificates.csv [target_lo target_hi]", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main(*sys.argv[1:]))
