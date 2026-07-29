---
name: Bounded research task
about: Assign one mathematical claim without requiring a repository-wide review
title: "Audit: "
labels: []
assignees: []
---

## Exact claim

State one sentence to prove, disprove, reproduce, or explain.

## Why it matters

State the exact implication for RH or for an existing route.

## Task type

Choose one:

- [ ] explanation
- [ ] proof audit
- [ ] counterexample search
- [ ] literature/dependency check
- [ ] computation reproduction

## Inputs

List every file, PR, issue, commit, theorem, or script the agent may inspect.
Anything not listed is out of scope unless the task cannot be completed without
it.

- `docs/CURRENT_STATE.md`
- 

## Reviewed baseline

Copy the baseline from `docs/CURRENT_STATE.md` or name a narrower commit range.

## First suspected unsupported step

Name it when known. Otherwise ask the agent to identify it and stop there.

## Allowed work

State any equations to recompute or commands to run.

## Forbidden work

- no new route;
- no stronger theorem;
- no large computation;
- no whole-repository review;
- no unrelated PR review.

## Completion requirement

Use the handoff format in `AGENTS.md` and keep it under 250 words.
