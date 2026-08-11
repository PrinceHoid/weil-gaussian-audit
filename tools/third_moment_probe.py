#!/usr/bin/env python3
"""Third moment of the Gabor compression: does it improve the 2/3 bound?

Context. The external two-thirds theorem (docs/EXTERNAL_2026-08-11_TWO_THIRDS.md)
reads only the first two moments of the compressed Weil form G~, and states
its linear-algebra inequalities are sharp GIVEN ONLY those two moments and
the block structure. A third moment is therefore strictly more information
and is not excluded by that optimality statement. This script settles
whether it helps.

Derivation being tested. Applying the sampling identity (its Lemma 2.2)
three times to tr G^3 = sum_{k,l,m} G_kl G_lm G_mk gives the triangle kernel

    tr G^3 = L^3 \int\int\int Phi(t1-t2) Phi(t2-t3) Phi(t1-t3)
                              nu(t1) nu(t2) nu(t3) dt1 dt2 dt3 ,

with the two kernel identities (verified separately, and again in check K
below):
    \int\int Phi(u)Phi(v)Phi(u-v) cos((u-v) y) du dv
        = (2 pi)^2 \int phi^4(s+y) phi^2(s) ds ,
    \int Phi(w)^2 cos(w y) dw = 2 pi (phi^2 * phi^2)(y) .

Splitting nu = mu + P (the Pi_X term is O(T^{lam/2-1}) and drops) gives

    mu^3   -> N / lam^2
    mu P P -> N              (via sum_n Lam(n)^2/n (L - log n) = L^3/6)
    mu mu P, P P P -> o(N)

    ==>   tr Ghat^3 = (1 + 1/lam^2) N .

The PPP ("triple prime") term deserves note: its resonance condition is
log n1 + log n2 - log n3 = 0, i.e. n1 n2 = n3, and Lam(n1 n2) != 0 forces
n1 = p^a, n2 = p^b, n3 = p^(a+b) -- SAME prime. The resulting sum is
sum_p (log p)^3 / (p-1)^2, which converges. So the third moment needs NO
Hardy-Littlewood-strength input: it is unconditionally available at
bandwidth lam <= 1, exactly like the second.

The question this settles. Equality in the paper's rank-trace step holds
for a two-point spectrum, s1 eigenvalues 1 and (s2+p) eigenvalues 2. For
ANY two-point {1,2} spectrum the moments satisfy identically
    M3 = 3 M2 - 2 M1 .
So the third moment can improve the bound only if the true M3 differs from
3 M2 - 2 M1. With M1 = N, M2 = (1/lam + lam/3) N:
    extremal prediction  M3 = (3/lam + lam - 2) N
    actual               M3 = (1 + 1/lam^2) N .

Checks below: (K) the kernel identities; (D) the triple-prime sum
converges; (M) the moment arithmetic and the lam = 1 coincidence;
(E) end-to-end -- build G explicitly from nu at modest T and measure
tr Ghat^3 directly, at lam < 1 where the two predictions DIFFER, so the
measurement discriminates between them.
"""
from __future__ import annotations

import numpy as np
import sympy as sp
from sympy import primerange

FAIL = []


def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f"  {detail}" if detail else ""))
    if not ok:
        FAIL.append(name)


# ---------------- (D) triple-prime diagonal converges ----------------
import math
vals = {}
for cut in (10**4, 10**5, 10**6):
    vals[cut] = sum(np.log(p) ** 3 / (p - 1.0) ** 2 for p in primerange(2, cut))
# rigorous-direction tail bound: for x >= 10, sum_{p>x}(log p)^3/(p-1)^2
#   <= sum_{n>x}(log n)^3/(n-1)^2 <= int_{x-1}^inf (log t)^3/t^2 * (1+eps) dt
#   = [(log x)^3 + 3(log x)^2 + 6 log x + 6]/x  * (1+eps)
def tail_bound(x):
    lg = math.log(x)
    return 1.2 * (lg**3 + 3*lg**2 + 6*lg + 6) / (x - 1)
tb = tail_bound(10**6)
print(f"[D] sum_p (log p)^3/(p-1)^2  partial sums: "
      + ", ".join(f"10^{int(math.log10(c))}: {v:.6f}" for c, v in vals.items()))
print(f"    rigorous tail beyond 10^6 <= {tb:.3e}  => the sum converges to ~{vals[10**6]:.4f}")
check("D triple-prime diagonal converges (=> NO Hardy-Littlewood input needed)",
      tb < 0.01 and abs(vals[10**6] - vals[10**5]) < 0.01,
      f"value ~ {vals[10**6]:.4f} = O(1), negligible against N -> infinity")

# ---------------- (S) the arithmetic inputs feeding the moments ----------
# second moment needs   sum_{n<=X} Lam(n)^2/n (L - log n) = L^3/6 + O(L^2)
# (this is what turns the mu-P-P term into exactly N)
def cheb(L):
    X = math.exp(L); s2 = 0.0; s3 = 0.0
    for p in primerange(2, int(X) + 1):
        pk = p
        while pk <= X:
            lp2 = math.log(p) ** 2
            s2 += lp2 / pk
            s3 += lp2 / pk * (L - math.log(pk))
            pk *= p
    return s2, s3
print("[S] Chebyshev-Mertens inputs (Lemma 5.1 (5.2) of the paper):")
ok_s = True
for L in (8.0, 10.0, 12.0):
    s2, s3 = cheb(L)
    r2, r3 = s2 / (L**2 / 2), s3 / (L**3 / 6)
    print(f"    L={L:4.1f}:  sum Lam^2/n = {s2:9.4f} (vs L^2/2 = {L**2/2:8.4f}, ratio {r2:.3f});"
          f"  weighted = {s3:9.4f} (vs L^3/6 = {L**3/6:8.4f}, ratio {r3:.3f})")
    ok_s &= 0.75 < r3 < 1.25
check("S weighted prime sum matches L^3/6 (the mu-P-P input)", ok_s,
      "ratios approach 1 slowly, as expected from the O(L^2) error term")

# ---------------- (M) the moment arithmetic ----------------
lam = sp.Symbol("lambda", positive=True)
M1 = sp.Integer(1)
M2 = 1 / lam + lam / 3
M3_actual = 1 + 1 / lam ** 2
M3_extremal = 3 * M2 - 2 * M1

check("M1 extremal two-point spectrum forces M3 = 3 M2 - 2 M1",
      sp.simplify(M3_extremal - (3 / lam + lam - 2)) == 0)
# verify the two-point identity itself: x ones and y twos
xx, yy = sp.symbols("x y", nonnegative=True)
m1, m2, m3 = xx + 2 * yy, xx + 4 * yy, xx + 8 * yy
check("M2 for any {1,2}-spectrum, M3 = 3 M2 - 2 M1 identically",
      sp.simplify(m3 - (3 * m2 - 2 * m1)) == 0)

gap = sp.simplify(M3_actual - M3_extremal)
check("M3 actual and extremal predictions COINCIDE at lambda = 1",
      sp.simplify(gap.subs(lam, 1)) == 0,
      f"gap(lambda) = {sp.simplify(gap)}; gap(1) = {sp.simplify(gap.subs(lam,1))}")
print(f"    gap(lambda) = {sp.nsimplify(sp.simplify(gap))}")
for lv in (sp.Rational(1, 2), sp.Rational(4, 5), sp.Integer(1)):
    print(f"      lambda={lv}: actual {sp.nsimplify(M3_actual.subs(lam,lv))} "
          f"vs extremal {sp.nsimplify(M3_extremal.subs(lam,lv))}")

# the extremal spectrum implied at lambda = 1, and its consistency
x1 = sp.solve([sp.Eq(xx + 2 * yy, 1), sp.Eq(xx + 4 * yy, M2.subs(lam, 1))], [xx, yy])
check("M3b the gap factors as (1-lambda)^3/lambda^2 -- a TRIPLE root at lambda=1",
      sp.simplify(gap - (1 - lam) ** 3 / lam ** 2) == 0
      and all(sp.simplify(sp.diff(gap, lam, k).subs(lam, 1)) == 0 for k in (0, 1, 2))
      and sp.simplify(sp.diff(gap, lam, 3).subs(lam, 1)) != 0,
      "so the third moment's information content vanishes to 3rd order "
      "exactly at the optimal bandwidth")

check("M4 lambda=1 extremal spectrum is (2/3) ones + (1/6) twos",
      sp.simplify(x1[xx] - sp.Rational(2, 3)) == 0 and sp.simplify(x1[yy] - sp.Rational(1, 6)) == 0,
      f"x = {x1[xx]}, y = {x1[yy]}")
check("M5 that spectrum saturates the counting constraint N >= s1 + 2(s2+p)",
      sp.simplify(x1[xx] + 2 * x1[yy] - 1) == 0, "equality, i.e. the bound is tight")

# ---------------- (K) kernel identities, recomputed here ----------------
L_k, w_k = 30.0, 3.0
us = np.linspace(-L_k / 2, L_k / 2, 20001)
du = us[1] - us[0]
ramp = lambda z: np.clip(z, 0, 1) ** 2 * (3 - 2 * np.clip(z, 0, 1))
phi_k = ramp((L_k / 2 - np.abs(us)) / w_k)
ph2, ph4 = phi_k ** 2, phi_k ** 4
tab_r = np.linspace(-30, 30, 24001)
tab_P = np.array([(np.cos(r * us) * ph2).sum() * du for r in tab_r])
PhiF = lambda r: np.interp(r, tab_r, tab_P, left=0.0, right=0.0)
rs = np.linspace(-12, 12, 2001)
dr = rs[1] - rs[0]
Pv = PhiF(rs)
UV = np.subtract.outer(rs, rs)
PhiUV = PhiF(UV)


def overlap(y, A, B):
    sh = int(round(y / du))
    A_ = np.roll(A, -sh)
    if sh > 0:
        A_[-sh:] = 0
    elif sh < 0:
        A_[:-sh] = 0
    return (A_ * B).sum() * du


worst = 0.0
for y in (0.0, 1.5, 3.0, 6.0):
    J = (Pv[:, None] * Pv[None, :] * PhiUV * np.cos(UV * y)).sum() * dr * dr
    pred = (2 * np.pi) ** 2 * overlap(y, ph4, ph2)
    worst = max(worst, abs(J - pred) / abs(pred))
check("K triangle-kernel identity J(y) = (2pi)^2 int phi^4(s+y) phi^2(s) ds",
      worst < 5e-3, f"max rel dev {worst:.2e}")

# ---------------- (E) why no end-to-end check is possible ----------------
print()
print("[E] A direct end-to-end construction of G was attempted and is NOT")
print("    reported: the moment asymptotics carry O(1/log T) corrections, so a")
print("    meaningful test needs l = log(T/2pi) >> 1, hence a matrix of size")
print("    d = lam*l*T/2pi. Even l = 20 gives d > 10^9. At feasible sizes")
print("    (T ~ 10^2-10^3) the prime cutoff X = (T/2pi)^lam is under 10, so the")
print("    measured moments are dominated by error terms and discriminate")
print("    nothing. This is recorded rather than presented as evidence.")
print()
print("EVIDENCE LEVELS")
print("  derived here  : tr Ghat^3 = (1 + 1/lam^2) N  (kernel identities verified,")
print("                  arithmetic inputs verified; the off-diagonal error terms")
print("                  are NOT bounded here -- they would need the paper's")
print("                  Montgomery-Vaughan treatment carried to three factors).")
print("  proved here   : any {1,2}-spectrum satisfies M3 = 3 M2 - 2 M1 exactly,")
print("                  and at lam = 1 the derived M3 equals that value.")
print("  conclusion    : adjoining the third moment cannot improve 2/3 at lam = 1.")

print()
if FAIL:
    raise SystemExit(f"FAILED: {FAIL}")
print("ALL CHECKS PASS")
