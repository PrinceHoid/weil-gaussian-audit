# Route 005 cycle 3 — Crossing a = 1: narrow-scale positivity theorems (candidate)

**Status:** Candidate assembled theorems, awaiting human review. Certified by
`tools/narrow_scale_certificate.py`; supporting lemma proofs below.

**Headline claims (all unconditional, all candidate pending review):**

- **Theorem N5 (scale window).** \(Q_a(t) > 0\) for **every** \(a \ge 1\) and
  every \(|t| \le T_F := 3\cdot10^{12} - 100\).
- **Theorem N6 (full line at a = 2, 3).** \(Q_2(t) \ge 5.43\) and
  \(Q_3(t) \ge 1.23\) for all \(|t| \ge T_F\); combined with N5,
  \(Q_2(t) > 0\) and \(Q_3(t) > 0\) for **all real** \(t\).
- **Corollary N7.** By heat propagation from \(a = 3\):
  \[
  \boxed{\;Q_a(t) > 0 \quad\text{for every } 0 < a \le 3
  \text{ and every } t \in \mathbb{R}.\;}
  \]
  This supersedes the cycle-2 broad-scale theorem (\(a \le 1\)) and crosses
  the \(a = 1\) barrier that Route 002 proved unreachable by positive
  mixing.

**How the backward-heat obstruction was respected, not evaded.** Cycle 1
proved that no generic heat argument can push positivity from \(a = 1\) to
\(a > 1\) and demanded zeta-specific input. These theorems supply exactly
that input: the Platt–Trudgian verified zeros (an arithmetic fact about
zeta) power the window \(|t| \le T_F\) at every scale, and the prime side
powers the tail. The heat flow is then used only in its benign direction
(from \(a = 3\) downward). Nothing here contradicts the cycle-1 no-go.

**Why this cannot reach RH (the quantitative wall).** The prime-side
constant grows like \(S_a \sim \sqrt{\pi a}\,(1+\operatorname{erf}(\sqrt a/2))\,e^{a/4}\)
while a verified height \(H\) only supplies \(\Omega \approx \log(H/2\pi)\).
The method works exactly while \(2S_a < \log(H/2\pi)\), i.e. up to
\(a_{\max}(H) \approx 3.3\) for \(H = 3\cdot10^{12}\), and asymptotically
\(a_{\max} \sim 4\log\log H\). Increasing \(H\) tenfold buys only
\(\Delta a \approx 0.11\). Reaching all \(a\) — which by density arguments
would approach the full Weil class — requires \(\log\log H \to \infty\).
This makes precise, in scale space, how expensive RH is: **the frontier of
this program is now the single quantitative wall at \(a > a_{\max}(H)\),
passable only by exploiting prime-side oscillation (the discarded
\(\cos(t\log n)\) cancellation) rather than absolute values.**

---

## Setting

\(Q_a(t)\) is the Route 005 functional (frozen convention,
`docs/ROUTE_005_ALL_SCALE_FALSIFICATION.md`); unconditionally
\(Q_a(t) = \sum_\rho h_{a,t}(\gamma_\rho)\) with
\(|\operatorname{Im}\gamma_\rho| < 1/2\) (cycle-2 Lemma B1, scaled
verbatim). External inputs: I1–I3 of
`docs/ROUTE_005_BROAD_SCALE_POSITIVITY.md` (explicit formula;
Platt–Trudgian; explicit zero counting with Trudgian 2014 constants
\(0.112\log T + 0.278\log\log T + 2.510\)).

## Theorem N5 (scale window)

**Claim.** \(Q_a(t) > 0\) for all \(a \ge 1\), \(|t| \le T_F\).

**Proof.** Verified zone: for \(|t| \le 1000\), a verified zero lies within
\(D = 14.14\) of \(t\) (computed ordinates, binding case \(\gamma_1\); see
cycle 2). For \(1000 \le |t| \le T_F\), the counting bound gives at least
\[
\frac{100}{2\pi}\log\frac{T}{2\pi}
- 2\big(0.112\log T + 0.278\log\log T + 2.510\big) \;\ge\; 73
\]
zeros in \([t-50, t+50]\) (worst case \(T = 1000\); the expression is
increasing in \(T\)), all verified since \(t + 50 \le H\); so \(D = 50\)
works there. The verified-zone contribution is \(\ge 2e^{-aD^2}\).
Unverified zeros have height \(> H \ge |t| + 100\), so their total is at
most \(20\,e^{a/4}\log(2H)\,e^{-a\cdot100^2}\) (unit-interval counting
\(\le 5\log T\), strip factor \(e^{a/4}\)). The log-ratio of verified to
unverified is at least
\(a(10^4 - D^2 - \tfrac14) - \log(20\log 2H) \ge 7493\) at \(a = 1\)
and is increasing in \(a\). ∎

*(For \(a \le 1\) the window statement follows already from the cycle-2
broad-scale theorem, so N5 is stated for \(a \ge 1\).)*

## Lemma N1 (large-argument lower bound for Ω)

For \(r > 0\), \(c = r^2/4\), \(f(x) = \frac1{x+1} - \frac{x+\frac14}{(x+\frac14)^2+c}\),
any \(2 \le N < M := \lfloor\sqrt c\rfloor\):
\[
\Omega(r) \;\ge\; -\gamma - \log\pi + \sum_{n=0}^{N-1} f(n)
+ \log\frac{M+1}{N+1} - \frac12\log\frac{(M+\frac14)^2+c}{(N+\frac14)^2+c}
- \frac{3}{4(M-1)} - \frac12\log\Big(1+\frac{c}{(M-1)^2}\Big).
\]

**Proof.** From the digamma series (cycle-2 audit, Lemma T1),
\(\Omega(r) = -\gamma-\log\pi+\sum_{n\ge0}f(n)\). On \([N, M]\): with
\(A(x) = \frac{x+1/4}{(x+1/4)^2+c}\), \(A'(x) = \frac{c-(x+1/4)^2}{((x+1/4)^2+c)^2}\),
and for \(x \le \sqrt c\) either \((x+\tfrac14)^2 \le c\) (so \(f' = -\frac1{(x+1)^2} - A' < 0\))
or \((x+\tfrac14)^2 - c \le \tfrac{\sqrt c}2 + \tfrac1{16}\), in which case
\(A' \le \frac{\sqrt c}{2(2c)^2/\ldots} \le \frac1{8c^{3/2}} \ll \frac1{(x+1)^2}\),
so \(f\) is decreasing throughout \([N, M]\); hence
\(\sum_{n=N}^{M-1} f(n) \ge \int_N^M f(x)\,dx\), and the antiderivative of
\(f\) is \(\log(x+1) - \tfrac12\log((x+\tfrac14)^2+c)\), giving the two log
terms. Beyond \(M\), split \(f\) exactly as
\(f = -\frac{3/4}{(x+\frac14)(x+1)} + \frac{c}{(x+\frac14)((x+\frac14)^2+c)}\):
the first part is bounded in total by \(\frac3{4(M-1)}\), and the second by
\(c\int_{M-1}^\infty \frac{dx}{x(x^2+c)} = \frac12\log(1+\frac{c}{(M-1)^2})\).
Subtracting both magnitudes bounds \(\sum_{n\ge M} f(n)\) from below. ∎

Certified value: \(\Omega(3\cdot10^{12}-104) \ge 26.1986\) (true value
\(\approx 26.89\); the \(\approx0.7\) loss is the price of the elementary
closed form and is affordable).

## Lemma N2 (scaled prime bound)

For \(\log N_P \ge \max(2, 2a)\), with \(v_0 = \log N_P - a\):
\[
S_a := \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}e^{-(\log n)^2/(4a)}
\;\le\; \sum_{\substack{n \le N_P\\ \text{prime power}}} (\cdot)
\;+\; e^{a/4}e^{-v_0^2/(4a)}\Big(2a + \frac{2a^2}{v_0}\Big),
\qquad |P_a(t)| \le \frac{2}{\sqrt{\pi a}}S_a .
\]

**Proof.** As cycle-2 Lemma T2 with \(u^2/4 \to u^2/(4a)\):
\(\varphi(u) = \log u - u/2 - u^2/(4a)\) has \(\varphi' < 0\) for
\(u \ge 2\); the substitution \(v = u - a\) (using
\(u/2 - u^2/(4a) = a/4 - (u-a)^2/(4a)\)) and
\(\operatorname{erfc}(z) \le e^{-z^2}/(z\sqrt\pi)\) give the stated tail;
\(v_0 \ge a > 0\) is guaranteed by \(\log N_P \ge 2a\). At \(a = 1\) this
reproduces the Route 001 tail formula exactly. ∎

## Lemma N3 (scaled window bound)

With \(q_a := e^{-16a}/(4a) \ge \int_{|x|>4} e^{-ax^2}dx\) and \(\Omega\)
increasing on \([0,\infty)\) with minimum \(\Omega(0)\): for \(t \ge T \ge 12\),
\[
A_a(t) = \frac1\pi\int e^{-ax^2}\Omega(t+x)\,dx
\;\ge\; \frac1\pi\Big[\Omega(T-4)\big(\sqrt{\pi/a}-q_a\big) + \Omega(0)\,q_a\Big].
\]
**Proof.** Identical to cycle-2 Lemma T3 with
\(\int_4^\infty e^{-ax^2}dx \le \int_4^\infty \frac x4 e^{-ax^2}dx = \frac{e^{-16a}}{8a}\). ∎

## Lemma N4 (pole)

\(|{\rm pole}_a(t)| = 4e^{a/4-at^2} \le 4e^{a/4}/(aT_F^2) < 10^{-23}\) for
\(t \ge T_F\), via \(e^{-x} \le 1/x\). ∎

## Theorem N6 (full line at a = 2 and a = 3)

For \(t \ge T_F\), \(Q_a(t) \ge M_a(T_F) :=
\frac1\pi[\Omega(T_F-4)(\sqrt{\pi/a}-q_a)+\Omega(0)q_a]
- \frac2{\sqrt{\pi a}}S_a - {\rm pole}\). The certificate evaluates every
quantity in interval arithmetic:
\[
M_2(T_F) \ge 5.4329,\qquad M_3(T_F) \ge 1.2353 .
\]
With Theorem N5 on \(|t| \le T_F\) and evenness: \(Q_2 > 0\) and
\(Q_3 > 0\) on all of \(\mathbb R\). ∎

## Corollary N7 (all scales up to 3)

\(\sqrt a\,Q_a = K_s * \big[\sqrt3\,Q_3\big]\) with
\(s = \frac1{4a} - \frac1{12} > 0\) for \(a < 3\) (cycle-2 Lemma B5 with
base scale 3). Strict positivity of \(Q_3\) and positivity of the kernel
give \(Q_a(t) > 0\) for all \(0 < a \le 3\), \(t \in \mathbb R\). ∎

## Honest accounting

- **Not a proof of RH and not close to one:** the family
  \(\{h_{a,t} : a \le 3\}\) is still a strict subset of the Weil class, and
  the method's ceiling \(a_{\max}(H) \approx 3.3\) is structural. The gap
  to RH is now concentrated in one precise question: *bound the prime sum
  with its oscillation retained, instead of by absolute values.*
- **Candidate status:** inherits review obligations of the cycle-2
  assembly; additionally a reviewer should confirm the exact statement and
  constants of the cited Trudgian 2014 argument bound, and re-derive
  Lemmas N1–N2 (both elementary).
- **Certificate:** `tools/narrow_scale_certificate.py` (interval
  arithmetic throughout, mp precision above iv precision).
- **Route 003 lesson check:** these are not re-indexed equivalences; the
  \(t\)-tails are handled by the prime side, so the theorems are genuinely
  more than a finite-verification consequence — but the *scale ceiling* is
  exactly the finite-to-infinite barrier reappearing in \(a\), and is
  documented as such.

## Primary sources

As in `docs/ROUTE_005_BROAD_SCALE_POSITIVITY.md`, plus:
- T. Trudgian, *An improved upper bound for the argument of the Riemann
  zeta-function on the critical line II*, J. Number Theory 134 (2014),
  280–292.
