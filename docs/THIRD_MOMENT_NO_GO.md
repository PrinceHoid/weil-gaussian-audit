# Moments of the compression: the third is exactly useless, the fourth is not

> **Correction notice (same day).** An earlier version of this document
> closed the moment direction outright and predicted that `k = 4` "also
> agrees at `λ = 1`". **That prediction is false.** The fourth moment is
> computed in §6 below and *differs* from the extremal prediction by
> `−N/15`, which reopens the direction. The `k = 3` analysis (§§1–5) is
> unaffected and stands. The prediction is left visible rather than
> silently deleted, per this repository's practice.

**Date:** 11 August 2026. **Status:** candidate derivation plus a proved
no-go at `k = 3`, and a REOPENING at `k = 4`; machine-checked by
`tools/third_moment_probe.py` (14 checks, all pass). Human review required
before any claim of novelty.

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

1. **The `k = 3` direction is closed.** Adjoining `tr G̃³` cannot beat
   `2/3`. But this does *not* close the moment direction as a whole — see
   §6, where `k = 4` breaks the pattern. The other routes to improvement
   remain **bandwidth** (`λ > 1`, the Hardy–Littlewood wall, which this
   repository's Proposition O1 met from the other side) and a genuinely
   different functional of the spectrum.
2. ~~**Higher moments are presumably worse.**~~ **This was wrong — see §6.**
   The reasoning ("every higher moment is a fixed function of `M₁, M₂` at
   the extremiser") is correct, but that is exactly *why* a disagreement at
   `k = 4` is informative: it shows the extremiser is not realised.
3. **What is not claimed.** RH; any improvement of `2/3` (see §6.4 for
   exactly why the `k = 4` slack does not yet yield one); novelty (the
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

---

## 6. The fourth moment — where the pattern breaks

### 6.1 The general moment skeleton

The `tr G^k` kernel is the **k-cycle** `∏_i Φ(τ_i − τ_{i+1})` (for `k = 3`
the cycle happens to be the complete graph, which is why the `k = 3` case
looked like a triangle). Splitting `ν = μ + P` and collecting terms, in the
sharp-taper limit with the prime density `y dy` on `[0, L]`:

| term | contribution |
|---|---|
| `μ^k` | `N/λ^{k−1}` |
| `μ^{k−2}PP` | `C(k,2)·λ^{3−k}·N/3` |
| `μ^{k−3}PPP` | `o(N)` (same-prime collapse) |
| `PPPP` | first appears at `k = 4` |

The middle row is checked against the two known cases: `k = 2` gives
`λN/3` and `k = 3` gives `N` — both exactly right (check F1). That is the
main evidence the skeleton is correct.

### 6.2 The four-prime term

At `k = 4` a genuinely new term appears. Resonance forces the four
frequencies to **pair up** with opposite signs (all-same-prime
configurations are `O(1)`, as in §2). Machine-enumerating the 3 pairings ×
4 sign choices against the 4-cycle kernel gives the "spread" multiset

- **4** configurations with spread `max(y,z)`,
- **8** configurations with spread `y + z`

(confirmed numerically over random `(y,z)`), so the weight is
`4(L − max(y,z))₊ + 8(L − y − z)₊`. With the density `y dy`:

\[
S=\iint yz\big[4(L-\max)_++8(L-y-z)_+\big]
=4\cdot\tfrac{L^5}{20}+8\cdot\tfrac{L^5}{120}=\tfrac{4L^5}{15},
\]

giving a contribution of `(4/15)λN` (check F2). Hence

\[
\boxed{\;\frac{M_4}{N}=\frac1{\lambda^{3}}+\frac2{\lambda}+\frac{4\lambda}{15}\;}
\qquad\text{and at }\lambda=1:\quad \frac{M_4}{N}=\frac{49}{15}.
\]

### 6.3 The extremal configuration is infeasible

The two-point extremiser is fixed by `M₁, M₂` alone, so it *predicts*

\[
M_4^{\text{ext}}/N=\tfrac{7\lambda}{3}-6+\tfrac7\lambda
\qquad\text{at }\lambda=1:\quad \tfrac{10}{3}=\tfrac{50}{15}.
\]

\[
\boxed{\;\frac{49}{15}\;\neq\;\frac{50}{15},\qquad \text{gap}=-\frac{N}{15}.\;}
\]

Contrast with `k = 3`, where the gap vanished to *third* order. At `k = 4`
it is nonzero. **No spectrum supported on `{0,1,2}` matches all four
moments** (check F4): the actual fourth moment is *smaller*, i.e. the true
spectrum is more concentrated than the extremiser, with less mass at the
eigenvalue `2`.

### 6.4 What this does and does not mean

**Does mean.** The configuration that saturates the paper's rank–trace
step at `λ = 1` is **not realised** by the actual matrix. So that
inequality is not tight for `G̃`, and the `2/3` constant is *not* certified
optimal by the moment data. There is genuine slack, and its size is now
quantified: `N/15` in the fourth moment.

**Does not mean.** That `2/3` can be improved. Converting slack into a
better constant requires a **new inequality that consumes `M₄`**, and the
paper's Lemma 3.2 does not: its proof (von Neumann's trace inequality
against `x² ≥ cx − c²/4`) reads only the trace and the Frobenius norm. I do
not have such an inequality. Nor does this contradict the paper's stated
`0.68185` ceiling, which is a *separate, configuration-wise* argument at
bandwidth one, and sits comfortably above `2/3`.

**The precise open problem, now well posed:**

> Strengthen the rank–trace inequality (Lemma 3.2) to consume a fourth
> moment. Concretely: for Hermitian `P ⪰ 0` of rank `≤ r` and Hermitian `Q`
> with `≤ b` positive eigenvalues, bound `r` from below in terms of
> `tr P`, `tr Q`, `‖P+Q‖²_F` **and** `tr (P+Q)⁴`. Then feed in
> `M₄/N = 49/15` at `λ = 1` and see whether the resulting constant exceeds
> `2/3`. The scalar inequality being transplanted is no longer
> `x² ≥ 2x − 1` but a quartic one; the natural candidates are the
> nonnegative quartics `(x−1)²(x−α)² ≥ 0`.

That is a bounded, self-contained linear-algebra question, and it is where
the next hour of work on this should go. The gap `N/15` is small — any
improvement it buys will be small too — but it is real, and the direction
is no longer closed.

### 6.5 Caveats specific to §6

Same as §"Evidence levels", plus: the four-prime term uses the sharp-taper
idealisation (`φ² ≡ 1` on `[−L/2, L/2]`), which incurs `O(w/L)` corrections
that vanish in the limit but are not tracked; and the `k = 4` off-diagonal
error terms are, like `k = 3`, not bounded here. Both would need the
paper's Montgomery–Vaughan treatment carried to four factors before `M₄`
could be used in a theorem rather than a diagnostic.
