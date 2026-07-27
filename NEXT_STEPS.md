# What collaborators should do next

## Current priority

The active research program is **Route 004: spectral convergence of localized
Weil ground states**.

Do not spend the next research cycle matching more real zeros. The decisive
question is whether the actual continuum ground states converge, strongly
enough off the real axis, to a published prolate proxy whose transforms are
already known to converge to Riemann's completed `Xi` function.

RH remains unsolved.

## Route 004 in one dependency chain

Use the consistent parametrization

```text
c = lambda^2
L = log(c) = 2 log(lambda).
```

The support cutoff `c` controls prime powers up to `c`; it need not itself be a
prime.

The current bridge is:

```text
exact continuum operator and normalization
        |
        v
simple, isolated, even continuum ground state
        |
        v
scalar-aligned comparison with the prolate proxy k_lambda
        |
        v
local-uniform transform convergence on |Im z| < 1/2
        |
        v
published finite real-zero theorem + Hurwitz
        |
        v
RH
```

The last implication is standard once every earlier hypothesis is proved. The
two independent open mathematical obligations are:

1. prove simplicity and evenness of the continuum lowest eigenvalue along an
   unbounded cutoff sequence;
2. prove a transform-controlling comparison between the corresponding ground
   state `theta_lambda` and the prolate proxy `k_lambda`.

One clean sufficient comparison is

```text
E_lambda
  = inf_b ||b theta_lambda-k_lambda||_2
  = O(lambda^(-1/2)).
```

This rate is sufficient, not known, and not claimed to be necessary.

## What is already established

### Known published results

- The localized Weil form has a continuum operator formulation with compact
  resolvent under the stated setup.
- Continuum or finite ground-state transforms have real zeros under their
  respective simple/even hypotheses.
- The transforms of the prolate proxy `k_lambda` converge to `Xi` uniformly on
  closed substrips of `|Im z|<1/2`.

### Exact repository-level results awaiting independent review

- The critical-strip transfer lemma: the displayed
  `O(lambda^(-1/2))` comparison transfers the published proxy convergence to
  the true transforms and would imply RH.
- An explicit convolution counterexample: positivity, compact support, a
  simple even ground state, a uniform gap, and real zeros at every finite stage
  do not imply analytic compactness or convergence.

### Finite numerical evidence

- At `c=13`, `T=80`, and `z=0.49i`, a Galerkin probe's absolute error relative
  to normalized `Xi` decreased from about `1.95e-3` at `N=8` to `6.81e-5` at
  `N=20`.
- A negative eigenvalue seen at `T=40` disappeared at `T=80` and `T=160`,
  demonstrating that an artificial archimedean cutoff can create false signs
  or branch changes.

These computations prove no `N`, archimedean, or cutoff limit.

## Keep the constructions separate

Do not silently transfer a theorem between:

1. the continuum localized Weil operator `A_lambda`;
2. finite Galerkin matrices `Q_(c,N,T)`;
3. the prolate comparison family `k_lambda`;
4. Suzuki's distinct self-adjoint-extension family.

For every result, state the Hilbert space, domain, parity, transform convention,
centering or retained zero-free phase, scalar normalization, and order of
limits.

## Ordered Route 004 work queue

### R4.1 — Freeze the mathematical object

Produce an equation-level specification of:

- the localized Weil distribution and quadratic form;
- convolution and involution;
- pole, archimedean, and prime terms with signs;
- the map `c=lambda^2`;
- logarithmic centering;
- the self-adjoint operator and its domain;
- the parity involution;
- the ground-state normalization;
- the Fourier–Mellin transform.

Test the specification against the published `c=13` matrix. A numerical
implementation must not silently replace the source operator with a different
discretization.

### R4.2 — Independently audit the bridge

Have separate reviewers check:

1. the published proxy-transform convergence theorem;
2. the repository's `L^2`-to-critical-strip estimate;
3. the Hurwitz/Rouché implication;
4. the explicit noncompactness counterexample;
5. the claim that only `|Im z|<1/2` is required.

This review contains no numerical premise.

### R4.3 — Build a verified comparison experiment

Implement `k_lambda` with a stable high-precision prolate routine and implement
the Weil matrices with a cutoff-free archimedean term or a certified tail.

First reproduce the existing `c=13` off-axis table while independently
refining:

- Galerkin dimension `N`;
- archimedean cutoff or tail treatment;
- working precision;
- parity sector and selected spectral branch.

Only after that baseline is reproduced should a cutoff sequence be
preregistered for measuring:

```text
E_lambda = inf_b ||b theta_lambda-k_lambda||_2,
sqrt(lambda) E_lambda,
parity leakage,
the lowest even and odd eigenvalues,
the spectral gap,
central versus endpoint mass,
and centered transform errors at fixed |Im z| < 1/2.
```

Finite data can reject a declared finite error model or expose instability.
They cannot by themselves disprove an asymptotic big-O claim.

### R4.4 — Attack ground-state alignment analytically

The direct goal is the scalar-aligned comparison above. One possible sufficient
route, after verifying all domain assumptions, is:

1. normalize `k_lambda`;
2. bound its Rayleigh excess above the true lowest eigenvalue;
3. prove a lower bound for separation from the remaining spectrum;
4. use the min-max principle or a certified spectral-projection estimate to
   obtain `L^2` alignment.

A small Rayleigh quotient alone is insufficient. Do not assume global
localized Weil positivity to prevent cancellation; that positivity is
RH-equivalent and would make the proof circular.

If an `L^2` rate weaker than `O(lambda^(-1/2))` is obtained, seek weighted
localization or exponential-moment estimates that still give local-uniform
transform convergence on every closed substrip.

### R4.5 — Prove continuum simplicity and evenness

Separately establish that the actual continuum lowest eigenvalue is simple,
isolated, and represented by an even eigenfunction along an unbounded cutoff
sequence. Finite-matrix parity or a numerically selected
"smallest-positive" branch is not this theorem.

## Earliest falsification

The first numerical warning test is whether `sqrt(lambda) E_lambda` grows over
a verified, preregistered sequence while all discretization errors shrink.
That is evidence against the clean rate, not a proof of asymptotic failure.

A rigorous falsification of the rate requires an analytic lower bound or a
certified unbounded subsequence. Such a result would reject this sufficient
comparison mechanism, not RH.

The alternative normal-family route is falsified in its stated form if the
centered, normalized transforms are proved unbounded on one fixed compact set
inside `|Im z|<1/2`.

## Numerical safeguards

- Use interval or ball arithmetic for any claimed certificate.
- Bound the archimedean tail; agreement at two `T` values is not a proof.
- Bound Galerkin error and certify the relevant eigenvalue separation.
- Certify the lowest full spectrum, not only a smallest-positive branch.
- Verify parity and simplicity with disjoint eigenvalue enclosures.
- Track eigenvectors by certified subspace angles.
- Separate discretization, arithmetic precision, support cutoff, and branch
  error.
- Predeclare parameters, norms, evaluation points, and pass/fail thresholds.
- Preserve raw matrices, hashes, environment data, and an independent
  verification program.
- Never infer an asymptotic rate from a short fitted sequence.
- Never infer RH from agreement with finitely many zeta zeros.

## Secondary and closed lessons

### Route 001 — restricted Gaussian positivity

**Status:** Explored; secondary computational baseline.

Do not enlarge the finite grid unless a new theorem bridges its restricted
family to Weil's universal criterion. If developed as a computational note,
its transform conventions, admissibility, and numerical bounds still require
independent audit.

### Route 002 — fixed-scale Gaussian cone obstruction

**Status:** Candidate intermediate obstruction awaiting independent review.

It blocks positive-cone density for the original fixed-width family. It is not
evidence for or against RH.

### Route 003 — countable determining family

**Status:** Rejected as a new route.

Countability and separability do not remove the infinite positivity burden.
Reopen this route only with a genuinely new theorem that propagates a finite or
strictly weaker premise to the full infinite tail.

## Proposal template for any new route

Before substantial work, record:

1. **Claim:** the exact statement to be proved.
2. **Connection to RH:** a proof of what success would imply.
3. **Prior art:** the closest primary-source results and the difference.
4. **Novel step:** the genuinely new lemma or construction.
5. **First unproved step:** the earliest missing implication.
6. **Failure test:** the quickest way to expose the obstruction.
7. **Dependencies and evidence:** assumptions, computations, and status labels.

Add the route to [RESEARCH_MAP.md](RESEARCH_MAP.md) only after answering these
questions.

## Guidance for AI collaborators

- Work on one auditable lemma, source reconstruction, counterexample, or
  diagnostic at a time.
- Begin every session by answering the five required questions.
- Label known theorem, exact derivation, rigorous computation, finite numerical
  evidence, heuristic, candidate claim, and falsification separately.
- Prefer an early obstruction or certified instability to a larger grid.
- Preserve negative results and normalization corrections.
- Never use agreement among AI systems as independent verification.

## Guidance for human collaborators

- An analytic number theorist should audit the exact Weil functional and the
  RH implication.
- A functional analyst should audit domains, compact resolvent, parity,
  simplicity, min-max arguments, and spectral separation.
- A special-functions expert should audit the prolate construction.
- A complex analyst should audit the transform convergence and Hurwitz step.
- A rigorous-numerics specialist should design certified tail, Galerkin,
  eigenvalue, and eigenvector bounds.
- An independent reviewer should try to falsify both the alignment and
  localization mechanisms.

The first valuable human verdict is whether the comparison-and-localization
program is mathematically viable, not whether RH has already been proved.

## Breakthrough protocol

A claimed proof or disproof must not be merged merely because several AI
systems agree. It must receive:

1. a line-by-line dependency map;
2. independent attempts to falsify every new lemma;
3. checks for circular use of RH;
4. verification of all load-bearing cited theorems from primary sources;
5. independent reproduction of any computation;
6. review by qualified human mathematicians.

Until then, label it **candidate**.
