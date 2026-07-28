# AGENTS.md

> [!CAUTION]
> # STOP — MANDATORY PR #6/#7 HANDOFF
>
> **DO NOT begin route work, reuse a route number, or merge PR #7 until you complete this handoff. Status last checked 2026-07-27; fetch the live PR state before acting.**
>
> 1. **Inspect and adversarially audit [PR #6](https://github.com/PrinceHoid/weil-gaussian-audit/pull/6).** It reserves **Route 004** for spectral convergence. Its transfer lemma and supporting arguments are candidate results pending independent mathematical review; they do not prove RH. Preserve the Route 004 identifier even if that route is later rejected—record the disposition instead of recycling the number.
> 2. **Do not merge [PR #7](https://github.com/PrinceHoid/weil-gaussian-audit/pull/7) wholesale in its current form.** It was prepared from the old `main`, did not audit PR #6, and independently reused Route 004. Separate its Routes 001/002 reproduction audit, candidate Route 001 tail work, and future-route proposals before integration.
> 3. **HALT fixed-scale Route 001 sweeps at `t = 1737`; keep PR #7's tail theorem labelled `candidate`.** Do not extend or regenerate the `[1737, 2000]` sweep as research progress; retain it only as flawed historical audit material. Before any promotion of the separate analytic tail claim, repair and independently verify all of the following: interval endpoints in `tools/tail_certificate.py` are routed through ordinary default-precision `mp.mpf`, which can narrow an enclosure; `src/sweep_extension_1737_2000.py` underestimates a decreasing-series tail; the CSV verifier trusts reported margins rather than recomputing the mathematics and must reject non-finite values; and the inherited cosine-reduction, summation-pad, Binet-remainder, and curvature-bound obligations remain unresolved. Recompute with a publication-grade interval/ball system such as Arb/FLINT and an independent verifier.
> 4. **Do not import PR #7's proposed route numbers unchanged.** If the proposals survive review, use **Route 005 — all-scale Gaussian**, **Route 006 — de Bruijn–Newman**, **Route 007 — Nyman–Beurling/Báez–Duarte**, and **Route 008 — Robin/Lagarias**.
> 5. **Correct factual and scope claims before integration.** The published unconditional de Bruijn–Newman bound is already [`Λ <= 0.20`](https://arxiv.org/abs/2004.09765), and PR #7's categorical dismissal of spectral/Connes approaches is unsupported.
>
> **Mechanical GitHub mergeability, successful CI, or agreement among AI systems is not mathematical acceptance. Nothing in PR #6 or PR #7 currently proves or disproves RH.**

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
