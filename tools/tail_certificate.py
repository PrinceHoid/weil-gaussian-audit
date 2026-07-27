#!/usr/bin/env python3
"""Executable interval certificate for the Route 001 tail theorem.

Certifies, in mpmath.iv interval arithmetic, the bound

    Q(t) >= M(T) > 0   for every t >= T,   with T = 2000,

for the Route 001 functional

    Q(t) = 4 exp(1/4 - t^2) cos(t)
           - (2/sqrt(pi)) sum_{n>=2} Lambda(n)/sqrt(n) exp(-(log n)^2/4) cos(t log n)
           + (1/pi) integral_R exp(-x^2) Omega(t+x) dx,
    Omega(r) = Re psi(1/4 + i r/2) - log(pi).

Mathematical content (full proofs in docs/ROUTE_001_TAIL_THEOREM.md):

  Lemma T1. Omega(r) = -euler_gamma - log(pi)
                        + sum_{n>=0} [ 1/(n+1) - (n+1/4) / ((n+1/4)^2 + r^2/4) ].
            Omega is even, increasing on [0, oo), and
            Omega(0) = psi(1/4) - log(pi) = -euler_gamma - pi/2 - 3 log 2 - log pi.

  Lemma T2. S = sum_{n>=2} Lambda(n)/sqrt(n) exp(-(log n)^2/4) satisfies
            S <= S_N + exp(1/4) exp(-v0^2/4) (2 + 2/v0),  v0 = log(N) - 1,
            where S_N is the sum over prime powers n <= N.

  Lemma T3. For t >= T >= 12, with q = exp(-16)/4 >= integral_{|x|>4} exp(-x^2) dx,

            A(t) >= (1/pi) [ Omega(T-4) (sqrt(pi) - q) + Omega(0) q ].

  Theorem.  For all t >= T,
            Q(t) >= (1/pi)[Omega(T-4)(sqrt(pi)-q) + Omega(0) q]
                    - (2/sqrt(pi)) S_upper - 4 exp(1/4 - T^2)  =:  M(T).

Every quantity below is enclosed with mpmath.iv (true outward-rounded interval
arithmetic). Trust base: mpmath.iv elementary functions and the lemma proofs in
the accompanying document. Evidence level: rigorous computation modulo
mpmath.iv correctness; corroboration, not human verification.
"""
from __future__ import annotations

import mpmath as mp
from mpmath import iv
from sympy import primerange

iv.dps = 30

T = 2000                 # tail threshold; T - 4 = 1996, c = (T-4)^2/4 exact integer
N_SERIES = 20000         # digamma-series terms for Omega(T-4)
N_PRIME = 20000          # prime-power cutoff for S

# ---- Euler-Mascheroni constant as a rigorous enclosure ----
try:
    EULER = +iv.euler
except AttributeError:
    # 30-digit enclosure, DLMF 5.2.3
    EULER = iv.mpf(["0.577215664901532860606512090082",
                    "0.577215664901532860606512090083"])

LOGPI = iv.log(iv.pi)

# ---- Lemma T1: Omega(T-4) by the digamma series with explicit tail ----
r = T - 4
c16 = 4 * r * r          # 16 * c where c = r^2/4;   (n+1/4)^2 + c = ((4n+1)^2 + 16c)/16
series = iv.mpf(0)
for n in range(N_SERIES):
    fn = 4 * n + 1
    series += iv.mpf(1) / (n + 1) - iv.mpf(4 * fn) / (fn * fn + c16)
# tail enclosure: sum_{n>=N} term_n  in  ( -3/(4(N-1)) , c/(2(N-3/4)^2) )
tail_lo = -iv.mpf(3) / (4 * (N_SERIES - 1))
tail_hi = (iv.mpf(r) * r / 4) / (2 * (iv.mpf(N_SERIES) - iv.mpf(3) / 4) ** 2)
series += iv.mpf([mp.mpf(tail_lo.a), mp.mpf(tail_hi.b)])
omega_far = -EULER - LOGPI + series
print(f"[omega] Omega({r}) in [{mp.nstr(mp.mpf(omega_far.a), 12)}, {mp.nstr(mp.mpf(omega_far.b), 12)}]  "
      f"(series N={N_SERIES} + explicit tail)")
assert mp.mpf(omega_far.a) > 0, "window bound requires Omega(T-4) > 0"

# Omega(0) = psi(1/4) - log(pi) = -euler - pi/2 - 3 log 2 - log pi  (exact, DLMF 5.4.13)
omega0 = -EULER - iv.pi / 2 - 3 * iv.log(2) - LOGPI
print(f"[omega] Omega(0) in [{mp.nstr(mp.mpf(omega0.a), 12)}, {mp.nstr(mp.mpf(omega0.b), 12)}]  (exact constants)")

# ---- Lemma T2: rigorous upper bound on S over prime powers ----
S = iv.mpf(0)
count = 0
for p in primerange(2, N_PRIME + 1):
    lp = iv.log(p)
    pk = p
    while pk <= N_PRIME:
        u = iv.log(pk)
        S += lp / iv.sqrt(pk) * iv.exp(-u * u / 4)
        count += 1
        pk *= p
v0 = iv.log(N_PRIME) - 1
S_tail = iv.exp(iv.mpf(1) / 4) * iv.exp(-v0 * v0 / 4) * (2 + 2 / v0)
S_upper = iv.mpf(mp.mpf((S + S_tail).b))
print(f"[prime] S <= {mp.nstr(mp.mpf(S_upper.b), 12)}  ({count} prime-power terms, "
      f"tail <= {mp.nstr(mp.mpf(S_tail.b), 3)})")

# ---- Lemma T3 pieces ----
q = iv.exp(iv.mpf(-16)) / 4                  # >= integral_{|x|>4} exp(-x^2) dx
pole = 4 * iv.exp(iv.mpf(1) / 4 - T * T)     # >= |pole(t)| for t >= T
print(f"[mass]  q <= {mp.nstr(mp.mpf(q.b), 3)}   [pole] <= {mp.nstr(mp.mpf(pole.b), 3)}")

# ---- Theorem: M(T) ----
arch_lower = (omega_far * (iv.sqrt(iv.pi) - q) + omega0 * q) / iv.pi
M = arch_lower - (2 / iv.sqrt(iv.pi)) * S_upper - pole
M_lo = mp.mpf(M.a)
print(f"[result] M({T}) >= {mp.nstr(M_lo, 9)}")
if M_lo <= 0:
    raise SystemExit(f"FAILED: certified lower bound M({T}) = {mp.nstr(M_lo, 9)} is not positive")
print(f"\nTHEOREM (certified): Q(t) >= {mp.nstr(M_lo, 6)} > 0 for every t >= {T}.")
print("scope=tail of Route 001 family only; modulo lemma proofs in docs/ROUTE_001_TAIL_THEOREM.md")
print("and mpmath.iv correctness; no bearing on Weil's universal class or RH")
