---
title: "Research Handoff Memorandum"
subtitle: "Restricted Gaussian Weil-Positivity Experiment for the Riemann Hypothesis"
author: "Prepared for Jacob Thompson and collaborators"
date: "24 July 2026"
---

> **Status in one sentence:** We have a reproducible computer experiment and a plausible candidate certificate for one restricted Gaussian family, but we do **not** have a proof of the Riemann Hypothesis, and the supplied package is not yet a self-contained computer-assisted proof.

# Executive summary

The work began by reviewing three standard reformulations of the Riemann Hypothesis (RH): the Guinand-Weil explicit formula, Weil's positivity criterion, and Li's coefficient criterion. Those are established results from the literature; reproducing them was useful orientation but was not new progress.

The first genuinely focused step was to choose the one-parameter even Gaussian family

$$
h_t(r)=e^{-(r-t)^2}+e^{-(r+t)^2}
$$

and to study the corresponding explicit-formula functional $Q(t)$ entirely from its prime, pole, and archimedean terms. With the Fourier convention used in the project, the resulting expression is

$$
\boxed{
Q(t)=4e^{1/4-t^2}\cos t
-\frac{2}{\sqrt\pi}\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 e^{-(\log n)^2/4}\cos(t\log n)
+\frac1\pi\int_{-\infty}^{\infty}e^{-x^2}\Omega(t+x)\,dx
}
$$

where

$$
\Omega(r)=\operatorname{Re}\psi\!\left(\frac14+\frac{ir}{2}\right)-\log\pi.
$$

The earlier criticism that the archimedean integral had been truncated to a half-line was incorrect and was withdrawn. The displayed formula uses the full line and is consistent with the Gaussian folding identity.

Independent high-precision calculations match the project values at important test points. For example,

```text
t            zero-side cross-check       prime-side cross-check
11           1.08002678128256e-4         1.08002678067730e-4
12.25        5.73236684079535e-2         5.73236684078808e-2
17.57838     2.83047510997127e-5         2.83047510330443e-5
```

The small differences are consistent with truncating the independently computed prime-power sum. These checks strongly support the normalization of $Q(t)$, but they do not prove RH.

The uploaded program `rigorous_weil_sweep.py` was executed without modification. In the test environment it completed in about 13 seconds and reported:

```text
[pass 0] d=0.1562500000 ... uncert. measure=7.968750
[pass 1] d=0.0312500000 ... uncert. measure=2.093750
[pass 2] d=0.0039062500 ... uncert. measure=0.000000
[coverage] union of 11720 certified intervals reaches t = 1737.09375
[result] Q(t) >= 0 certified on [11, 1737]
[result] worst certified margin = 4.349e-07
```

An exact rational union check confirms that the 11,720 rows in the supplied `certificates.csv` cover $[11,1737]$ without gaps. The narrowest mesh used was $1/256$, and the smallest reported margin was $4.34877\times10^{-7}$ on $[17.57421875,17.578125]$.

That is meaningful progress: the project now has a concrete function, a reproducible finite computation, explicit tail estimates, and a small set of well-defined audit questions. However, the current package still has major limitations:

1. The supplied `CERTIFICATE_SUMMARY.txt` contradicts the actual code and CSV by claiming that $11\le t<12.25$ was not covered. The code and CSV do cover it.
2. The summary's claim that the zero-side Gaussian sum is unconditionally positive is circular: away from RH, the zero parameters are complex, so the terms are not automatically nonnegative real squares.
3. The claimed analytic result for all $t\ge1736.452$ appears only as a comment and prose statement. Its executable interval proof is not included.
4. Several implementation bounds remain to be independently proved or replaced by a mature rigorous-numerics library before the finite sweep should be called a theorem.
5. Even a fully validated proof that $Q(t)\ge0$ for every $t$ in this one family would establish only a restricted slice of Weil positivity, not RH itself.

Accordingly, the current result should be described as a **candidate computer-assisted lemma for a restricted Gaussian test family**, not as a proof or near-proof of RH.

# 1. Mathematical background

## 1.1 The Riemann Hypothesis

RH states that every nontrivial zero $\rho$ of the Riemann zeta function satisfies

$$
\operatorname{Re}\rho=\frac12.
$$

It remains an open Millennium Prize Problem as of July 2026.[1]

## 1.2 The explicit formula

The Guinand-Weil explicit formula is a rigorous identity converting a suitable sum over zeta zeros into a combination of prime-power, pole, and archimedean terms. It is the bridge used throughout this project.[2,3]

The formula itself does not prove RH. It lets one translate a question about zeros into a question about primes and special functions.

## 1.3 Weil positivity

In one standard formulation, RH is equivalent to a positivity condition for a quadratic form constructed from the explicit formula, tested on every admissible convolution square. Bombieri's official Clay exposition describes Weil's criterion in multiplicative-convolution language.[2]

The crucial word is **every**. Positivity for one convenient family may be interesting, but it is not equivalent to RH.

## 1.4 Li's criterion

Li proved that RH is equivalent to nonnegativity of an infinite sequence of real coefficients $\lambda_n$.[4] Bombieri and Lagarias later related Li's criterion directly to Weil's criterion and the Guinand-Weil formula.[5]

Checking finitely many Li coefficients is evidence only. It cannot establish that all coefficients are nonnegative.

# 2. The selected Gaussian family

The project selected

$$
h_t(r)=e^{-(r-t)^2}+e^{-(r+t)^2}.
$$

This choice is useful because it is even, rapidly decreasing, localized near $\pm t$, and has an explicit Fourier transform. Under the convention

$$
h(r)=\int_{-\infty}^{\infty}g(u)e^{iru}\,du,
$$

we obtain

$$
g_t(u)=\frac1{\sqrt\pi}e^{-u^2/4}\cos(tu).
$$

Substituting $g_t$ and $h_t$ into the explicit formula gives the displayed $Q(t)$.

The family is intended to represent a one-dimensional path through the Weil positivity cone. A final paper must state the precise function space and Fourier/Mellin convention and prove admissibility there. Merely writing $h_t=|\varphi_t|^2$ pointwise is not a substitute for stating the exact convolution-square condition in the selected convention.

# 3. What the zero side says - and what it does not say

Write a nontrivial zero as

$$
\rho=\frac12+i\gamma_\rho.
$$

Without assuming RH, $\gamma_\rho$ may be complex. The explicit formula gives a zero-side identity schematically of the form

$$
Q(t)=\sum_\rho h_t(\gamma_\rho).
$$

Under RH, the $\gamma_\rho$ are real. Pairing the positive and negative ordinates then gives

$$
Q(t)=2\sum_{\gamma>0}
\left(e^{-(\gamma-t)^2}+e^{-(\gamma+t)^2}\right)>0.
$$

This is a clean explanation of why RH implies positivity for this family. It is **not** an unconditional proof of positivity, because the step treating $\gamma$ as real is precisely the RH assumption.

This distinction corrects a recurring error in the Fable summaries. The statement

> "The explicit formula identity makes $Q(t)$ a positive sum for every $t$."

is circular unless RH has already been assumed.

There was also a factor-of-two inconsistency in the later "wall" discussion. Near $t=11$, the first-zero contribution is approximately

$$
2e^{-(\gamma_1-t)^2}\approx1.0800\times10^{-4},
$$

not $4e^{-(\gamma_1-t)^2}\approx2.1600\times10^{-4}$. The code and the earlier numerical table use the former normalization.

# 4. Prime-side formula and numerical normalization

The prime-side expression has three components:

- a negligible pole term $4e^{1/4-t^2}\cos t$ for $t\ge11$;
- an oscillating prime-power sum;
- a positive-dominant archimedean convolution involving $\Omega$.

At the difficult point $t=17.57838$, independent high-precision evaluation gives approximately

$$
P(t)=-0.57987173157644,
$$

$$
A(t)=0.57990003632747,
$$

and hence

$$
Q(t)=A(t)+P(t)+\text{pole}
\approx2.8304751\times10^{-5}.
$$

This explains why rigorous certification is delicate: two terms near $0.58$ cancel to leave a result near $3\times10^{-5}$.

The cancellation is real, but the later claim that the interval $11\le t<12.25$ forms an insurmountable numerical wall is contradicted by the program itself. The second-order threshold is

$$
\frac{L_2\delta^2}{8}.
$$

With the reported $L_2\approx13.889892$ and $\delta=1/256$, the threshold is about $2.6493\times10^{-5}$, comfortably below the $t=11$ value near $1.08\times10^{-4}$. That is why the uploaded program successfully certifies the region using only the third refinement pass.

# 5. The uploaded computational package

The supplied ZIP contains:

- `rigorous_weil_sweep.py` - interval-style sweep and coverage generator  
  SHA-256: `62bbbacf9d51fb208b87237301acb95844fdda96070296beffabc7a8a6ddb445`
- `certificates.csv` - 11,720 interval rows  
  SHA-256: `7c0d6f2c3a58fe7ab29a1d307dd9a65d2f5f6fa17deec9c5f6887ced885ab8ca`
- `CERTIFICATE_SUMMARY.txt` - prose summary containing contradictions  
  SHA-256: `26b8391cf85d3fd3aaf0cbfdc31fd65cf6563b368756e977adc2d9fdb1b5d9e7`

## 5.1 Reproduction environment

The code was reproduced in the following environment:

```text
Python 3.13.5
NumPy 2.3.5
mpmath 1.3.0
SymPy 1.14.0
```

The script completed successfully in approximately 12.9 seconds.

## 5.2 Coverage result

The supplied CSV has:

- 11,720 interval rows;
- minimum left endpoint $11$;
- maximum right endpoint $1737.09375$;
- exact rational union coverage of $[11,1737]$;
- 10,996 intervals of width $5/32$;
- 188 intervals of width $1/32$;
- 536 intervals of width $1/256$;
- a smallest reported certified margin of $4.34877\times10^{-7}$.

![The program uses finer intervals only in regions where the coarse second-order test fails.](assets/adaptive_mesh.png){width=90%}

![The smallest reported margins occur between the first two zeros, near t = 17.58.](assets/certified_margin.png){width=90%}

The exact coverage check is important but limited: it proves that the listed intervals leave no geometric gaps. It does **not** by itself prove that the lower bound attached to every interval is mathematically sound.

## 5.3 Contradictions in the supplied narrative

The package's prose summary says the mesh covers only $[12.25,1737]$ and that $11\le t<12.25$ would require about $10^8$ grid points. This is false for the supplied code and data. The actual CSV includes rows beginning

```text
11,11.00390625,0.00390625,...
11.00390625,11.0078125,0.00390625,...
```

and the program's exact rational check reports complete coverage from $11$.

The prose summary also claims unconditional positivity on the missing region from the zero-side formula. As explained above, that argument assumes RH.

Finally, the code writes a comment claiming a separate analytic theorem for $t\ge1736.452$, but no executable function or certificate for that theorem is included. The finite mesh overlaps the alleged threshold, but it stops at $1737$; it does not prove the infinite tail.

# 6. Audit of the claimed rigor

The program is far more serious than a normal floating-point plot. It constructs outward-expanded intervals using `nextafter`, custom logarithm and cosine routines, explicit Gaussian-cell bounds, prime truncation estimates, a curvature bound, and exact rational coverage. That is useful work.

Nevertheless, "the script runs" and "the script is a proof" are not the same claim. The following points still need independent mathematical verification.

## 6.1 Cosine argument reduction

The routine selects the multiple of $2\pi$ using

```python
q = floor(mid / 6.283185307179586 + 0.5)
```

and then evaluates a Taylor polynomial intended for a reduced argument of magnitude at most about $3.2$. The package does not certify that the chosen integer $q$ is always correct for every interval. A rigorous version should reduce the argument using an interval enclosure for $2\pi$ and assert that the final reduced interval lies inside the Taylor domain.

## 6.2 Vector summation bound

The routine `i_sumpad` adds a manual error pad proportional to

$$
1.2\times10^{-16}\,n\sum|x_i|.
$$

This is plausible, but it needs a proof tied to the actual reduction algorithm, data layout, overflow assumptions, and rounding behavior. NumPy documents that its floating-point summation method and precision can depend on the selected axis and memory layout.[6]

A stronger approach is to perform the sums in a mature ball-arithmetic package or to use a separately verified dot-product enclosure.

## 6.3 Binet remainder and archimedean bounds

The code uses the fourth-order digamma expansion

$$
\psi(z)=\log z-\frac1{2z}-\frac1{12z^2}+\frac1{120z^4}-R_3
$$

with the bound

$$
|R_3|\le\frac1{63|z|^4r}.
$$

This may be valid, but the proof is not included in the package. The derivative and quadrature estimates built on it should be written as formal lemmas with every domain restriction stated.

## 6.4 Global curvature bound

The certificate uses $L_2\le13.889892$. The source contains an unexplained `1e-6` allowance for the omitted prime-curvature tail and compact code for the archimedean second-derivative bound. Both may be safely oversized, but they need explicit derivations before the mesh implication

$$
\min(Q(a),Q(b))\ge\frac{L_2(b-a)^2}{8}
\quad\Longrightarrow\quad Q(t)\ge0\text{ on }[a,b]
$$

can be treated as certified.

## 6.5 Interval-library trust

The code uses `mpmath.iv` for one-time constants. The official mpmath site describes its interval support as rudimentary and limited to basic functions.[7] That does not show the present calculations are wrong, but it is not the ideal foundation for a high-profile proof certificate.

A clean reimplementation in FLINT/Arb or `python-flint` would reduce the hand-built floating-point trust base. Arb's documented inclusion principle is specifically designed to return a set enclosing every exact result associated with the input balls.[8]

## 6.6 Code and CSV mismatch

The uploaded script writes NumPy scalar representations such as

```text
np.float64(11.0)
```

because it uses `repr()` formatting on NumPy values. The supplied CSV contains corrected plain decimals. This is a minor formatting issue, but it shows the checked data file is not literally the raw output of the supplied script. A final package should regenerate all artifacts from one pinned commit and record hashes automatically.

# 7. Current claim ladder

The clearest way to prevent further confusion is to separate claims by strength.

## Level A - established literature

The following are standard theorems:

- the Guinand-Weil explicit formula for admissible tests;
- Weil's positivity criterion;
- Li's criterion;
- the equivalence of these positivity formulations to RH when required for the full admissible class or full sequence.

## Level B - independently reproduced in this project

The following have been checked directly:

- the full-line archimedean formula and normalization of $Q(t)$;
- agreement of the prime-side and zero-side evaluations at selected $t$ values;
- successful execution of the supplied program;
- 11,720 rows in the supplied CSV;
- exact rational coverage of $[11,1737]$ by those rows;
- the reported smallest margin and mesh-width counts.

## Level C - candidate computer-assisted lemma

Subject to validating every implementation bound, the package is attempting to prove:

> For the single Gaussian family $h_t(r)=e^{-(r-t)^2}+e^{-(r+t)^2}$, the associated explicit-formula functional satisfies $Q(t)\ge0$ for $11\le t\le1737$.

This is the strongest honest summary of the finite computation.

## Level D - not established

The following have not been proved by the supplied work:

- $Q(t)\ge0$ for every $t\ge1737$;
- positivity for every admissible Weil test function;
- RH;
- an information-theoretic obstruction preventing other methods from treating low $t$;
- the existence of a Hilbert-Polya operator or missing cohomology space.

# 8. What has actually been accomplished

Despite the corrections, the project has moved beyond vague discussion. Its useful accomplishments are:

1. **A focused research object.** The problem has been reduced from "prove RH" to auditing one explicit scalar function $Q(t)$.
2. **A correct normalization.** The full-line archimedean term, pole term, and prime-power weights have been reconciled numerically.
3. **A reproducible implementation.** The supplied program executes quickly and produces a finite certificate data set.
4. **A verified coverage structure.** The interval union has been independently checked with exact rational arithmetic.
5. **A located numerical bottleneck.** The tightest finite margin occurs near $t\approx17.58$, between the first two zero ordinates.
6. **A precise remaining audit list.** The project can now be reviewed lemma by lemma instead of relying on persuasive prose.

This is worthwhile, but it is best viewed as the beginning of a rigorous computational note rather than progress toward a complete RH proof.

# 9. Recommended next steps

## Priority 1: freeze the mathematics

Write a two- to four-page derivation that fixes one Fourier convention and proves:

1. the exact Guinand-Weil normalization;
2. the formula for $g_t$;
3. the formula for $Q(t)$;
4. the admissibility of the Gaussian family in the selected Weil criterion;
5. the precise zero-side identity without assuming RH;
6. the conditional simplification under RH.

No code should be changed until this derivation is stable.

## Priority 2: replace the numerical core with ball arithmetic

Reimplement the prime sum, $\Omega$ evaluation, Gaussian integral, curvature bound, and mesh test using FLINT/Arb through `python-flint`, with no NumPy reductions and no hand-coded trigonometric argument reduction. FLINT's Arb layer is built for rigorous midpoint-radius enclosures and supports elementary and special functions.[8]

## Priority 3: provide an independent verifier

The certificate generator and verifier should be separate programs. The verifier should:

- read a versioned certificate format;
- recompute every interval lower bound independently;
- verify exact coverage;
- reject NaNs, infinities, overlaps with malformed endpoints, and missing rows;
- print a short deterministic proof transcript;
- record software versions and SHA-256 hashes.

## Priority 4: include the infinite-tail theorem

If the analytic threshold $t\ge1736.452$ is retained, include the actual executable interval calculation and the full human-readable inequality proving monotonic positivity beyond the threshold. A comment in the CSV is not a certificate.

## Priority 5: decide the research purpose

After the restricted family is fully certified, there are two honest directions:

- **Computational-note direction:** publish a rigorous, reproducible positivity result for this Gaussian family and explain its numerical structure.
- **RH-research direction:** enlarge the family in a mathematically meaningful way and investigate whether positivity can be proved uniformly over a dense or structurally important subclass of the Weil cone.

The second direction is vastly harder. Testing more values of $t$ in the same one-parameter family does not move the result toward Weil's universal quantifier.

# 10. Prompt for additional AI reviewers

The following can be given directly to another AI system:

> We are reviewing a candidate computer-assisted lemma related to Weil positivity for the Riemann zeta function. This is not claimed to prove RH. The test family is $h_t(r)=e^{-(r-t)^2}+e^{-(r+t)^2}$, and the prime-side functional is
> $$
> Q(t)=4e^{1/4-t^2}\cos t-\frac{2}{\sqrt\pi}\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}e^{-(\log n)^2/4}\cos(t\log n)+\frac1\pi\int_{-\infty}^{\infty}e^{-x^2}\Omega(t+x)dx.
> $$
> The supplied Python program outputs 11,720 interval rows whose exact union covers $[11,1737]$. Audit the work in this order: (1) derive the formula and all constants from a fixed explicit-formula convention; (2) prove the Gaussian is admissible for the chosen Weil criterion; (3) prove the Binet remainder, prime tails, archimedean tails, and global second-derivative bound; (4) audit cosine reduction and floating-point summation; (5) reimplement the certificate using Arb/FLINT ball arithmetic; (6) independently verify every certificate row and coverage; (7) do not infer positivity from the zero-side sum unless RH is explicitly assumed; and (8) do not call positivity for this one family a proof of RH.

# Conclusion

The project is no longer merely restating RH equivalences. It has produced a specific Gaussian family, a consistent explicit-formula functional, reproducible values, and a finite interval data set that appears to support positivity on $[11,1737]$.

The strongest defensible conclusion today is:

> **A promising restricted-family computational certificate has been built and reproduced, but it still needs a formal numerical audit and does not imply the Riemann Hypothesis.**

That statement is neither dismissive nor inflated. It accurately identifies what is valuable and what remains missing.

# References

1. Clay Mathematics Institute, "Riemann Hypothesis," current Millennium Prize Problem page, accessed 24 July 2026. https://www.claymath.org/millennium/riemann-hypothesis/
2. E. Bombieri, "Problems of the Millennium: The Riemann Hypothesis," Clay Mathematics Institute. https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf
3. J.-F. Burnol, "The Explicit Formula in Simple Terms," arXiv:math/9810169. https://arxiv.org/abs/math/9810169
4. X.-J. Li, "The Positivity of a Sequence of Numbers and the Riemann Hypothesis," Journal of Number Theory 65 (1997), 325-333. https://doi.org/10.1006/jnth.1997.2137
5. E. Bombieri and J. C. Lagarias, "Complements to Li's Criterion for the Riemann Hypothesis," Journal of Number Theory 77 (1999), 274-287. https://doi.org/10.1006/jnth.1999.2392
6. NumPy Developers, `numpy.sum` documentation, version 2.2 notes on floating-point summation. https://numpy.org/doc/2.2/reference/generated/numpy.sum.html
7. mpmath project, official feature overview and interval-arithmetic note. https://mpmath.org/
8. FLINT Developers, "Using Ball Arithmetic" and Arb documentation. https://flintlib.org/doc/using.html
