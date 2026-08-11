#!/usr/bin/env python3
"""Independent audit of the load-bearing steps of the "two thirds" paper.

Paper: "More than two thirds of the zeros of the Riemann zeta function lie
on the critical line" (CLAUDE, 10 Aug 2026). Claims, unconditionally,
liminf N*_0(T,2T)/N(T,2T) >= 2/3 (Thm A), the same for simple on-line
zeros (Thm B), and >= 5/6 distinct (Thm C).

Per AGENTS.md ("do not treat agreement among AI systems as mathematical
verification"; "require independent adversarial review of any claimed
breakthrough"), this script re-derives the steps that are checkable
mechanically. It does NOT verify the analytic prime-side asymptotics
(Montgomery's second moment, Theorem 5.8), which rest on cited literature
[Mon73, BGSTB24, GS25/26]; those are flagged as unaudited inputs.

Checks:
  A1  Lemma 3.1  inertia under pull-back (random stress test).
  A2  signature of an off-line pair block is exactly (1,1)  [symbolic]
      -- this is the step that REPLACES the Riemann hypothesis.
  A3  the pair contribution 2 m Re(x conj(y)) is the correct grouping of
      the two summands of a conjugate pair  [symbolic]
  A4  Lemma 3.2  rank-trace inequality (random stress test + equality case).
  A5  Lemma 3.2 => Prop 4.4(i)  3 s1 + 4 s2 + 4 p >= 4 tr - ||.||_F^2
      and the descent to (ii), (iii)  [symbolic in the counting variables]
  A6  Lemma 3.3  thresholded Cauchy-Schwarz (random stress test).
  A7  Lemma 2.2  Gabor/Poisson sampling identity sum_k phihat(tau-tau_k)^2
      = a L^2, which is what makes tr P <= N_on  (numerical).
  A8  the constants: H(1)=2/3, H_d(1)=5/6, F(1)=3/4, crossover at
      3-sqrt(6), H increasing on (0,1] (so lambda=1 is optimal), and the
      final assembly 4 - 2 - (1/lam + lam/3) = H(lam).
  A9  Montgomery-Taylor optimum quoted in Theorem D (0.6725, 0.83625).
"""
from __future__ import annotations

import numpy as np
import sympy as sp

rng = np.random.default_rng(20260811)
FAIL = []


def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f"  {detail}" if detail else ""))
    if not ok:
        FAIL.append(name)


def n_plus(M, tol=1e-9):
    return int((np.linalg.eigvalsh((M + M.conj().T) / 2) > tol).sum())


# ---------- A1: inertia under pull-back ----------
ok = True
for _ in range(300):
    m, u = rng.integers(2, 7), rng.integers(1, 7)
    Qm = rng.normal(size=(m, m)) + 1j * rng.normal(size=(m, m))
    Qm = (Qm + Qm.conj().T) / 2
    A = rng.normal(size=(m, u)) + 1j * rng.normal(size=(m, u))
    if rng.random() < 0.4:                      # force rank deficiency
        A[:, -1] = A[:, 0]
    if n_plus(A.conj().T @ Qm @ A) > n_plus(Qm):
        ok = False
check("A1 Lemma 3.1 inertia under pull-back (incl. degenerate A)", ok)

# ---------- A2/A3: the off-line pair block ----------
# NOTE: decompose into real/imaginary parts -- sympy will not evaluate re()
# on unevaluated complex symbols, which makes the naive test vacuously fail.
xr, xi, yr, yi = sp.symbols("xr xi yr yi", real=True)
x, y = xr + sp.I * xi, yr + sp.I * yi
mr = sp.Symbol("m", positive=True)
# a conjugate pair {rho, 1-conj(rho)} has gamma-values g and conj(g);
# its two summands in c* A c are m*l_g(c)*conj(l_g(c)) with the roles swapped
pair_sum = mr * (x * sp.conjugate(y) + y * sp.conjugate(x))
check("A3 pair contribution = 2 m Re(x conj(y))",
      sp.simplify(sp.expand(pair_sum - 2 * mr * sp.re(x * sp.conjugate(y)))) == 0)
B = sp.Matrix([[0, mr], [mr, 0]])
vv = sp.Matrix([x, y])
check("A3b that pair form has matrix [[0,m],[m,0]] exactly",
      sp.simplify(sp.expand((vv.H * B * vv)[0, 0] - pair_sum)) == 0)
evs = list(B.eigenvals().keys())
check("A2 off-line pair block has signature (1,1)  [REPLACES RH]",
      sorted(sp.simplify(e) for e in evs) == sorted([-mr, mr]),
      f"eigenvalues {evs}")
# deep pairs: signature does not degrade with |beta-1/2|
check("A2b signature is independent of the pair's depth off the line",
      all(sorted(sp.Matrix([[0, k], [k, 0]]).eigenvals().keys()) == sorted([-k, k])
          for k in (sp.Integer(1), sp.Integer(7), sp.Rational(1, 1000))))

# ---------- A4: rank-trace inequality ----------
ok, tight = True, 1e9
for _ in range(4000):
    d = int(rng.integers(2, 9))
    r = int(rng.integers(0, d + 1))
    U = np.linalg.qr(rng.normal(size=(d, d)))[0]
    pe = np.zeros(d)
    if r:
        pe[:r] = np.abs(rng.normal(size=r)) * rng.uniform(0.1, 3)
    P = U @ np.diag(pe) @ U.T
    V = np.linalg.qr(rng.normal(size=(d, d)))[0]
    qe = rng.normal(size=d) * rng.uniform(0.1, 3)
    Q = V @ np.diag(qe) @ V.T
    b = int((qe > 0).sum())
    lhs = np.linalg.norm(P + Q, "fro") ** 2
    for c in (0.5, 1.0, 2.0, 3.0):
        rhs = c * np.trace(P) - c * c / 4 * r + 2 * c * np.trace(Q) - c * c * b
        if lhs < rhs - 1e-8:
            ok = False
        if c == 2.0:
            tight = min(tight, lhs - rhs)
check("A4 Lemma 3.2 rank-trace inequality (4000 random cases, c in {.5,1,2,3})",
      ok, f"min slack at c=2: {tight:.3e}")
# equality case from the lemma statement: P = (c/2) Pi1, Q = c Pi2, orthogonal
c = 2.0
d, r, b = 9, 3, 4
P = np.zeros((d, d)); Q = np.zeros((d, d))
for i in range(r):
    P[i, i] = c / 2
for i in range(r, r + b):
    Q[i, i] = c
lhs = np.linalg.norm(P + Q, "fro") ** 2
rhs = c * np.trace(P) - c * c / 4 * r + 2 * c * np.trace(Q) - c * c * b
check("A4b equality case is attained", abs(lhs - rhs) < 1e-12, f"|lhs-rhs| = {abs(lhs-rhs):.2e}")

# ---------- A5: the counting descent ----------
s1, s2, p, N, tr, fro = sp.symbols("s1 s2 p N tr fro", nonnegative=True)
# Lemma 3.2 with c=2, r=s1, b=s2+p, trP1 <= s1:
#   fro >= 2 trP1 - s1 + 4(tr - trP1) - 4(s2+p) >= 4 tr - 3 s1 - 4 s2 - 4 p
prop_i = sp.simplify((3 * s1 + 4 * s2 + 4 * p) - (4 * tr - fro))   # >= 0 claimed
# (ii): using 4 s2 + 4 p <= 2N - 2 s1  (from N >= s1 + 2 s2 + 2 p)
sub_ii = prop_i.subs(4 * s2 + 4 * p, 2 * N - 2 * s1)
check("A5a Prop 4.4(ii) descent  s1 >= 4tr - 2N - fro",
      sp.simplify(sp.expand(sub_ii) - sp.expand((s1 + 2 * N) - (4 * tr - fro))) == 0)
# (iii): 3s1+4s2+4p = 2(s1+s2+p) + (s1+2s2+2p) <= 2(s1+s2+p) + N
check("A5b Prop 4.4(iii) regrouping identity",
      sp.simplify((3 * s1 + 4 * s2 + 4 * p) - (2 * (s1 + s2 + p) + (s1 + 2 * s2 + 2 * p))) == 0)

# ---------- A6: thresholded Cauchy-Schwarz ----------
ok = True
for _ in range(2000):
    d = int(rng.integers(2, 10))
    U = np.linalg.qr(rng.normal(size=(d, d)))[0]
    ev = rng.normal(size=d) * 2
    R = U @ np.diag(ev) @ U.T
    th = float(abs(rng.normal()) * 0.3)
    if np.trace(R) > th * d:
        lhs = int((ev > th).sum())
        rhs = (np.trace(R) - th * d) ** 2 / np.trace(R @ R)
        if lhs < rhs - 1e-9:
            ok = False
check("A6 Lemma 3.3 thresholded Cauchy-Schwarz (2000 cases)", ok)

# ---------- A7: Gabor/Poisson sampling identity ----------
# phi = smooth taper on [-L/2, L/2]; sum_k phihat(tau - tau_k)^2 = a L^2,
# a = (1/L) int phi^2, tau_k = T + k h, h = 2 pi / L.
L, w = 40.0, 4.0
us = np.linspace(-L / 2, L / 2, 200001)
du = us[1] - us[0]


def ramp(z):
    z = np.clip(z, 0, 1)
    return z * z * (3 - 2 * z)          # C^1 nondecreasing 0->1


phi = ramp((L / 2 - np.abs(us)) / w)
a_const = np.trapezoid(phi ** 2, us) / L


def phihat(r):
    return np.trapezoid(phi * np.cos(r * us), us)   # phi even -> real


h = 2 * np.pi / L
worst = 0.0
for tau in (0.0, 0.017, 0.31, 1.4):
    tot = sum(phihat(tau - k * h) ** 2 for k in range(-260, 261))
    worst = max(worst, abs(tot - a_const * L * L) / (a_const * L * L))
check("A7 Lemma 2.2 sampling identity sum_k phihat^2 = a L^2 (no aliasing)",
      worst < 2e-6, f"max rel. dev {worst:.2e}, a = {a_const:.6f}")

# ---------- A8: the constants and the assembly ----------
lam = sp.Symbol("lambda", positive=True)
H = 2 - 1 / lam - lam / 3
Hd = (1 + H) / 2
F = lam / (1 + lam ** 2 / 3)
check("A8a H(1) = 2/3", sp.simplify(H.subs(lam, 1) - sp.Rational(2, 3)) == 0)
check("A8b H_d(1) = 5/6", sp.simplify(Hd.subs(lam, 1) - sp.Rational(5, 6)) == 0)
check("A8c F(1) = 3/4", sp.simplify(F.subs(lam, 1) - sp.Rational(3, 4)) == 0)
cross = sp.solve(sp.Eq(H, 0), lam)
check("A8d crossover H_d >= F <=> lambda >= 3 - sqrt(6)",
      any(sp.simplify(c - (3 - sp.sqrt(6))) == 0 for c in cross),
      f"roots {[sp.nsimplify(c) for c in cross]}")
# H increasing on (0,1]: H' = 1/lam^2 - 1/3 > 0 for lam < sqrt(3)
Hp = sp.diff(H, lam)
check("A8e H is increasing on (0,1], so lambda = 1 is optimal",
      sp.simplify(Hp - (1 / lam ** 2 - sp.Rational(1, 3))) == 0
      and sp.simplify(Hp.subs(lam, 1)) > 0,
      f"H'(1) = {sp.simplify(Hp.subs(lam,1))}, critical point at lambda = sqrt(3) > 1")
# final assembly: 4*tr - 2N - ||.||^2 with tr -> N, ||.||^2 -> (1/lam + lam/3) N
assembled = 4 - 2 - (1 / lam + lam / 3)
check("A8f assembly 4 - 2 - (1/lam + lam/3) = H(lam)", sp.simplify(assembled - H) == 0)
check("A8g at lambda=1 the assembly gives exactly 2/3",
      sp.simplify(assembled.subs(lam, 1) - sp.Rational(2, 3)) == 0)

# ---------- A9: Montgomery-Taylor optimum quoted in Theorem D ----------
# MT kernel: sup over normalised f of the same functional; the paper quotes
# 0.6725 for simple/on-line and 0.83625 = (1+0.6725)/2 for distinct.
mt = 0.6725
check("A9 Theorem D distinct constant = (1 + 0.6725)/2", abs((1 + mt) / 2 - 0.83625) < 5e-6,
      f"(1+{mt})/2 = {(1+mt)/2}")

print()
print("UNAUDITED INPUTS (cited literature, not checked here):")
print("  - Montgomery's prime-side second moment and its unconditional form")
print("    [Mon73, BGSTB24, GS25/GS26]; Theorem 5.8's error terms.")
print("  - Weil's explicit formula normalisation (paper's Appendix A).")
print("  - Montgomery-Vaughan generalised Hilbert inequality [MV74].")
print("  - The claimed 0.68185 ceiling for bandwidth-one certificates.")
print()
if FAIL:
    raise SystemExit(f"FAILED: {FAIL}")
print("ALL MECHANICALLY CHECKABLE STEPS PASS")
