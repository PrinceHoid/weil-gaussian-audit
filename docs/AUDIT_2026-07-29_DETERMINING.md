# Limited baseline audit — ROUTE_005_DETERMINING_THEOREM.md (29 July 2026)

Scope restricted to the four requested checkpoints. Verdict first: **no
fatal gap found**; the theorems stand at candidate level. Three precision
notes for the human reviewer, none load-bearing.

**1. Interchange of the Weil functional and the Gaussian integral (G0).**
Sound. \(v_{\mathrm e,a} \in C_c^\infty\), so the explicit-formula
(zero-side) representation of \(W\) applies to it directly; the
sum–integral interchange needs
\(\sum_\rho \int |H_{\mathrm e}(t)|\,e^{a v_\rho^2 - a(x_\rho-t)^2}\,dt < \infty\),
which follows from \(H_{\mathrm e}\) Schwartz, \(|v_\rho| < 1/2\), and
\(N(T) = O(T\log T)\) — as the document asserts via
\(Q_a(t) = O_a(\log(2+|t|))\). *Reviewer note:* the crucial structural
point — that the ≥ 0 conclusion for \(W(v_{\mathrm e,a})\) uses only the
hypothesis \(Q_a \ge 0\) and \(H_{\mathrm e} \ge 0\), never that
\(v_{\mathrm e,a}\) is itself a convolution square — is correct and worth
stating explicitly, since it is what makes the mollification legitimate.

**2. Fourier normalization and the factor 1/2.**
Verified by direct computation under the frozen convention
\(\widehat\psi(r) = \int \psi(u)e^{iru}du\):
\(\widehat{e^{-u^2/(4a)}} = \sqrt{4\pi a}\,e^{-ar^2}\), product ↦
\((2\pi)^{-1}\) convolution, giving
\(\widehat{v_{\mathrm e,a}}(r) = \sqrt{a/\pi}\int H_{\mathrm e}(s)e^{-a(r-s)^2}ds\);
the evenized half-sum form and the resulting \(\tfrac12\sqrt{a/\pi}\)
prefactor are exactly right. The evenization step \(W(v) = W(v_{\mathrm e})\)
relies on the evenness of the explicit-formula distribution (zero-set
symmetry \(z \mapsto -z\) plus the even archimedean/prime sides) — fine,
but the reviewer should confirm it against the frozen convention once.

**3. Generic translation with a unique dominant zero class (G1).**
Sound. Profiles are downward parabolas with common leading coefficient, so
two distinct profiles meet at most once; zeros within one unit of the
window are finite in number; deleting finitely many crossings and centers
leaves a generic \(t_0\) with a unique strict maximizer and a positive gap
\(\delta\). Distant zeros are uniformly below \(-3/4\). The multiplicity
grouping (identical \((x, v^2)\)) is handled correctly.

**4. Control of the infinitely many nondominant zeros (G2).**
Sound. For \(a \ge 1\) and \(\Phi_z(t_0) - \Phi_* \le 0\) the normalized
terms are dominated by the \(a\)-independent summable majorant
\(e^{\Phi_z(t_0) - \Phi_*} \le e^{-\Phi_*}e^{1/4 - (x_\rho - t_0)^2}\)
(convergent by zero counting), each term tends to 0 as \(a \to \infty\),
and dominated convergence gives the \(o(e^{a\Phi_*})\) remainder.
*Reviewer note:* the bounded-window constant \(\delta\) must also cap the
far-zero exponent (\(\Phi_* - \delta \ge -3/4\)); adjusting \(\delta\)
downward if necessary is harmless and worth one sentence in a revision.

**Proposition O1** (checked in passing since cycle 5 builds on it): the
pigeonhole simultaneous-approximation argument is standard and correct;
alignment at \(\cos = +1\) is consistent across prime powers, so no
per-prime-power constraint obstructs it. The cycle-3 uniform constant is
indeed sharp, which is what forces the cycle-5 height-coupled design.

**Smallest repairs suggested (non-fatal):** one sentence each for the
convolution-square remark (checkpoint 1), the evenness-of-W justification
(checkpoint 2), and the \(\delta\) cap (checkpoint 4).
