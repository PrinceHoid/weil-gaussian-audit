# Route proposals — 27 July 2026

**Purpose.** The repository asked collaborators either to audit existing
routes or to propose new ones through the seven-question template in
`NEXT_STEPS.md`. Routes 001–003 are audited. This document proposes four
new routes (004–007) and records the avenues that were surveyed and
deliberately *not* proposed, so later collaborators do not repeat the
survey.

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

## Route 004 — All-scale Gaussian family Q_a(t) (continuation of 001/002)

1. **Claim.** Derive, from one frozen explicit-formula convention, the
   prime-side functional `Q_a(t)` for
   `h_{a,t}(r) = exp(-a(r-t)^2) + exp(-a(r+t)^2)`, `a > 0`, and prove a
   rigorously stated scale-evolution inequality (a differential or
   monotonicity relation in `a` with explicit remainder signs).
2. **Connection to RH.** The Route 002 obstruction proves fixed-scale
   positive mixing cannot reach narrower Gaussians; varying `a` is the
   minimal enlargement that contains them. A proved positivity statement
   uniform in `(a, t)` would still not be RH (the Weil class is larger),
   but a scale-evolution *mechanism* would be a genuinely new structural
   tool, and its failure would kill the Gaussian program cleanly.
3. **Prior art.** Bombieri's Clay exposition for the criterion; Route 001
   handoff for the `a = 1` functional; Connes–Consani's work on Weil
   positivity (trace-formula positivity in the semilocal case) is the
   research frontier for positivity approaches and must be read before
   claiming novelty.
4. **Novel step.** The scale-evolution inequality itself. Nothing in
   Routes 001–003 supplies any inequality linking different `a`.
5. **Failure test.** Before any large computation: derive `Q_a(t)`
   symbolically, then rigorously evaluate the predeclared set
   `a in {2, 4}`, `t in {0, 11, 14.1347, 17.58}` (per
   `NEXT_STEPS.md`). A negative value, or failure of the proposed
   monotonicity, ends the route (that outcome is progress).
6. **Dependencies.** The admissibility/convention memorandum
   (`NEXT_STEPS.md` step 1) is a hard prerequisite; informal rescaling of
   the `a = 1` formula is forbidden because prime weights, Fourier
   factors, pole and archimedean terms all change with `a`.
7. **Status.** Proposed. Blocked on the convention memorandum.

## Route 005 — de Bruijn–Newman constant: shrink the interval around Λ = 0

1. **Claim.** Improve the unconditional upper bound on the de
   Bruijn–Newman constant Λ (currently Λ ≤ 0.22 by Polymath15, with ≤ 0.2
   available conditionally on extended zero verification), or make any
   rigorous quantitative improvement to the heat-flow/barrier machinery.
2. **Connection to RH.** RH is equivalent to Λ ≤ 0; Rodgers–Tao proved
   Λ ≥ 0 unconditionally, so RH ⟺ Λ = 0. Every reduction of the upper
   bound is an unconditional theorem strictly between "nothing" and RH —
   the only known attack venue where partial progress is guaranteed to be
   publishable and quantifiable.
3. **Prior art.** de Bruijn 1950 (Λ ≤ 1/2); Ki–Kim–Lee 2009 (Λ < 1/2);
   Rodgers–Tao 2018 (Λ ≥ 0); Polymath15 2019 (Λ ≤ 0.22; effective
   heat-flow approximations, barrier computations, published methodology
   and open-source code in the `dbn_upper_bound` repository).
4. **Novel step.** Either (i) push the Polymath15 barrier computation
   further using modern rigorous numerics (Arb) and the post-2020 zero
   verification height 3·10^12 (Platt–Trudgian), which post-dates the
   Polymath15 computations; or (ii) a sharper effective bound in their
   analytical lemmas. Both are bounded, checkable tasks.
5. **Failure test.** Reproduce the published Λ ≤ 0.22 pipeline first. If
   the barrier computation cannot be reproduced or the cost model shows
   the next improvement needs infeasible compute, record that and stop.
6. **Dependencies.** Polymath15's published papers and code; Arb/FLINT;
   the Platt–Trudgian verification height as an external theorem.
7. **Status.** Proposed. This is the best fit in this document for the
   repository's demonstrated strength (rigorous certified computation).

## Route 006 — Quantitative Nyman–Beurling / Báez-Duarte analysis

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

## Route 007 — Disproof direction: Robin/Lagarias counterexample search

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
7. **Status.** Proposed, low priority — a weekend-scale project kept
   honest by exact arithmetic; its realistic value is pedagogical and
   negative-evidence.

---

## Avenues surveyed and not proposed

- **Hilbert–Pólya / spectral operators** (Berry–Keating `xp`,
  Bender–Brody–Müller, etc.): no known route from the heuristics to a
  self-adjointness proof; every step that matters is exactly as hard as
  RH. Nothing bounded to compute or falsify.
- **Connes / F_1 / arithmetic-site program:** serious mathematics by
  specialists, decades deep; a repository like this can *read* it (and
  must, for Route 004 prior art) but cannot contribute incrementally
  without years of background. Not a route here.
- **de Branges spaces:** the published counterexamples to earlier
  positivity conditions (Conrey–Li) make unguided work here likely to
  repeat known failures.
- **Random matrix / GUE statistics:** produces evidence and conjectures,
  not proofs; already influenced Route 001's design implicitly.
- **Zero-density / critical-line percentage improvements** (Levinson,
  Conrey ≥ 40%, later ~41.7%): real unconditional progress, but the
  techniques (mollifier optimization) are a specialist industry with an
  enormous engineering cost per 0.1%; dominated by Route 005 for this
  team.
- **Extending brute-force zero verification** beyond 3·10^12
  (Platt–Trudgian): not proposed as progress toward proof (Route 003's
  finite-to-infinite barrier), though Route 005 consumes such results as
  input.
- **Another equivalence reformulation** (countable families, discretized
  criteria, moment reformulations): rejected on the Route 003 lesson
  unless a propagation mechanism comes with it.

## What "exhausting reasonable effort" means for this repository

1. **Finish Route 001 to publication quality** (admissibility memorandum;
   Arb port; independent verifier; then a short rigorous computational
   note). A finished negative-or-partial result in the literature outlives
   any unfinished attack.
2. **Run Route 004's falsification experiment** as soon as the convention
   memorandum exists — it is the cheapest way to learn whether the
   Gaussian program has any future.
3. **Invest sustained effort only in Route 005**, the one venue where
   unconditional quantitative progress is structurally guaranteed to be
   meaningful.
4. **Engage humans.** Post the hardened Route 001/002 material where
   analytic number theorists will see it; AI agreement is not
   verification (repository rule), and expert contact is itself a
   required step of reasonable effort.
5. **Accept the honest endpoint.** If Routes 004–007 end in recorded
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
