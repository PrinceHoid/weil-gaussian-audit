# Plain-language guide to this research

This page explains the project for readers without a technical mathematics background. The technical route documents remain authoritative when precision matters.

## What question is the project studying?

The project studies the **Riemann Hypothesis (RH)**, one of mathematics' most famous unsolved problems.

Very roughly, RH says that certain special points called the non-trivial zeros of the Riemann zeta function all lie exactly on one vertical line in the complex plane.

No file in this repository proves or disproves RH.

## A useful analogy

One established reformulation of RH, called **Weil's positivity criterion**, resembles an enormous safety inspection:

> Every test in a very large collection must pass a positivity check.

The difficulty is the word **every**. Testing many examples—even millions of them—does not prove that all possible tests pass.

This repository began by examining one convenient family of bell-shaped tests called Gaussians. The later research asked whether success on that family could somehow cover the full safety inspection.

## Route 001: the original Gaussian computation

The original work evaluated thousands of shifted bell curves. It produced positive numerical results over a finite interval and a dataset containing 11,720 certificate rows.

That work is useful as a reproducible computational experiment, but it does not prove RH because:

- it covers only a finite range;
- some numerical error bounds still require independent formal verification;
- it tests only one narrow family of shapes;
- Weil's criterion requires every admissible test.

**Analogy:** We tested thousands of examples of one model of lock. RH requires proving that every permitted lock design can never fail.

**Current status:** explored computational route; no known bridge to RH.

Technical details: [`RH_Weil_Gaussian_Handoff.md`](RH_Weil_Gaussian_Handoff.md).

## Route 002: why the original bell curves are too limited

We investigated whether positive mixtures of the original bell curves could generate all the other shapes needed by Weil's criterion.

They cannot.

The exact proof shows that positive mixtures of the fixed-width curves can make broader, flatter Gaussians, but cannot make narrower, more concentrated ones. A strengthened version gives a general limit on how sharply any generated shape can concentrate at any location.

**Analogy:** Combining broad paintbrush strokes can create other broad patterns, but it cannot produce an arbitrarily fine pencil line.

This result does not say RH is false. It says one natural argument for promoting Route 001 to the full Weil criterion cannot work.

**Current status:** candidate exact audit result awaiting independent human review.

Technical details: [`ROUTE_002_GAUSSIAN_CONE_OBSTRUCTION.md`](ROUTE_002_GAUSSIAN_CONE_OBSTRUCTION.md).

## Route 003: can we replace “every test” with a numbered list?

We next considered replacing the huge collection by an explicit list:

```text
test 1, test 2, test 3, ...
```

Under standard continuity assumptions, such a determining list can be constructed. If every item on a sufficiently dense infinite list passed, every admissible test would pass.

But this does not solve the problem. The list is still infinite, and proving that every item passes is essentially RH again.

Mathematicians already knew this idea. Li's 1997 criterion expresses RH as the positivity of an explicit infinite sequence, and later work connects it to Weil's criterion.

**Analogy:** We replaced “inspect every point on an endless road” with “inspect mile marker 1, mile marker 2, mile marker 3, and so on forever.” The instructions are clearer, but the road remains endless.

Published research also explains why checking only the first finitely many items provides only finite zero-free information, not RH.

**Current status:** rejected as a new research route because the structural reduction is already known and does not weaken the problem.

Technical details: [`ROUTE_003_COUNTABLE_DETERMINING_FAMILIES.md`](ROUTE_003_COUNTABLE_DETERMINING_FAMILIES.md).

## What did the project actually accomplish?

The project has not moved close to proving or disproving RH. It has nevertheless produced useful research outcomes:

- It prevented a finite computation from being mistaken for an infinite proof.
- It documented which parts of the original calculation are reproduced and which remain unaudited.
- It proved an exact limitation of the fixed-width Gaussian mixing strategy.
- It found a broader candidate concentration bound for that Gaussian cone.
- It independently rechecked the central Route 002 calculation.
- It identified that the countable-family proposal was already known.
- It recorded these dead ends so humans and AI systems do not repeat them.
- It isolated one bounded mathematical obligation that should be completed next.

Finding that a plausible route does not work is legitimate progress when the failure is proved precisely and preserved for later researchers.

## What must happen next?

Before doing another large numerical computation, the repository must settle its **admissibility and convention problem**.

In plain language, the project currently moves between different mathematical languages for describing Weil's tests. The next task is to choose one exact version and prove that the Gaussian tests really satisfy all of its rules.

That task should specify:

- the exact class of permitted test functions;
- the Fourier and Mellin transform conventions;
- the convolution and symmetry operations;
- every pole-cancellation or vanishing-moment condition;
- the exact formula connecting the repository's Gaussian to Weil's criterion.

Until this is done, expanding to more translations or more Gaussian widths risks computing quantities whose logical relationship to RH has not been fully established.

## The strategic decision after admissibility

Once admissibility is settled, humans should explicitly choose between two goals.

### Option A: finish a computational note

Audit Route 001's numerical bounds using mature ball arithmetic, provide a separate verifier, and publish a careful result about this restricted Gaussian family.

This could be worthwhile computational mathematics, but it should not be presented as a path that currently approaches RH.

### Option B: begin a genuinely different RH route

Freeze Routes 001–003 as explored or rejected and require any new route to identify a new mathematical mechanism—not another reformulation, larger grid, or finite verification.

Every proposed route should state:

1. the exact claim;
2. the proved connection to RH;
3. the closest primary literature;
4. the genuinely new step;
5. the first unproved lemma;
6. the quickest falsification test;
7. all assumptions and evidence levels.

## Guidance for AI collaborators

- Read `README.md`, `AGENTS.md`, `RESEARCH_MAP.md`, and `NEXT_STEPS.md` before working.
- Attack the earliest unproved step, not the most impressive conclusion.
- Label known theorems, exact proofs, rigorous computations, numerical evidence, heuristics, and speculation separately.
- Never turn a finite check into an infinite claim without a proved bridge.
- Never replace Weil's full test class with a restricted family without proving the implication.
- Check whether an apparent new equivalence is already known before developing it.
- Prefer early counterexamples and obstruction proofs to large computations.
- Preserve failed approaches and corrections.
- Never claim RH is solved without a complete proof, dependency audit, adversarial review, and qualified human verification.

## Guidance for human collaborators

- Have an analyst independently review the Route 002 separator and its strengthened concentration bound.
- Have an analytic number theorist freeze the exact Weil formulation and admissibility conditions.
- Decide explicitly whether Route 001 is a computational note or an active RH route.
- Require mature rigorous numerics and an independent verifier for computer-assisted claims.
- Reject new proposals based only on countability, density, reformulation, or larger finite computations.
- Treat a rigorously demonstrated dead end as useful progress.

## Bottom line

> We have not proved or disproved RH. We have learned, rigorously, why two plausible bridges do not solve the problem and what must be clarified before more computation is meaningful.

The immediate next step is a short, exact convention-and-admissibility memorandum—not another large numerical sweep.
