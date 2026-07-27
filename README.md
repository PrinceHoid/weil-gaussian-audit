# Is every non-trivial zero of the Riemann zeta function on the critical line?

## The question

> **Does every non-trivial zero rho of the Riemann zeta function satisfy**
>
> # `Re(rho) = 1/2`?

This is the **Riemann Hypothesis (RH)**. It remains unsolved. No file or
computation in this repository proves or disproves it.

## Mission

Humans and AI systems use this repository to seek:

1. a valid proof of RH;
2. a valid counterexample; or
3. a rigorously justified new intermediate result that materially narrows the
   problem.

Failed routes, counterexamples, normalization corrections, and negative
experiments are preserved so later collaborators do not repeat them.

## New here?

Start with the
[plain-language guide](docs/PLAIN_LANGUAGE_GUIDE.md). It explains the four
research routes without assuming technical mathematics.

For the formal record, read [RESEARCH_MAP.md](RESEARCH_MAP.md). The current
work queue is in [NEXT_STEPS.md](NEXT_STEPS.md), and AI collaborators must also
follow [AGENTS.md](AGENTS.md).

## Current research status

| Route | Status | What was learned |
|---|---|---|
| 001 — restricted Gaussian positivity | Explored | A reproducible finite computation does not satisfy Weil's universal criterion and does not prove RH. |
| 002 — fixed-scale Gaussian cone | Candidate result | Positive mixtures of the original fixed-width Gaussians cannot generate arbitrarily concentrated test functions. This blocks one proposed bridge, not RH. |
| 003 — countable determining family | Rejected as new route | Countable positivity criteria are already known; proving every inequality is still equivalent to RH. |
| 004 — spectral convergence | Active | A precise finite-to-infinite bridge has been isolated, together with a counterexample showing that convergence is not automatic. Two decisive continuum hypotheses remain unproved. |

### The active frontier: Route 004

Recent spectral constructions associate finite or localized problems with
transforms whose zeros are real under stated ground-state hypotheses. Separately,
a published prolate proxy `k_lambda` has a transform that converges to Riemann's
completed `Xi` function on closed substrips of

```text
|Im z| < 1/2.
```

The repository proved the following conditional transfer:

```text
If the true centered continuum ground state theta_lambda is simple and even,
and scalars b_lambda can be chosen so that

  ||b_lambda theta_lambda - k_lambda||_2 = O(lambda^(-1/2)),

then its transforms converge locally uniformly to Xi in the critical strip;
Hurwitz's theorem would then imply RH.
```

That comparison estimate and the required continuum simplicity/evenness are
open. Therefore this is a precise route to RH, not a proof of RH.

The same audit produced an explicit counterexample showing that positivity, a
simple even ground state, a uniform spectral gap, compact support, and real
zeros at every finite stage still do **not** force analytic convergence. A
zeta-specific comparison with `k_lambda` is indispensable.

An exploratory finite probe at `c=13`, `T=80`, and `z=0.49i` improved as the
Galerkin dimension rose from `N=8` to `N=20`, reducing the absolute error from
about `1.95e-3` to `6.81e-5`. This is numerical evidence only. A false negative
eigenvalue at `T=40` disappeared at larger archimedean cutoffs, demonstrating
why all cutoffs and discretizations must be refined independently.

Technical records:

- [Route 004 research program](docs/ROUTE_004_SPECTRAL_CONVERGENCE.md)
- [Critical-strip transfer lemma and falsification cycle](docs/ROUTE_004_CRITICAL_STRIP_BRIDGE.md)

## Required questions for every proposed approach

Before substantial work, answer:

1. **What exact claim are you trying to prove?**
2. **If proved, does it imply RH, disprove RH, or only establish an
   intermediate result? Prove that implication.**
3. **What is genuinely new rather than a known theorem, reformulation, or
   finite verification?**
4. **What is the first currently unproved step?**
5. **What observation could falsify the approach early?**

Put each distinct approach on its own branch or pull request.

## Evidence labels

Every result must be labelled as one of:

- known theorem;
- exact repository-level proof awaiting or having received review;
- rigorous computation with certified error bounds;
- floating-point numerical evidence;
- heuristic;
- speculation.

Do not mix the continuum localized operator, a finite Galerkin matrix, and
Suzuki's self-adjoint-extension family. Their hypotheses and limiting problems
are different.

## Standards

- Never label a known equivalence as a proof.
- Never extrapolate a finite computation to an infinite statement without a
  proved bridge.
- Never assume global Weil positivity inside a proposed proof of RH; that would
  be circular.
- State normalizations, cutoffs, domains, and limit order explicitly.
- Prefer primary sources.
- Require independent adversarial review of every claimed theorem.
- Treat a rigorously demonstrated obstruction as useful progress.

Historical Gaussian materials remain under `docs/`, `src/`, `data/`, and
`tools/`.
