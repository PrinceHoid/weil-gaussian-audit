#!/usr/bin/env python3
"""Executable interval certificate for the Route 005 narrow-scale theorems.

Certifies, in mpmath.iv interval arithmetic (mp precision kept above iv
precision per the 2026-07-28 audit), the prime-side bound

    Q_a(t) >= M_a(T_F) > 0   for every t >= T_F := 3*10^12 - 100,

for a in {2, 3}, where (docs/ROUTE_005_NARROW_SCALE_THEOREMS.md, Lemmas N1-N4):

  N1' (large-argument Omega lower bound, sharpened 28 Jul). With
     f(n) = 1/(n+1) - (n+1/4)/((n+1/4)^2+c), c = r^2/4, and M = c - 1:
       Omega(r) >= -gamma - log(pi) + sum_{n<N} f(n)
                   + log((M+1)/(N+1)) - (1/2) log(((M+1/4)^2+c)/((N+1/4)^2+c))
                   - 3/(4(M-1)) - (1/2) log(1 + c/(M-1)^2).
     f is decreasing on [N, M] for the full range x + 1/4 <= c: when
     (x+1/4)^2 <= c this is immediate; otherwise
     (a^2-c)(a+1)^2 - (a^2+c)^2 = 2a^3 + a^2 - 3ca^2 - 2ca - c - c^2 < 0
     for a := x+1/4 <= c. Extending the comparison from sqrt(c) to c
     recovers the ~log(2)/2 x 2 loss of the earlier version.

  N2 (scaled prime bound). S_a <= finite sum over prime powers n <= N_P
     plus tail e^{a/4} e^{-v0^2/(4a)} (2a + 2a^2/v0), v0 = log(N_P) - a,
     valid for log(N_P) >= max(2, 2a); |P_a(t)| <= (2/sqrt(pi a)) S_a.

  N3 (scaled window bound). With q_a = e^{-16a}/(4a) and Omega increasing:
     A_a(t) >= (1/pi) [ Omega(T-4) (sqrt(pi/a) - q_a) + Omega(0) q_a ].

  N4 (pole). |pole_a(t)| = 4 e^{a/4 - a t^2} <= 4 e^{a/4} / (a T^2) <= 1e-23
     for t >= T_F, via e^{-x} <= 1/x.

Also prints the verified-zone constants for the scale-window theorem
(Theorem N5): the covering/tail ratio in the region |t| <= T_F, which is
monotone in a and checked at its worst point.

Evidence level: rigorous computation modulo mpmath.iv and the lemma proofs
in the accompanying document; corroboration, not human verification.
"""
from __future__ import annotations

import math
import time

import mpmath as mp
from mpmath import iv
from sympy import primerange

iv.dps = 30
mp.mp.dps = 50   # endpoint materialization must exceed iv precision

H = 3 * 10**12            # Platt-Trudgian verified height
T_F = H - 100             # tail threshold
R = T_F - 4               # archimedean window edge argument
N_SERIES = 100_000        # digamma-series finite part
N_PRIME = 50_000          # prime-power cutoff
A_VALUES = (2, 3)         # must certify
A_CEILING = (3.2, 3.3, 3.35, 3.4)   # ceiling squeeze: certify as many as possible

try:
    EULER = +iv.euler
except AttributeError:
    EULER = iv.mpf(["0.577215664901532860606512090082",
                    "0.577215664901532860606512090083"])
LOGPI = iv.log(iv.pi)

# ---------- Lemma N1: Omega lower bound at r = R ----------
t0 = time.time()
c4 = R * R                       # 4c = r^2  (exact integer; c = r^2/4)
series = iv.mpf(0)
for n in range(N_SERIES):
    fn = 4 * n + 1
    series += iv.mpf(1) / (n + 1) - iv.mpf(4 * fn) / (fn * fn + 4 * c4)
M = c4 // 4 - 1                  # c - 1: full range of the monotonicity proof
intN = (iv.log(iv.mpf(M + 1)) - iv.log(iv.mpf(N_SERIES + 1))
        - (iv.log(iv.mpf((4 * M + 1) ** 2 + 4 * c4))
           - iv.log(iv.mpf((4 * N_SERIES + 1) ** 2 + 4 * c4))) / 2)
beyond = iv.mpf(3) / (4 * (M - 1)) + iv.log(1 + iv.mpf(c4) / (4 * (M - 1) ** 2)) / 2
omega_R = -EULER - LOGPI + series + intN - beyond
omega_R_lo = iv.mpf(mp.mpf(omega_R.a))
print(f"[N1] Omega({R}) >= {mp.nstr(mp.mpf(omega_R_lo.a), 12)}   "
      f"(series N={N_SERIES}, closed-form integral to M={M}; {time.time()-t0:.0f}s)")
assert mp.mpf(omega_R_lo.a) > 0

omega0 = -EULER - iv.pi / 2 - 3 * iv.log(2) - LOGPI     # Omega(0), exact constants

# ---------- Lemma N2: S_a with tail ----------
prime_terms = []
for p in primerange(2, N_PRIME + 1):
    lp = iv.log(p)
    pk = p
    while pk <= N_PRIME:
        prime_terms.append((iv.log(pk), lp / iv.sqrt(pk)))
        pk *= p
print(f"[N2] {len(prime_terms)} prime-power terms up to {N_PRIME}")

def S_upper(a: iv.mpf):
    assert mp.log(N_PRIME) >= max(2, 2 * mp.mpf(a.b)), "N2 monotonicity condition"
    s = iv.mpf(0)
    for u, w in prime_terms:
        s += w * iv.exp(-u * u / (4 * a))
    v0 = iv.log(iv.mpf(N_PRIME)) - a
    tail = iv.exp(a / 4) * iv.exp(-v0 * v0 / (4 * a)) * (2 * a + 2 * a * a / v0)
    return iv.mpf(mp.mpf((s + tail).b)), iv.mpf(mp.mpf(tail.b))

# ---------- Theorem N: assemble M_a(T_F) ----------
def certify(a_str: str):
    a = iv.mpf(a_str)
    S_ub, S_tail = S_upper(a)
    q_a = iv.exp(-16 * a) / (4 * a)
    pole = 4 * iv.exp(a / 4) / (a * iv.mpf(T_F) ** 2)              # e^{-x} <= 1/x
    arch_lo = (omega_R_lo * (iv.sqrt(iv.pi / a) - q_a) + omega0 * q_a) / iv.pi
    M_a = arch_lo - (2 / iv.sqrt(iv.pi * a)) * S_ub - pole
    M_lo = mp.mpf(M_a.a)
    print(f"[N ] a={a_str}: S_a <= {mp.nstr(mp.mpf(S_ub.b), 10)} (tail {mp.nstr(mp.mpf(S_tail.b), 3)}), "
          f"pole <= {mp.nstr(mp.mpf(pole.b), 3)}  =>  M_a(T_F) >= {mp.nstr(M_lo, 8)}")
    return M_lo

results = {}
for a in A_VALUES:
    M_lo = certify(str(a))
    results[str(a)] = M_lo
    if M_lo <= 0:
        raise SystemExit(f"FAILED: M_{a}(T_F) not certified positive")
best = str(A_VALUES[-1])
for a_str in A_CEILING:
    M_lo = certify(str(a_str))
    if M_lo > 0:
        results[str(a_str)] = M_lo
        best = str(a_str)
    else:
        print(f"[N ] a={a_str}: NOT certified (method ceiling reached)")
        break
print(f"[N ] best certified scale: a* = {best}")

# ---------- Theorem N5 constants: verified-zone covering vs tail ----------
# covering distance D = 50 for |t| in [1000, T_F] (explicit counting), 14.14 below;
# verified-zone lower bound 2 e^{-a D^2}; unverified tail <= 20 e^{a/4} log(2H) e^{-a(H-t)^2},
# (H - t) >= 100.  log-ratio = a(10^4 - D^2 - 1/4) - log(20 log 2H), increasing in a;
# worst case a = 1:
worst_log_ratio = (10**4 - 50**2 - mp.mpf("0.25")) - mp.log(20 * mp.log(2 * H))
print(f"[N5] verified/tail log-margin at worst case a=1: {mp.nstr(worst_log_ratio, 6)} > 0: "
      f"{worst_log_ratio > 0}")
assert worst_log_ratio > 0
# explicit-counting window at the worst point T = 1000 (Trudgian 2014 constants):
Tw = mp.mpf(1000)
count_lb = (100 / (2 * mp.pi)) * mp.log(Tw / (2 * mp.pi)) \
    - 2 * (mp.mpf("0.112") * mp.log(Tw) + mp.mpf("0.278") * mp.log(mp.log(Tw)) + mp.mpf("2.510"))
print(f"[N5] zeros guaranteed in any [T-50, T+50], T >= 1000: >= {mp.nstr(count_lb, 5)} "
      f"(needs >= 1: {count_lb >= 1})")
assert count_lb >= 1

print(f"\nTHEOREM (certified): Q_a(t) >= M_a(T_F) > 0 for all t >= {T_F}, at scales:")
for a, m in results.items():
    print(f"  a={a}:  Q_a(t) >= {mp.nstr(m, 6)}")
print("Combined with the verified-zone theorem (|t| <= T_F) this gives full-line")
print(f"positivity at each certified scale, and by heat propagation for every 0 < a <= {best}.")
print("scope=modulo lemma proofs in docs/ROUTE_005_NARROW_SCALE_THEOREMS.md, mpmath.iv,")
print(f"and cited external theorems; not a statement about a > {best} or about RH")
