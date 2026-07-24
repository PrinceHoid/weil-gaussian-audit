# AGENTS.md

## Primary objective

Investigate the question:

> Does every non-trivial zero of the Riemann zeta function satisfy
> Re(rho) = 1/2?

A valid proof or counterexample is the ultimate objective. The repository does
not currently contain either.

## Required startup reading

Read, in order:

1. `README.md`
2. `RESEARCH_MAP.md`
3. `NEXT_STEPS.md`

Read route-specific documents only after selecting a route.

## Before working on an approach

State:

- the exact target claim;
- the proved logical connection from that claim to RH;
- the closest known literature;
- the first genuinely new and unproved step;
- an early falsification test;
- every assumption;
- the evidence level.

If these cannot be stated, do not launch a large derivation or computation.

## Non-negotiable rules

- Do not present a known equivalence or reformulation as progress by itself.
- Do not infer an infinite statement from finite verification without a proved
  bridge.
- Do not substitute one test family for a universal quantifier.
- Do not use RH, explicitly or implicitly, inside a purported proof of RH.
- Do not treat agreement among AI systems as mathematical verification.
- Do not conceal failed approaches or corrections.
- Preserve original artifacts and add critiques separately.
- Cite primary sources for material theorem dependencies.
- Label proof, rigorous computation, numerical evidence, heuristic, and
  speculation distinctly.
- Use a focused branch or pull request for each route.

## How to collaborate

- One AI proposes a precise lemma.
- Another independently tries to disprove it.
- Another checks its literature and dependencies.
- Another reproduces any computation independently.
- Summarize disagreements rather than forcing consensus.

## Current warning

The Gaussian/Guinand–Weil computation is one explored route. Its finite
certificate is not a proof of RH and is not the repository's overall research
program. Do not continue extending its numerical range unless a precise
argument explains how doing so could bridge to the full RH claim.

## Definition of progress

Useful progress includes:

- a new lemma with a correct proof and a demonstrated implication toward RH;
- a counterexample that eliminates a proposed route;
- a hidden assumption or circular step identified;
- a known obstruction made precise;
- an independent rigorous reproduction;
- a genuinely new intermediate theorem confirmed by expert review.

More algebra, citations, code, or numerical data are not progress unless they
resolve a stated obstacle.
