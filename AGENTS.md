# AGENTS.md

## Mission

Audit a restricted Gaussian Weil-positivity computation carefully and
reproducibly. The repository is exploratory work, not a proof of the Riemann
Hypothesis.

## Mandatory starting point

Read these files before proposing research changes:

1. `README.md`
2. `NEXT_STEPS.md`
3. `docs/AUDIT_PLAN.md`
4. `docs/RH_Weil_Gaussian_Handoff.md`

Then work on the first incomplete stage in `NEXT_STEPS.md`. The immediate
priority is the line-by-line mathematical derivation of Q(t), not a larger
numerical sweep.

## Rules for AI assistants

- Never describe this project as a proof or near-proof of RH.
- Distinguish established literature, reproduced computation, candidate claims,
  and unestablished statements.
- Do not treat the zero-side Gaussian terms as unconditionally nonnegative;
  zero ordinates are real only under RH.
- Do not imply that positivity for this one-parameter family proves Weil's
  criterion for every admissible test function.
- Do not call the CSV verifier an independent mathematical verifier. It checks
  structure and exact coverage only.
- State every Fourier convention, domain restriction, assumption, and error
  bound explicitly.
- Prefer primary mathematical sources and official software documentation.
- Preserve the original supplied artifacts; add corrections separately.
- Record commands, dependency versions, hashes, and reproducible outputs.
- Treat a counterexample or discovered flaw as a successful research result.
- Use a focused branch and pull request for each substantial change.

## Definition of useful progress

Useful progress means one of the following:

- a derivation step has been independently justified;
- a numerical bound has been rigorously proved;
- a claim has been falsified or narrowed;
- an independent implementation has reproduced a result;
- an unresolved proof obligation has been made more precise;
- an expert review has been recorded and addressed.

Generating more persuasive prose or testing more t-values without resolving a
listed proof obligation is not useful progress.
