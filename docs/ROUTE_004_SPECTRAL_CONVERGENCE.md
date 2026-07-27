# Route 004 audit — spectral convergence of truncated Weil forms

**Status:** Active research program; a rigorous critical-strip transfer lemma and abstract obstruction have been recorded, but there is no proof of RH.

## Plain-language idea

For each support cutoff `c=lambda^2`, controlling prime powers `p^m<=c`, recent work constructs a localized or finite spectral problem. The value `c` need not itself be prime. Under stated ground-state hypotheses, the transform associated with its lowest eigenfunction has zeros only on the critical line. Computations suggest that, as more primes are included, these finite zeros approach zeros of the Riemann zeta function.

The missing bridge is convergence. A finite list of increasingly accurate-looking zeros is evidence, not a proof that every zeta zero is reached in the limit.

## The five required questions

### 1. What exact claim is being investigated?

Let `Q_c` denote the Connes–van Suijlekom truncated Weil quadratic form at support cutoff `c=lambda^2`, on the interval whose length is `L = log c`. Let `xi_c` be its normalized even lowest-eigenvalue state whenever that state exists, is isolated, and is simple. Let `F_c` be the associated entire Fourier/Mellin transform, normalized at a fixed nonzero reference value.

The target convergence claim is:

> As `c -> infinity`, `F_c` converges locally uniformly on the strip `|Im z| < 1/2` to the completed zeta function `Xi`, up to an explicitly controlled zero-free factor.

A weaker acceptable version would prove directly that every zero of `Xi` is approximated by zeros of `F_c`, with no uncontrolled loss. Multiplicity tracking is useful for a stronger theorem but is not a separate requirement for the basic RH implication.

Before this is a formal theorem statement, the precise normalization and the exact operator/formula must be transcribed from the primary source and locked in the repository. No numerical implementation may silently substitute a different discretization for `Q_c`.

### 2. Why would it matter for RH?

The finite criticality theorem says that, under its operator hypotheses, every zero of each `F_c` is real in the Fourier variable, corresponding to the critical line for zeta.

If `F_c -> Xi` locally uniformly and the limit is not identically zero, Hurwitz's theorem (or a local Rouché argument that also tracks multiplicity) transfers this real-zero property to `Xi`. That would imply the Riemann Hypothesis.

This implication is conditional on all of the following:

1. the finite operator hypotheses hold for sufficiently large cutoffs;
2. the transforms are normalized without introducing singularities;
3. convergence is locally uniform on complex neighborhoods, not merely pointwise on the real axis;
4. the limit is actually `Xi` up to a zero-free factor;
5. every possible off-real zero lies in the domain where the convergence theorem applies.

### 3. What would be genuinely new?

The published numerical agreement is finite computation. The proposed new intermediate result is an analytic compactness-and-identification theorem for the normalized transforms.

A useful first theorem would be a cutoff-independent exponential-moment estimate such as

```text
For every 0 < A < 1/2,

  sup_c  integral exp(A |u|) |xi_c(u)| du / |integral xi_c(u) du| < infinity,
```

with the conventions adjusted to the exact transform. This would imply local boundedness of the normalized entire functions and hence normal-family compactness by Montel's theorem.

That estimate alone would not prove RH. A second theorem would still be needed to identify every subsequential limit uniquely with `Xi` up to a zero-free factor.

### 4. What is the first unproved step?

The first zeta-specific comparison target is **quantitative comparison of the true continuum ground state with the published prolate proxy `k_lambda`**. A second independent open hypothesis is simplicity and evenness of the continuum ground state along an unbounded cutoff sequence.

The eigenfunctions live on intervals of length `log c`. Unit `L^2` norm and compact support at each fixed cutoff do not provide a cutoff-independent bound. The elementary Cauchy–Schwarz estimate has the bad form

```text
|Fhat_c(z)| <= sqrt(log c) * exp((log c) |Im z| / 2),
```

before normalization. For fixed nonreal `z`, this can grow like a power of `c`. Therefore “take a convergent subsequence” is not justified by finite support or `L^2` normalization alone.

The route needs either:

- uniform localization of the ground states near the center;
- a cutoff-independent exponential-moment bound;
- a different renormalization and topology strong enough to preserve zeros; or
- a structural resolvent/operator convergence theorem that supplies compactness indirectly.

Connes already proves that the Fourier transforms of `k_lambda` converge to `Xi` on closed substrips of `|Im z|<1/2`. A repository-level transfer lemma shows that the scalar-aligned estimate `||b_lambda theta_lambda-k_lambda||_2 = O(lambda^(-1/2))` would transfer that convergence to the true ground states. The other prerequisite is simplicity and evenness of the continuum lowest eigenvalue for an unbounded cutoff sequence.

### 5. What is the earliest falsification test?

Test whether the proposed normalized family is locally bounded away from the real axis.

For increasing cutoffs, compute with certified error bounds:

1. the normalization denominator;
2. mass in central windows versus mass near the expanding endpoints;
3. exponential moments for several fixed positive exponents;
4. `|F_c(x + i y)|` on fixed compact rectangles with `y != 0`;
5. the spectral gap above the lowest eigenvalue.

The present convergence strategy is falsified in its stated form if any of the following is demonstrated:

- the normalization denominator tends to zero too quickly;
- ground-state mass escapes toward the endpoints;
- normalized transforms are unbounded on a fixed compact set;
- two cutoff subsequences approach different normalized limits;
- the ground state repeatedly loses simplicity/isolation;
- the spectral gap collapses in a way that makes the selected state unstable.

A failed finite test would not disprove RH or an asymptotic rate; it would reject a declared finite error model or expose instability. Rigorously rejecting the asymptotic mechanism requires an analytic obstruction or a certified unbounded subsequence.

## Dependency map

```text
Exact continuum operator, centering, and normalization
        |
        v
Simple/even continuum ground states along an unbounded sequence
        |
        v
Proxy comparison or another zeta-specific compactness theorem
        |
        v
Local-uniform convergence to Xi on |Im z| < 1/2
        |
        v
Continuum real-zero theorem + Hurwitz/Rouché
        |
        v
RH
```

## Known result, computation, heuristic, and new claim

- **Known conditional results:** the continuum and finite transforms have only real zeros under their respective self-adjoint ground-state hypotheses.
- **Finite computation:** reported truncated matrices reproduce many low zeta zeros to high precision for selected cutoffs and discretizations.
- **Heuristic:** increasing the support cutoff appears to make selected finite zeros converge to zeta zeros.
- **Open problem:** convergence to every zeta zero has not been proved.
- **Repository-level result:** a standard-analysis transfer lemma reduces the bridge to `||b_lambda theta_lambda-k_lambda||_2 = O(lambda^(-1/2))` on the critical strip, and an explicit convolution example proves that finite real-rootedness, positivity, and a uniform gap do not supply compactness abstractly. These claims require independent review and do not prove RH.

## Immediate work queue

1. Freeze the continuum, Galerkin, and Suzuki families separately; never interchange their hypotheses or limits.
2. Prove simplicity and evenness of the continuum lowest eigenvalue along an unbounded cutoff sequence.
3. Implement `k_lambda` with a verified high-precision prolate routine and cutoff-free/interval-certified Weil matrices.
4. Measure and then prove the scalar-aligned error `E_lambda = inf_b ||b theta_lambda-k_lambda||_2`.
5. Attack the sufficient rate `E_lambda = O(lambda^(-1/2))` using the semilocal trace formula without assuming global Weil positivity.
6. Continue off-axis falsification tests on `|Im z|<1/2`, independently refining `N`, archimedean cutoff, precision, and the support cutoff.

## First research-cycle result

See [`ROUTE_004_CRITICAL_STRIP_BRIDGE.md`](ROUTE_004_CRITICAL_STRIP_BRIDGE.md) for the proof of the transfer lemma, source corrections, counterexamples, exploratory off-axis data, and the next falsification protocol.

## Sources

- Alain Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time*, arXiv:2602.04022.
- Alain Connes and Walter D. van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral Action*, arXiv:2511.23257.
- Alain Connes, Caterina Consani, and Henri Moscovici, localized Weil/spectral construction, arXiv:2511.22755.
- Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096.
- Akiva Groskin, *High-Precision Approximation of Riemann Zeros via the Truncated Weil Form*, arXiv:2605.20224.
- Akiva Groskin, *A finite Guinand-Weil dictionary and archimedean tail order for the truncated Weil quadratic form*, arXiv:2607.02828.

The sources explicitly distinguish the proved finite real-zero statement and numerical approximation from the unproved cutoff-to-infinity convergence needed for RH.