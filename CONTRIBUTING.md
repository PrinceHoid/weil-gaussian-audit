# Contributing

Thank you for helping investigate and audit this project.

Create a focused branch and pull request for each research route or correction.
Explain what claim is affected, what was checked, how it can be reproduced, and
what remains uncertain.

## Required pull-request summary

Every research pull request must answer:

1. What exact claim is being made?
2. What is the proved logical relationship to RH?
3. What is known from the literature, and what is new?
4. What is the first unproved step?
5. What is the earliest falsification test?
6. What assumptions and external theorems are used?
7. What evidence level applies to each result?

Link the corresponding entry in `RESEARCH_MAP.md` and preserve failed or
superseded approaches rather than erasing them.

## Evidence labels

Distinguish among:

- known theorem with primary-source citation;
- exact derivation or proof;
- candidate repository-level theorem awaiting independent review;
- rigorous interval or ball-arithmetic computation;
- exact structural or data-integrity check;
- floating-point numerical experiment;
- heuristic or conjecture;
- assumption, including any use of RH.

Do not describe a floating-point result as certified. Do not describe a
finite verification as an asymptotic theorem.

## Computational contributions

Record:

- code revision and environment;
- all mathematical normalizations;
- support cutoff and included prime powers;
- basis or Galerkin dimension;
- archimedean cutoff or a rigorous tail treatment;
- arithmetic precision;
- parity and spectral-branch selection;
- pass/fail thresholds;
- raw artifacts or hashes;
- an independent verification path.

Refine independent error sources independently. Agreement at two parameter
values is evidence, not an error bound.

## Route 004 contributions

Do not conflate the continuum Weil operator, a finite Galerkin matrix, the
prolate proxy, or Suzuki's separate family.

For spectral convergence work, state:

- whether the claim concerns the continuum or a discretization;
- the relation `c=lambda^2`;
- the interval and centering convention;
- the scalar normalization and zero-free phase;
- the exact theorem supplying real zeros;
- the complex domain on which convergence is claimed;
- the order and control of every limit.

The comparison

```text
inf_b ||b theta_lambda-k_lambda||_2 = O(lambda^(-1/2))
```

is an unproved sufficient target. A finite trend, small eigenvalue, small
Rayleigh quotient, or high overlap is not a proof of it.

## Review and status

A new mathematical claim stays labelled **candidate** until:

- its dependencies are checked from primary sources;
- an independent reviewer attempts to falsify it;
- every computation is independently reproduced or verified;
- any circular use of RH is excluded;
- qualified human experts review load-bearing steps.

Corrections and negative results are welcome. A clean obstruction is useful
progress and should be documented rather than hidden.
