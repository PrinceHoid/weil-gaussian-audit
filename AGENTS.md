# Agent instructions

## Start here — do not audit the whole repository

Read only:

1. `docs/CURRENT_STATE.md`;
2. the assigned GitHub issue;
3. files explicitly listed under that issue's **Inputs** section.

Do not automatically inspect every open pull request, route document, commit,
certificate CSV, or generated artifact. Fetch PR #6 or PR #7 only when the
assigned issue specifically requires it.

The reviewed baseline is recorded in `docs/CURRENT_STATE.md`. Prefer the relevant
diff after that baseline. Read older history only to check a specifically named
claim.

## One task means one claim

Before doing work, state:

- the exact claim being checked;
- why it matters to RH;
- the first unproved step;
- the files and commit range you will inspect;
- the fastest plausible failure test.

Do not create a new route, stronger theorem, large derivation, or large
computation unless the issue explicitly authorizes it.

## Mathematical guardrails

- This repository does not currently prove or disprove RH.
- Never infer an infinite statement from finite verification without a proved
  bridge.
- Never substitute a restricted test family for a universal criterion.
- Never use RH, explicitly or implicitly, inside a purported proof of RH.
- Successful code, CI, mergeability, and agreement among AI systems are not
  mathematical verification.
- Do not present a known equivalence or reformulation as a new result.
- Preserve failed routes, corrections, and counterexamples.
- Cite primary sources for material theorem dependencies.

Label important statements as established theorem, exact algebra, rigorous
computation, numerical evidence, unverified assumption, candidate result,
heuristic, contradicted, or rejected.

## Current route controls

The short status is maintained in `docs/CURRENT_STATE.md`.

- Route 001: explored finite computation; fixed-scale sweeps are halted.
- Route 002: candidate obstruction; default audit target.
- Route 003: rejected.
- Route 004: spectral convergence, reserved by PR #6.
- Route 005: all-scale Gaussian candidate material in PR #7.
- Route 006: de Bruijn–Newman.
- Route 007: Nyman–Beurling / Báez–Duarte.
- Route 008: Robin / Lagarias.

Never recycle route numbers. Do not merge PR #7 wholesale.

## Collaboration roles

Keep invention and verification separate:

- one agent may propose or reconstruct a precise lemma;
- another independently attempts to disprove it;
- another checks literature and dependencies;
- another reproduces computation when required.

Do not make every agent repeat every role on the entire repository.

## Completion handoff

Add a handoff of no more than 250 words to the assigned issue:

- exact claim examined;
- files and commit range examined;
- earliest unsupported step;
- verdict;
- evidence produced;
- one next action.

Update `docs/CURRENT_STATE.md` only when repository-level status changes.
