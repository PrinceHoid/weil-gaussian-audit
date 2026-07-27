# Independent audit — 27 July 2026

**Auditor:** an AI collaborator (Claude Code session). Per repository policy,
everything below is **corroboration, not human verification**, and does not
change any route's need for qualified human review.

**Scope:** reproduction and machine-checking of already-claimed results. No new
route is proposed, no claim is promoted, and nothing here bears on the truth of
RH.

## Environment

```text
Python 3.11.15
NumPy 2.4.6
mpmath 1.3.0
SymPy 1.14.0
```

Note this differs from the handoff's recorded environment (Python 3.13.5,
NumPy 2.3.5), which makes the bit-level agreement below a cross-environment
reproducibility result rather than a re-run of the same binary stack.

## Checks performed

### 1. Structural certificate verification (exact structural check)

`python tools/verify_certificate_csv.py data/certificates.csv` reports
11,720 rows, exact rational coverage of [11, 1737] with union reaching
55587/32 = 1737.09375, width counts 5/32:10996, 1/32:188, 1/256:536, and
smallest reported margin 4.34877e-07 on [17.57421875, 17.578125]. All values
match the handoff memorandum.

### 2. Full sweep reproduction (floating-point experiment, cross-environment)

`src/rigorous_weil_sweep.py` was executed with only the output path changed.
It completed in about 21 s and reproduced the recorded pass structure
(pass 0/1/2, uncertified measure 7.968750 → 2.093750 → 0), the coverage
result, and the worst certified margin 4.349e-07.

All 11,720 regenerated rows were then compared to `data/certificates.csv`
after normalizing the known `np.float64(...)` repr formatting (handoff §6.6):
**every numeric field of every row is identical (maximum absolute difference
0.0)**. This resolves the handoff's concern that the committed CSV "is not
literally the raw output of the supplied script" at the level of values: the
difference is formatting only. The recommendation to regenerate artifacts from
one pinned commit still stands.

### 3. Route 002 separator identities (exact algebraic, machine-checked)

`tools/verify_route_002_symbolic.py` (added by this audit) verifies in exact
sympy arithmetic:

- `integral(h_t) = 2 sqrt(pi)` and `h_t(0) = 2 exp(-t^2)`, hence
  `Lambda(h_t) = 2 sqrt(pi) (1 - exp(-t^2)) >= 0`;
- `Lambda(exp(-a r^2)) = sqrt(pi) (a^(-1/2) - 1) < 0` for `a > 1`;
- the Route 003 strengthening
  `Lambda_c(h_t) = sqrt(pi) (2 - exp(-(c-t)^2) - exp(-(c+t)^2)) >= 0`;
- the positive-mixture identity
  `integral_t exp(-beta t^2) exp(-(r-t)^2) dt
   = sqrt(pi/(beta+1)) exp(-(beta/(beta+1)) r^2)`,
  with scale map `a = beta/(beta+1)` increasing and of range (0, 1).

On the topological step the script does not check: `f ↦ integral(f)` and
`f ↦ f(c)` are continuous on Schwartz space (`|f(c)| <= sup|f|` and
`|integral f| <= pi * sup (1+r^2)|f|`), so each `Lambda_c` is continuous and
nonnegativity on the generators passes to the closed positive cone. This
one-line argument still requires the human analyst review already requested
in NEXT_STEPS.md.

### 4. Q(t) normalization cross-check (high-precision floating point)

`tools/crosscheck_qt_normalization.py` (added by this audit) recomputes both
sides of the explicit-formula identity independently of the sweep code:
zero side from the first 25 zero ordinates (mpmath `zetazero`), prime side
from the displayed formula with an independent prime-power cutoff (120000),
mpmath quadrature for the archimedean term, and 30-digit working precision.

```text
t            zero side                 prime side                abs diff
11           1.08002678128256e-4       1.08002678101790e-4       2.65e-14
12.25        5.73236684079535e-2       5.73236684079950e-2       4.15e-14
17.57838     2.83047510997127e-5       2.83047511264661e-5       2.68e-14
```

The zero-side digits match the handoff table exactly; agreement is two to
three orders tighter than the handoff's (consistent with the larger prime
cutoff used here). At t = 17.57838 the components reproduce the handoff's
cancellation: P(t) = -0.579871731576348, A(t) = 0.579900036327475.

## What this audit does not change

Every open obligation in the handoff (§6) and AUDIT_PLAN.md remains open,
in particular:

- the admissibility/convention memorandum (the repository's bounded next task);
- the unproved implementation bounds: cosine argument reduction has no runtime
  assertion that the reduced argument stays in the Taylor domain, the
  `i_sumpad` rounding constant, the Binet remainder lemma, the prime and
  archimedean tail lemmas, and the derivation of the `L2` curvature bound
  (including its unexplained `1e-6` allowance);
- the missing executable certificate for the claimed tail theorem
  `t >= 1736.452`;
- migration of the numerical core to mature ball arithmetic (FLINT/Arb);
- human review of Routes 001 and 002.

Levels C and D of the handoff's claim ladder are unchanged. Nothing here is
progress toward RH; it is confirmation that the recorded artifacts are what
they claim to be, at the evidence levels stated.
