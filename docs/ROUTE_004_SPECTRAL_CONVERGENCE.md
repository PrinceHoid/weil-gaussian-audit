# Route 004 audit — spectral convergence of truncated Weil forms

**Status:** Active research program; no proof of RH and no new theorem yet.

## Plain-language idea

For each prime cutoff `c`, recent work constructs a finite/truncated spectral problem. Under stated ground-state hypotheses, the transform associated with its lowest eigenfunction has zeros only on the critical line. Computations suggest that, as more primes are included, these finite zeros approach zeros of the Riemann zeta function.

The missing bridge is convergence. A finite list of increasingly accurate-looking zeros is evidence, not a proof that every zeta zero is reached in the limit.

## The five required questions

### 1. What exact claim is being investigated?

Let `Q_c` denote the Connes–van Suijlekom truncated Weil quadratic form at prime cutoff `c`, on the interval whose length is `L = log c`. Let `xi_c` be its normalized even lowest-eigenvalue state whenever that state exists, is isolated, and is simple. Let `F_c` be the associated entire Fourier/Mellin transform, normalized at a fixed nonzero reference value.

The target convergence claim is:

> As `c -> infinity`, `F_c` converges locally uniformly on the complex plane to the completed zeta function `Xi`, up to an explicitly controlled zero-free factor.

A weaker acceptable version would prove that every zero of `Xi` is approximated, with multiplicity, by zeros of `F_c`, with no uncontrolled loss or creation of zeros.

Before this is a formal theorem statement, the precise normalization and the exact operator/formula must be transcribed from the primary source and locked in the repository. No numerical implementation may silently substitute a different discretization for `Q_c`.

### 2. Why would it matter for RH?

The finite criticality theorem says that, under its operator hypotheses, every zero of each `F_c` is real in the Fourier variable, corresponding to the critical line for zeta.

If `F_c -> Xi` locally uniformly and the limit is not identically zero, Hurwitz's theorem (or a local Rouché argument that also tracks multiplicity) transfers this real-zero property to `Xi`. That would imply the Riemann Hypothesis.

This implication is conditional on all of the following:

1. the finite operator hypotheses hold for sufficiently large cutoffs;
2. the transforms are normalized without introducing singularities;
3. convergence is locally uniform on complex neighborhoods, not merely pointwise on the real axis;
4. the limit is actually `Xi` up to a zero-free factor;
5. every relevant zero and its multiplicity are controlled.

### 3. What would be genuinely new?

The published numerical agreement is finite computation. The proposed new intermediate result is an analytic compactness-and-identification theorem for the normalized transforms.

A useful first theorem would be a cutoff-independent exponential-moment estimate such as

```text
For every A > 0,

  sup_c  integral exp(A |u|) |xi_c(u)| du / |integral xi_c(u) du| < infinity,
```

with the conventions adjusted to the exact transform. This would imply local boundedness of the normalized entire functions and hence normal-family compactness by Montel's theorem.

That estimate alone would not prove RH. A second theorem would still be needed to identify every subsequential limit uniquely with `Xi` up to a zero-free factor.

### 4. What is the first unproved step?

The first unproved step is **uniform compactness as the interval grows**.

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

After compactness, the next unproved step is uniqueness: derive an equation or variational characterization that forces every subsequential limit to be the completed zeta function rather than another real-entire function.

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

A failed test would not disprove RH. It would disprove this proposed convergence mechanism or show that a stronger renormalization is required.

## Dependency map

```text
Exact Q_c and normalization
        |
        v
Finite ground-state hypotheses for all large c
        |
        v
Uniform off-axis bounds / normal-family compactness   <-- first target
        |
        v
Identification and uniqueness of subsequential limit
        |
        v
Multiplicity-preserving zero convergence
        |
        v
Finite real-zero theorem + Hurwitz/Rouché
        |
        v
RH
```

## Known result, computation, heuristic, and new claim

- **Known conditional finite result:** the finite transform has only real zeros when the specified self-adjoint ground-state hypotheses hold.
- **Finite computation:** reported truncated matrices reproduce many low zeta zeros to high precision for selected cutoffs and discretizations.
- **Heuristic:** increasing the prime cutoff appears to make the finite zeros converge to zeta zeros.
- **Open problem:** convergence to every zeta zero has not been proved.
- **New claim made here:** none. This document isolates a candidate intermediate theorem and a falsification protocol.

## Immediate work queue

1. Transcribe the exact quadratic form, domain, interval convention, transform, and normalization from the primary papers.
2. Prove or delimit the ground-state existence, simplicity, isolation, and gap assumptions as `c` varies.
3. Derive an identity or inequality capable of controlling endpoint mass.
4. Reproduce the numerical experiment while recording off-axis bounds, localization, normalization, and gap data—not only zero locations.
5. Attempt the exponential-moment theorem; if it fails, construct the failure mechanism explicitly.
6. Only after compactness is established, attack unique identification of the limit with `Xi`.

## Sources

- Alain Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time*, arXiv:2602.04022.
- Alain Connes and Walter D. van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral Action*, arXiv:2511.23257.
- Akiva Groskin, *High-Precision Approximation of Riemann Zeros via the Truncated Weil Form*, arXiv:2605.20224.

The sources explicitly distinguish the proved finite real-zero statement and numerical approximation from the unproved cutoff-to-infinity convergence needed for RH.