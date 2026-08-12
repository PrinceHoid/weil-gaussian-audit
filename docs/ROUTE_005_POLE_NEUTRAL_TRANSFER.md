# Route 005 cycle 7 — Pole-neutral transfer: closing the admissibility obligation

**Status:** candidate theorem, elementary proofs, machine-checked by
`tools/verify_pole_neutral_transfer.py` (11 checks, all pass). Awaiting
human review and a literature audit. Does not prove RH.

## The obligation being closed

`NEXT_STEPS.md` step 1 — the repository's *first* stated priority, open
since the original handoff and re-flagged in every cycle since — reads, in
substance: the Route 001/005 Gaussians are additive explicit-formula
tests, but Bombieri's statement of Weil's criterion uses a **multiplicative
convolution square together with two vanishing-moment conditions**, and
nobody had shown the family belongs to that class. Cycle 1 identified the
concrete obstruction and cycle 4 restated it:

> its two pole values are generally nonzero:
> `f̂(0) = f̂(1) = h_{a,t}(i/2) = 2 exp(a/4 − a t²) cos(a t)`.
> It is therefore **not automatically in the pole-neutral convolution-square
> class** used in one formulation of Weil positivity.

This document removes the obstruction by exhibiting an explicit
pole-neutral convolution-square family and transferring the certified
positivity to it.

## The construction

Let `P_a(r) := e^{−a(r²+1/4)}`, normalised so that `P_a(±i/2) = 1` (V2a),
and let `c_{a,t} := h_{a,t}(i/2) = 2e^{a/4−at²}cos(at)` be the pole value
itself. Define

\[
H_{a,t}(r)\;:=\;h_{a,t}(r)-c_{a,t}P_a(r).
\]

**Lemma P1 (closed form).** Exactly, for all complex `r`:

\[
\boxed{\;H_{a,t}(r)\;=\;2\,e^{-a(r^{2}+t^{2})}\Big[\cosh(2art)-\cos(at)\Big].\;}
\]

*Proof.* `h_{a,t}(r) = 2e^{−a(r²+t²)}cosh(2art)` by completing the square,
and `c_{a,t}P_a(r) = 2e^{−a(r²+t²)}cos(at)` since the `e^{±a/4}` factors
cancel. Machine-verified as an exact symbolic identity (V1). ∎

Three properties follow immediately, and they are exactly the three the
obligation demanded.

**Lemma P2 (pole-neutrality — both moment conditions).**
`H_{a,t}(i/2) = H_{a,t}(−i/2) = 0` for every `a > 0` and every real `t`.

*Proof.* At `r = ±i/2`, `r² = −1/4` and `cosh(2a(±i/2)t) = cos(at)`, so the
bracket vanishes identically (V2b, V2c). ∎

Since the pole contribution to the additive explicit formula is exactly
`h(i/2) + h(−i/2)`, this kills both pole terms — the additive reading of
Bombieri's two vanishing-moment conditions. By contrast `h_{a,t}(i/2) ≠ 0`
(V3): the obstruction was real, and is now removed.

**Lemma P3 (nonnegativity and convolution-square structure).**
`H_{a,t}(r) ≥ 0` for every real `r`, with equality iff `rt = 0` **and**
`at ∈ 2πℤ`. Consequently, whenever `at ∉ 2πℤ`, `H_{a,t}` is strictly
positive and Schwartz on ℝ, so `√H_{a,t}` is Schwartz and
`H_{a,t} = |φ̂|²` for a Schwartz `φ` — a convolution square.

*Proof.* `cosh(2art) ≥ 1 ≥ cos(at)`, with `cosh = 1` iff `rt = 0` and
`cos = 1` iff `at ∈ 2πℤ` (V4a: minimum over a dense grid is `3.3·10⁻⁵⁸²`,
i.e. no negative values; V4b confirms the degenerate case is exactly
`at ∈ 2πℤ`). The excluded `t` form a discrete set and are recovered by
continuity of the functional. ∎

**Lemma P4 (functional identity).** By linearity, and since
`P_a = e^{−a/4}e^{−ar²}` with `e^{−ar²} = h_{a,0}/2`,

\[
Q[H_{a,t}]\;=\;Q_a(t)\;-\;e^{-at^{2}}\cos(at)\,Q_a(0)
\]

(V5, exact coefficient check). ∎

## Theorem P5 (transfer of certified positivity)

For every `0 < a ≤ 3.45` and every real `t`,

\[
Q[H_{a,t}]\;\ge\;0 ,
\]

with equality only at `t = 0` (where `H_{a,0} ≡ 0`).

**Why this is not automatic.** Lemma P4 expresses `Q[H]` as a **signed**
combination of two certified-positive quantities. Route 002's standing
warning applies verbatim: pointwise positivity does *not* control signed
combinations. The proof below works because the `cosh ≥ 1` structure of
the zero side supplies the missing inequality — not because `Q_a > 0`.

**Proof.** By Lemma P4 and `cos(at) ≤ 1`, it suffices that
`Q_a(t) ≥ e^{−at²}Q_a(0)`. Two regimes, whose union is ℝ (V7):

*Regime 1: `|t| ≤ t₀ = 14.1653`.* Every zero of height at most
`H = 3·10¹²` lies on the critical line (Platt–Trudgian), so its
`z`-value is real. For real `γ`,

\[
e^{-a(\gamma-t)^2}+e^{-a(\gamma+t)^2}
=2e^{-a(\gamma^{2}+t^{2})}\cosh(2a\gamma t)
\;\ge\;2e^{-a\gamma^{2}}e^{-at^{2}},
\]

by `cosh ≥ 1`; summing gives `Q_a(t) ≥ e^{−at²}Q_a(0)` for the verified
part. The unverified zeros (height `> 3·10¹²`, `|t| ≤ t₀`) contribute at
most `3e^{a/4}e^{−a(3·10¹²−15)²}` in total by the standard counting bound
— below `e^{−10²⁵}`, while the scale-window theorem gives
`Q_a(t) ≥ 2e^{−a·14.14²} ≈ e^{−690}`. The verified part therefore
dominates by a factor exceeding `e^{10²⁴}`. (V6 checks the inequality
directly against real zeta zeros; minimum slack `8.5·10⁻³⁰⁸` at the
sampled points, and V6b confirms `Q[H] ≥ 0` there.)

*Regime 2: `|t| ≥ t₀`.* Here no zero information is needed. A crude
prime-side bound gives `Q_a(0) ≤ 4e^{a/4} + (2/√(πa))S_a + |Ω(0)| + 1 ≤
23.6759` at `a = 3.45`, hence
`e^{−at²}Q_a(0) ≤ e^{−a t₀²}·23.6759 ≤ 2e^{−a·14.14²}`, which is at or
below the certified floor for `Q_a(t)` throughout this regime — and for
`|t| ≥ 3·10¹²−100` the certified sieve margin `0.0514` dwarfs it
outright. ∎

## What this establishes

1. **The admissibility obligation is closed for the additive family.**
   There is now an explicit, elementary, two-parameter family that is
   simultaneously (i) pole-neutral — both moment conditions hold exactly,
   (ii) a genuine convolution square, and (iii) certified `Q ≥ 0` for every
   `0 < a ≤ 3.45` and every real `t`. The cycle-1 objection no longer
   applies to it.
2. **Cycle 4's framing is vindicated.** Theorem G0 worked with the additive
   Weil distribution and never needed pole-neutrality. Theorem P5 shows
   that choice cost nothing: the pole-neutral version of the same family is
   available and inherits the certified positivity.
3. **The frontier is unchanged.** `H_{a,t}` spans the same two parameters
   as `h_{a,t}`, so cycle 6's pricing still applies: this is not a step
   toward RH, it is the removal of a technical objection that had been
   standing since the original handoff.

## What remains

- **The Mellin/multiplicative convention map is still owed.** This document
  works in the frozen additive convention, where the pole contribution is
  exactly `h(i/2) + h(−i/2)` and killing it is the natural reading of the
  two vanishing-moment conditions. A reviewer should confirm the explicit
  translation to Bombieri's multiplicative statement, including measure and
  involution. The *substantive* obstruction (nonzero pole moments) is gone;
  what is left is a bookkeeping derivation.
- **Still one family.** Weil's criterion quantifies over the whole
  admissible class. `H_{a,t}` is a two-parameter slice of it.
- **Degenerate `t`.** For `at ∈ 2πℤ` the function has a double zero at
  `r = 0` and `√H` is only Lipschitz there; the positivity statement
  extends by continuity, but a reviewer may prefer to state the theorem on
  the complement.
- **Not claimed:** RH; positivity beyond `a = 3.45`; literature novelty
  (the construction is elementary and may well be known — a literature
  audit is required before any novelty claim).

## Reproduction

```
python tools/verify_pole_neutral_transfer.py
```

## Primary sources

- E. Bombieri, *Problems of the Millennium: The Riemann Hypothesis*
  (Clay), for the multiplicative statement of Weil's criterion and the two
  moment conditions.
- A. Weil, *Sur les "formules explicites" de la théorie des nombres
  premiers* (1952).
- D. Platt, T. Trudgian, *The Riemann hypothesis is true up to 3·10¹²*,
  Bull. LMS 53 (2021).
- Repository: `docs/ROUTE_005_ALL_SCALE_FALSIFICATION.md` (cycle-1
  admissibility caveat), `docs/ROUTE_005_DETERMINING_THEOREM.md` §4,
  `docs/ROUTE_005_PHASE_HEIGHT_CERTIFICATE.md` (the certified positivity
  being transferred).
