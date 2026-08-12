# Route proposals — 27 July 2026

**Purpose.** The repository asked collaborators either to audit existing
routes or to propose new ones through the seven-question template in
`NEXT_STEPS.md`. Routes 001–003 are audited, and Route 004 is assigned to the active spectral-convergence program in PR #6. This document records Route 005's completed first falsification cycle, proposes Routes 006–008, and records the avenues that were surveyed and deliberately *not* proposed, so later collaborators do not repeat the survey.

**Selection principle.** Per the Route 003 lesson, no route below is "yet
another countable/dense/computable equivalence of RH." Each proposed route
satisfies at least one of:

1. incremental **unconditional** theorems are possible (progress that is
   publishable even if RH stays open);
2. it attacks in the **disproof** direction with cheap falsification;
3. it is the unique honest continuation of the repository's existing work.

**Honesty clause.** No route below is expected to prove RH. The rational
objective of this repository is: new intermediate theorems, eliminated
routes, hardened computational results, and engagement with the expert
community. Anyone claiming a full proof must pass the breakthrough
protocol in `NEXT_STEPS.md`.

---

## Route 005 — All-scale Gaussian family Q_a(t) (continuation of 001/002)

1. **Exact target and result.** Starting from the frozen Route 001 Fourier
   convention, derive the exact prime-side functional for
   `h_{a,t}(r) = exp(-a(r-t)^2) + exp(-a(r+t)^2)` and test whether a
   scale law propagates known positivity from `a=1` to `a>1`. The exact
   result is
   `4a^2 partial_a Q_a + partial_t^2 Q_a + 2a Q_a = 0`.
2. **Connection to RH.** These are valid additive explicit-formula tests,
   and under RH their exact zero side is a sum of nonnegative Gaussians.
   Therefore a rigorously certified negative `Q_a(t)` would disprove RH.
   Failure of a proposed monotonicity only rejects that bridge. Even
   positivity for every `(a,t)` would not prove RH because this family is
   smaller than Weil's universal test class.
3. **Closest prior art.** Bombieri's Clay exposition for Weil's criterion;
   Route 001 for the `a=1` normalization; heat-flow positivity methods in
   the de Bruijn–Newman literature; and Connes–Consani for semilocal Weil
   positivity. The elementary heat identity is not claimed as literature
   novelty.
4. **First unproved step now.** Find a genuinely zeta-specific invariant or
   inequality that controls the required backward heat flow. Ordinary heat
   positivity supplies control only in the opposite direction.
5. **Early falsification result.** The preregistered
   `a in {2,4}`, `t in {0,11,14.1347,17.58}` conditional zero-side probe
   found no negative forecast and rejected naive pointwise monotonicity at
   six of eight points. These are diagnostics, not certified prime-side
   signs.
6. **Assumptions and evidence.** The Fourier transform, scaled explicit
   formula, PDE, and heat-flow direction are exact derivations under the
   repository convention and were independently reconstructed by a second AI;
   expert review is still required. The Gaussian's pole moments are generally
   nonzero, so a separate subtraction or admissibility bridge is required for
   the pole-neutral convolution-square version of Weil positivity. The eight
   numerical values conditionally insert three critical-line zero ordinates;
   they are finite evidence only.
7. **Status.** Explored. Do not run a larger grid without a new backward-heat
   invariant. Full record:
   [`ROUTE_005_ALL_SCALE_FALSIFICATION.md`](ROUTE_005_ALL_SCALE_FALSIFICATION.md).

## Route 006 — de Bruijn–Newman constant: shrink the interval around Λ = 0

1. **Claim.** Improve the unconditional upper bound on the de
   Bruijn–Newman constant Λ (currently Λ ≤ 0.20 unconditionally by Platt–Trudgian, building on
   Polymath15), or make any
   rigorous quantitative improvement to the heat-flow/barrier machinery.
2. **Connection to RH.** RH is equivalent to Λ ≤ 0; Rodgers–Tao proved
   Λ ≥ 0 unconditionally, so RH ⟺ Λ = 0. Every reduction of the upper
   bound is an unconditional theorem strictly between "nothing" and RH —
   a clear scalar benchmark where every verified strict improvement is an
   unconditional quantitative theorem.
3. **Prior art.** de Bruijn 1950 (Λ ≤ 1/2); Ki–Kim–Lee 2009 (Λ < 1/2);
   Rodgers–Tao 2018 (Λ ≥ 0); Polymath15 2019 (Λ ≤ 0.22; effective
   heat-flow approximations, barrier computations, published methodology
   and open-source code); and Platt–Trudgian 2021 (the zero verification
   that makes Λ ≤ 0.20 unconditional).
4. **Novel step.** First independently reproduce the published Λ ≤ 0.20 result and its
   certificate-to-theorem interfaces. Only then seek a smaller explicit
   bound using modern rigorous numerics or sharper analytical lemmas.
5. **Failure test.** Reproduce the published Λ ≤ 0.20 pipeline first. If
   the barrier computation cannot be reproduced or the cost model shows
   the next improvement needs infeasible compute, record that and stop.
6. **Dependencies.** Polymath15's published papers and code; Arb/FLINT;
   the Platt–Trudgian verification height as an external theorem.
7. **Status.** Proposed. This is the best fit in this document for the
   repository's demonstrated strength (rigorous certified computation).

## Route 007 — Quantitative Nyman–Beurling / Báez-Duarte analysis

1. **Claim.** Study the Báez-Duarte distances `d_N` (distance in the
   Nyman–Beurling criterion restricted to integer dilations) with the goal
   of new *unconditional* results about their structure — e.g. improved
   explicit lower bounds, or rigorous computations of `d_N` for ranges of
   `N` with certified error.
2. **Connection to RH.** Báez-Duarte 2003: RH ⟺ `d_N → 0`. The
   conjectured rate is `d_N^2 ~ C / log N` with
   `C = sum_rho 1/|rho|^2 = 2 + gamma - log(4 pi)` (on RH with simple
   zeros). Proving `d_N → 0` is RH again (Route 003 lesson applies!), so
   the route's deliverables are restricted to: unconditional lower-bound
   theorems (cf. Burnol), certified numerics, and structural results about
   the optimizing coefficients.
3. **Prior art.** Nyman 1950, Beurling 1955, Báez-Duarte 2003, Burnol's
   lower bounds, and the computational literature on `d_N`.
4. **Novel step.** A certified (interval-arithmetic) computation of `d_N`
   beyond current published ranges, or any new unconditional inequality
   for the natural approximations.
5. **Failure test.** The Gram-matrix computation for `d_N` is notoriously
   ill-conditioned; if certified linear algebra cannot reach interesting
   `N`, record the conditioning obstruction quantitatively and stop.
6. **Dependencies.** Arb certified linear algebra; primary sources above.
7. **Status.** Proposed. Explicitly NOT another equivalence-restatement:
   the only claimed deliverables are unconditional.

## Route 008 — Disproof direction: Robin/Lagarias counterexample search

1. **Claim.** Systematically search for a counterexample to Robin's
   inequality `sigma(n) < e^gamma n log log n` (`n > 5040`), equivalent to
   RH, over the only viable candidates (colossally abundant and similar
   highly-composite-type integers), with certified arithmetic.
2. **Connection to RH.** A single verified counterexample disproves RH —
   outcome (2) of the repository mission. No counterexample proves
   nothing (the search space is infinite), but the structured candidate
   set makes each sweep cheap.
3. **Prior art.** Robin 1984; Lagarias 2002 (`sigma(n) <= H_n + e^{H_n}
   log H_n` ⟺ RH); existing computational searches which found no
   counterexample and established large lower bounds on any violator.
   Check current records before running anything.
4. **Novel step.** None mathematically; the value is a cheap, certified,
   reproducible falsification harness consistent with this repository's
   standards, extending the checked range of CA-number candidates.
5. **Failure test.** Trivial: the search either finds a counterexample
   (extraordinary claim → breakthrough protocol) or extends a bound.
6. **Dependencies.** Exact integer arithmetic (no floats near the
   boundary); enumeration of colossally abundant numbers.
7. **Status.** Proposed, low priority — a bounded but nontrivial rigorous-numerics project requiring exact integer
   arithmetic, real ball enclosures for transcendental comparisons, and a
   complete candidate enumeration; its realistic value is negative evidence.

---

## Avenues surveyed and not proposed

- **Localized Weil spectral convergence:** tracked as active Route 004 in
  PR #6. Its precise proxy-comparison and continuum ground-state targets must
  not be conflated with generic Hilbert–Pólya heuristics.
- **Generic Hilbert–Pólya heuristics** (Berry–Keating `xp`,
  Bender–Brody–Müller, etc.): no bounded operator-and-convergence target is
  proposed here.
- **Broader Connes / F_1 / arithmetic-site program:** relevant background for
  Route 004, but not proposed as a second independent route.
- **de Branges spaces:** the published counterexamples to earlier
  positivity conditions (Conrey–Li) make unguided work here likely to
  repeat known failures.
- **Random matrix / GUE statistics:** produces evidence and conjectures,
  not proofs; already influenced Route 001's design implicitly.
- **Zero-density / critical-line percentage improvements** (Levinson,
  Conrey ≥ 40%, later ~41.7%): real unconditional progress, but the
  techniques (mollifier optimization) are a specialist industry with an
  enormous engineering cost per 0.1%; dominated by Route 006 for this
  team.
- **Extending brute-force zero verification** beyond 3·10^12
  (Platt–Trudgian): not proposed as progress toward proof (Route 003's
  finite-to-infinite barrier), though Route 006 consumes such results as
  input.
- **Another equivalence reformulation** (countable families, discretized
  criteria, moment reformulations): rejected on the Route 003 lesson
  unless a propagation mechanism comes with it.

## What "exhausting reasonable effort" means for this repository

1. **Halt fixed-scale Route 001 at `t=1737`.** Preserve its candidate
   analytic tail for correction and possible publication, but do not extend
   the finite sweep; Route 002 already blocks the proposed universal bridge.
2. **Treat Route 005 cycle one as complete.** The exact heat direction and
   failed monotonicity test rule out a larger grid unless a new backward-heat
   invariant is first proved.
3. **Audit, then invest sustained effort in Route 006**, the proposed venue
   where a strict bound improvement would be an unconditional quantitative
   theorem even if RH remains open.
4. **Engage humans.** Post the hardened Route 001/002 material where
   analytic number theorists will see it; AI agreement is not
   verification (repository rule), and expert contact is itself a
   required step of reasonable effort.
5. **Accept the honest endpoint.** If proposed Routes 005–008 end in recorded
   obstructions, the repository has done what a rational actor can do:
   converted an unbounded ambition into a set of proved lemmas, eliminated
   bridges, and reproducible artifacts.

## Primary references

- Polymath15, *Effective approximation of heat flow evolution of the
  Riemann ξ function, and a new upper bound for the de Bruijn–Newman
  constant*: https://arxiv.org/abs/1904.12438
- B. Rodgers, T. Tao, *The de Bruijn–Newman constant is non-negative*,
  Forum of Mathematics, Pi (2020):
  https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/de-bruijnnewman-constant-is-nonnegative/D4B85BA067E2D5A71D87E4FFB0D21E46
- D. Platt, T. Trudgian, *The Riemann hypothesis is true up to 3·10^12*,
  Bull. LMS (2021): https://arxiv.org/abs/2004.09765
- L. Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for
  the Riemann hypothesis* (2003).
- G. Robin, *Grandes valeurs de la fonction somme des diviseurs et
  hypothèse de Riemann* (1984); J. Lagarias, *An elementary problem
  equivalent to the Riemann hypothesis* (2002):
  https://arxiv.org/abs/math/0008177
- Polymath15 computational repository:
  https://github.com/km-git-acc/dbn_upper_bound
