#!/usr/bin/env python3
"""Independent floating-point cross-check of the Q(t) normalization.

Compares the two sides of the explicit-formula identity for the Route 001
family h_t(r) = exp(-(r-t)^2) + exp(-(r+t)^2) at the handoff test points.

Zero side (uses computed zero ordinates; the zeros involved are verified to
lie on the critical line, so the truncated sum is unconditional):

    Q(t) = 2 * sum_{gamma > 0} [exp(-(gamma-t)^2) + exp(-(gamma+t)^2)]

Prime side (the displayed formula from docs/RH_Weil_Gaussian_Handoff.md):

    Q(t) = 4 exp(1/4 - t^2) cos(t)
           - (2/sqrt(pi)) sum_{n>=2} Lambda(n)/sqrt(n) exp(-(log n)^2/4) cos(t log n)
           + (1/pi) integral_R exp(-x^2) Omega(t+x) dx,
    Omega(r) = Re psi(1/4 + i r/2) - log(pi).

Evidence level: high-precision floating-point experiment (mpmath, 30 dps),
NOT a rigorous enclosure. Agreement supports the normalization of Q(t) only;
it does not certify positivity and does not bear on RH.
"""
from __future__ import annotations

import mpmath as mp
from sympy import primerange

mp.mp.dps = 30

TEST_POINTS = [mp.mpf("11"), mp.mpf("12.25"), mp.mpf("17.57838")]
N_ZEROS = 25       # Gaussian decay: zeros beyond gamma ~ t + 8 contribute < 1e-28
N_PRIME = 120000   # exp(-(log N_PRIME)^2 / 4) ~ 1e-15
TOLERANCE = mp.mpf("1e-10")

print(f"computing first {N_ZEROS} zero ordinates...")
gammas = [mp.im(mp.zetazero(k)) for k in range(1, N_ZEROS + 1)]

print(f"building prime-power table up to {N_PRIME}...")
terms = []  # (log n, Lambda(n)/sqrt(n) * exp(-(log n)^2/4)) over prime powers n
for p in primerange(2, N_PRIME + 1):
    log_p = mp.log(p)
    pk = p
    while pk <= N_PRIME:
        u = mp.log(pk)
        terms.append((u, log_p / mp.sqrt(pk) * mp.exp(-u * u / 4)))
        pk *= p
print(f"  {len(terms)} prime-power terms")


def zero_side(t: mp.mpf) -> mp.mpf:
    return 2 * mp.fsum(mp.exp(-((g - t) ** 2)) + mp.exp(-((g + t) ** 2)) for g in gammas)


def omega(r: mp.mpf) -> mp.mpf:
    return mp.re(mp.digamma(mp.mpf("0.25") + 1j * r / 2)) - mp.log(mp.pi)


def prime_side(t: mp.mpf) -> mp.mpf:
    pole = 4 * mp.exp(mp.mpf("0.25") - t * t) * mp.cos(t)
    prime_term = -2 / mp.sqrt(mp.pi) * mp.fsum(w * mp.cos(t * u) for (u, w) in terms)
    arch = mp.quad(lambda x: mp.exp(-x * x) * omega(t + x), [-mp.inf, 0, mp.inf]) / mp.pi
    return pole + prime_term + arch


print()
print(f"{'t':>10}  {'zero side':>24}  {'prime side':>24}  {'abs diff':>10}")
worst = mp.mpf(0)
for t in TEST_POINTS:
    zs = zero_side(t)
    ps = prime_side(t)
    diff = abs(zs - ps)
    worst = max(worst, diff)
    print(f"{mp.nstr(t, 8):>10}  {mp.nstr(zs, 15):>24}  {mp.nstr(ps, 15):>24}  {mp.nstr(diff, 3):>10}")

if worst > TOLERANCE:
    raise SystemExit(f"FAILED: worst disagreement {mp.nstr(worst, 6)} exceeds {mp.nstr(TOLERANCE, 3)}")
print(f"\nagreement within {mp.nstr(worst, 3)} at all test points (tolerance {mp.nstr(TOLERANCE, 3)})")
print("scope=normalization cross-check only; not a rigorous enclosure; no bearing on RH")
