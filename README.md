# Weil Gaussian Audit

Independent reproduction and audit of a restricted Gaussian Weil-positivity
computation related to the Riemann zeta function.

> [!IMPORTANT]
> This repository does **not** contain a proof of the Riemann Hypothesis.
> It contains an AI-assisted exploratory calculation and a candidate
> computer-assisted lemma whose mathematical and numerical proof obligations
> still require independent expert review.

## Why this repository exists

The project began with the question:

> Is the real part of every non-trivial zero of the Riemann zeta function
> equal to \(1/2\)?

That question is exactly the Riemann Hypothesis, which remains open. Several AI
systems helped explore a one-parameter Gaussian test family and produced a
finite interval certificate. This repository preserves that work while making
its claims, limitations, and verification status explicit.

The maintainers are technically trained non-specialists. Contributions from
mathematicians and rigorous-numerics practitioners are welcome, especially
when they include reproducible derivations or tests.

## What has been checked

- The supplied CSV contains 11,720 interval rows.
- An exact-rational structural check reports that their union covers
  \([11,1737]\).
- The supplied sweep was previously reproduced in the environment recorded in
  `docs/REPRODUCTION_LOG.txt`.
- Selected prime-side and zero-side numerical evaluations were reported to
  agree closely.

These checks do **not** independently prove every lower bound in the CSV.

## What has not been established

- The implementation bounds have not received independent expert validation.
- The claimed infinite-tail theorem is not included as executable proof.
- Positivity for this single Gaussian family would not establish the universal
  Weil criterion and therefore would not prove RH.
- Statements that infer unconditional positivity from the zero-side Gaussian
  sum are circular unless RH is assumed.

See [docs/AUDIT_PLAN.md](docs/AUDIT_PLAN.md) for the verification roadmap and
[docs/RH_Weil_Gaussian_Handoff.md](docs/RH_Weil_Gaussian_Handoff.md) for the
full handoff memorandum.

## Repository layout

```text
data/     supplied certificate data
docs/     handoff, reproduction record, and audit notes
src/      supplied certificate generator
tools/    independent structural verifier
```

## Run the structural verifier

```bash
python tools/verify_certificate_csv.py data/certificates.csv
```

The verifier checks parsing, interval widths, nonnegative reported margins,
and exact rational coverage. It deliberately does not certify the underlying
mathematical lower bounds.

## Collaboration rules

1. Keep claims proportional to evidence.
2. Label assumptions and distinguish numerical evidence from proof.
3. Provide reproducible commands and software versions.
4. Use branches and pull requests for proposed changes.
5. Do not describe this repository as an RH proof.

