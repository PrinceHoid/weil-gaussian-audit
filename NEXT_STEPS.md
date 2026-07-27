# What collaborators should do next

## Immediate task

Do not assume the existing Gaussian route is the project.

Each collaborator should propose or audit **one clearly defined route** connected
to the original question:

> Does every non-trivial zero of the Riemann zeta function have real part 1/2?

## For a new route

Create a short proposal containing:

1. **Claim:** the exact statement to be proved.
2. **Connection to RH:** a proof showing what success would imply.
3. **Prior art:** the closest known results and how this differs.
4. **Novel step:** the first genuinely new lemma or construction.
5. **Failure test:** the quickest way to expose a contradiction or known
   obstruction.
6. **Dependencies:** assumptions, computations, and external theorems used.
7. **Status:** speculation, heuristic, numerical evidence, candidate lemma, or
   proof.

Do not begin a large computation until these seven points are written down.

## For an existing route

Audit the earliest unproved step, not the most impressive conclusion.

- Check every implication leading back to RH.
- Look for a hidden RH assumption.
- Look for a finite-to-infinite leap.
- Look for a restricted test family being substituted for a universal class.
- Check whether the result is already known.
- Produce counterexamples to intermediate claims when possible.

## Current routes

The route index is [RESEARCH_MAP.md](RESEARCH_MAP.md). Add a route there only
after its proposal answers the seven questions above.

The Gaussian/Guinand–Weil route is preserved as Route 001. Its current finite
certificate does not prove RH, and further work on it must identify a credible
bridge to the full universal criterion before expanding the computation.

Route 002 proves a candidate obstruction to one such bridge: the positive cone
of the fixed-scale translated Gaussians cannot contain narrower centered
Gaussians. See
[`docs/ROUTE_002_GAUSSIAN_CONE_OBSTRUCTION.md`](docs/ROUTE_002_GAUSSIAN_CONE_OBSTRUCTION.md).
This means that more translation samples at the existing scale cannot resolve
Weil's universal quantifier by positive-cone density alone.

## Recommended sequence after Route 002

### 1. Freeze admissibility and conventions

Before new numerical work, write a short derivation that fixes:

- the additive Fourier convention used by `Q(t)`;
- the exact multiplicative Mellin convention used for Weil's criterion;
- the map between the two formulations;
- the involution and convolution measure;
- the pole terms and signs;
- the two vanishing-moment conditions in Bombieri's formulation;
- the precise topological test space.

The result must show whether the present `h_t` belongs to the selected
admissible class. Pointwise positivity of `h_t` and the sign-changing inverse
transform `g_t` are not substitutes for this proof.

### 2. Independently review the Route 002 proof

An independent reviewer should recompute:

```text
Lambda(h_t) = 2 sqrt(pi) (1 - exp(-t^2))
Lambda(exp(-a r^2)) = sqrt(pi) (a^(-1/2) - 1)
```

and check continuity of integration and point evaluation in the declared
topology. Until then, keep the route labelled **candidate result**.

### 3. If pursuing Gaussians, formulate an all-scale route

Define

```text
h_{a,t}(r) = exp(-a(r-t)^2) + exp(-a(r+t)^2),  a > 0,
```

and derive the corresponding prime-side `Q_a(t)` from the frozen convention.
Do not obtain it by informal rescaling: the prime weights, Fourier factors,
pole term, and archimedean convolution all change with `a`.

The proposal must identify a structural claim, such as a rigorously stated
scale-evolution inequality. Merely computing a grid in `(a,t)` is numerical
evidence, not a bridge to RH.

### 4. Run a small falsification experiment first

Before a large computation, predeclare a small set such as

```text
a in {2, 4}
t in {0, 11, 14.1347, 17.58}
```

and evaluate it with rigorous ball arithmetic after the formula is independently
checked. Search first for:

- a negative value;
- failure of scale monotonicity;
- a hidden pole or moment-condition violation;
- loss of a uniform tail or curvature bound.

A failure is useful progress and should be added to the route record.

### 5. Separate mathematical and numerical review

If an all-scale lemma survives early falsification:

- one reviewer derives the formula and admissibility;
- another tries to disprove the scale lemma;
- another checks primary-source dependencies;
- another implements ball arithmetic;
- a separate program verifies every generated certificate.

Do not use agreement among AI systems as verification.

## Guidance for AI collaborators

- State the five required questions before derivation or computation.
- Label known results, exact algebra, rigorous computation, numerical evidence,
  heuristics, and speculation separately.
- Never infer unconditional positivity from the zero-side Gaussian sum; real
  zero ordinates are an RH assumption.
- Never cite Wiener or universal-kernel density without stating that signed
  coefficients are allowed and therefore positivity is not preserved.
- Prefer counterexamples and separating functionals to larger grids.
- Preserve failed lemmas, normalization corrections, and negative experiments.
- Do not claim literature novelty until a primary-source search and expert
  review have been completed.

## Guidance for human collaborators

- Assign an analyst to review Route 002's topology and separation argument.
- Assign an analytic number theorist to select and normalize the exact Weil
  criterion used by the project.
- Decide explicitly whether Route 001 is intended as a rigorous computational
  note or as the seed of an all-scale RH route.
- Require mature ball arithmetic and an independent verifier for any new
  computer-assisted claim.
- Require a line-by-line dependency map and adversarial review before promoting
  a candidate theorem.
- Treat a clean obstruction as progress even when it narrows rather than solves
  the research program.

## Breakthrough protocol

A claimed proof or disproof must not be merged as accepted merely because
several AI systems agree. It must receive:

1. a line-by-line dependency map;
2. independent attempts to falsify every new lemma;
3. checks for circular use of RH;
4. verification of all cited theorems from primary sources;
5. review by qualified human mathematicians.

Until then, label it **candidate**.
