# Plain-language guide to this research

This page explains the project without assuming a technical mathematics
background. The technical route documents are authoritative when precision
matters.

## What question are we studying?

The project studies the **Riemann Hypothesis (RH)**, one of mathematics' most
famous unsolved problems.

Very roughly, a mathematical object called the Riemann zeta function has
special points called non-trivial zeros. RH says that every one of those points
lies exactly on one vertical line in the complex plane.

No file or computation in this repository proves or disproves RH.

## Why is this so difficult?

Some statements equivalent to RH look like enormous safety inspections:

> Every test in a very large collection must pass.

The difficult word is **every**. Testing a thousand, a million, or any other
finite number of examples does not prove that all possible tests pass. An
infinite argument needs a theorem explaining why the finite work covers every
remaining case.

That missing theorem is called a **bridge** throughout this repository.

## Route 001: the original Gaussian computation

The project began by evaluating thousands of shifted bell-shaped tests called
Gaussians. It produced a reproducible data set with 11,720 certificate rows and
positive numerical results over a finite interval.

That is useful as a computational experiment, but it does not prove RH because:

- it covers only a finite range;
- some numerical error bounds still require independent formal verification;
- it tests only one narrow family of shapes;
- the relevant full criterion requires every permitted test.

**Analogy:** We tested thousands of examples of one model of lock. RH requires
proving that every permitted lock design can never fail.

**Status:** explored computational route; no known bridge to RH.

Technical details:
[`RH_Weil_Gaussian_Handoff.md`](RH_Weil_Gaussian_Handoff.md).

## Route 002: why those bell curves are too limited

We asked whether positive mixtures of the original bell curves could generate
all the other shapes needed by the full criterion.

They cannot.

The exact argument shows that positive mixtures of those fixed-width curves can
make broader, flatter Gaussians, but cannot make arbitrarily narrow,
concentrated ones.

**Analogy:** Combining broad paintbrush strokes can create other broad
patterns, but it cannot produce an arbitrarily fine pencil line.

This does not say RH is false. It rules out one proposed way of promoting
Route 001 to the full criterion.

**Status:** candidate exact obstruction awaiting independent expert review.

Technical details:
[`ROUTE_002_GAUSSIAN_CONE_OBSTRUCTION.md`](ROUTE_002_GAUSSIAN_CONE_OBSTRUCTION.md).

## Route 003: can “every test” become a numbered list?

We next considered replacing the huge collection of tests by an explicit list:

```text
test 1, test 2, test 3, ...
```

Under standard mathematical assumptions, a sufficiently dense infinite list
can determine the answer. But this does not solve the problem. The list is
still infinite, and proving that every item passes is essentially RH again.

Mathematicians already knew versions of this idea. Li's criterion, for example,
expresses RH as positivity of an explicit infinite sequence.

**Analogy:** We replaced “inspect every point on an endless road” with “inspect
mile marker 1, mile marker 2, mile marker 3, and so on forever.” The
instructions are clearer, but the road remains endless.

**Status:** rejected as a new route because the reduction is known and does not
weaken the infinite problem.

Technical details:
[`ROUTE_003_COUNTABLE_DETERMINING_FAMILIES.md`](ROUTE_003_COUNTABLE_DETERMINING_FAMILIES.md).

## Route 004: can finite spectral models converge to zeta?

Route 004 studies a newer idea with a genuine **conditional** path to RH.

For each cutoff, mathematicians build a localized spectral problem. Under
specific assumptions about its lowest-energy state, the associated transform
has zeros only in the desired place. Finite computations show that many such
zeros are extremely close to known zeta zeros.

That is encouraging, but it is not the missing proof.

**Analogy:** Imagine making increasingly detailed maps. Every pin on every
finite map lies on one straight road, and the pins appear close to real cities.
We must still prove that the maps converge to the actual landscape, that every
city is represented, and that nothing is lost between the finite maps and the
limit.

### The proposed bridge

A published helper object, called the **prolate proxy** and written
`k_lambda`, already has a transform known to approach Riemann's completed zeta
function `Xi` in the part of the complex plane where an RH counterexample could
occur.

The true lowest-energy state of the localized Weil problem, written
`theta_lambda`, is not yet proved to stay sufficiently close to that proxy.

After allowing a harmless rescaling, define their best distance as

```text
E_lambda = inf_b ||b theta_lambda-k_lambda||_2.
```

A clean sufficient target is

```text
E_lambda <= C / sqrt(lambda)
```

for one constant `C` at all sufficiently large selected cutoffs. In plain
language, the true state must approach the proxy at least as fast as the
inverse square root of the cutoff.

If this estimate is proved, and if the true lowest state is also proved to stay
unique and symmetric along an unbounded sequence of cutoffs, then standard
complex-analysis theorems transfer the real-zero property to `Xi`. That would
imply RH.

Those are two independent missing hypotheses. Neither has been proved here.
The rate is a sufficient target, not the only imaginable route.

### Why correct finite zeros are not enough

This project built an exact warning example. In that example:

- the finite operator is positive;
- its lowest state is unique and symmetric;
- the gap above that state stays stable;
- every finite transform has only real zeros.

Despite all of this, the transforms blow up away from the real line and do not
converge as the interval grows.

**Analogy:** Every photograph can show its markers on the correct road while
the camera's scale and distortion become uncontrollable. Correct-looking
markers in each photograph do not prove that the photographs converge to one
real map.

This counterexample does not refute the zeta construction and says nothing
against RH. It proves that convergence cannot be obtained from the generic
finite properties alone. A zeta-specific comparison or localization theorem is
indispensable.

### What the first computation says

An exploratory test evaluated a centered transform away from the real axis at
`c=13`. As the finite matrix dimension increased from `N=8` to `N=20`, its
error against the corresponding `Xi` value decreased from about `0.002` to
about `0.000068`.

That is relevant evidence because it probes complex behavior instead of merely
matching a finite list of real zeros. It is still one finite support cutoff
with finite matrix and archimedean approximations. It proves no limit.

A false negative eigenvalue appeared with an archimedean cutoff `T=40` and
disappeared at `T=80` and `T=160`. This is a useful warning: a stable-looking
answer can still be an artifact of one numerical cutoff.

**Status:** active route with a conditional bridge, an exact obstruction to an
insufficient shortcut, and preliminary numerical evidence. RH remains
unsolved.

Technical details:

- [`ROUTE_004_SPECTRAL_CONVERGENCE.md`](ROUTE_004_SPECTRAL_CONVERGENCE.md)
- [`ROUTE_004_CRITICAL_STRIP_BRIDGE.md`](ROUTE_004_CRITICAL_STRIP_BRIDGE.md)

## What did the project actually accomplish?

The project has not proved or disproved RH. It has nevertheless produced
concrete research outcomes:

- It stopped a finite computation from being mistaken for an infinite proof.
- It documented what the original Gaussian work does and does not establish.
- It proved an exact limitation of the fixed-width Gaussian mixing strategy.
- It identified the countable-family proposal as known and insufficient.
- It isolated a precise Route 004 bridge that would imply RH if its hypotheses
  were proved.
- It reduced one clean comparison target to
  `E_lambda=O(lambda^(-1/2))`.
- It proved by counterexample that real finite zeros, positivity, uniqueness,
  and a stable spectral gap do not imply convergence.
- It showed that only the strip `|Im z|<1/2` must be controlled, rather than
  the whole complex plane.
- It designed off-axis falsification tests and recorded preliminary finite
  evidence.
- It preserved failed ideas and corrections so humans and AI systems do not
  repeat them.

Finding a precise bridge and identifying exactly what does **not** establish
that bridge is legitimate progress. The remaining step is still very hard, but
it is now a named estimate that can be attacked or falsified.

## What must happen next?

The main task is no longer “compute more real zeros.” It is to compare the true
continuum state with the prolate proxy.

The next work should:

1. independently verify the critical-strip transfer lemma and the cited proxy
   convergence theorem;
2. freeze the exact continuum operator, centering, normalization, and
   definition of `k_lambda`;
3. prove that the continuum lowest state is unique and symmetric along an
   unbounded sequence of cutoffs;
4. build independently checked, high-precision calculations of `E_lambda`;
5. refine matrix dimension, archimedean treatment, precision, support cutoff,
   and spectral branch independently;
6. test whether `sqrt(lambda) E_lambda` remains bounded;
7. seek an analytic proof from the zeta-specific trace formula without
   assuming global Weil positivity, which would be circular;
8. continue centered tests at complex points with `|Im z|<1/2`.

A worsening finite trend can expose instability or reject a declared numerical
model, but it cannot disprove an asymptotic rate by itself. Rigorously rejecting
the clean rate requires an analytic lower bound or a certified unbounded
subsequence.

If that rate fails, this sufficient mechanism fails—not RH and not every
possible spectral approach.

If the comparison estimate, the continuum ground-state hypotheses, and the
published proxy convergence are all proved and independently checked, the
Route 004 bridge would imply RH. That is why these obligations deserve effort
instead of a larger table of matching zeros.

Route 001's separate convention-and-admissibility audit remains necessary if
the Gaussian computation is developed into a rigorous computational note.

## Guidance for AI collaborators

- Read `README.md`, `AGENTS.md`, `RESEARCH_MAP.md`, and `NEXT_STEPS.md` first.
- Attack the earliest unproved step, not the most impressive conclusion.
- Separate the continuum operator, finite Galerkin matrices, the prolate proxy,
  and Suzuki's different family.
- Label known theorems, exact proofs, rigorous computations, numerical
  evidence, heuristics, and speculation.
- Never turn a finite check into an infinite claim without a proved bridge.
- Prefer early counterexamples and obstruction proofs to large computations.
- Preserve failures and normalization corrections.
- Never claim RH is solved without a complete proof, dependency audit,
  adversarial review, and qualified human verification.

## Guidance for human collaborators

- Have an analytic number theorist audit the exact Weil form and the implication
  to RH.
- Have a functional analyst audit domains, parity, simplicity, and spectral
  estimates.
- Have a special-functions expert audit the prolate construction.
- Have a complex analyst audit the convergence and Hurwitz step.
- Have a rigorous-numerics specialist design certified tail, discretization,
  eigenvalue, and eigenvector bounds.
- Assign an independent reviewer to try to break the comparison and
  localization arguments.

The first valuable human verdict is whether this comparison-and-localization
program is mathematically viable, not whether RH is already proved.

## Bottom line

> We have not proved or disproved RH. Route 004 gives a precise conditional
> bridge: the finite or localized transforms have real zeros under stated
> hypotheses, and a published proxy approaches `Xi`, but we must prove that
> the true continuum ground state approaches that proxy fast enough and
> remains unique and symmetric.

An exact counterexample proves that the finite real-zero property and a stable
ground state do not make convergence automatic. The immediate job is to audit,
measure, try to falsify, and ultimately prove the two missing hypotheses.
