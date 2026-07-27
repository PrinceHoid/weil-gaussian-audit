# AGENTS.md

## Primary objective

Investigate:

> Does every non-trivial zero of the Riemann zeta function satisfy
> `Re(rho) = 1/2`?

A valid proof or counterexample is the ultimate objective. The repository
contains neither.

## Required startup reading

Read, in order:

1. `README.md`
2. `RESEARCH_MAP.md`
3. `NEXT_STEPS.md`
4. the documents for the selected route

Use `docs/PLAIN_LANGUAGE_GUIDE.md` for orientation, but use the technical route
documents and primary sources when precision matters.

## Before working on an approach

State:

- the exact target claim;
- the proved logical connection from that claim to RH;
- the closest known literature;
- what is genuinely new;
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
- Do not conceal failed approaches, negative experiments, or corrections.
- Preserve original artifacts and add critiques separately.
- Cite primary sources for load-bearing theorem dependencies.
- Label known theorem, exact proof, rigorous computation, floating-point
  evidence, heuristic, and speculation distinctly.
- Use a focused branch or pull request for each route.

## Active frontier: Route 004

Route 004 asks whether localized Weil ground-state transforms converge to
Riemann's completed `Xi` function. It has not proved RH.

The repository has a conditional transfer lemma. If, along an unbounded cutoff
sequence:

1. the true continuum lowest eigenvalue is simple and its ground state is even;
2. after scalar alignment,

   ```text
   ||b_lambda theta_lambda-k_lambda||_2 = O(lambda^(-1/2));
   ```

3. the published proxy-transform convergence theorem for `k_lambda` applies;

then the true transforms converge locally uniformly on
`|Im z|<1/2`, and Hurwitz's theorem implies RH.

Items 1 and 2 are open. Treat the displayed rate as a clean **sufficient**
target, not a necessary condition and not an established estimate.

## Route 004 guardrails

Identify the exact family before writing a theorem or running code:

1. the continuum localized Weil operator `A_lambda`;
2. the finite Galerkin form `Q_(c,N,T)`;
3. the prolate comparison family `k_lambda`;
4. Suzuki's distinct self-adjoint-extension family.

Record the Hilbert space, transform convention, centering or retained
zero-free phase, scalar normalization, parameter relation
`c=lambda^2`, theorem hypotheses, and order of limits. The support cutoff `c`
controls primes `p<=c`; `c` need not itself be prime.

For this route:

- Do not state that the continuum ground-state transform is real-rooted for
  large `lambda` unless simplicity, isolation, and evenness have been proved
  for the cutoffs in question.
- Do not treat a finite `(c,N,T)` computation as a continuum statement.
- Refine `N`, archimedean treatment, precision, `c`, and spectral-branch
  selection independently.
- Do not infer convergence from agreement with finitely many real zeros. The
  bridge needs locally uniform complex convergence on each closed substrip of
  `|Im z|<1/2`, or another theorem capturing every `Xi` zero.
- Call `hat(k_lambda) -> Xi` the published **proxy-transform** convergence
  theorem. It does not establish convergence of the actual Weil ground state.
- A small Rayleigh quotient, tiny eigenvalue, large overlap, or visually stable
  eigenvector does not prove ground-state proximity. Require a direct norm
  estimate or certified spectral projection/residual and separation.
- Do not assume positivity of every localized Weil form; global localized Weil
  positivity is RH-equivalent and would make the argument circular.
- Finite data cannot disprove an asymptotic big-O claim. Rejecting the rate
  requires an analytic lower bound or a certified unbounded subsequence.
- Failure of this comparison rate rejects this sufficient transfer mechanism,
  not RH and not every spectral route.

## Numerical work requirements

Before a large run, preregister:

- the claim being tested;
- cutoff values;
- Galerkin dimensions;
- archimedean treatment;
- working precision;
- normalization and branch-selection rule;
- evaluation points and norms;
- pass/fail thresholds.

Any rigorous numerical claim must include certified tail and discretization
bounds, raw artifacts or hashes, a reproducible environment, and an independent
verifier. Root-finder output and agreement across two cutoffs remain numerical
evidence until validated.

## How to collaborate

- One collaborator proposes a precise lemma.
- Another independently tries to disprove it.
- Another checks its literature and dependencies.
- Another reproduces any computation independently.
- Summarize disagreements rather than forcing consensus.

## Legacy-route warnings

- Route 001's finite Gaussian certificate is not a proof of RH. Do not extend
  its grid without a theorem bridging its restricted family to the full
  criterion.
- Route 002 blocks one fixed-scale positive-cone bridge; it says nothing for or
  against RH.
- Route 003 shows that countability merely re-indexes the infinite burden.
  Reopen it only with a genuinely new tail-propagation mechanism.

## Definition of progress

Useful progress includes:

- a new lemma with a correct proof and a demonstrated implication toward RH;
- a counterexample eliminating a proposed route;
- a hidden assumption or circular step identified;
- a known obstruction made precise;
- an independent rigorous reproduction;
- a finite experiment that cleanly falsifies a preregistered model;
- a genuinely new intermediate theorem confirmed by expert review.

More algebra, citations, code, or numerical data are not progress unless they
resolve a stated obstacle.
