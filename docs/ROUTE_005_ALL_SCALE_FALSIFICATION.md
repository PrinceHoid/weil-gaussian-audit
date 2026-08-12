# Route 005 — all-scale Gaussian falsification, cycle 1

**Status:** Exact scale identity and a conditional numerical diagnostic. No
counterexample to RH was found. No statement here proves RH.

## Executive verdict

The scaled family has an exact heat-flow structure. After normalization,
increasing the concentration parameter `a` runs that heat flow backward.
Therefore positivity at the already studied scale `a=1` does not propagate to
the narrower tests `a>1`.

This is a rigorous obstruction to the naive scale-propagation mechanism, not
an obstruction to RH and not a proof that every all-scale strategy fails.

The eight preregistered conditional zero-side values were positive. The same
diagnostic rejected the naive pointwise monotonicity claim for
`sqrt(a) Q_a(t)` at six of eight points. These numbers are normalization
forecasts, not unconditional prime-side evaluations or certificates.

## Frozen formula

Let

```text
h_(a,t)(r) = exp(-a(r-t)^2) + exp(-a(r+t)^2),  a > 0.
```

Under the Route 001 convention

```text
h(r) = integral_R g(u) exp(i r u) du,
```

Fourier inversion gives

```text
g_(a,t)(u)
  = 1/sqrt(pi a) exp(-u^2/(4a)) cos(tu).
```

Substitution into the repository's Guinand–Weil formula gives

```text
Q_a(t)
  = 4 exp(a/4-a t^2) cos(a t)
    - 2/sqrt(pi a) sum_(n>=2)
        Lambda(n)/sqrt(n)
        exp(-(log n)^2/(4a)) cos(t log n)
    + 1/pi integral_R exp(-a x^2) Omega(t+x) dx,

Omega(r)
  = Re psi(1/4+i r/2) - log pi.
```

Setting `a=1` recovers Route 001 exactly.

This derivation is exact algebra under the selected explicit-formula
normalization. An independent reconstruction confirmed every displayed factor
and sign.

## Admissibility boundary

The Gaussian is a valid additive Guinand–Weil explicit-formula test: it is
entire, even, real and nonnegative on the real axis, and rapidly decaying in
horizontal strips. Its multiplicative representative is

```text
f_(a,t)(x)
  = x^(-1/2) / sqrt(pi a)
    exp(-(log x)^2/(4a)) cos(t log x).
```

However, its two pole values are generally nonzero:

```text
f_hat(0) = f_hat(1) = h_(a,t)(i/2)
         = 2 exp(a/4-a t^2) cos(a t).
```

It is therefore not automatically in the pole-neutral convolution-square
class used in one formulation of Weil positivity. A pole subtraction or an
exact admissibility bridge is required before using this family to approximate
that universal class.

The direct falsification implication is unaffected: under RH the exact zero
side is

```text
2 sum_(gamma>0)
  [exp(-a(gamma-t)^2) + exp(-a(gamma+t)^2)] >= 0.
```

Thus a rigorously enclosed negative value of the full explicit-formula
functional would contradict RH. Failure of a scale monotonicity law would only
reject that proposed bridge.

## Exact scale identity

For either Gaussian summand,

```text
partial_a exp(-a(r-t)^2)
  = -(r-t)^2 exp(-a(r-t)^2),

partial_t^2 exp(-a(r-t)^2)
  = (-2a+4a^2(r-t)^2) exp(-a(r-t)^2).
```

Consequently,

```text
4a^2 partial_a h_(a,t)
  + partial_t^2 h_(a,t)
  + 2a h_(a,t)
  = 0.
```

The Guinand–Weil functional is linear and differentiation is valid in the
Schwartz topology, so

```text
4a^2 partial_a Q_a(t)
  + partial_t^2 Q_a(t)
  + 2a Q_a(t)
  = 0.
```

Define

```text
G(a,t) = sqrt(a) Q_a(t),
tau = 1/(4a).
```

Then

```text
partial_tau G = partial_t^2 G.
```

Equivalently, for `0 < a < b`,

```text
G(a,.) = K_(1/(4a)-1/(4b)) * G(b,.),
```

where `K` is the positive heat kernel. Thus positivity at a narrower scale
`b` propagates to a broader scale `a`. The Route 001 information at `a=1`
does not propagate in the required direction to `a>1`; doing so would be
backward heat flow.

The heat identity is elementary and is not claimed as literature novelty.
Its value is that it precisely identifies why the obvious all-scale bridge
fails.

## Preregistered diagnostic

The script `conditional_zero_side_probe.py` inserted the first three positive
critical-line zero ordinates into the truncated RH-side expression

```text
2 sum_(gamma>0)
  [exp(-a(gamma-t)^2) + exp(-a(gamma+t)^2)].
```

This is not an unconditional evaluation of `Q_a(t)` and does not search over
unknown zeros. It is a normalization and scale forecast.

| a | t | truncated forecast | d/da of sqrt(a) times forecast |
|---:|---:|---:|---:|
| 2 | 0 | 1.16486568009652e-173 | -3.28716728235953e-171 |
| 2 | 11 | 5.83228924143788e-9 | -7.89879681605581e-8 |
| 2 | 14.1347 | 1.99999999747157 | +7.07106778504745e-1 |
| 2 | 17.58 | 2.00338407832563e-10 | -3.28894363793799e-9 |
| 4 | 0 | 3.39228013166683e-347 | -1.35464231081625e-344 |
| 4 | 11 | 1.70077988978960e-17 | -3.30002380326217e-16 |
| 4 | 14.1347 | 1.99999999494315 | +4.99999996207359e-1 |
| 4 | 17.58 | 1.00388494442038e-20 | -2.35577297025135e-19 |

No forecast is negative. The derivative changes sign, so the simplest
pointwise monotonicity model does not even hold in the conditional forecast.

## Why a direct prime-side grid is not the next step

Increasing `a` broadens the prime-side Fourier weight

```text
exp(-(log n)^2/(4a)).
```

At `a=4`, `t=0`, the conditional scale is about `3e-347`. A direct
prime/archimedean computation would need hundreds of digits of cancellation
and a rigorous oscillatory prime-tail treatment. A modest prime cutoff cannot
certify that sign.

Moreover, all selected `t` values are far below the published verified-zero
height. After combining that theorem with an explicit bound for the omitted
zero tail, the grid should be provably positive. It is therefore useful for
formula validation but is not a plausible counterexample search.

## Evidence labels

- **Known theorem:** the Guinand–Weil explicit formula.
- **Exact repository derivation:** the scaled Fourier transform, `Q_a(t)`
  formula, PDE, and heat-flow direction; awaiting independent expert review.
- **Finite conditional diagnostic:** the eight zero-side forecasts above.
- **Not established:** any unconditional prime-side sign at those eight
  points, a counterexample to RH, or an all-scale positivity theorem.

## Decision and next work

1. Do not run a larger all-scale grid.
2. Have an analytic number theorist audit the formula and admissibility.
3. If Route 005 continues, require a genuinely new backward-heat invariant or
   a zeta-specific inequality. Ordinary heat positivity and pointwise
   monotonicity are closed as bridges.
4. Keep Route 004 spectral convergence as the primary direct RH program.
5. Treat a negative numerical candidate as a likely normalization or
   truncation error until independently enclosed in Arb/FLINT and reconciled
   with verified-zero data.

## Primary sources

- E. Bombieri, *Problems of the Millennium: The Riemann Hypothesis*:
  https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf
- A. Weil, *Sur les formules explicites de la théorie des nombres premiers*
  (1952): https://cds.cern.ch/record/471308
- D. Platt and T. Trudgian, *The Riemann hypothesis is true up to
  3 x 10^12*: https://arxiv.org/abs/2004.09765


