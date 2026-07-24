# Research map

This file tracks proposed routes toward proving or disproving the Riemann
Hypothesis. It records why each route matters, its first unresolved step, and
its current status.

## Status vocabulary

- **Proposed:** not yet audited.
- **Active:** has a precise unresolved target and ongoing work.
- **Blocked:** cannot proceed without resolving a named obstacle.
- **Rejected:** contains a demonstrated fatal flaw.
- **Explored:** produced information but currently has no credible bridge to RH.
- **Candidate result:** appears proved but lacks independent expert acceptance.
- **Accepted intermediate result:** independently verified new theorem with a
  demonstrated relationship to RH.

## Route 001 — Restricted Gaussian / Guinand–Weil positivity

**Status:** Explored; no current bridge to RH.

**Idea:** Evaluate the explicit-formula functional for

```text
h_t(r) = exp(-(r-t)^2) + exp(-(r+t)^2)
```

and attempt to certify positivity as t varies.

**What was produced:**

- a displayed prime-side functional Q(t);
- a numerical sweep and 11,720 certificate rows;
- exact structural coverage of the finite interval [11, 1737];
- a handoff memorandum documenting unresolved numerical obligations.

**What it establishes today:**

- the supplied data structurally cover the claimed finite interval;
- the computation is reproducible in a recorded environment;
- selected prime-side and zero-side values agree numerically.

**What it does not establish:**

- validation of every rigorous-numerics bound;
- positivity for all t;
- positivity for every admissible Weil test function;
- the Riemann Hypothesis.

**Central obstacle:** Weil's criterion has a universal quantifier over an
admissible class. Positivity for this one-parameter family does not satisfy that
quantifier. Extending the same finite sweep does not resolve this obstacle.

**Required before further expansion:** exhibit and prove a credible bridge from
this family to the full admissible class, or state a genuinely new intermediate
theorem that this route can establish.

**Historical materials:** `docs/`, `src/`, `data/`, and `tools/`.

## Proposed future routes

Add a new numbered route only after completing the proposal template in
`NEXT_STEPS.md`. Do not erase rejected routes; preserving them prevents
repetition.
