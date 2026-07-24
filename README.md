# Is every non-trivial zero of the Riemann zeta function on the critical line?

## The question

> **Does every non-trivial zero \(\rho\) of the Riemann zeta function satisfy**
>
> # \(\operatorname{Re}(\rho)=\tfrac12\)?

This is the **Riemann Hypothesis (RH)**. It remains unsolved.

## Mission of this repository

Use collaborating humans and AI systems to investigate the question above.

The intended outcome is one of:

1. a valid proof of RH;
2. a valid counterexample disproving RH; or
3. a rigorously justified new intermediate result that materially advances one
   of those goals.

This is intentionally ambitious. No current file in this repository proves or
disproves RH.

## Required questions for every proposed approach

Before doing substantial work, answer:

1. **What exact claim are you trying to prove?**
2. **If the claim is proved, does it prove RH, disprove RH, or only establish an
   intermediate result? Show the logical implication.**
3. **What part is genuinely new rather than a known theorem, reformulation, or
   finite verification?**
4. **What is the first step that is not currently proved?**
5. **What observation could falsify the approach early?**

Put each distinct approach on its own branch or pull request. Record failed
approaches as carefully as successful ones so later collaborators do not repeat
them.

## Current research status

The repository began with an AI-generated Gaussian/Guinand–Weil computation.
It produced a reproducible finite interval data set, but subsequent review
showed that this route currently proves far less than RH and may reproduce a
consequence of already published zero verification.

That work is preserved as an **explored route**, not as the mission of the
repository and not as a claimed advance toward RH. See
[RESEARCH_MAP.md](RESEARCH_MAP.md).

## Start here

- Humans: read [RESEARCH_MAP.md](RESEARCH_MAP.md) and
  [NEXT_STEPS.md](NEXT_STEPS.md).
- AI assistants: also follow [AGENTS.md](AGENTS.md).
- Historical Gaussian materials remain under `docs/`, `src/`, `data/`, and
  `tools/`.

## Standards

- Never label a known equivalence as a proof.
- Never extrapolate a finite computation to an infinite statement without a
  proved bridge.
- State assumptions explicitly.
- Distinguish proof, rigorous computation, numerical evidence, heuristic, and
  speculation.
- Prefer primary sources.
- Treat a discovered flaw or dead end as useful progress.
- Require independent adversarial review of any claimed breakthrough.
