# Route 004 — critical-strip transfer lemma and first falsification cycle

**Status:** Rigorous repository-level reduction and obstruction, plus exploratory finite computation. This is **not** a proof of RH.

## Bottom line

The prolate proxy route can imply the Riemann Hypothesis, but two independent continuum hypotheses remain unproved: simple/even ground-state control and quantitative comparison with the proxy.

Connes constructs a prolate proxy `k_lambda` and proves that its Fourier transform converges to Riemann's completed `Xi` uniformly on closed substrips of

```text
|Im z| < 1/2.
```

The true missing bridge is to prove that the actual localized Weil ground state is sufficiently close to this proxy. It is not necessary to prove convergence on the whole complex plane.

## Dependency zero: do not conflate three families

### Continuum localized Weil ground state

Let `A_lambda` be the canonical lower-bounded self-adjoint operator representing the localized Weil quadratic form on

```text
L^2([lambda^(-1), lambda], du/u).
```

It has discrete spectrum and a ground state. To invoke the continuum real-zero theorem for an unbounded sequence `lambda -> infinity`, one must still prove that the lowest eigenvalue is simple, isolated, and has an even eigenfunction for those cutoffs.

### Galerkin ground states

At fixed `(lambda,N)`, the trigonometric Galerkin matrix gives finite real-rooted transforms when the finite ground-state hypotheses hold. Passing to RH requires control of the `N -> infinity` limit at fixed `lambda`, the `lambda -> infinity` limit, and any numerical archimedean cutoff `T`. These limits cannot be silently interchanged.

### Suzuki's self-adjoint-extension family

Suzuki constructs a different family `W(a,theta;z)` whose zeros are unconditionally real. Its proposed limiting formula is also conjectural; the motivating calculation assumes RH in order to take a positivity parameter equal to zero, and Suzuki explicitly identifies control of the arithmetic/prime contribution as open.

## The critical-strip transfer lemma

Write

```text
a = log lambda,
I_lambda = [-a,a],
Xi(z) = xi(1/2 + i z).
```

Let `theta_lambda` be a scalar-normalized continuum ground state on `I_lambda`, and let `k_lambda` be the Connes–Consani–Moscovici prolate proxy on the same interval.

### Proposition

Assume:

1. for all sufficiently large `lambda`, the continuum ground state is simple and even, so its Fourier transform has only real zeros;
2. scalars `b_lambda != 0` can be chosen so that

```text
|| b_lambda theta_lambda - k_lambda ||_2 = O(lambda^(-1/2));
```

3. the already-published proxy-transform convergence theorem holds:

```text
hat(k_lambda) -> Xi
```

uniformly on every closed substrip `|Im z| <= r < 1/2`.

Then the Riemann Hypothesis follows.

### Proof

For `|Im z| <= r < 1/2`, Cauchy–Schwarz gives

```text
|b_lambda hat(theta_lambda)(z) - hat(k_lambda)(z)|
 <= ||b_lambda theta_lambda-k_lambda||_2
    * (integral_{-a}^a exp(2r|t|) dt)^(1/2).
```

For fixed `r>0`, the second factor is

```text
((exp(2ra)-1)/r)^(1/2) = O(lambda^r).
```

Consequently the assumed `O(lambda^(-1/2))` error makes the transform difference

```text
O(lambda^(r-1/2)) -> 0
```

on every closed substrip. Together with the known convergence of `hat(k_lambda)`, this gives locally uniform convergence of the normalized true ground-state transforms to `Xi` throughout `|Im z|<1/2`.

Every nontrivial zero `rho=beta+i gamma` corresponds to

```text
z_rho = gamma - i(beta-1/2),
```

which lies in that strip. Hurwitz's theorem therefore rules out a nonreal zero of `Xi`, because every approximating ground-state transform is zero-free off the real axis. Hence RH follows.

A more general sufficient condition is

```text
||b_lambda theta_lambda-k_lambda||_2 = o(lambda^(-r))
```

for every fixed `r<1/2`. The `O(lambda^(-1/2))` condition is a clean single-rate target.

## Alternative sufficient compactness formulation

For centered transforms normalized by a nonzero scalar, it is sufficient to establish cutoff-independent exponential moments for every `b<1/2`, together with pointwise identification on a real set having an accumulation point. Vitali's theorem then gives local uniform convergence in the strip and Hurwitz gives RH.

Either center the interval or explicitly retain the resulting zero-free exponential factor. Translating `[0,log c]` to `[-log(c)/2,log(c)/2]` removes a cutoff-dependent factor that can otherwise create apparent functional divergence without changing any zeros.

## What the finite real-zero theorem does not give

On `I_L=[-L/2,L/2]`, consider the convolution distribution

```text
D_L = delta_0 - 1/L.
```

Its operator is `I-P_L`, where `P_L` projects onto constants. It is nonnegative, has a simple even ground state, and has uniform spectral gap `1`. The normalized ground-state transform is

```text
F_L(z) = sin(Lz/2)/(Lz/2),
```

whose zeros are all real. Nevertheless,

```text
F_L(i b) = sinh(bL/2)/(bL/2) -> infinity
```

for every `b>0`.

Thus even all of the following together do not imply convergence:

- positivity;
- a simple even ground state;
- a uniform spectral gap;
- compact support;
- real finite zeros.

A zeta-specific comparison with `k_lambda` is indispensable.

## Why a small Rayleigh quotient is insufficient

Connes shows that `QW_lambda(k_lambda)` is extremely small, making the proxy a near-radical vector. Small energy alone does not prove that a vector is close to the ground state unless one has suitable sign and spectral information.

For example, for

```text
A = diag(-1,1),
v = (1,1)/sqrt(2),
```

one has `<Av,v>=0`, but `v` is not close to either eigenvector and `||Av||=1`. Invoking positivity of every localized Weil operator to avoid this cancellation would be circular, because global localized Weil positivity is equivalent to RH.

The safe alternatives are:

- prove the `L^2` comparison with `k_lambda` directly;
- prove an appropriate spectral-projection estimate;
- or certify a residual and spectral separation without assuming RH.

A naive Davis–Kahan route would require

```text
R_lambda = ||(A_lambda-mu_lambda)k_lambda||,
Delta_lambda = certified separation from the remaining spectrum,
R_lambda/Delta_lambda = O(lambda^(-1/2)).
```

This is sufficient, but may be much stronger than the needed `L^2` comparison because the localized Weil operator is unbounded and can amplify tiny high-energy components.

## Exploratory computation

The public `connes-cvs` implementation was used only as a falsification probe. These results use finite `N`, finite archimedean cutoff `T`, and floating-point/prolate evaluations; they are not certificates.

At `c=13`, `T=80`, the centered normalized transform was evaluated at `z=0.49 i`. The exact target is

```text
Xi(0.49 i)/Xi(0) = 1.0055618480129357...
```

The finite results were:

| N | computed ratio | absolute error |
|---:|---:|---:|
| 8 | 1.0075075553588220 | 1.95e-3 |
| 12 | 1.0064085259410531 | 8.47e-4 |
| 16 | 1.0059084028599841 | 3.47e-4 |
| 20 | 1.0056299051884389 | 6.81e-5 |

This is encouraging finite evidence for off-axis convergence, which is much more relevant than matching a finite list of real zeros. It is still not a proof of the `N`, `T`, or `lambda` limits.

The same probe found a negative eigenvalue at `c=13,N=12,T=40`, while none appeared at `T=80` or `T=160`. The selected transform was comparatively stable. This reproduces the central numerical warning from the current literature: a finite archimedean cutoff can create false signs and branch changes even when a selected eigenvector appears stable.

A preliminary double-precision reconstruction of the prolate proxy at `c=13,N=12` had approximately `0.9845` overlap with the selected even ground vector, but its raw operator residual was not small. This suggests that direct `L^2` comparison or a low-energy spectral projection may be better suited than an unweighted operator-residual estimate. Because standard spheroidal routines became unstable at larger parameters, this observation is exploratory only.

## Earliest decisive falsification tests

Define the best scalar-aligned error

```text
E_lambda = inf_b ||b theta_lambda-k_lambda||_2.
```

The clean bridge above is falsified only by a rigorous asymptotic obstruction, such as an analytic lower bound or a certified unbounded sequence showing that

```text
lambda^(1/2) E_lambda
```

grows without bound. A worsening finite trend is diagnostic evidence, not a disproof of a big-O claim. Failure of this rate would not disprove RH; it would reject this particular sufficient `L^2` transfer condition.

For an exponential-moment route, measure centered normalized values on the imaginary axis for `b in {0.1,0.25,0.4,0.49}`. For nonnegative even states, one scalar value `F_lambda(i b)` controls the corresponding exponential moment up to a factor of two.

All numerical tests must independently refine:

1. the Galerkin dimension `N`;
2. the archimedean cutoff or cutoff-free evaluation;
3. working precision;
4. the prime/support cutoff `lambda`;
5. the selected spectral branch.

## Concrete next work

1. Implement `k_lambda` with an independently verified, high-precision prolate routine and freeze its normalization.
2. Implement cutoff-free or interval-certified Galerkin matrices before interpreting minuscule eigenvalues and gaps.
3. Measure `E_lambda`, parity leakage, and the low-energy spectral projection over a preregistered cutoff sequence.
4. Seek a direct analytic inequality for `E_lambda` from the semilocal trace formula, rather than from global Weil positivity.
5. Separately prove simplicity and evenness of the continuum lowest eigenvalue for an unbounded cutoff sequence.

## Primary sources

- Alain Connes and Walter D. van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral Action*, arXiv:2511.23257.
- Alain Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time*, especially Sections 6.4–6.6, arXiv:2602.04022.
- Alain Connes, Caterina Consani, and Henri Moscovici, finite localized Weil/spectral construction, arXiv:2511.22755.
- Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096.
- Akiva Groskin, *High-Precision Approximation of Riemann Zeros via the Truncated Weil Form*, arXiv:2605.20224.
- Akiva Groskin, *A finite Guinand-Weil dictionary and archimedean tail order for the truncated Weil quadratic form*, arXiv:2607.02828.
