# External result — "More than two thirds of the zeros … lie on the critical line" (11 Aug 2026)

**Paper.** *More than two thirds of the zeros of the Riemann zeta function
lie on the critical line*, author: an Anthropic large language model
("CLAUDE"), dated 10 August 2026; problem posed and investigation guided by
Jarred Sumner; studied and communicated by Ralph Furman and Levent Alpöge.
35 pp., with a Lean 4 formalisation and symbolic checks (its Appendix B).

**Claims.** Unconditionally, `liminf N*₀(T,2T)/N(T,2T) ≥ 2/3` (Thm A); the
same proportion is *simple and on the line* (Thm B); `≥ 5/6` of zeros are
distinct (Thm C); optimising the test family gives 0.6725 / 0.6725 /
0.83625 (Thm D) and the same for Dirichlet L-functions (Thm E). Previous
unconditional records: 5/12 = 0.4166 on the line (Pratt–Robles–Zaharescu–
Zeindler 2020, in the Levinson line) and 0.6603 distinct (Wu 2015).

**Vetting (external to this repository).** The result is public and has
been examined by qualified human mathematicians: Levent Alpöge and Ralph
Furman studied it and take responsibility for its communication, and Brian
Conrey and Daniel Goldston examined it. It is accompanied by a Lean 4
formalisation (`anthropics/zeta-23-lean`), a provenance appendix and
process transcripts, and is also on arXiv (2511.20059). **It is treated
here as a vetted external theorem, not as a candidate.**

**Status here:** external work; not this repository's. Recorded because it
resolves — in general form — the precise obstruction Routes 001–005 spent
seven cycles circling. §3 records an independent mechanical reproduction of
its linear-algebraic core, done for our own understanding rather than to
adjudicate a result already under expert review.

## 1. The mechanism, in one paragraph

Weil's Hermitian form `W(f,g) = Σ_ρ m_ρ f̂(γ_ρ) conj(ĝ(γ_ρ))` is positive
on all of `C²_c(ℝ)` **iff** RH. Instead of asking for positivity, the paper
restricts `W` to a finite-dimensional Gabor family — modulated copies
`φ(u)e^{iτ_k u}` of one compactly supported window, centres equispaced
through `[T,2T]` at critical density `h = 2π/L` — and studies the `d×d`
matrix `G̃` of `W|_V`. Then:

- **(Z) inertia, not positivity.** Each distinct *on-line* point contributes
  a rank-one PSD form; each *off-line pair* `{ρ, 1−ρ̄}` contributes a
  **hyperbolic block `[[0,m],[m,0]]` of signature (1,1)**. By Sylvester's
  law (pull-back cannot raise the positive index, Lemma 3.1 — no
  injectivity needed) the off-line zeros add at most `p` to `n₊`.
- **(P) magnitude.** `tr G̃` and `‖G̃‖²_F` are Montgomery's first and second
  pair-correlation moments; both are mean values of Dirichlet polynomials
  of length `≤ T`, hence **unconditional**, evaluating to `N` and
  `(1/λ + λ/3)N`.
- **(L) linear algebra.** A rank–trace inequality (Lemma 3.2, via von
  Neumann's trace inequality) plays the role of the integrality step
  `m² ≥ 2m − 1`.

Assembly: `s ≥ 4N − 2N − (1/λ + λ/3)N = H(λ)N`, and `H(1) = 2/3`.

## 2. Why this matters *to this repository*

The single sentence that has governed every route here — `AGENTS.md`:
*"Never infer positivity from the zero-side Gaussian sum without explicitly
assuming RH"* — names the trap this paper escapes. Our own record:

| this repo | that paper |
|---|---|
| Cycle 4 (Thm G0/G3): RH ⟺ `Q_a(t) ≥ 0` for unbounded scales. Correct, and a dead end: positivity *is* RH-hard for this family. | Never asks for positivity. Asks for **inertia**, which is not RH-hard. |
| Cycle 6 (Thm D′): one off-line zero forces a negative **spike** in `Q_a` at an explicit `t*` — but needs an `O(1)` on-line window hypothesis, and is **vacuous** below `a ≈ 19.7`. | An off-line pair forces a **signature-(1,1) block** — no window hypothesis, no genericity, and *independent of the pair's depth* off the line (audit A2b). |
| Cycles 3/5: *buy* structural input with verified zeros (Platt–Trudgian), ceiling `a* ≈ 3.45`, cost doubly exponential in `a`. | Gets the structural input **free from the functional equation**: `ρ ↦ 1−ρ̄` is what makes the block hyperbolic. |

The comparison is unflattering to our program and worth stating plainly.
Cycle 6 detected off-line zeros by **magnitude** — a spike that must
outgrow a `log`-sized background, which is why the price came out as
`a ≳ 4 log log T` and why the certified frontier (`a = 3.45`) was nowhere
near it. The paper detects them by **sign structure** — an eigenvalue
count — which costs nothing. That is the whole difference, and it is the
"genuinely new mechanism" our Route 003 lesson demanded and none of our
cycles supplied.

**Independent corroboration of our wall.** The paper's restriction
`λ ≤ 1` is essential for exactly our reason: beyond bandwidth one, "the
off-diagonal prime sums would require information on prime pairs of
Hardy–Littlewood strength." That is our Proposition O1 (the uniform
absolute-value prime bound is globally sharp) seen from the other side.
Two independent programs hitting the same arithmetic wall is evidence the
wall is real.

**What is *not* invalidated.** Nothing here makes our results wrong; they
are a different and much weaker kind of statement (pointwise positivity of
one functional at one scale, versus a counting theorem). Route 002's cone
obstruction stands. Cycle 7's pole-neutral construction is orthogonal — the
paper's `Π_X` absorbs the pole terms, so pole-neutrality never arises.

## 3. Independent mechanical reproduction of the core

`tools/audit_two_thirds_paper.py` — 19 checks, all pass:

- **A1** Lemma 3.1 (inertia under pull-back), 300 random cases including
  deliberately rank-deficient `A`.
- **A2/A2b/A3/A3b** the off-line pair block: the two conjugate summands sum
  to `2m Re(x ȳ)`, its matrix is exactly `[[0,m],[m,0]]`, eigenvalues
  `±m`, and **the signature does not degrade with depth off the line**.
  *This is the step that replaces RH.*
- **A4/A4b** Lemma 3.2 (rank–trace), 4000 random cases at `c ∈ {½,1,2,3}`,
  plus the stated equality case (attained to `3.6e−15`).
- **A5** the counting descent to Prop 4.4(ii)/(iii), symbolically.
- **A6** Lemma 3.3 (thresholded Cauchy–Schwarz), 2000 cases.
- **A7** Lemma 2.2, the Gabor/Poisson sampling identity
  `Σ_k φ̂(τ−τ_k)² = aL²` with **no aliasing** — checked numerically to
  `5.5e−12` relative. This is what makes `tr P ≤ N_on` work.
- **A8** all constants and the assembly: `H(1)=2/3`, `H_d(1)=5/6`,
  `F(1)=3/4`, crossover at `3−√6`, `H` increasing on `(0,1]` (critical
  point `√3 > 1`, so `λ=1` is optimal), and `4−2−(1/λ+λ/3) = H(λ)`.
- **A9** Theorem D's `0.83625 = (1+0.6725)/2`.

**One correction, to our own test rather than the paper:** the first run
reported A3 as FAILED. The cause was in the audit script — `sympy` will not
evaluate `re()` on unevaluated complex symbols, so the comparison was
vacuous. With an explicit real/imaginary decomposition the identity is
exact. The paper was right; the check was wrong. Recorded because this
repository's rule is to publish failed checks, including its own.

**Not reproduced here** (cited literature and analysis beyond mechanical
checking; covered by the paper's own Lean formalisation and by its expert
review, not by us):

1. Montgomery's prime-side second moment and its **unconditional form**
   [Mon73; Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh 2024;
   Goldston–Suriajaya 2025/26] — the analytic core, on which
   `tr G̃ → N` and `‖G̃‖²_F → (1/λ+λ/3)N` rest.
2. Theorem 5.8's error terms, including the endpoint `λ = 1`.
3. The explicit-formula normalisation (its Appendix A).
4. The Montgomery–Vaughan generalised Hilbert inequality application.
5. The **0.68185 ceiling** for bandwidth-one certificates.

The distinction matters only for what this repository can claim to have
re-derived on its own: the linear-algebraic mechanism, in full, plus every
constant. The analytic inputs are Montgomery's and are attested elsewhere.

## 4. Can it be pushed farther?

Honest reading, given the paper's own Remark 1.1:

- **Within the method: nearly closed.** The stated ceiling for
  bandwidth-one, configuration-wise certificates is `0.68185`. Theorem A is
  at `0.6667`, Theorem D at `0.6725` — within `0.0094` of the ceiling.
  There is essentially nothing left to extract.
- **Beyond bandwidth one: the Hardy–Littlewood wall.** Reaching
  `0.70 / 0.80 / 0.90` needs pair-correlation support out to roughly
  `1.04 / 1.26 / 1.70`. This is the same wall our Prop O1 identified, and
  it is a major open problem, not an engineering gap.
- **Higher moments — the one genuinely open direction we can name.** The
  method reads only `tr G̃` and `‖G̃‖²_F`; the paper states its §3
  inequalities are sharp *given only those two moments and the block
  structure*. A third moment `tr G̃³` is therefore strictly more
  information and is not excluded by the stated optimality. But `tr G̃³`
  is a **triple** correlation of prime powers, so it plausibly meets the
  same Hardy–Littlewood-strength obstruction one level higher, and its
  unconditional evaluation is not in the literature. Anyone tempted should
  first check whether the diagonal terms of `tr G̃³` can be isolated
  unconditionally at bandwidth `λ ≤ 1`; if they cannot, the direction
  closes immediately and cheaply. That is the recommended next falsification
  test, in this repository's usual style.

## 5. Consequence for this repository's plan

Route 005's remaining ambitions should be re-scoped. Its positivity
program cannot produce counting theorems of this kind, and the mechanism
that does — inertia in a finite compression — is now published and does
not need our certified scales. The repository's honest remaining assets are
the audit tooling and the negative results (Route 002's cone obstruction,
Prop O1, cycle 6's pricing), which retain their value as a record of what
does *not* work and why.

## Primary sources

- The paper (PDF supplied 11 Aug 2026); arXiv:2511.20059; Lean 4
  formalisation at `github.com/anthropics/zeta-23-lean`.
- H. L. Montgomery, *The pair correlation of zeros of the zeta function*
  (1973).
- S. Baluyot, D. A. Goldston, A. I. Suriajaya, C. L. Turnage-Butterbaugh
  (2024); D. A. Goldston, A. I. Suriajaya (2025, 2026).
- A. Weil (1952); E. Bombieri, *Remarks on Weil's quadratic functional*
  (2000) — the negative index of truncations counting off-line zeros.
- N. Levinson (1974); J. B. Conrey (1989); Pratt–Robles–Zaharescu–Zeindler
  (2020); Wu (2015).
