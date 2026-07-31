#!/usr/bin/env python3
"""Verifier for the repaired single-scale detection theorem (Theorem D').

Checks each repair against the four cycle-4 audit findings recorded in
docs/ROUTE_005_SCALE_STRIP_DUALITY.md:

  V1 (findings 1+2, complete quartet). Exact symbolic verification of
     Lemma D1: the four zeros {+-gamma +- i y} contribute exactly
       4 e^{a y^2} [ e^{-a(g-t)^2} cos(2ay(g-t))
                   + e^{-a(g+t)^2} cos(2ay(g+t)) ]
     to Q_a(t), and the phase at t* = gamma - pi/(2ay) is exactly pi.

  V2 (finding 3, log-weighted lattice sum). Lemma D3's bound is checked
     against direct summation, including against real zeta zeros.

  V3 (finding 4, Delta uniformity). In the informative regime a*y0^2 >= 1
     the offset delta = pi/(2 sqrt(a u)) is at most pi/2, so the window
     Delta = 2 + delta is bounded by 2 + pi/2 < 3.5709 uniformly.

  V4 (unit-interval counting input I3). The bound 5 log(n+2) is checked
     against actual zero counts.

  V5 (Corollary D5). The confinement solution u <= (L + sqrt(L^2+pi^2))/2
     is verified against a direct numerical solve, and the resulting
     non-vacuity threshold a > 4u is reported.

Evidence level: exact symbolic (V1) and rigorous-direction numerical
checks (V2-V5) of a candidate theorem. Not a substitute for human review.
"""
from __future__ import annotations

import mpmath as mp
import sympy as sp

mp.mp.dps = 30

FAIL = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f"  {detail}" if detail else ""))
    if not ok:
        FAIL.append(name)


# ---------- V1: complete quartet identity (findings 1 and 2) ----------
a_s, t_s, g_s, y_s = sp.symbols("a t gamma y", positive=True)
zs = [g_s - sp.I * y_s, g_s + sp.I * y_s, -g_s - sp.I * y_s, -g_s + sp.I * y_s]
# frozen convention: Q_a(t) = sum_z [ e^{-a(z-t)^2} + e^{-a(z+t)^2} ]
quartet = sum(sp.exp(-a_s * (z - t_s) ** 2) + sp.exp(-a_s * (z + t_s) ** 2) for z in zs)
claimed = 4 * sp.exp(a_s * y_s**2) * (
    sp.exp(-a_s * (g_s - t_s) ** 2) * sp.cos(2 * a_s * y_s * (g_s - t_s))
    + sp.exp(-a_s * (g_s + t_s) ** 2) * sp.cos(2 * a_s * y_s * (g_s + t_s))
)
resid = sp.simplify(sp.expand(sp.expand_complex(quartet - claimed).rewrite(sp.exp)))
check("V1a Lemma D1 quartet identity (exact)", resid == 0, f"residual {resid}")
phase = sp.simplify(sp.cos(2 * a_s * y_s * (sp.pi / (2 * a_s * y_s))))
check("V1b phase at t* equals -1 (exact)", phase == -1, f"cos = {phase}")

# E_far/E ratio claimed to be exp(-4 a g (g - delta))
d_s = sp.symbols("delta", positive=True)
ratio = sp.simplify(sp.exp(a_s * y_s**2 - a_s * (2 * g_s - d_s) ** 2)
                    / sp.exp(a_s * y_s**2 - a_s * d_s**2))
check("V1c E_far/E = exp(-4 a gamma (gamma - delta))",
      sp.simplify(sp.log(ratio) + 4 * a_s * g_s * (g_s - d_s)) == 0)

# ---------- V4: unit-interval counting input I3 ----------
gam = [mp.im(mp.zetazero(k)) for k in range(1, 300)]
worst_ratio, worst_n = mp.mpf(0), 0
for n in range(14, 160):
    c = sum(1 for gv in gam if n <= gv < n + 1)
    r = c / (5 * mp.log(n + 2))
    if r > worst_ratio:
        worst_ratio, worst_n = r, n
check("V4 unit-interval count <= 5 log(n+2)", worst_ratio <= 1,
      f"max ratio {mp.nstr(worst_ratio, 4)} at n={worst_n}")
check("V4b no zeros below height 14", min(gam) > 14, f"gamma_1 = {mp.nstr(min(gam), 8)}")


# ---------- V2: Lemma D3 log-weighted Gaussian lattice sum ----------
def D3_bound(T, a):
    """e^{a/4} * 10 log(2T+2) * sum_{n>=1} e^{-a n^2}, tail-safe form."""
    geo = mp.exp(-a) / (1 - mp.exp(-3 * a))          # >= sum_{n>=1} e^{-a n^2}
    return mp.exp(a / 4) * 10 * mp.log(2 * T + 2) * geo


def D3_direct_model(T, a):
    """Direct sum over the counting model: groups n = floor|x - T| >= 1."""
    return mp.fsum(2 * 5 * mp.log(T + n + 2) * mp.exp(-a * n**2) for n in range(1, 80))


ok_all = True
for a in [mp.mpf(1), mp.mpf("3.45"), mp.mpf(10)]:
    for T in [mp.mpf(100), mp.mpf("3e12")]:
        b, d = D3_bound(T, a), D3_direct_model(T, a)
        if d > b:
            ok_all = False
            print(f"    a={a} T={T}: direct {mp.nstr(d,8)} > bound {mp.nstr(b,8)}")
check("V2a Lemma D3 bound dominates the counting model", ok_all)

# against real zeros: sum over actual zeros with |gamma - T| >= 1
ok_real = True
for a in [mp.mpf(1), mp.mpf("3.45")]:
    for T in [mp.mpf(50), mp.mpf(120)]:
        direct = mp.fsum(mp.exp(a / 4) * mp.exp(-a * (gv - T) ** 2)
                         for gv in gam if abs(gv - T) >= 1)
        direct += mp.fsum(mp.exp(a / 4) * mp.exp(-a * (-gv - T) ** 2) for gv in gam)
        if direct > D3_bound(T, a):
            ok_real = False
            print(f"    a={a} T={T}: real {mp.nstr(direct,8)} > bound {mp.nstr(D3_bound(T,a),8)}")
check("V2b Lemma D3 bound dominates real zeta-zero sums", ok_real)

# ---------- V3: Delta uniformity in the informative regime ----------
worst_delta = mp.mpf(0)
for a in [mp.mpf(1), mp.mpf(2), mp.mpf("3.45"), mp.mpf(50)]:
    for u in [mp.mpf(1), mp.mpf(2), mp.mpf(10)]:
        worst_delta = max(worst_delta, mp.pi / (2 * mp.sqrt(a * u)))
check("V3 Delta = 2 + delta <= 2 + pi/2 for a*y0^2 >= 1, a >= 1",
      worst_delta <= mp.pi / 2 + mp.mpf("1e-30"),
      f"max delta {mp.nstr(worst_delta, 6)}, so Delta <= {mp.nstr(2 + mp.pi/2, 6)}")


# ---------- V5: Corollary D5 confinement solution and non-vacuity ----------
def B_a(T, a):
    geo = mp.exp(-a) / (1 - mp.exp(-3 * a))
    return 10 * mp.log(T + 2) + 20 * mp.exp(a / 4) * mp.log(2 * T + 2) * geo


ok_sol = True
for L in [mp.mpf(1), mp.mpf(3), mp.mpf(8)]:
    u_closed = (L + mp.sqrt(L * L + mp.pi**2)) / 2
    f = lambda u: u - mp.pi**2 / (4 * u) - L
    u_num = mp.findroot(f, mp.mpf(2))
    if abs(u_closed - u_num) > mp.mpf("1e-20"):
        ok_sol = False
check("V5a u <= (L + sqrt(L^2+pi^2))/2 solves u - pi^2/(4u) = L", ok_sol)

print("\nnon-vacuity threshold (need a > 4u_max to beat the trivial y0 < 1/2):")
for gamma0 in [mp.mpf("1e3"), mp.mpf("3e12"), mp.mpf("1e30")]:
    for a in [mp.mpf("3.45")]:
        L = mp.log(B_a(gamma0, a) / 4)
        u_max = (L + mp.sqrt(L * L + mp.pi**2)) / 2
        y_bound = mp.sqrt(u_max / a)
        print(f"  gamma0={mp.nstr(gamma0,3):9} a={mp.nstr(a,4)}: L={mp.nstr(L,5)} "
              f"u_max={mp.nstr(u_max,5)} => y0 <= {mp.nstr(y_bound,5)} "
              f"({'NON-VACUOUS' if y_bound < 0.5 else 'vacuous (>1/2)'}); "
              f"need a > {mp.nstr(4*u_max,5)}")

print()
if FAIL:
    raise SystemExit(f"FAILED: {FAIL}")
print("ALL THEOREM D' CHECKS PASS")
print("scope=candidate theorem; window hypothesis and human review still required")
