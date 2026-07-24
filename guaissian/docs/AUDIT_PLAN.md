# Audit plan

## Current status

The finite certificate is a candidate computer-assisted lemma for one
restricted Gaussian family. The structural coverage check is reproducible, but
the numerical proof obligations are not independently certified.

## Priority order

1. Freeze one explicit-formula and Fourier convention and derive every
   constant in the displayed functional.
2. Prove that the Gaussian family is admissible for the selected formulation
   of Weil's criterion.
3. Replace hand-built floating-point enclosures with mature ball arithmetic,
   preferably FLINT/Arb.
4. Independently prove or recompute:
   - cosine argument reduction;
   - vector-summation rounding bounds;
   - Binet/digamma remainder bounds;
   - prime and archimedean tails;
   - the global second-derivative bound.
5. Separate certificate generation from verification.
6. Supply an executable and human-readable proof of any infinite-tail claim.
7. Obtain review from specialists in analytic number theory and rigorous
   numerics.

## Suggested issue labels

- `math-derivation`
- `rigorous-numerics`
- `reproduction`
- `documentation`
- `claim-scope`
- `good-first-audit`

## Evidence levels

- **Established:** standard literature results with precise citations.
- **Reproduced:** independently executed or recomputed in a documented
  environment.
- **Candidate:** plausible result awaiting proof-obligation review.
- **Unestablished:** unsupported, incomplete, or dependent on an unstated
  assumption.

