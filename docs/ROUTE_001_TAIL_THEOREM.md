# Route 001 — Tail theorem: Q(t) > 0 for all t ≥ 2000

**Status:** Candidate computer-assisted result; elementary proofs below,
awaiting independent human review.

**Scope:** This document completes the missing infinite-tail obligation of
Route 001 (handoff §5.3 and §9 Priority 4): the original package *claimed*
`Q(t) > 0 for t >= 1736.452` in a CSV comment with no proof and no
certificate. Here the claim is proved (at the slightly weaker threshold
`t >= 2000`) from elementary lemmas plus one interval-arithmetic evaluation,
and the gap `[1737, 2000]` is closed by an extension of the existing sweep.
Nothing here bears on Weil's universal test class or on RH; the Route 002
obstruction is unaffected.

## Statement

For the Route 001 functional

$$
Q(t)=4e^{1/4-t^2}\cos t
-\frac{2}{\sqrt\pi}\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 e^{-(\log n)^2/4}\cos(t\log n)
+\frac1\pi\int_{-\infty}^{\infty}e^{-x^2}\,\Omega(t+x)\,dx,
\qquad
\Omega(r)=\operatorname{Re}\psi\!\left(\tfrac14+\tfrac{ir}2\right)-\log\pi,
$$

**Theorem.** For every real \(t \ge 2000\),

$$
Q(t)\;\ge\;M(2000)\;\ge\;0.0791187\;>\;0 .
$$

The constant is certified by `tools/tail_certificate.py` in `mpmath.iv`
interval arithmetic. Combined with the finite certificates (below), this
yields the

**Corollary (candidate).** \(Q(t)\ge 0\) for every \(t\ge 11\):

- \([11,\,1737]\): original sweep, `data/certificates.csv` (11,720 rows);
- \([1737,\,2000]\): extension sweep, `data/certificates_extension.csv`
  (1,684 rows, one coarse pass, worst margin \(1.105674\));
- \([2000,\,\infty)\): the theorem above.

The two sweep segments inherit every open numerical obligation of the
original program (handoff §6). The tail segment depends only on Lemmas
T1–T3 below and on `mpmath.iv` correctness.

## Lemma T1 (series representation, monotonicity, and minimum of Ω)

For all real \(r\),

$$
\Omega(r) = -\gamma-\log\pi+\sum_{n\ge0}
\left[\frac1{n+1}-\frac{n+\tfrac14}{(n+\tfrac14)^2+r^2/4}\right].
$$

\(\Omega\) is even, nondecreasing on \([0,\infty)\), and its global minimum is

$$
\Omega(0)=\psi(\tfrac14)-\log\pi=-\gamma-\tfrac\pi2-3\log2-\log\pi
=-5.372183419\ldots
$$

**Proof.** The digamma series \(\psi(z)=-\gamma+\sum_{n\ge0}
\left[\frac1{n+1}-\frac1{n+z}\right]\) (DLMF 5.7.6) with
\(z=\tfrac14+\tfrac{ir}2\) gives
\(\operatorname{Re}\frac1{n+z}
=\frac{n+1/4}{(n+1/4)^2+r^2/4}\), which yields the display. Each summand
depends on \(r\) only through \(r^2\) and is increasing in \(r^2\) (the map
\(c\mapsto a/(a^2+c)\) is decreasing for \(a>0,\,c\ge0\)); the series
converges locally uniformly, so \(\Omega\) is even and nondecreasing in
\(|r|\), with minimum at \(r=0\). The value \(\psi(\tfrac14)=-\gamma-\tfrac\pi2-3\log2\)
is the Gauss digamma theorem (DLMF 5.4.13). ∎

**Tail enclosure used by the certificate.** For \(a_n=n+\tfrac14\),
\(c=r^2/4\), and any \(N\ge2\), each term splits as

$$
\frac1{n+1}-\frac{a_n}{a_n^2+c}
=\underbrace{-\frac{3/4}{a_n(n+1)}}_{<0}
+\underbrace{\frac{c}{a_n(a_n^2+c)}}_{>0},
$$

so, using \(\sum_{n\ge N}n^{-2}\le\frac1{N-1}\) and
\(\sum_{n\ge N}a_n^{-3}\le\int_{N-1}^\infty(x+\tfrac14)^{-3}dx
=\frac1{2(N-3/4)^2}\),

$$
\sum_{n\ge N}\left[\frac1{n+1}-\frac{a_n}{a_n^2+c}\right]
\in\left(-\frac{3}{4(N-1)},\;\frac{c}{2(N-3/4)^2}\right).
$$

## Lemma T2 (prime-sum bound; proves the sweep's tail formula)

Let \(S=\sum_{n\ge2}\Lambda(n)n^{-1/2}e^{-(\log n)^2/4}\). For any
\(N\ge3\), with \(v_0=\log N-1\),

$$
S\;\le\;\sum_{\substack{n\le N\\ n\text{ prime power}}}
\Lambda(n)n^{-1/2}e^{-(\log n)^2/4}
\;+\;e^{1/4}e^{-v_0^2/4}\left(2+\frac2{v_0}\right),
$$

and hence \(|P(t)|\le\frac{2}{\sqrt\pi}S\) for all \(t\).

**Proof.** For \(n>N\) use \(\Lambda(n)\le\log n\) and majorize by
\(g(x)=(\log x)\,x^{-1/2}e^{-(\log x)^2/4}\) summed over **all** integers
\(n>N\). Writing \(u=\log x\), \(g=e^{\varphi(u)}\) with
\(\varphi(u)=\log u-\tfrac u2-\tfrac{u^2}4\) and
\(\varphi'(u)=\tfrac1u-\tfrac12-\tfrac u2<0\iff u^2+u-2>0\iff u>1\), so
\(g\) is decreasing for \(x>e\) and
\(\sum_{n>N}g(n)\le\int_N^\infty g(x)\,dx\). Substituting \(u=\log x\)
(\(dx=e^u du\)) and \(v=u-1\), using \(\tfrac u2-\tfrac{u^2}4
=\tfrac14-\tfrac{(u-1)^2}4\):

$$
\int_N^\infty g\,dx=e^{1/4}\int_{v_0}^\infty(v+1)e^{-v^2/4}dv
=e^{1/4}\left[2e^{-v_0^2/4}+\sqrt\pi\,\mathrm{erfc}(v_0/2)\right]
\le e^{1/4}e^{-v_0^2/4}\left(2+\frac2{v_0}\right),
$$

by \(\mathrm{erfc}(z)\le e^{-z^2}/(z\sqrt\pi)\). ∎

**Remark.** With \(v=v_0/2\) this is exactly the tail formula
\(\frac{2}{\sqrt\pi}e^{1/4}e^{-v^2}(2+\frac1v)\), \(v=\frac{\log N-1}2\),
used without proof by `ptable()` in `src/rigorous_weil_sweep.py`. Lemma T2
therefore resolves the prime-tail item of the handoff's open-obligation
list (§6), for both the coarse and fine tables.

## Lemma T3 (archimedean window bound)

Let \(q=e^{-16}/4\) and \(T\ge12\) with \(\Omega(T-4)>0\). Then for every
\(t\ge T\),

$$
A(t)=\frac1\pi\int_{\mathbb R}e^{-x^2}\Omega(t+x)\,dx
\;\ge\;\frac1\pi\Big[\Omega(T-4)\big(\sqrt\pi-q\big)+\Omega(0)\,q\Big].
$$

**Proof.** Split at \(|x|=4\). The excluded mass satisfies
\(m:=\int_{|x|>4}e^{-x^2}dx\le2\int_4^\infty\frac x4e^{-x^2}dx=e^{-16}/4=q\).
On \(|x|\le4\): \(t+x\ge t-4\ge T-4\ge0\), so by Lemma T1
\(\Omega(t+x)\ge\Omega(T-4)>0\), giving
\(\int_{|x|\le4}\ge\Omega(T-4)(\sqrt\pi-m)\ge\Omega(T-4)(\sqrt\pi-q)\).
On \(|x|>4\): \(\Omega(t+x)\ge\Omega(0)\) (global minimum), and since
\(\Omega(0)<0\), \(\int_{|x|>4}\ge\Omega(0)\,m\ge\Omega(0)\,q\). ∎

## Proof of the Theorem

For \(t\ge T\): \(|{\rm pole}(t)|=4e^{1/4-t^2}|\cos t|\le4e^{1/4-T^2}\),
\(|P(t)|\le\frac2{\sqrt\pi}S\) (Lemma T2), and \(A(t)\) is bounded below by
Lemma T3, whose bound is nondecreasing in \(T\). Hence

$$
Q(t)\;\ge\;M(T):=\frac1\pi\Big[\Omega(T-4)(\sqrt\pi-q)+\Omega(0)q\Big]
-\frac2{\sqrt\pi}S-4e^{1/4-T^2}.
$$

`tools/tail_certificate.py` encloses every quantity at \(T=2000\) in
interval arithmetic:

```text
Omega(1996) in [5.75977988932, 5.76106248957]   (Lemma T1, N=20000 + tail enclosure)
Omega(0)    in [-5.37218341924, -5.37218341923] (exact constants)
S          <=  2.80977271607                    (2328 prime powers <= 20000, tail <= 7.1e-9)
q          <=  2.81e-8        |pole| <= 6.1e-1737178
M(2000)    >=  0.0791187
```

∎

## Honest accounting

- **What is new:** the infinite tail now has a proof and an executable
  certificate; previously it existed only as an unproven CSV comment. The
  proof deliberately avoids the unproven Binet/digamma expansion of the
  sweep code: monotonicity of \(\Omega\) (Lemma T1) replaces all derivative
  and quadrature estimates. Lemma T2 additionally discharges the sweep's
  prime-tail formula.
- **Evidence level:** Lemmas T1–T3 are exact elementary proofs. The
  evaluation of \(M(2000)\) is a rigorous computation modulo `mpmath.iv`.
  The corollary's finite segments remain subject to the handoff §6
  obligations (cosine reduction, summation pad, Binet remainder, \(L_2\)
  derivation). All of it awaits human review.
- **Not covered:** \(t\in[0,11)\), where \(Q(t)\) is positive but
  astronomically small (of order \(e^{-(14.13-t)^2}\)); certifying it would
  require high-precision ball arithmetic (Arb), not this method.
- **Not implied:** positivity for any other Weil test function, or RH. By
  the Route 002 obstruction, no amount of work inside this fixed-scale
  family can bridge to Weil's universal criterion.

## Reproduction

```text
python tools/tail_certificate.py                                  # tail theorem at T=2000
python src/sweep_extension_1737_2000.py                           # regenerates extension CSV (~3 s)
python tools/verify_certificate_csv.py data/certificates.csv                 # [11, 1737]
python tools/verify_certificate_csv.py data/certificates_extension.csv 1737 2000
```

## Sources

- NIST DLMF §5.4.13, §5.7.6 (digamma special values and series):
  https://dlmf.nist.gov/5.4 , https://dlmf.nist.gov/5.7
- E. Bombieri, *Problems of the Millennium: The Riemann Hypothesis*:
  https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf
