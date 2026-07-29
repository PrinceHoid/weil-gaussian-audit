# Common failure modes

Use only the sections relevant to the assigned claim.

## Logic and scope

- The conclusion is stronger than the proved premises.
- A sufficient condition is presented as necessary, or the reverse.
- A conditional statement silently becomes unconditional.
- A reformulation of RH is described as progress toward proving RH.
- The argument assumes the conclusion in a disguised equivalent form.

## Finite versus infinite

- A finite range is extrapolated to all inputs.
- A finite matrix is treated as the limiting operator without a convergence
  theorem.
- Numerical stability is treated as analytic convergence.
- A finite collection of inequalities is treated as the infinite family.
- Tail bounds are missing, nonuniform, or depend on the point being certified.

## Function classes

- Positivity on one family is substituted for positivity on an admissible class.
- Density uses signed coefficients while the argument requires positive
  coefficients.
- Closure is invoked without naming the topology.
- Continuity of the separating functional is not proved in that topology.
- Fourier or Mellin conventions change without updating constants and signs.

## Analysis

- Sum, integral, derivative, expectation, or limit operations are interchanged
  without domination or uniform convergence.
- Boundary or pole terms are omitted.
- A branch choice is inconsistent.
- A theorem is applied outside its domain.
- Big-O constants depend on a variable that must be uniform.

## Computation

- Floating-point output is called rigorous without interval or ball bounds.
- The verifier checks file structure but not the mathematical quantity.
- The generator and verifier share the same bug or implementation.
- Precision conversion narrows an interval.
- A remainder bound omits a first term, endpoint, or rounding allowance.
- Successful CI checks parsing or execution rather than the claimed theorem.

## Novelty

- The closest known theorem was not identified.
- A standard criterion is renamed.
- The new result follows immediately from a cited theorem but is called novel.
- Literature searches rely on summaries rather than primary sources.
