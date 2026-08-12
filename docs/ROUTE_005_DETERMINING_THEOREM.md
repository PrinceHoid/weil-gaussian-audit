# Route 005 cycle 4 — Gaussian determining theorem and the true oscillation wall

**Status:** Candidate exact theorem and exact obstruction, awaiting independent
human review. This document does not prove RH: it proves that the unresolved
all-scale positivity statement is equivalent to RH and identifies the form
that any improvement of the prime-side tail argument must take.

## Executive verdict

The clustering problem left open in the scale–strip duality document can be
removed.

For every unbounded set of scales \(\mathcal A\subset(0,\infty)\),

\[
\boxed{\quad
\mathrm{RH}
\quad\Longleftrightarrow\quad
Q_a(t)\ge 0
\ \text{for every }a\in\mathcal A\text{ and every }t\in\mathbb R .
\quad}
\]

One proof is a Gaussian-mollification corollary of Weil's published
positive-distribution criterion. A second, direct proof for a continuous tail
of scales uses a dominant-exponent argument: if an off-line zero exists, one
can choose a generic real translation \(t\) at which one conjugate zero class
has a strictly larger Gaussian growth exponent than every competing class.
Along a suitable unbounded sequence of scales, that class has phase \(\pi\),
so it is negative and exponentially dominates the complete zero sum. Nearby
off-line clusters do not obstruct the argument; distinct heights give
distinct affine crossings of the exponent profiles and can be avoided by the
single generic choice of \(t\).

On the prime side, the absolute-value bound used in cycle 3 is globally sharp:
for each fixed \(a\), the weighted prime-power cosine sum comes arbitrarily
close to its full absolute sum at arbitrarily large heights. Consequently no
uniform-in-\(t\) cancellation estimate can improve the cycle-3 constant. A
successful attack on the remaining wall must couple phase alignment to the
height \(t\), where the archimedean term grows like \(\log t\).

## 1. Frozen zero-side convention

For a nontrivial zero \(\rho=\beta+i\gamma\), write

\[
z_\rho=\frac{\rho-\frac12}{i}
      =\gamma-i\Big(\beta-\frac12\Big)=x_\rho+i v_\rho .
\]

The nontrivial-zero multiset \(\mathcal Z\), with multiplicity, is invariant
under

\[
z\longmapsto \bar z,\qquad z\longmapsto -z.
\]

The Route 005 explicit-formula normalization gives the absolutely convergent
identity

\[
Q_a(t)=\sum_{z\in\mathcal Z}
\left(e^{-a(z-t)^2}+e^{-a(z+t)^2}\right).
\]

Indeed, \(|v_\rho|<\tfrac12\), and

\[
\left|e^{-a(z-t)^2}\right|
=e^{a v_\rho^2-a(x_\rho-t)^2}
\le e^{a/4-a(x_\rho-t)^2}.
\]

The classical bound \(N(T)=O(T\log T)\) therefore gives absolute convergence
for every \(a>0\) and real \(t\). By the symmetry \(z\mapsto-z\),

\[
Q_a(t)=2S_a(t),\qquad
S_a(t):=\sum_{z\in\mathcal Z}e^{-a(z-t)^2}.
\]

The symmetry \(z\mapsto\bar z\) makes \(S_a(t)\) real.

## 2. Strong determining theorem via the Weil distribution

Weil's criterion can be stated as follows. Let \(W\) be the Weil distribution
on \(C_c^\infty(\mathbb R)\), with the Fourier convention

\[
\widehat\psi(r)=\int_{\mathbb R}\psi(u)e^{iru}\,du.
\]

Then RH is equivalent to

\[
W(\psi*\widetilde\psi)\ge0
\qquad\text{for every }\psi\in C_c^\infty(\mathbb R),
\qquad
\widetilde\psi(u)=\overline{\psi(-u)}.
\]

### Theorem G0 (unbounded-scale determining property)

Let \(\mathcal A\subset(0,\infty)\) be any unbounded set. Then RH is
equivalent to

\[
Q_a(t)\ge0
\qquad(a\in\mathcal A,\ t\in\mathbb R).
\]

### Proof

The forward implication follows immediately from the real zero side under RH.

For the converse, fix \(\psi\in C_c^\infty(\mathbb R)\), set
\(v=\psi*\widetilde\psi\), and put

\[
H(r)=\widehat v(r)=|\widehat\psi(r)|^2\ge0.
\]

Replace \(H\) by its even part
\(H_{\rm e}(r)=\tfrac12(H(r)+H(-r))\). The zero multiset is invariant under
\(z\mapsto-z\), so this replacement does not change \(W(v)\). Let
\(v_{\rm e}\) be the inverse Fourier transform of \(H_{\rm e}\), and define

\[
v_{{\rm e},a}(u)=e^{-u^2/(4a)}v_{\rm e}(u).
\]

Because \(v_{\rm e}\) is smooth and compactly supported,
\(v_{{\rm e},a}\to v_{\rm e}\) in \(C_c^\infty\) as \(a\to\infty\).
The product-convolution rule and the Gaussian Fourier transform give

\[
\widehat{v_{{\rm e},a}}(r)
=\sqrt{\frac a\pi}\int_{\mathbb R}
H_{\rm e}(t)e^{-a(r-t)^2}\,dt
\]

and, by evenness of \(H_{\rm e}\),

\[
\widehat{v_{{\rm e},a}}(r)
=\frac12\sqrt{\frac a\pi}\int_{\mathbb R}H_{\rm e}(t)
\left(e^{-a(r-t)^2}+e^{-a(r+t)^2}\right)\,dt.
\]

Consequently,

\[
W(v_{{\rm e},a})
=\frac12\sqrt{\frac a\pi}
\int_{\mathbb R}H_{\rm e}(t)Q_a(t)\,dt\ge0
\qquad(a\in\mathcal A).
\]

Here \(H_{\rm e}\) is nonnegative and Schwartz. The interchange with the zero
sum is justified by Gaussian decay and \(N(T)=O(T\log T)\); equivalently,
\(Q_a(t)=O_a(\log(2+|t|))\) is enough.

Choose any sequence \(a_j\in\mathcal A\) with \(a_j\to\infty\). Continuity of
the Weil distribution gives

\[
W(v)=W(v_{\rm e})
=\lim_{j\to\infty}W(v_{{\rm e},a_j})\ge0.
\]

This holds for every \(\psi\), so Weil's criterion implies RH.
\(\square\)

The exact Gaussian corollary above was not located verbatim in the literature
search. It is presented as an elementary corollary of Weil's criterion, not
as a claimed new criterion or a literature-novel theorem.

## 3. Direct clustering proof by dominant profiles

For \(z=x+iv\), define its real growth profile at translation \(t\) by

\[
\Phi_z(t)=v^2-(x-t)^2.
\]

### Lemma G1

If \(\mathcal Z\) contains a nonreal point, then there are a real \(t_0\), a
nonreal conjugate class

\[
\mathcal C_*=\{x_*+iv_*,\,x_*-iv_*\},\qquad v_*>0,
\]

and a number \(\delta>0\) such that:

1. \(\Phi_*:=v_*^2-(x_*-t_0)^2>0\);
2. \(x_*\ne t_0\);
3. every zero class with a different profile satisfies
   \(\Phi_z(t_0)\le\Phi_*-\delta\).

Identical points and repeated copies of \(\mathcal C_*\) are absorbed into its
positive integer multiplicity.

### Proof

Choose a nonreal \(z_0=x_0+iv_0\). On the open interval

\[
I=(x_0-|v_0|,\,x_0+|v_0|),
\]

its profile is positive. Restrict to a smaller nondegenerate closed interval
\(J\subset I\). Uniformly on \(J\), any zero whose real part is farther than
one unit from \(J\) has profile at most \(1/4-1=-3/4\), while the \(z_0\)
profile has a positive lower bound.

Only finitely many zeros have real part within one unit of \(J\). After
grouping conjugates and multiplicities, their profiles have the common
quadratic term \(-t^2\):

\[
\Phi_{x,v}(t)=-t^2+2xt+(v^2-x^2).
\]

Two distinct profiles are therefore equal at at most one real \(t\); profiles
are identical only when both \(x\) and \(v^2\) agree. Delete from \(J\) the
finitely many pairwise crossing points and the finitely many centers \(t=x\).
Any remaining \(t_0\) has a unique maximizing profile, its maximum is positive,
and its center differs from \(t_0\). The maximum cannot come from a real zero,
whose profile is nonpositive. Finiteness gives a positive gap \(\delta\).
\(\square\)

### A clustered off-line zero forces a negative Gaussian

### Lemma G2

With the objects from Lemma G1, let \(m_*\) be the multiplicity of each member
of the dominant conjugate pair. Then, as \(a\to\infty\),

\[
S_a(t_0)
=2m_*e^{a\Phi_*}
 \cos\!\big(2av_*(x_*-t_0)\big)
+o\!\left(e^{a\Phi_*}\right).
\]

### Proof

The dominant conjugate pair contributes exactly

\[
e^{-a(x_*-t_0+iv_*)^2}
+e^{-a(x_*-t_0-iv_*)^2}
=2e^{a\Phi_*}
\cos\!\big(2av_*(x_*-t_0)\big).
\]

Every other zero in a fixed bounded height interval has exponent at most
\(\Phi_*-\delta\), so its total is
\(O(e^{a(\Phi_*-\delta)})\).

For the infinite remainder, use

\[
\frac{|e^{-a(z-t_0)^2}|}{e^{a\Phi_*}}
\le e^{a(\Phi_z(t_0)-\Phi_*)}.
\]

Outside the bounded interval used in Lemma G1, the exponent is negative.
For \(a\ge1\), these terms are dominated by a constant multiple of
\(e^{-(x_\rho-t_0)^2}\), whose sum converges by
\(N(T)=O(T\log T)\). Each normalized term tends to zero, so dominated
convergence makes the normalized infinite remainder \(o(1)\).
\(\square\)

### Theorem G3 (direct tail-scale version)

For every fixed \(A>0\), the following are equivalent:

1. RH is true.
2. \(Q_a(t)\ge0\) for every \(a\ge A\) and every real \(t\).

### Proof

Under RH every \(z_\rho\) is real, and every summand in the zero-side formula
for \(Q_a(t)\) is strictly positive. Thus (1) implies (2).

Conversely, suppose an off-line zero exists. Lemma G1 supplies
\(t_0,x_*,v_*\) with \(v_*(x_*-t_0)\ne0\). Choose

\[
a_k=\frac{(2k+1)\pi}
{2|v_*(x_*-t_0)|}.
\]

Then \(a_k\to\infty\) and the cosine in Lemma G2 equals \(-1\). Hence

\[
S_{a_k}(t_0)
=-2m_*e^{a_k\Phi_*}
+o(e^{a_k\Phi_*})<0
\]

for all sufficiently large \(k\). Since \(Q_{a_k}(t_0)=2S_{a_k}(t_0)\) and
eventually \(a_k\ge A\), condition (2) fails. Therefore (2) implies RH.
\(\square\)

## 4. What this resolves—and what it does not

Theorem G3 closes the distinct-height clustering gap in the earlier
scale–strip document. The key is not to isolate a preselected lowest or
largest off-line zero. One first takes the upper envelope of all local
profiles and then chooses a generic translation away from its finitely many
crossings.

These theorems are not a proof of RH. The branch currently proves candidate
positivity only for \(0<a\le3.35\), whereas Theorem G0 requires an unbounded
set of scales. They show that the remaining all-scale positivity problem is
exactly RH-hard for this family.

The statement concerns the additive Guinand–Weil tests and the exact
zero-side functional frozen in Route 005. It does not by itself put these
Gaussians into the pole-neutral multiplicative convolution-square class; that
separate admissibility distinction remains as documented in cycle 1.

It also bypasses the auxiliary on-line window used by the proposed
single-scale Theorem D. That estimate is not certified after the cycle-4
audit; if repaired, it would remain useful for effective localization from
one fixed scale, whereas Theorems G0 and G3 are all-scale statements.

## 5. The absolute prime bound is globally sharp

For fixed \(a>0\), put

\[
w_a(n)=\frac{\Lambda(n)}{\sqrt n}
       e^{-(\log n)^2/(4a)},\qquad
F_a(t)=\sum_{n\ge2}w_a(n)\cos(t\log n),
\qquad
S_a=\sum_{n\ge2}w_a(n).
\]

The sums are over prime powers because \(\Lambda(n)=0\) otherwise. They
converge absolutely.

### Proposition O1

For every \(a>0\),

\[
\sup_{t\in\mathbb R}F_a(t)
=\limsup_{t\to+\infty}F_a(t)
=S_a.
\]

### Proof

The upper bound \(F_a(t)\le S_a\) is immediate (and equality holds at
\(t=0\)). The content is that the same supremum is approached at arbitrarily
large heights.

Fix \(\varepsilon>0\). Choose a finite set \(E\) of prime powers whose omitted
weight is less than \(\varepsilon/4\), and let \(p_1,\ldots,p_d\) be the base
primes appearing in \(E\). Simultaneous Dirichlet approximation supplies
arbitrarily large positive integers \(q\) for which

\[
\left\|\frac{q\log p_j}{2\pi}\right\|
\]

is as small as desired for every \(j\). For completeness, apply the
pigeonhole principle to the \(Q^d+1\) points
\(k(\log p_1/(2\pi),\ldots,\log p_d/(2\pi))\bmod1\),
\(0\le k\le Q^d\). As \(Q\to\infty\), the resulting denominators are
unbounded; if a denominator repeats with zero error, its multiples already
give unbounded exact returns.

Choose the approximation tightly enough that
\(\cos(q\log n)\) is within the required tolerance of \(1\) for every
\(n\in E\). The finite part of \(F_a(q)\) then loses less than
\(\varepsilon/2\), while the omitted tail can reduce the sum by less than
\(\varepsilon/4\). After tightening the two harmless constants if necessary,
\(F_a(q)>S_a-\varepsilon\). Such \(q\) are arbitrarily large, proving the
claim. \(\square\)

## 6. The correctly posed oscillation problem

The prime term in \(Q_a(t)\) is

\[
-\frac{2}{\sqrt{\pi a}}F_a(t).
\]

Proposition O1 proves that the cycle-3 uniform lower bound

\[
-\frac{2}{\sqrt{\pi a}}S_a
\]

cannot be improved by any positive constant uniformly in \(t\), even if one
restricts to arbitrarily large \(t\). The phrase “retain oscillation” must
therefore not mean a height-independent saving.

The archimedean term grows asymptotically like
\(\log(t/2\pi)/\sqrt{\pi a}\). A viable wall-crossing theorem must prove a
**phase–height tradeoff**: if the prime phases are aligned closely enough that
\(F_a(t)\) nearly reaches \(S_a\), then \(t\) is already large enough for the
archimedean growth to pay for that alignment. Quantitative simultaneous
approximation or lower bounds for linear forms in the numbers \(\log p\) are
the natural language for that remaining problem.

This narrows the wall without crossing it:

- a uniform cancellation saving is impossible;
- a height-coupled saving remains open;
- the dangerous range is the finite interval between the verified-zero height
  and the point where the archimedean lower bound alone exceeds the sharp
  absolute prime constant.

## Evidence and review obligations

- **Known inputs:** the Guinand–Weil explicit formula, zeta-zero symmetries,
  \(0<\Re\rho<1\), and \(N(T)=O(T\log T)\).
- **Exact candidate results:** Theorem G0, Lemmas G1–G2, Theorem G3, and
  Proposition O1.
- **No numerical evidence is used.**
- **Not claimed:** literature novelty, RH, positivity beyond \(a=3.35\), or a
  phase–height estimate crossing the wall.
- **Required review:** an analytic number theorist should audit the exact
  zero-side normalization and absolute convergence; an analyst should audit
  the generic-envelope selection and dominated-convergence step; a
  Diophantine-approximation expert should audit Proposition O1 and formulate a
  useful quantitative phase–height target.

## Primary sources

- A. Weil, *Sur les “formules explicites” de la théorie des nombres
  premiers* (1952): https://cds.cern.ch/record/471308
- E. Bombieri, *Problems of the Millennium: The Riemann Hypothesis*:
  https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf
- M. Suzuki, *On the Hilbert space derived from the Weil distribution*,
  Canadian Journal of Mathematics (2025):
  https://doi.org/10.4153/S0008414X25101739
- H. Hedenmalm, P. Lindqvist, K. Seip, *A Hilbert space of Dirichlet series
  and systems of dilated functions in \(L^2(0,1)\)*, Duke Mathematical
  Journal 86 (1997): https://doi.org/10.1215/S0012-7094-97-08601-4
