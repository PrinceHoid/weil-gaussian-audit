# The third moment does not improve 2/3 — a closed direction

**Date:** 11 August 2026. **Status:** candidate derivation plus a proved
no-go; machine-checked by `tools/third_moment_probe.py` (10 checks, all
pass). Human review required before any claim of novelty.

## The question

The external two-thirds theorem (`docs/EXTERNAL_2026-08-11_TWO_THIRDS.md`)
reads only the **first two moments** of the compressed Weil form `G̃`, and
its stated optimality is explicitly conditional on that:

> given only `tr G̃`, `‖G̃‖²_F` and the block structure, the inequalities of
> §3 are sharp

A third moment is therefore *strictly more information* and is **not**
excluded by that statement. In the previous commit this repository flagged
it as the one direction the paper's optimality leaves open, and proposed a
cheap falsification test. This document runs it. The answer is **no**, and
the reason is sharper than expected.

## Step 1 — the third moment, derived

Applying the paper's sampling identity (its Lemma 2.2) three times to
`tr G³ = Σ_{k,l,m} G_kl G_lm G_mk` collapses the three index sums into a
**triangle kernel**:

\[
\operatorname{tr}G^{3}=L^{3}\iiint
\Phi(\tau_1-\tau_2)\,\Phi(\tau_2-\tau_3)\,\Phi(\tau_1-\tau_3)\;
\nu(\tau_1)\nu(\tau_2)\nu(\tau_3)\,d\tau_1 d\tau_2 d\tau_3 .
\]

Two kernel identities carry the evaluation (both verified numerically,
check K, max deviation `8.0e−05`):

\[
\iint \Phi(u)\Phi(v)\Phi(u-v)\cos((u-v)y)\,du\,dv=(2\pi)^2\!\int \phi^4(s+y)\phi^2(s)\,ds,
\]
\[
\int \Phi(w)^2\cos(wy)\,dw=2\pi\,(\phi^2\!\star\!\phi^2)(y).
\]

Splitting `ν = μ + P` (the `Π_X` term is `O(T^{λ/2−1})` and drops):

| term | contribution |
|---|---|
| `μμμ` | `N/λ²` |
| `μPP` (×3) | `N` — via `Σ_{n≤X} Λ(n)²/n · (L − log n) = L³/6` |
| `μμP`, `PPP` | `o(N)` |

\[
\boxed{\;\operatorname{tr}\hat G^{3}=\Big(1+\tfrac1{\lambda^{2}}\Big)N\;}
\]

*Cross-check:* the same machinery reproduces the paper's second moment
exactly — `μμ → N/λ` and `PP → λN/3`, i.e. `(1/λ + λ/3)N`. That agreement
is the main evidence the derivation is set up correctly.

## Step 2 — the third moment needs no new arithmetic

Worth recording separately, because it was the *expected* obstruction and
it does not occur. The `PPP` term's resonance condition is
`log n₁ + log n₂ − log n₃ = 0`, i.e. `n₁n₂ = n₃`. But `Λ(n₁n₂) ≠ 0` forces
all three to be powers of the **same** prime, `n₁ = p^a`, `n₂ = p^b`,
`n₃ = p^{a+b}`, and the resulting sum is

\[
\sum_p \frac{(\log p)^3}{(p-1)^2}=2.3156\ldots \quad(\text{tail beyond }10^6 < 4\cdot10^{-3}),
\]

a convergent constant — negligible against `N → ∞` (check D). **So the
third moment is unconditionally available at bandwidth `λ ≤ 1`, exactly
like the second: no Hardy–Littlewood-strength prime-pair input is needed.**
The wall that stops the *bandwidth* extension does not stop the *moment*
extension. That half of the open question resolves in the affirmative.

## Step 3 — but it certifies nothing new

Equality in the paper's rank–trace step (its Prop. 4.4(i)) holds for a
**two-point spectrum**: `s₁` eigenvalues equal to `1` and `(s₂+p)` equal to
`2`. For *any* `{1,2}`-spectrum with `x` ones and `y` twos,

\[
M_1=x+2y,\quad M_2=x+4y,\quad M_3=x+8y
\quad\Longrightarrow\quad
M_3=3M_2-2M_1 \ \text{identically.}
\]

So a third moment can improve the bound **only if** the true `M₃` differs
from `3M₂ − 2M₁`. Comparing:

\[
\text{extremal prediction } (3/\lambda+\lambda-2)N
\qquad\text{vs}\qquad
\text{actual } (1+1/\lambda^{2})N .
\]

At `λ = 1` both equal `2N`. **They agree exactly, so the extremal
configuration survives the third moment and the `2/3` bound is
unimprovable by it.**

## Step 4 — the agreement is a triple root, not a coincidence

The gap between the two factors:

\[
\boxed{\;\Delta(\lambda)=\Big(1+\tfrac1{\lambda^2}\Big)-\Big(\tfrac3\lambda+\lambda-2\Big)
=\frac{(1-\lambda)^{3}}{\lambda^{2}}\;}
\]

`Δ(1) = Δ′(1) = Δ″(1) = 0`, `Δ‴(1) = −6` (check M3b). The third moment's
information content vanishes **to third order exactly at the optimal
bandwidth**. For `λ < 1` the gap is strictly positive — the third moment
does carry information there — but `H(λ) = 2 − 1/λ − λ/3` is increasing on
`(0,1]`, so the optimum sits precisely at the one point where the extra
information is worth nothing.

## Step 5 — everything is tight at once

At `λ = 1` the extremal spectrum implied by the true moments is

- `(2/3)N` eigenvalues equal to `1`,
- `(1/6)N` eigenvalues equal to `2`,

and this **saturates the counting constraint** `N ≥ s₁ + 2(s₂+p)` with
equality (checks M4, M5). The rank–trace inequality, the moment data and
the counting constraint are simultaneously tight at the same configuration.
That is strong evidence that `2/3` is the exact truth of this method rather
than an artefact of a lossy inequality — consistent with, and independent
of, the paper's own `0.68185` ceiling claim.

## Consequences

1. **This direction is closed.** Adjoining `tr G̃³` cannot beat `2/3`. Any
   future improvement must come from **bandwidth** (`λ > 1`, the
   Hardy–Littlewood wall, which this repository's Proposition O1 met from
   the other side) or from a genuinely different functional of the
   spectrum — not from higher moments of the same compression.
2. **Higher moments are presumably worse, and cheaply so.** The same
   same-prime collapse should make `tr G̃^k` unconditionally computable at
   `λ ≤ 1` for every fixed `k`; but the `{1,2}`-spectrum is determined by
   two parameters, so *every* higher moment is a fixed function of `M₁, M₂`
   at the extremiser. The next collaborator can test `k = 4` in minutes by
   the same route; the prediction is that it also agrees at `λ = 1`.
3. **What is not claimed.** RH; any improvement of `2/3`; novelty (the
   moment computation is a routine extension of Montgomery's and may be
   known). The off-diagonal error terms in `tr G̃³` are **not** bounded
   here — that would need the paper's Montgomery–Vaughan treatment carried
   to three factors, and is the one analytic gap in the derivation.

## Evidence levels

- **Proved here:** any `{1,2}`-spectrum satisfies `M₃ = 3M₂ − 2M₁`; the
  gap identity `Δ(λ) = (1−λ)³/λ²` and its triple root; the tightness of the
  `λ=1` configuration against the counting constraint.
- **Derived here (candidate):** `tr Ĝ³ = (1 + 1/λ²)N`. Kernel identities
  and arithmetic inputs verified numerically; off-diagonal error terms not
  bounded.
- **Verified numerically:** the triangle-kernel identity; convergence of
  the same-prime triple sum; the Chebyshev–Mertens inputs.
- **Not attempted:** an end-to-end matrix construction. Meaningful
  asymptotics need `l = log(T/2π) ≫ 1`, hence `d = λlT/2π > 10⁹` even at
  `l = 20`; at feasible sizes the prime cutoff `X = (T/2π)^λ` is under 10
  and the measurement discriminates nothing. Recorded rather than
  presented as evidence.

## Reproduction

```
python tools/third_moment_probe.py
```

## Sources

- The external two-thirds paper (arXiv:2511.20059), especially its §3
  (linear algebra), §5 (prime side) and Remark 1.1 (optimality).
- H. L. Montgomery, *The pair correlation of zeros of the zeta function*
  (1973), for the moment machinery being extended.
- This repository: `docs/EXTERNAL_2026-08-11_TWO_THIRDS.md`,
  `docs/ROUTE_005_DETERMINING_THEOREM.md` (Prop. O1).
