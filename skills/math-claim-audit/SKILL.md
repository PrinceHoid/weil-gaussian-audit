---
name: math-claim-audit
description: Audit one precise mathematical claim without rereading the entire repository or extending the research program.
---

# Mathematical claim audit

Use this skill when an issue asks whether a lemma, derivation, computation, or
claimed implication is correct.

## Required inputs

Read only:

1. `AGENTS.md`;
2. `docs/CURRENT_STATE.md`;
3. the assigned issue;
4. files listed in the issue's **Inputs** section.

Do not open other routes or historical PR discussions merely for background.

## Workflow

### 1. Freeze the claim

Rewrite the target as one precise sentence. Define every symbol. State whether
success would prove RH, disprove RH, remove an approach, or establish only an
intermediate result.

### 2. Build the dependency chain

List the argument in order. Label every dependency as:

- established theorem;
- exact algebra;
- rigorous computation;
- numerical evidence;
- unverified assumption;
- candidate new result;
- heuristic.

### 3. Stop at the earliest unsupported step

Identify the first line that is not already justified. Do not spend context on
later conclusions until this step survives review.

### 4. Attack the step

Check, as applicable:

- missing hypotheses;
- sign or normalization errors;
- illegal limit or interchange operations;
- finite-to-infinite leaps;
- circular use of RH;
- a restricted family replacing a universal class;
- numerical evidence presented as proof;
- dependence on an unverified external theorem;
- a known result presented as novel.

Use `references/common-failure-modes.md` only when a detailed checklist is
needed.

### 5. Verify narrowly

Recompute only the equations necessary for the earliest unsupported step. Run
only the smallest relevant script or test. Do not regenerate full datasets unless
the issue explicitly requires it.

### 6. Return a verdict

Use `references/verdict-template.md`. Choose one verdict:

- proved from stated assumptions;
- conditionally valid;
- numerically supported but unproved;
- incomplete;
- contradicted;
- already known;
- unclear because definitions are missing.

### 7. Leave a handoff

Post no more than 250 words to the assigned issue with the exact claim, inspected
files and commit range, earliest unsupported step, verdict, evidence, and one
next action.

## Prohibited behavior

- Do not propose a stronger theorem unless explicitly asked.
- Do not create a new route.
- Do not review the entire repository.
- Do not treat AI agreement, passing CI, or successful execution as proof.
- Do not conceal a failed claim by replacing it with a nearby true statement.
