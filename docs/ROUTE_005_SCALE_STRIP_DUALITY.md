# Route 005 — Scale–strip duality: what crossing the wall would buy (candidate)

**Status:** Candidate theorem (Theorem D, elementary and effective) plus an
honestly-labeled open problem. Awaiting human review.

**Purpose.** Cycle 3 located the program's remaining difficulty at scales
\(a > a^*(H) \approx 3.35\). This document proves what certifying
positivity beyond the wall would purchase: an explicit *detection theorem*
converting scale-\(a\) positivity into zero localization. It upgrades
Route 005 from a one-way program (RH ⟹ positivity) into a two-way bridge
with a priced exchange rate, and states precisely which part is still
open.

## Theorem D (off-line zero detection at scale a)

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

**Proof.**

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
Adding the two totals gives \(B_a(\gamma_0)\). ∎

## The exchange rate

Contrapositive, solved for \(y_0\): full-line positivity at scale \(a\),
plus on-line knowledge in an \(O(1)\)-window, forces every off-line
candidate at height \(T\) into

\[
y_0 \;\lesssim\; \sqrt{\frac{\log\log T + C_a}{a}} .
\]

This is **non-vacuous** (i.e. beats the trivial \(y_0 < \tfrac12\))
exactly when \(a \gtrsim 4\log\log T\) — the same law as the cycle-3
ceiling \(a^*(H) \sim 4\log\log H\), now visible from both sides:

- **Buying positivity:** verified height \(H\) purchases scales up to
  \(4\log\log H\) (cycle 3).
- **Selling positivity:** scale \(a\) purchases zero-confinement up to
  height \(e^{e^{a/4}}\) (Theorem D).

The exchange rate is symmetric: **this family converts between scale and
double-exponential height at par.** Nothing is gained or lost by a round
trip — which is precisely why the current results, derived *from* verified
zeros, cannot output new zero information (no circularity), and why any
*unconditional* positivity proof at scale \(a > a^*(H)\) — one not
consuming zero verification — would immediately yield genuinely new
zero-confinement at heights beyond all current verification.

## What is genuinely open (the honest part)

1. **The wall itself.** Certifying \(Q_a \ge 0\) for some \(a > a^*(H)\)
   without consuming verified zeros requires bounding
   \(\sum_n \Lambda(n) n^{-1/2} e^{-(\log n)^2/4a}\cos(t\log n)\) with its
   oscillation retained. Such bounds are of exponential-sum type and are
   the classical hard currency of the field; this document does not
   attempt one.
2. **Full determining property.** "\(Q_a(t) \ge 0\) for *all* \(a, t\)
   implies RH" does not follow from Theorem D alone: the window
   hypothesis (nearby zeros on the line) fails precisely when off-line
   zeros cluster at nearby heights, and the natural induction on the
   lowest off-line zero controls only the window *below* it. Resolving
   the clustering case (e.g. by a maximal-\(y\) selection at a common
   height, which works, versus distinct nearby heights, which does not
   obviously) is an open, well-posed problem for a future cycle — and a
   good candidate for expert consultation, since a clean determining
   statement may exist in the literature on Weil-positivity test classes.
3. **Effectivity.** Theorem D's constants are explicit, but its
   *hypothesis* references unverified regions; its prospective use is as
   a payoff contract, not a present-day zero-free theorem.

## Route-003-lesson check

Theorem D is not an equivalence reformulation: it is a one-directional,
effective implication with explicit constants, and its point is to price
the program's frontier, not to re-index RH. The open determining-property
question is flagged as such and should not be re-proposed as a route
without a mechanism for the clustering case.

## Primary sources

As in `docs/ROUTE_005_NARROW_SCALE_THEOREMS.md`. The counting bound and
strip confinement are the same inputs I1–I3; no new external theorems are
consumed.
