# Route 005 cycle 5 — The frontier at a = 3.4 and 3.45, and the corrected wall

**Status:** rigorously proved reduction lemmas + computationally certified
sieve, pending human review. Labels per result at the end.

## Headline

1. **Diagnosis (the exact failing inequality).** The cycle-3 failure at
   \(a = 3.4\) was dominated by prime-tail slack, not by a real deficit:
   at cutoff \(N_P = 5\cdot10^4\) the Lemma-N2 tail bound contributes
   \(0.405\) to \(S_{3.4}\) while the true remainder is \(\approx 0.03\).
   Recomputing with \(N_P = 3\cdot10^5\) gives
   \(S_{3.4} \le 13.18756143\), and the **plain cycle-3 pipeline then
   certifies \(a = 3.4\) directly**: \(M_{3.4}(T_F) \ge 0.15807527 > 0\),
   so the tail theorem holds from \(T_F = 3\cdot10^{12}-100\) on, and with
   the scale-window theorem, \(Q_{3.4}(t) > 0\) for every real \(t\).
2. **The first real wall and its crossing.** At \(a = 69/20 = 3.45\) the
   uniform bound fails, and *not* merely through bound slack: recomputing
   the prime sum to \(N_P = 2\cdot10^6\) (rigorous tail \(\le 0.003\))
   gives \(2S_{3.45} = 26.89901323\) against
   \(\Omega(T_F-4) \le 26.8917514\), a **true** margin of \(-0.00726\)
   (our certified version: \(S_{69/20} \le 13.49727878\),
   \(M_{69/20}(T_F) \ge -0.031227335\)). By Proposition O1 no
   uniform-in-\(t\) estimate can remove such a deficit. The height-coupled
   sieve below closes it: **\(Q_{69/20}(t) > 0\) for every real \(t\)** —
   the first certification beyond the reach of the absolute-value bound.
   Heat propagation extends positivity to every \(0 < a \le 3.45\).
   The true uniform crossing therefore lies in \((3.4,\ 3.45)\).
3. **The next wall, with exact constants.** At \(a = 3.5\):
   \(2S_{3.5} \le 27.6259\) vs \(\Omega(T_F-4) \ge 26.8918\); sieve budget
   \(\tau(3.5) = 0.3671\), tail takeover at \(T_\mathrm{END} \approx 7\cdot10^{12}\),
   \(\approx 4.4\cdot10^{11}\) anchor intervals with much wider per-prime
   tolerances — feasible in principle with a hierarchical in-C second
   stage, not attempted in this run.

## The certified chain at a = 69/20

| segment | instrument | margin |
|---|---|---|
| \(\lvert t\rvert \le T_F = 3\cdot10^{12}-100\) | scale-window theorem (cycle 3, all \(a \ge 1\)) | factor \(e^{7493}\) |
| \(T_F \le \lvert t\rvert \le 4.5\cdot10^{12}\) | **phase–height sieve (this document)** | \(\mathrm{Pen} \ge \tau = 0.051404112\) |
| \(\lvert t\rvert \ge 4.5\cdot10^{12}\) | cycle-3 tail machinery | \(M_{69/20} \ge 0.091932473\) |

No verified-zero input enters the sieve segment; its inputs are integer
arithmetic and the frozen prime weights. The uniform-cancellation no-go
(Proposition O1) is respected: the saving is height-coupled.

## Lemma S1 (penalty budget)

Let \(\mathrm{Pen}(t) := \sum_{n\ge2} w_a(n)(1 - \cos(t\log n)) \ge 0\),
\(w_a(n) = \Lambda(n)n^{-1/2}e^{-(\log n)^2/(4a)}\). For
\(t \in [T_F, T_\mathrm{END}]\) and \(a = 69/20\):

\[
\mathrm{Pen}(t) \ge \tau := 0.051404112
\quad\Longrightarrow\quad Q_a(t) > 0 .
\]

**Proof.** \(F_a(t) = S_a - \mathrm{Pen}(t)\), where \(F_a\) is the prime
cosine sum. Repeating the cycle-3 assembly with \(S_a - \mathrm{Pen}(t)\)
in place of \(S_a\), and \(\Omega(t-4) \ge \Omega(T_F-4)\) (monotonicity),
positivity holds whenever
\(\mathrm{Pen}(t) \ge \tfrac{\sqrt{\pi a}}2(-M_a(T_F))\). All constants
interval-certified; \(\tau\) is the padded upper bound. ∎

## Lemma S2 (anchor on powers of two)

\(\mathrm{Pen}(t) \ge \mathrm{Pen}_2(\theta_2(t))\) with
\(\mathrm{Pen}_2(\theta) = \sum_k w_a(2^k)(1-\cos k\theta)\),
\(\theta_2(t) = t\log2 \bmod 2\pi\) (signed). Bisection at headroom
\(1.25\tau\) plus a Lipschitz grid verify
\(\mathrm{Pen}_2(\theta) \ge \tau\) for all
\(\theta_{2\max} \le |\theta| \le \pi\), \(\theta_{2\max} = 0.12740139\).
Hence every potentially-bad \(t\) lies in
\(I_{m_2} = \{t: |t\log2 - 2\pi m_2| \le \theta_{2\max}\}\) for an integer
\(m_2 \in [330953400217,\ 496430100345]\) (165.5 billion intervals). ∎

## Lemma S3 (per-interval clearing test)

For \(t \in I_{m_2}\): \(\theta_p(t) = 2\pi\,\mathrm{frac}(m_2\alpha_p)
+ \theta_2\alpha_p \bmod 2\pi\), \(\alpha_p = \log p/\log2\). With
\(d_p(m_2)\) the circular distance of \(2\pi\,\mathrm{frac}(m_2\alpha_p)\)
from 0 and \(s_p = \theta_{2\max}\alpha_p + 10^{-6}\):

\[
\min_{t\in I_{m_2}} \mathrm{Pen}(t) \;\ge\;
L(m_2) := \sum_{p\in P_0} w_a(p)\big(1-\cos(\max(0, d_p(m_2)-s_p))\big),
\]

\(P_0\) = the 45 odd primes \(\le 199\); dropped terms are nonnegative, so
the restriction is conservative. \(L(m_2) \ge \tau\) clears \(I_{m_2}\). ∎

## Theorem S4 (sieve certificate)

`tools/phase_sieve.c` evaluates \(L(m_2) \ge \tau\) for every \(m_2\) in
range. Phase arithmetic is exact 64-bit modular arithmetic (initialization
by exact 128-bit multiply); the only model error is the initial rounding
of \(\alpha_p\), whose accumulated drift over the range is \(<10^{-7}\)
rad (independently measured at \(7.93\cdot10^{-8}\) rad against a
predicted maximum of \(8.45\cdot10^{-8}\) rad, i.e. \(12.6\times\) inside
the \(10^{-6}\) rad guard), absorbed into \(s_p\).
\(w_a(p)\) rounded down, \(\tau\) padded up,
\(1-\cos\) tabulated by per-arc lower bounds, floored index vs ceiled
sweep offset. Survivors go to stage 2
(`tools/phase_height_certificate.py`, 60-digit arithmetic, 64-cell
\(\theta_2\) subdivision, primes to 500). **Result: zero stage-1
survivors across all 165,476,700,129 intervals; stage 2 empty.** Hence
\(\mathrm{Pen} \ge \tau\) on \([T_F, T_\mathrm{END}]\) and
\(Q_{69/20}(t) > 0\) there. Independent checker:
`tools/verify_phase_height.py` (from-scratch reimplementation of the
phase model and clearing logic; random-interval revalidation; survivor
re-check).

For the record, the same pipeline had already been run at \(a = 17/5\)
with the loose budget \(\tau = 0.073396936\) inherited from the
\(N_P = 5\cdot10^4\) table: zero survivors there as well (a fortiori
consistent with the direct certification of 3.4).

## Evidence labels

- **Rigorously proved:** Lemmas S1–S3; the direct certification of
  \(a = 17/5\) (interval arithmetic end to end); the tail-takeover and
  chaining; heat propagation to \(a \le 69/20\).
- **Computationally certified:** Theorem S4's sieve pass (exact integer
  phase arithmetic; conservatively rounded double comparisons with a
  \(10^{-6}\) guard on \(\tau\)).
- **Candidate (inherited):** the cycle-2/3 lemma stack (window theorem,
  \(\Omega\) bounds, heat identity) under its standing human-review
  obligation; nothing here upgrades it.
- **Heuristic:** the feasibility estimate for \(a = 3.5\) only.
- **Not claimed:** RH; positivity beyond \(a = 69/20\); any uniform
  prime-sum cancellation (impossible by Proposition O1); Theorem D.

## Reproduction

```
python tools/phase_height_certificate.py --a 17 5        # direct certification of 3.4
python tools/phase_height_certificate.py --a 69 20       # sieve certification of 3.45
python tools/verify_phase_height.py --a-num 69 --a-den 20 \
       --tau 0.051404112 --theta2max 0.12740139          # independent checks
```
