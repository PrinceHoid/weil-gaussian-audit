# Route 005 cycle 6 — Theorem D repaired: an effective single-scale detection theorem

**Status:** candidate theorem with complete elementary proofs and explicit
constants; every step machine-checked by `tools/verify_theorem_d_repaired.py`.
Awaiting human review. This document does not prove RH and does not, at the
repository's current certified scale, produce new zero-free information — it
makes the payoff contract exact and prices the remaining gap.

**What changed.** The cycle-4 adversarial audit rejected the proposed
Theorem D on four counts. All four are repaired below:

| audit finding | repair |
|---|---|
| 1. omitted terms of the selected pair need not be positive | Lemma D1 extracts the **complete quartet** exactly; the stray term is bounded by `E_far/E = exp(-4aγ₀(γ₀-δ))` |
| 2. conjugate zeros at `-γ₀` were misplaced into "everything else" | the quartet `{±γ₀ ± iy₀}` is extracted as one unit *before* the remainder is bounded |
| 3. unit-interval zero count cannot be frozen over an infinite lattice sum | Lemma D3: an explicit **log-weighted Gaussian lattice bound** in which the `log` growth is absorbed |
| 4. `log B_a = log log γ₀ + O_a(1)` not uniform in `y₀` (since `Δ = 2 + π/(2ay₀)`) | restricting to the **informative regime** `a y₀² ≥ 1` forces `δ ≤ π/2`, hence `Δ ≤ 2 + π/2 < 3.5709` **uniformly** |

## Setting

Frozen cycle-4 convention: for a nontrivial zero `ρ = β + iγ` put
`z_ρ = (ρ - ½)/i = γ - i(β - ½) = x_ρ + i v_ρ`, so `|v_ρ| < ½`. The
multiset `Z` is invariant under `z ↦ z̄` and `z ↦ -z`, and

\[
Q_a(t)=\sum_{z\in Z}\Big(e^{-a(z-t)^2}+e^{-a(z+t)^2}\Big)
      =2\sum_{z\in Z}e^{-a(z-t)^2}.
\]

**External inputs.** Only those already standing in this repository: the
explicit formula (zero-side representation, cycle-4 §1) and the
unit-interval counting bound **I3**: the number of zeros with height in
`[n, n+1)` is at most `5 log(n+2)` for integers `n ≥ 14`, and zero for
`0 ≤ n < 14`. (Verifier V4: worst observed ratio `0.0846`; `γ₁ = 14.1347`.)

## Lemma D1 (complete quartet, exact)

Let `ρ₀ = β₀ + iγ₀` be a nontrivial zero with `γ₀ > 0` and
`y₀ := β₀ - ½ ≠ 0`. The functional equation and conjugation give the four
zeros `ρ₀, 1-ρ₀, ρ̄₀, 1-ρ̄₀`, whose `z`-values are exactly
`{ +γ₀ - iy₀, +γ₀ + iy₀, -γ₀ - iy₀, -γ₀ + iy₀ }`. Their total contribution
to `Q_a(t)` is **exactly**

\[
4e^{ay_0^2}\Big[e^{-a(\gamma_0-t)^2}\cos\big(2ay_0(\gamma_0-t)\big)
+e^{-a(\gamma_0+t)^2}\cos\big(2ay_0(\gamma_0+t)\big)\Big].
\]

*Proof.* Direct expansion; machine-verified as an exact symbolic identity
(V1a). WLOG `y₀ > 0` by the functional equation. ∎

This is the repair of findings 1 and 2: the quartet is a single unit, and
no member of it is left in the remainder.

## Corollary D2 (the spike)

Let `δ := π/(2ay₀)` and `t* := γ₀ - δ`, and assume `γ₀ > δ`. Then the
quartet contributes at most

\[
-4E\Big(1-e^{-4a\gamma_0(\gamma_0-\delta)}\Big),
\qquad E:=e^{ay_0^2-a\delta^2}.
\]

*Proof.* At `t = t*`, `γ₀ - t* = δ`, so the first cosine is `cos(π) = -1`
exactly (V1b). The second term has magnitude at most
`e^{ay₀² - a(2γ₀-δ)²} = E·e^{-a[(2γ₀-δ)²-δ²]} = E·e^{-4aγ₀(γ₀-δ)}` (V1c),
and its sign is arbitrary. ∎

## Lemma D3 (log-weighted Gaussian lattice sum)

For real `T ≥ 10` and `a ≥ 1`,

\[
\sum_{z\in Z,\ |x_z-T|\ge1}\big|e^{-a(z-T)^2}\big|
\;\le\;
e^{a/4}\cdot 10\log(2T+2)\cdot\frac{e^{-a}}{1-e^{-3a}} .
\]

*Proof.* Since `|v_z| < ½`,
`|e^{-a(z-T)²}| = e^{a v_z² - a(x_z-T)²} ≤ e^{a/4}e^{-a(x_z-T)²}`. Group
the zeros by `n = ⌊|x_z - T|⌋ ≥ 1`, so that `|x_z - T| ≥ n`. By I3, and
counting both sides `x_z ≷ T`, the group has at most `2·5log(T+n+2)`
members. Hence the sum is at most
`e^{a/4} Σ_{n≥1} 10 log(T+n+2) e^{-an²}`. For `n ≤ T` use
`log(T+n+2) ≤ log(2T+2)`; the terms with `n > T ≥ 10` total less than
`10^{-40}` and are absorbed. Finally
`Σ_{n≥1} e^{-an²} ≤ e^{-a}(1 + e^{-3a} + e^{-6a} + …) = e^{-a}/(1-e^{-3a})`,
since `n² ≥ 1 + 3(n-1)`. ∎

This is the repair of finding 3: the `log` growth of the counting bound is
carried inside the lattice sum and dominated by Gaussian decay, rather
than frozen at a single height.

## Lemma D4 (in-window on-line zeros)

Let `Δ := 2 + δ`. If every zero with height in `(γ₀-Δ, γ₀+Δ)` other than
the quartet lies on the critical line, then the non-quartet zeros with
`|x_z - t*| < 1` contribute at most `5 log(t*+2)` to `Σ_z e^{-a(z-t*)²}`.

*Proof.* `|x_z - t*| < 1` means `x_z ∈ (γ₀-δ-1, γ₀-δ+1)`, contained in
`(γ₀-Δ, γ₀+Δ)` because `δ+1 < Δ` and `1-δ < Δ`. Such zeros have `v_z = 0`
by hypothesis, so each term is real and in `(0, 1]`; I3 bounds their
number by `5log(t*+2)`. (Their mirrors near `-t*` fall under Lemma D3.) ∎

## Theorem D′ (repaired detection theorem)

Let `a ≥ 1`. Let `ρ₀` be a nontrivial zero with `γ₀ ≥ 10` and
`y₀ = |β₀ - ½| > 0`, and assume the **informative regime**

\[
u:=a\,y_0^2\;\ge\;1 .
\]

Put `δ = π/(2ay₀) = π/(2√(au)) ≤ π/2`, `t* = γ₀ - δ`, and
`Δ = 2 + δ ≤ 2 + π/2 < 3.5709` (V3 — **uniformly bounded**, the repair of
finding 4). Assume every zero with height in `(γ₀-Δ, γ₀+Δ)` other than the
quartet lies on the critical line. Then

\[
\boxed{\;
Q_a(t^*)\;\le\;-4E\Big(1-e^{-4a\gamma_0(\gamma_0-\delta)}\Big)+B_a(t^*),\;}
\]
\[
E=e^{ay_0^2-a\delta^2},\qquad
B_a(T)=10\log(T+2)+20\,e^{a/4}\log(2T+2)\frac{e^{-a}}{1-e^{-3a}} .
\]

*Proof.* Split `Q_a(t*) = 2Σ_z e^{-a(z-t*)²}` into the quartet and the
rest. The quartet is bounded by Corollary D2 (note `γ₀ ≥ 10 > π/2 ≥ δ`,
so the hypothesis of D2 holds). The rest splits into the in-window
on-line zeros (Lemma D4, contributing at most `5log(t*+2)`) and the zeros
with `|x_z - t*| ≥ 1` (Lemma D3). Doubling both gives `B_a(t*)`. ∎

## Corollary D5 (effective zero confinement, with explicit constants)

Suppose `Q_a(t) ≥ 0` for every real `t`. Then every nontrivial zero
satisfying the hypotheses of Theorem D′ obeys

\[
u-\frac{\pi^2}{4u}\;\le\;L:=\log\frac{B_a(t^*)}{4\big(1-e^{-4a\gamma_0(\gamma_0-\delta)}\big)},
\qquad u=a\,y_0^2,
\]

hence, solving the quadratic in `u` exactly (V5a),

\[
a\,y_0^2\;\le\;u_{\max}:=\frac{L+\sqrt{L^2+\pi^2}}{2},
\qquad\text{i.e.}\qquad
|\beta_0-\tfrac12|\;\le\;\sqrt{u_{\max}/a}.
\]

Since `B_a(T) = O_a(log T)`, `L = log log γ₀ + O_a(1)` — now a **proved**
statement with explicit constants, not a heuristic. The bound improves on
the trivial `|β₀ - ½| < ½` exactly when `a > 4u_max`.

## What this costs and what it buys — the exchange rate, now proved

Verifier output (V5, at the repository's certified scale `a = 3.45`):

| height `γ₀` | `L` | `u_max` | implied `y₀` bound | scale needed for non-vacuity |
|---|---|---|---|---|
| `10³` | 3.0024 | 3.674 | 1.0319 (vacuous) | `a > 14.70` |
| `3·10¹²` | 4.4175 | 4.9191 | 1.1941 (vacuous) | `a > 19.68` |
| `10³⁰` | 5.2930 | 5.7240 | 1.2881 (vacuous) | `a > 22.90` |

Two consequences worth stating plainly.

1. **The `4 log log T` law is now a theorem, not a target.** The
   scale–strip document could only offer it as a "motivated heuristic."
   Theorem D′ + Corollary D5 establish it with explicit constants, subject
   to the window hypothesis.
2. **The gap to usefulness is priced exactly.** The certified frontier is
   `a = 3.45` (cycle 5); the smallest scale at which this theorem says
   anything non-trivial about zeros near the verified height is
   `a ≈ 19.7`. That is a factor `≈ 5.7` in `a` — and since the
   height-coupled sieve's cost grows like `exp(2S_a)` with
   `S_a ≍ e^{a/4}`, the implied computational distance is far beyond
   astronomically large. **No incremental extension of the current method
   reaches the payoff regime.**

## Honest accounting

- **Rigorously proved:** Lemmas D1, D3, D4; Corollaries D2, D5; Theorem D′
  — all elementary, all machine-checked, using only inputs already
  standing in this repository.
- **Still hypothesised:** the on-line window hypothesis (`O(1)`-wide, now
  uniformly bounded by `3.5709`). Theorem D′ is therefore an effective
  *conditional* detection theorem. The all-scale Theorems G0/G3 of cycle 4
  bypass this hypothesis but require unbounded scales.
- **Not established:** RH; any new zero-free region (the table above is
  vacuous at every scale this repository has certified); positivity beyond
  `a = 3.45`.
- **No circularity:** Corollary D5 consumes positivity as a hypothesis and
  produces zero localisation. The repository's certified positivity below
  `|t| ≤ 3·10¹²` is *derived from* verified zeros, so feeding it back
  yields nothing new — and the table shows it would be vacuous even if it
  were independent.

## Related result recorded in the same cycle

An attempt to certify `a = 7/2 = 3.5` by the cycle-5 pipeline **failed**,
and the failure is quantified rather than hidden: budget
`τ(3.5) = 0.36707184` (7.1× that of `a = 3.45`), anchor window
`θ₂max = 0.37744418` (3.0× wider), `T_END = 8·10¹²` with tail margin
`0.0744`, and `5.516·10¹¹` intervals. Measured stage-1 survivor density on
a `10⁷`-interval sample is **2.66%**, i.e. `≈ 1.5·10¹⁰` survivors — far
past what the stage-2 refinement can absorb. Crossing `a = 3.5` therefore
needs a hierarchical in-C second stage (more primes applied only to
survivors), which is engineering, not mathematics. Recorded so the next
collaborator does not rediscover it.

## Primary sources

Unchanged from `docs/ROUTE_005_SCALE_STRIP_DUALITY.md` and
`docs/ROUTE_005_DETERMINING_THEOREM.md`; no new external theorem is
consumed by this repair.
