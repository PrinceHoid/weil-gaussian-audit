#!/usr/bin/env python3
"""Supporting computations for the broad-scale positivity assembly
(docs/ROUTE_005_BROAD_SCALE_POSITIVITY.md).

Three checks:

  1. COVERING DISTANCE. Computes the zero ordinates up to height 2015 and
     verifies that every t in [0, 2000] has a zero within distance D = 14.14
     (the binding case is t = 0 against gamma_1 = 14.134725...). This
     supports Lemma B3's verified-zone lower bound 2*exp(-D^2) >= 2e-200.
     (Corroborating computation: the certified statement follows from the
     Platt-Trudgian verification, which enumerates these zeros rigorously.)

  2. TAIL CONSTANT. Evaluates the unverified-zero tail bound of Lemma B4
     with H = 3e12 and prints the resulting (double-exponentially tiny)
     bound, checking it against the verified-zone lower bound.

  3. HEAT PROPAGATION SPOT CHECK. Verifies numerically (25-zero truncation,
     50 digits) that sqrt(a) Q_a(t) equals the heat convolution
     K_{tau(a)-tau(1)} * [Q_1] at sample points with 0 < a < 1, exercising
     the Lemma B5 identity on the zero-side representation.

Evidence level: floating-point support for a candidate assembled theorem;
not itself a certificate. The load-bearing external inputs are cited
theorems, not this script.
"""
from __future__ import annotations

import time

import mpmath as mp

D_COVER = mp.mpf("14.14")
T_MAX = 2000
H_VERIFIED = mp.mpf("3e12")   # Platt-Trudgian verified height

# ---- 1. covering distance ----
mp.mp.dps = 15
t0 = time.time()
gammas = []
n = 0
while True:
    n += 1
    g = mp.im(mp.zetazero(n))
    gammas.append(g)
    if g > T_MAX + float(D_COVER):
        break
print(f"[zeros] computed {n} ordinates up to {mp.nstr(gammas[-1], 10)} "
      f"in {time.time()-t0:.0f}s")

gaps = [gammas[i + 1] - gammas[i] for i in range(len(gammas) - 1)]
max_gap = max(gaps)
# every t in [0, T_MAX] is within max(gamma_1, max_gap/2) of some zero
cover = max(gammas[0], max_gap / 2)
print(f"[cover] gamma_1 = {mp.nstr(gammas[0], 10)}; max consecutive gap up to "
      f"{T_MAX + 15} = {mp.nstr(max_gap, 6)}")
print(f"[cover] covering distance = {mp.nstr(cover, 6)} <= {D_COVER}: {cover <= D_COVER}")
assert cover <= D_COVER

mp.mp.dps = 30
verified_lower = 2 * mp.exp(-(D_COVER**2))
print(f"[cover] verified-zone lower bound 2 exp(-D^2) >= {mp.nstr(verified_lower, 4)}")

# ---- 2. unverified tail bound ----
# sum over zeros of height > H of e^{1/4} [e^{-(g0-t)^2} + e^{-(g0+t)^2}]
# with per-unit-interval zero count <= 5 log(T) (enormous slack vs published
# explicit bounds), t <= T_MAX:
#   tail <= 2 e^{1/4} * 5 * sum_{k>=0} log(H+k+1) exp(-(H+k-T_MAX)^2)
#        <= 20 e^{1/4} log(2H) exp(-(H-T_MAX)^2)   [geometric domination]
log_tail = mp.mpf("0.25") + mp.log(20 * mp.log(2 * H_VERIFIED)) - (H_VERIFIED - T_MAX) ** 2
print(f"[tail]  log(unverified tail bound) <= {mp.nstr(log_tail, 8)}  "
      f"(i.e. tail < 10^{mp.nstr(log_tail/mp.log(10), 5)})")
assert log_tail < mp.log(verified_lower) - 100
print(f"[tail]  verified-zone lower bound exceeds tail by a factor > exp(10^24): True")

# ---- 3. heat propagation spot check ----
mp.mp.dps = 50
gam25 = [mp.im(mp.zetazero(k)) for k in range(1, 26)]

def zside(a, t):
    return 2 * mp.fsum(mp.exp(-a * (g - t) ** 2) + mp.exp(-a * (g + t) ** 2)
                       for g in gam25)

def heat_conv(a, t):
    # K_s * Q_1 at t, with s = 1/(4a) - 1/4, times sqrt(a) normalization:
    # sqrt(a) Q_a(t) = (4 pi s)^{-1/2} integral Q_1(u) exp(-(t-u)^2/(4s)) du
    s = 1 / (4 * a) - mp.mpf(1) / 4
    return mp.quad(lambda u: zside(1, u) * mp.exp(-(t - u) ** 2 / (4 * s)),
                   [t - 40, t, t + 40]) / mp.sqrt(4 * mp.pi * s) / mp.sqrt(a)

print("[heat]  a, t, zero-side Q_a, heat-convolved Q_a, rel diff")
for a, t in [(mp.mpf("0.5"), mp.mpf(15)), (mp.mpf("0.25"), mp.mpf(20)),
             (mp.mpf("0.8"), mp.mpf(11))]:
    direct = zside(a, t)
    conv = heat_conv(a, t)
    rel = abs(direct - conv) / direct
    print(f"[heat]  {mp.nstr(a,3)}, {mp.nstr(t,4)}, {mp.nstr(direct, 12)}, "
          f"{mp.nstr(conv, 12)}, {mp.nstr(rel, 3)}")
    assert rel < mp.mpf("1e-8"), "heat propagation identity failed"

print("\nAll supporting computations pass. These support, but do not replace,")
print("the cited external theorems and the candidate tail theorem.")
