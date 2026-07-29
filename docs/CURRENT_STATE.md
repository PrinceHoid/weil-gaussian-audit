# Current project state

**Last reviewed:** 2026-07-29  
**Reviewed main baseline:** `c518749a7827e05ea5565056d71c29b4d9d2c9ae`

This file is the short, authoritative orientation document for humans and AI
agents. Read it before opening historical pull requests or route documents.

## Bottom line

The repository does **not** prove or disprove the Riemann Hypothesis. No claim
from open PR #6 or PR #7 is mathematically accepted merely because it is
written, reproducible, mergeable, or supported by multiple AI systems.

## Accepted repository-level conclusions

- **Route 001 — restricted Gaussian / Guinand–Weil positivity:** explored.
  The committed data record a finite computation, not RH and not full Weil
  positivity. Do not extend the fixed-scale sweep as research progress.
- **Route 002 — fixed-scale Gaussian positive-cone obstruction:** candidate
  result. The separating-functional argument is short and promising, but still
  needs independent review of its topology and conventions.
- **Route 003 — countable determining families:** rejected as a research route.
  Countability re-indexes the infinite burden and does not weaken RH.

## Open pull requests

- **PR #6:** reserves **Route 004 — spectral convergence**. It contains a
  conditional research program and candidate lemmas, not a proof of RH.
- **PR #7:** contains independent audit material, repaired candidate numerical
  work, and **Route 005 — all-scale Gaussian** proposals. Do not merge it
  wholesale. Its layers must be split and reviewed independently.

PR metadata may change. Fetch a live PR only when the assigned task explicitly
requires that PR.

## Preserved route numbering

- Route 004 — spectral convergence
- Route 005 — all-scale Gaussian
- Route 006 — de Bruijn–Newman
- Route 007 — Nyman–Beurling / Báez–Duarte
- Route 008 — Robin / Lagarias

Never recycle a route number, even after rejection.

## Default work queue

Until a maintainer assigns otherwise:

1. Explain and audit Route 002 one lemma at a time.
2. Freeze Routes 004 and 005 against new extensions.
3. Do not launch new routes or large computations.
4. Prefer finding the earliest unsupported step over strengthening a conclusion.

## Context-budget protocol

For a normal task, read only:

1. `AGENTS.md`;
2. this file;
3. the assigned GitHub issue;
4. files explicitly listed under that issue's **Inputs** section.

Do **not** automatically read all route documents, PR discussions, certificate
CSVs, generated artifacts, or repository history.

This file summarizes repository state through the reviewed baseline above. For
new work, inspect only the assigned files and the relevant diff after that
baseline. Go further back only when the issue identifies an older claim that
must be checked.

## Evidence labels

Every output must label each important statement as one of:

- established theorem;
- exact algebra;
- rigorous computation;
- ordinary numerical evidence;
- unverified assumption;
- candidate result;
- heuristic or speculation;
- contradicted or rejected.

## Required task handoff

At the end of a task, add a handoff of no more than 250 words to the assigned
issue containing:

- exact claim examined;
- files and commit range examined;
- earliest unsupported step;
- verdict;
- evidence produced;
- single next action.

Update this file only when the repository-level status changes. Do not rewrite
project history into it after every small task.
