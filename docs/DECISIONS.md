# Repository decisions

This file records durable process decisions. Mathematical route status belongs in
`CURRENT_STATE.md` and route documents.

## 2026-07-29 — Use bounded agent context

**Decision:** AI agents must not begin by reviewing the entire repository or all
open pull requests.

**Reason:** repeated repository-wide orientation consumes substantial model
usage, duplicates prior audits, and encourages agents to continue impressive
later conclusions before checking the earliest unsupported step.

**Implementation:**

- `docs/CURRENT_STATE.md` is the concise authoritative orientation document.
- `AGENTS.md` contains stable rules rather than full project history.
- Every task should be a GitHub issue naming one exact claim and an explicit
  input list.
- The reviewed baseline identifies which history is already summarized.
- Agents inspect only relevant changes after that baseline unless an older claim
  is specifically named.
- Route-specific status and instruction files may narrow context further.
- Completed tasks leave a handoff of no more than 250 words.

**Consequence:** an agent may request one additional file when the assigned task
cannot be completed from the listed inputs, but it must explain why that file is
necessary. It must not silently expand into a whole-repository review.

## 2026-07-29 — Separate invention from verification

**Decision:** the same agent output must not be treated as both the invention and
independent certification of a candidate theorem.

**Reason:** agreement within one generated chain, or among agents sharing the
same context and assumptions, is not independent mathematical verification.

**Implementation:** use narrow roles such as explanation, adversarial proof
audit, literature/dependency check, and independent computation reproduction.
