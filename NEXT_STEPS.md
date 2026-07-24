# NEXT RESEARCH STEPS

> [!CAUTION]
> **This file defines the current research program.**
>
> Do not skip directly to larger computations, stronger claims, or publicity.
> Complete the stages below in order and record evidence for every conclusion.

## Stage 1 — Freeze and verify the mathematics

**This is the immediate next task.**

Produce a readable, line-by-line derivation of the functional

```text
Q(t) = pole term + prime-power term + archimedean term
```

from one explicitly stated version of the Guinand–Weil formula.

The derivation must:

1. state the exact explicit-formula theorem and admissible function space;
2. state one Fourier-transform convention;
3. derive the transform of the chosen Gaussian family;
4. derive every constant, sign, factor of two, and factor of pi in Q(t);
5. prove or precisely source the Gaussian family's admissibility;
6. state the zero-side identity without assuming RH;
7. separately show what simplification becomes valid if RH is assumed;
8. identify every step that still requires expert confirmation;
9. cite primary sources wherever practical;
10. avoid using the numerical program as evidence for the derivation it implements.

**Completion evidence:** a short derivation document that another reviewer can
check line by line without running the code.

## Stage 2 — Audit the existing numerical implementation

After Stage 1 is stable, inspect every claimed rigorous bound in
`src/rigorous_weil_sweep.py`.

At minimum, verify:

- cosine argument reduction;
- floating-point and NumPy summation bounds;
- logarithm and Taylor-series remainders;
- Binet/digamma remainder bounds;
- prime-power truncation tails;
- archimedean quadrature and tail bounds;
- the global second-derivative bound;
- all domain restrictions and rounding assumptions;
- the mismatch between prose claims and generated data.

**Completion evidence:** a checklist linking each code claim to a proof,
counterexample, or clearly labeled unresolved obligation.

## Stage 3 — Build an independent implementation

Reimplement the calculation without copying the custom interval core. Prefer a
mature ball-arithmetic system such as FLINT/Arb through `python-flint`.

The independent program should:

- recompute every interval lower bound;
- verify exact coverage;
- reject malformed data, NaNs, and infinities;
- print a deterministic verification transcript;
- record dependency versions and artifact hashes;
- keep certificate generation separate from certificate verification.

**Completion evidence:** two independent implementations that agree, with the
second using a smaller and better-documented trust base.

## Stage 4 — Seek outside review

Ask for review from people with relevant expertise:

- analytic number theory and explicit formulas;
- Weil's criterion and admissible test-function spaces;
- validated or rigorous numerics;
- floating-point error analysis;
- Arb/FLINT ball arithmetic.

Invite reviewers to find errors. A discovered flaw is useful progress and
should be documented.

**Completion evidence:** review comments, corrections, and responses preserved
in issues or pull requests.

## Claim discipline

At every stage:

- This repository is **not a proof of RH**.
- Reproduction is not the same as proof.
- Exact interval coverage does not validate the bound attached to each row.
- Positivity for one Gaussian family does not satisfy Weil's universal
  quantifier.
- Do not infer unconditional positivity from the zero-side Gaussian expression
  by treating zero ordinates as real; that assumes RH.
- Label results as established, reproduced, candidate, or unestablished.
