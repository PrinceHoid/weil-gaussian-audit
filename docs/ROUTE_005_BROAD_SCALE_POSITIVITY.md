# Route 005 cycle 2 — Broad-scale positivity theorem (candidate)

**Status:** Candidate assembled theorem, awaiting human review. Assembled
from published external theorems, the Route 005 heat identity, and the
(repaired, re-review-pending) Route 001 tail theorem. No new computation
beyond a small supporting script; no grid was run.

**One-sentence claim:** the explicit-formula functional of the scaled
Gaussian family is unconditionally strictly positive on the entire broad
half of the scale range:

$$
Q_a(t) > 0 \qquad \text{for every } 0 < a \le 1 \text{ and every real } t .
$$

This is the repository's first all-\(t\), all-scale-slice positivity
statement. It does **not** touch \(a > 1\), does not enlarge the Weil test
class, and does not prove RH. Its value: it settles the entire region that
Route 002 proved reachable by positive mixing, and localizes all remaining
RH content of this program at \(a > 1\).

## Inputs

| # | Input | Status |
|---|-------|--------|
| I1 | Guinand–Weil explicit formula for admissible even tests (e.g. Iwaniec–Kowalski, Thm 5.12) | published theorem |
| I2 | Platt–Trudgian: all zeros with \(0 < \operatorname{Im}\rho \le 3\cdot10^{12}\) lie on the critical line | published theorem |
| I3 | An explicit zero-counting bound: the number of zeros with height in any unit interval \([T, T+1]\) is at most \(5\log T\) for \(T \ge 10\) | published (Backlund 1918; Trudgian 2014 give far sharper constants; enormous slack) |
| I4 | Route 001 tail theorem: \(Q_1(t) \ge 0.0791\) for \(t \ge 2000\) | repository candidate (repaired 28 Jul, re-review pending) |
| I5 | Route 005 heat identity: \(G(a,t)=\sqrt a\,Q_a(t)\), \(\tau=1/(4a)\) solves \(\partial_\tau G=\partial_t^2 G\) | repository exact derivation (symbolically machine-checked) |

## Lemma B1 (zero-side representation)

Each \(h_{a,t}(r)=e^{-a(r-t)^2}+e^{-a(r+t)^2}\) with \(a>0\), \(t\in\mathbb R\)
is even in \(r\), entire, and Gaussian-decaying in every horizontal strip,
hence admissible for the explicit formula (I1). Therefore, unconditionally,

$$
Q_a(t)\;=\;\sum_{\rho}\,h_{a,t}(\gamma_\rho),
\qquad \gamma_\rho := \tfrac{\rho-1/2}{i},
$$

summed over nontrivial zeros \(\rho\) with multiplicity; the sum converges
absolutely (Lemma B4 bounds the tail) and is real, since zeros come in
conjugate pairs and \(h_{a,t}(\bar\gamma) = \overline{h_{a,t}(\gamma)}\).

Writing \(\rho = \beta + i\gamma_0\) with \(0<\beta<1\), we have
\(\gamma_\rho = \gamma_0 - i(\beta - \tfrac12)\), so every zero satisfies
\(|\operatorname{Im}\gamma_\rho| < \tfrac12\), and \(\gamma_\rho\) is real
exactly when \(\rho\) is on the critical line.

## Lemma B2 (verified-zone positivity)

By I2, every zero with \(|\gamma_0| \le H := 3\cdot10^{12}\) has real
\(\gamma_\rho\), and its term \(h_{1,t}(\gamma_\rho) \ge 0\). Moreover for
every \(t \in [0, 2000]\) there is a verified zero within distance
\(D = 14.14\) of \(t\): the binding case is \(t=0\) against
\(\gamma_1 = 14.1347\ldots\), and consecutive-zero gaps up to height 2015
are all far below \(2D\) (largest is \(\gamma_2-\gamma_1 = 6.887\ldots\);
`tools/broad_scale_support.py` recomputes the ordinates, and the certified
gap data is contained in the I2 computation itself). Hence

$$
\sum_{|\gamma_0|\le H} h_{1,t}(\gamma_\rho)\;\ge\;2\,e^{-D^2}\;>\;2\cdot e^{-200}
\qquad (0\le t\le 2000),
$$

using the pairing of \(\pm\gamma\). By evenness of \(Q_a\) in \(t\), the
same holds for \(-2000 \le t \le 0\).

## Lemma B3 (unverified-zero tail)

For any zero with \(|\gamma_0| > H\) and \(|t| \le 2000\),
\(|h_{1,t}(\gamma_\rho)| \le e^{1/4}\big(e^{-(|\gamma_0|-t)^2}+e^{-(|\gamma_0|+t)^2}\big)\)
since \(|\operatorname{Im}\gamma_\rho|<\tfrac12\). Summing over unit
intervals of height with the counting bound I3,

$$
\Big|\sum_{|\gamma_0|>H} h_{1,t}(\gamma_\rho)\Big|
\;\le\; 20\,e^{1/4}\log(2H)\,e^{-(H-2000)^2}
\;<\; e^{-10^{24}} .
$$

The margin over Lemma B2's lower bound is a factor exceeding
\(\exp(10^{24})\); no numerical care is required.

## Theorem B4 (full-line positivity at \(a=1\))

Combining B1–B3: \(Q_1(t) > 0\) for \(|t| \le 2000\), unconditionally.
With input I4 for \(|t| \ge 2000\):

$$
Q_1(t) \;>\; 0 \qquad \text{for every real } t .
$$

**Remark (what is new here).** On \([11, 2000]\) this statement was already
morally known: the repository's own README anticipated that the Route 001
certificate "may reproduce a consequence of already published zero
verification," and B2–B3 make that folklore precise — with the bonus that
the previously untouchable region \([0, 11)\), where \(Q_1\) is of order
\(e^{-200}\) and no feasible prime-side computation can certify the sign,
falls to the same argument for free. The finite sweep retains independent
value as a *prime-side* verification that does not consume I2. The
genuinely load-bearing new pieces on the full line are the tail theorem
(I4) and the assembly itself.

## Lemma B5 (heat propagation)

For \(0 < a < 1\), set \(s = \tfrac1{4a} - \tfrac14 > 0\). For every complex
center \(\gamma\) with \(|\operatorname{Im}\gamma| < \tfrac12\), the exact
Gaussian convolution identity

$$
\sqrt a\,e^{-a(\gamma - t)^2}
=\int_{\mathbb R} K_s(t-u)\,e^{-(\gamma-u)^2}\,du,
\qquad
K_s(v)=\frac{e^{-v^2/(4s)}}{\sqrt{4\pi s}},
$$

holds (absolutely convergent; direct completion of the square, valid for
complex \(\gamma\)). Summing over zeros and interchanging sum and integral
(justified by dominated convergence: the zero-counting bound I3 against
Gaussian decay) gives

$$
\sqrt a\,Q_a(t)\;=\;\big(K_s * Q_1\big)(t).
$$

This is the integrated form of the Route 005 heat identity (I5), in the
benign (broadening) direction.

## Theorem B6 (broad-scale positivity)

By Theorem B4, \(Q_1\) is continuous, strictly positive on \(\mathbb R\).
Convolution with the strictly positive kernel \(K_s\) preserves strict
positivity, so by Lemma B5:

$$
\boxed{\;Q_a(t) > 0 \quad \text{for every } 0 < a \le 1
\text{ and every } t \in \mathbb R.\;}
$$

## Interpretation

1. **Exact frontier with Route 002.** Route 002 proved that positive
   mixtures of the fixed-scale family generate precisely the scales
   \(0 < a \le 1\) and cannot reach \(a > 1\). Theorem B6 shows positivity
   in fact *holds* on that entire reachable region, unconditionally. The
   two results together draw a sharp line: everything at \(a \le 1\) is
   settled and RH-free; every remaining question of this program lives at
   \(a > 1\), where (per the cycle-1 heat analysis) any propagation
   argument must run backward and must consume zeta-specific input.

2. **Consistency with de Bruijn–Newman.** The \(a \le 1\) direction is the
   forward-flow direction that de Bruijn's 1950 theorems make benign; the
   \(a > 1\) barrier is the direction whose genericity Rodgers–Tao's
   \(\Lambda \ge 0\) forecloses. The theorem lands exactly where that
   literature says the boundary must be.

3. **Not a step toward proving RH by itself.** The family
   \(\{h_{a,t}: a \le 1\}\) is strictly inside the cone where positivity
   was reachable without RH content. The theorem's research value is
   sharpening the boundary and retiring the broad half of the parameter
   space permanently.

## Dependencies, falsification, honesty

- **Falsifiable points:** any error in the covering distance (B2), the
  counting constant (B3), the complex-center convolution identity (B5), or
  the tail theorem (I4). A single rigorous negative value of \(Q_a(t)\)
  with \(a \le 1\) would disprove RH via B1 — none is expected.
- **Conditional links:** Theorem B4 on \(|t| \ge 2000\) inherits the
  candidate status of I4 (repaired 28 Jul; awaiting the auditing
  collaborator's re-review). Everything else rests on published theorems
  plus exact identities machine-checked in this repository.
- **Supporting script:** `tools/broad_scale_support.py` (covering
  distance, tail constant, numerical check of Lemma B5 at sample points).
- **Not established:** anything at \(a > 1\); positivity for the
  pole-neutral convolution-square Weil class; RH.

## Primary sources

- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloquium
  Publications 53 (2004), Theorem 5.12 (explicit formula).
- D. Platt, T. Trudgian, *The Riemann hypothesis is true up to
  3·10^12*, Bull. LMS 53 (2021): https://arxiv.org/abs/2004.09765
- R. Backlund, *Über die Nullstellen der Riemannschen Zetafunktion* (1918);
  T. Trudgian, *An improved upper bound for the argument of the Riemann
  zeta-function on the critical line II*, J. Number Theory 134 (2014).
- B. Rodgers, T. Tao, *The de Bruijn–Newman constant is non-negative*,
  Forum of Math, Pi 8 (2020).
- Repository: `docs/ROUTE_001_TAIL_THEOREM.md`,
  `docs/ROUTE_005_ALL_SCALE_FALSIFICATION.md`,
  `docs/ROUTE_002_GAUSSIAN_CONE_OBSTRUCTION.md`.
