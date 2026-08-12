# Route 005 — Scale–strip duality: proposed single-scale payoff

**Status:** The displayed single-scale detection estimate is **not certified**.
A cycle-4 adversarial audit found gaps in its quartet and infinite-tail bounds;
the original statement and derivation are retained below as a repair target.
The all-scale clustering problem is resolved separately at the candidate-proof
level in
[`ROUTE_005_DETERMINING_THEOREM.md`](ROUTE_005_DETERMINING_THEOREM.md).

> **Cycle-6 update (29 July 2026): the repair is complete.** All four audit
> findings below are addressed in
> [`ROUTE_005_THEOREM_D_REPAIRED.md`](ROUTE_005_THEOREM_D_REPAIRED.md) —
> complete-quartet extraction (findings 1–2), a log-weighted Gaussian
> lattice-sum lemma (finding 3), and restriction to the informative regime
> `a y₀² ≥ 1`, which bounds `Δ ≤ 2 + π/2 < 3.5709` uniformly (finding 4).
> Theorem D′ there carries explicit constants and is machine-checked by
> `tools/verify_theorem_d_repaired.py`. The `4 log log T` exchange law,
> described below as a heuristic target, is a proved consequence of the
> repaired theorem. **The statement of Proposed Theorem D on this page is
> still the superseded one and must not be cited.**

**Purpose.** Cycle 3 located the program's remaining difficulty at scales
\(a > a^*(H) \approx 3.35\). This document proposes an explicit
single-scale detection estimate converting scale-\(a\) positivity into zero
localization. Its qualitative scale-versus-height law remains a useful target,
but the constants and implication below must not be cited as a theorem until
the audit findings are repaired.

## Proposed Theorem D (not currently certified)

Let \(a \ge 1\). Suppose \(\rho_0 = \beta_0 + i\gamma_0\) is a zeta zero
with \(\gamma_0 \ge 10\) and \(y_0 := |\beta_0 - \tfrac12| > 0\), and
suppose every zero with height in the window
\((\gamma_0 - \Delta,\, \gamma_0 + \Delta)\), other than \(\rho_0\) and its
mirror partner \(1 - \bar\rho_0\), lies on the critical line, where
\(\Delta := 2 + \tfrac{\pi}{2ay_0}\). Then, at
\(t^* = \gamma_0 - \tfrac{\pi}{2ay_0}\),

\[
Q_a(t^*)\;\le\;-2\,e^{\,a y_0^2 - \frac{\pi^2}{4 a y_0^2}}\;+\;B_a(\gamma_0),
\qquad
B_a(\gamma_0) := 10\log(2\gamma_0 + 2\Delta + 2)\Big(2 + \sqrt{\tfrac\pi a}\Big)
\big(1 + e^{a/4} e^{-a}\big).
\]

In particular, if \(Q_a(t) \ge 0\) for all \(t\), then

\[
a y_0^2 - \frac{\pi^2}{4 a y_0^2} \;\le\; \log\!\big(B_a(\gamma_0)/2\big)
\;=\; \log\log \gamma_0 + O_a(1).
\]

**Original proof sketch (retained for audit; not a valid proof).**

*Spike.* The pair \(\rho_0,\, 1-\bar\rho_0\) contributes the \(\gamma\)-values
\(\gamma_0 \mp i y_0\). At \(t^*\), \(\gamma_0 - t^* = \tfrac{\pi}{2ay_0}\), so

\[
e^{-a(\gamma_0 - iy_0 - t^*)^2} + e^{-a(\gamma_0 + iy_0 - t^*)^2}
= 2\,e^{-a\left(\frac{\pi^2}{4a^2y_0^2} - y_0^2\right)}
  \cos\!\Big(2a\cdot\tfrac{\pi}{2ay_0}\cdot y_0\Big)
= -2\,e^{\,a y_0^2 - \frac{\pi^2}{4ay_0^2}} ,
\]

since the phase is exactly \(\pi\). (The \(e^{-a(\gamma + t^*)^2}\) mirror
terms of this pair are positive but bounded by \(e^{a/4}e^{-a(2\gamma_0-\ldots)^2}\),
absorbed into \(B_a\).)

*Everything else.* Every other zero contributes at most its absolute
value. Zeros **on the line** (which by hypothesis includes all zeros in
the window, and possibly others outside) contribute
\(h_{a,t^*}(\gamma) \le e^{-a(\gamma - t^*)^2} + e^{-a(\gamma + t^*)^2}\)
with \(\gamma\) real; summing over unit intervals of height with the
counting bound \(\le 5\log T\) per interval:

\[
\sum_{\text{on line}} h \;\le\; 2\cdot 5\log(2\gamma_0+2\Delta+2)
\sum_{k \ge 0} e^{-a\max(k-1,0)^2}
\;\le\; 10\log(2\gamma_0+2\Delta+2)\Big(2+\sqrt{\tfrac\pi a}\Big),
\]

using \(\sum_{k\ge0} e^{-a\max(k-1,0)^2} \le 2 + \int_0^\infty e^{-ax^2}dx\).
Zeros **off the line outside the window** have \(|{\rm Im}\,\gamma| < \tfrac12\)
and height distance \(\ge \Delta\) from \(\gamma_0\), hence distance
\(\ge \Delta - \tfrac{\pi}{2ay_0} = 2\) from \(t^*\); each contributes at
most \(e^{a/4}e^{-a(\text{dist})^2}\) and the same unit-interval counting
gives a total at most
\(10\log(2\gamma_0+2\Delta+2)(2+\sqrt{\pi/a})\,e^{a/4}e^{-a\cdot 1^2}\)
(shifting the count by one unit; \(e^{a/4}e^{-a} = e^{-3a/4} < 1\)).
Adding the two totals was claimed to give \(B_a(\gamma_0)\).

### Cycle-4 audit findings

The proof above does not establish the displayed estimate:

1. The omitted terms from the selected pair are not necessarily positive.
   With
   \(\delta=\pi/(2ay_0)\), the complete quartet contributes
   \[
   -4E-4E_{\rm far}\cos(4a\gamma_0y_0),\qquad
   E=e^{ay_0^2-a\delta^2},\quad
   E_{\rm far}=e^{ay_0^2-a(2\gamma_0-\delta)^2}.
   \]
   The second sign is arbitrary and must be bounded explicitly.
2. The conjugate zeros at height \(-\gamma_0\) were put into “everything
   else,” but one of their two Gaussian terms is centered at \(-t^*\) and is
   not covered by the asserted distance-\(2\) estimate. A repair must extract
   the complete quartet before bounding the remainder.
3. The unit-interval zero count grows with the interval height. It cannot be
   frozen at \(\log(2\gamma_0+2\Delta+2)\) over an infinite lattice sum
   without a separate lemma showing that Gaussian decay absorbs that growth.
4. Since \(\Delta=2+\pi/(2ay_0)\), the stated
   \(\log B_a=\log\log\gamma_0+O_a(1)\) does not follow uniformly in \(y_0\).
   A repaired theorem must retain the \(\Delta\)-dependence or impose and prove
   a quantitative restriction relating \(\Delta\) to \(\gamma_0\).

A corrected single-scale theorem may still be true with a complete-quartet
extraction and an explicit logarithmically weighted lattice-sum bound. No
counterexample was found, but that repair has not been completed here.

## Proposed exchange rate

If a corrected version of Proposed Theorem D supplies the required bounds, its
contrapositive would say that full-line positivity at scale \(a\), plus
on-line knowledge in an \(O(1)\)-window, forces an off-line candidate at height
\(T\) into a strip of the form

\[
y_0 \;\lesssim\; \sqrt{\frac{\log\log T + C_a}{a}} .
\]

This would be **non-vacuous** (i.e. beat the trivial \(y_0 < \tfrac12\))
exactly when \(a \gtrsim 4\log\log T\) — the same law as the cycle-3
ceiling \(a^*(H) \sim 4\log\log H\), now visible from both sides:

- **Buying positivity:** verified height \(H\) purchases scales up to
  \(4\log\log H\) (cycle 3).
- **Selling positivity (proposed):** scale \(a\) would purchase
  zero-confinement up to height \(e^{e^{a/4}}\), modulo a repaired
  single-scale theorem.

The matching \(4\log\log T\) scales are a motivated heuristic target, not a
certified exchange theorem in the present document. Current positivity results
derived from verified zeros cannot be sent around this proposed round trip to
produce new zero information.

## What remains open—and what cycle 4 resolves

1. **The wall itself.** Certifying \(Q_a \ge 0\) for some \(a > a^*(H)\)
   without consuming verified zeros requires bounding
   \(\sum_n \Lambda(n) n^{-1/2} e^{-(\log n)^2/4a}\cos(t\log n)\) with its
   oscillation retained. Such bounds are of exponential-sum type and are
   the classical hard currency of the field; this document does not
   attempt one.
2. **The single-scale payoff — RESOLVED in cycle 6.** The repair asked for
   here (complete-quartet extraction, a logarithmically weighted Gaussian
   lattice-sum bound, and control of \(\Delta=2+\pi/(2ay_0)\)) is carried
   out in
   [`ROUTE_005_THEOREM_D_REPAIRED.md`](ROUTE_005_THEOREM_D_REPAIRED.md).
   Theorem D′ is an effective conditional zero-confinement theorem with
   explicit constants. It remains vacuous at every scale this repository
   has certified: non-vacuity at height \(3\cdot10^{12}\) requires
   \(a > 19.68\) against a certified frontier of \(a = 3.45\).
3. **Full determining property (candidate resolution in cycle 4).**
   Theorem D alone still needs its window hypothesis, but the all-scale
   statement can bypass that hypothesis. The cycle-4 dominant-profile
   argument proves, at candidate level, that positivity at every real
   translation along any unbounded set of scales is equivalent to RH.
   Gaussian mollification in Weil's positive-distribution criterion proves
   the strong statement; independently, a generic translation makes one
   local off-line profile uniquely dominant, including in the
   distinct-height clustering case, and a tailored unbounded scale sequence
   makes its phase negative. See
   [`ROUTE_005_DETERMINING_THEOREM.md`](ROUTE_005_DETERMINING_THEOREM.md).
   Human review and a literature audit remain mandatory; no novelty claim
   is made.
4. **Effectivity.** Even after the proof is repaired, the hypothesis will
   reference unverified regions; its prospective use is as a payoff contract,
   not a present-day zero-free theorem.

## Route-003-lesson check

Proposed Theorem D is intended as a one-directional effective implication, not
an equivalence reformulation, but it remains unproved after the cycle-4 audit.
Cycle 4 separately resolves the determining-property question as an
equivalence and labels it accordingly; it does not count that reformulation as
a wall crossing or as evidence for RH.

## Primary sources

As in `docs/ROUTE_005_NARROW_SCALE_THEOREMS.md`. The counting bound and
strip confinement are the same inputs I1–I3; no new external theorems are
consumed.
