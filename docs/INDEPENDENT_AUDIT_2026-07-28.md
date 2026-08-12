# Independent audit — 28 July 2026

**Auditor:** an AI collaborator (Claude Code session, same agent as the
27 July audit and PR #7). Everything below is corroboration or correction,
not human verification. No route status is promoted here.

## Part 1 — Response to the audit findings against PR #7

The repository audit recorded two defects in the PR #7 tail work
(`RESEARCH_MAP.md`, Route 001 entry). Both were diagnosed, confirmed real,
and fixed. Both were rigor-class, not correctness-class: after the fixes,
every certified number is unchanged at the reported precision.

### Finding A — interval-endpoint narrowing in `tools/tail_certificate.py`

**Diagnosis (confirmed).** The script set `iv.dps = 30` but left the `mp`
working precision at its default (53 bits). `mpmath` materializes interval
endpoints (`.a`/`.b`) as `mpf` values at the *current mp precision with
round-to-nearest*, so every endpoint extraction — including the final
certified constant `M.a` — could round inward by up to half an ulp at the
lower precision.

**Fix.** `mp.mp.dps = 50 > iv.dps` makes every endpoint materialization
exact, and the script now claims a safe decimal constant strictly below the
certified endpoint (`0.0791`) instead of a rounded display value.

**Impact.** None at reported precision: `M(2000) >= 0.0791187203` before
and after. The theorem statement is unchanged.

### Finding B — underestimated decreasing-series remainder in the extension

**Diagnosis (confirmed, with wider scope).** `T2iv(b, M)` bounded the tail
`sum_{n>=M} (n+1/4)/((n+1/4)^2+b^2)^2` by `1/(2(M+1/4)^2)`, which is
`int_M^inf (x+1/4)^{-3} dx` alone. The integral test for a decreasing series
starting at `n = M` requires the first term as well:
`sum_{n>=M} f(n) <= f(M) + int_M^inf f(x) dx`. The same omission occurs at
the `NSEQ` tail (`1/(2*400.25^2)` missing `1/400.25^3`). **Both defects are
inherited verbatim from `src/rigorous_weil_sweep.py`** — they affect the
original `[11, 1737]` certificate exactly as much as the extension.

**Fix.** Both sites corrected in `src/sweep_extension_1737_2000.py`
(first term added, outward rounding preserved); extension regenerated and
re-verified: same 1,684 intervals, exact coverage of [1737, 2000], worst
margin 1.105674 — unchanged at reported precision.

**Measured impact on the original certificate.** The same fix was applied
to a scratch copy of `rigorous_weil_sweep.py` and the full sweep re-run
(the committed artifact was deliberately left untouched, per repository
policy that original artifacts are preserved and critiques added
separately). Result: identical pass structure and interval set (11,720
rows), maximum margin shift `1.0e-10`, smallest margin `4.348752e-07`
(previously reported `4.34877e-07`), zero negative rows. The original
certificate therefore survives the corrected bound; applying the fix and
regenerating `data/certificates.csv` from one pinned commit is recommended
but is the repository owner's decision.

### Status consequence

With both findings repaired and re-run, the tail argument and extension
again support the candidate statement `Q(t) >= 0 for all t >= 11`,
**pending the auditing collaborator's re-review** — the "not certified"
label in `RESEARCH_MAP.md` is theirs to lift, not this session's. The
handoff §6 obligations on the finite segments are unchanged (and Finding B
adds evidence for prioritizing the Arb port: hand-built enclosures keep
yielding exactly this class of bug).

## Part 2 — Corroboration of Route 005 cycle 1

`tools/verify_route_005_symbolic.py` (added) machine-checks the recorded
derivation in exact symbolic arithmetic:

- the scaled Fourier pair `g_{a,t}(u) = (pi a)^(-1/2) exp(-u^2/(4a)) cos(tu)`
  (forward transform computed exactly; the pair is then fixed by the
  inversion theorem on Schwartz space);
- the exact scale identity `4a^2 d_a h + d_t^2 h + 2a h = 0`;
- the heat normalization `d_tau G = d_t^2 G` for
  `G = sqrt(a) exp(-a(r-t)^2)`, `tau = 1/(4a)` — confirming that
  increasing `a` is the backward direction;
- the pole identity `h_{a,t}(i/2) + h_{a,t}(-i/2) = 4 exp(a/4 - a t^2) cos(a t)`,
  which equals the displayed pole term of `Q_a(t)`;
- the derivative formula implemented by `probe_route_005_conditional.py`.

The eight preregistered diagnostic points were also recomputed
independently (mpmath, 60 digits, **25** zero ordinates instead of the
probe's 3): every value and every derivative matches the recorded table to
at least 12 digits, and the 6-of-8 monotonicity failure pattern is
confirmed. The 3-zero truncation was adequate at all eight points.

This is a third-party reconstruction consistent with the route document's
"independent reconstruction" note; expert human review is still required.

## Part 3 — Literature context for the missing backward-heat invariant

Route 005's cycle-1 conclusion — "ordinary heat positivity is closed as a
bridge; a genuinely new backward-heat invariant or zeta-specific inequality
is required" — is not merely plausible; it is precisely what the de
Bruijn–Newman literature already says, and that literature should be cycle
2's starting point rather than a fresh search.

**The flows are the same operation.** On the Fourier side, moving between
scales `b > a` multiplies the test's transform by a Gaussian factor
(`exp(-u^2/(4b)) -> exp(-u^2/(4a))`); the de Bruijn–Newman deformation
`H_lambda` of the Riemann xi function applies exactly this one-parameter
family of Gaussian Fourier multipliers to the function whose zeros are in
question. Route 005 flows the test against fixed zeros; de Bruijn–Newman
flows the zeros' generating function against fixed tests. The hard
direction (controlling the growing-multiplier side) coincides.

**What is known about that hard direction.**

- de Bruijn (1950) proved the benign direction: the multiplier flow toward
  broader Gaussians preserves reality/strip confinement of zeros — the
  analogue of Route 005's "positivity propagates from narrow to broad."
- Newman (1976) defined Λ and conjectured Λ >= 0, "the Riemann hypothesis,
  if true, is only barely so."
- Rodgers–Tao (2020) proved Λ >= 0: **no margin exists on the backward
  side.** Any generic (zeta-independent) backward-propagation principle
  strong enough to serve Route 005 would contradict the sharpness this
  theorem establishes; a workable invariant must consume arithmetic input
  (the prime side), exactly as cycle 1 concluded.
- Polymath15 (2019) is the state of the art for *quantitative* control
  along this flow (effective approximations, barrier certificates), and its
  published toolchain is directly reusable machinery for any cycle-2
  attempt — and is the same toolchain proposed Route 006 (Λ upper bound)
  would reproduce. The two routes share infrastructure; work on either
  compounds.

**Recommendation for cycle 2.** Before hunting an invariant from scratch:
(i) read de Bruijn 1950 for the exact statements of what the forward flow
preserves (several strip theorems there are sharper than plain
positivity-propagation and may transfer); (ii) treat Rodgers–Tao's proof
technique — which extracts a contradiction from *assumed* backward
regularity using zero statistics — as the template for what any proposed
invariant must evade; (iii) evaluate whether the Polymath15 barrier
approach can certify positivity of `Q_a(t)` on bounded `(a, t)` rectangles
directly, which would convert Route 005's grid question into that
project's already-solved effective-bound format.

## Primary sources

- N. G. de Bruijn, *The roots of trigonometric integrals*, Duke Math. J.
  17 (1950), 197–226.
- C. M. Newman, *Fourier transforms with only real zeros*, Proc. Amer.
  Math. Soc. 61 (1976), 245–251.
- B. Rodgers, T. Tao, *The de Bruijn–Newman constant is non-negative*,
  Forum of Mathematics, Pi 8 (2020):
  https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/de-bruijnnewman-constant-is-nonnegative/D4B85BA067E2D5A71D87E4FFB0D21E46
- D. H. J. Polymath, *Effective approximation of heat flow evolution of
  the Riemann ξ function, and a new upper bound for the de Bruijn–Newman
  constant*: https://arxiv.org/abs/1904.12438
- D. Platt, T. Trudgian, *The Riemann hypothesis is true up to 3·10^12*:
  https://arxiv.org/abs/2004.09765
