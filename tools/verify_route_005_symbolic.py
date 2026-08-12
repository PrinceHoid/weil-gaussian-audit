#!/usr/bin/env python3
"""Exact symbolic verification of the Route 005 cycle-1 identities.

Machine-checks, in exact arithmetic (sympy), every displayed identity in
docs/ROUTE_005_ALL_SCALE_FALSIFICATION.md:

  1. the scaled Fourier pair: under h(r) = integral g(u) exp(iru) du,
     h_{a,t} corresponds to g_{a,t}(u) = (pi*a)^(-1/2) exp(-u^2/(4a)) cos(tu);
  2. the exact scale identity 4a^2 d_a h + d_t^2 h + 2a h = 0 for h_{a,t};
  3. the heat-flow normalization: with tau = 1/(4a), each summand of
     sqrt(a) h_{a,t} satisfies d_tau = d_t^2 (increasing a is backward flow);
  4. the pole identity h_{a,t}(i/2) + h_{a,t}(-i/2) = 4 exp(a/4 - a t^2) cos(a t),
     matching the displayed pole term of Q_a(t);
  5. the derivative formula used by tools/probe_route_005_conditional.py:
     d/da [ sqrt(a) exp(-a D^2) ] = sqrt(a) (1/(2a) - D^2) exp(-a D^2).

Evidence level: exact algebraic machine check of the recorded derivation.
This is corroboration, not human verification, and says nothing about the
unproved parts of Route 005 (admissibility bridge, backward-heat invariant).
"""
from __future__ import annotations

import sympy as sp

r, t, u, x, tau, D = sp.symbols("r t u x tau D", real=True)
a = sp.symbols("a", positive=True)

h_at = sp.exp(-a * (r - t) ** 2) + sp.exp(-a * (r + t) ** 2)


def check(label: str, residual: sp.Expr) -> None:
    residual = sp.simplify(residual)
    if residual != 0:
        # push trig factors into exponentials before giving up
        residual = sp.simplify(sp.expand(residual.rewrite(sp.exp)))
    if residual != 0:
        raise SystemExit(f"FAILED {label}: residual {residual}")
    print(f"verified {label}")


# 1. Fourier pair: g(u) = (1/2pi) integral h(r) exp(-iur) dr
g_claimed = sp.exp(-u**2 / (4 * a)) * sp.cos(t * u) / sp.sqrt(sp.pi * a)
g_derived = sp.integrate(h_at * sp.exp(-sp.I * u * r), (r, -sp.oo, sp.oo)) / (2 * sp.pi)
check("g_{a,t}(u) = (pi a)^(-1/2) exp(-u^2/(4a)) cos(tu)", g_derived - g_claimed)
# The exact forward transform above, together with the Fourier inversion
# theorem on Schwartz space, already identifies (h_{a,t}, g_{a,t}) as the
# transform pair under the repository convention; no separate check needed.

# 2. exact scale identity
check(
    "4a^2 d_a h + d_t^2 h + 2a h = 0",
    4 * a**2 * sp.diff(h_at, a) + sp.diff(h_at, t, 2) + 2 * a * h_at,
)

# 3. heat-flow normalization: kernel form of sqrt(a) exp(-a(r-t)^2) at a = 1/(4 tau)
G = sp.sqrt(1 / (4 * tau)) * sp.exp(-((r - t) ** 2) / (4 * tau))
check("d_tau G = d_t^2 G for G = sqrt(a) exp(-a(r-t)^2), tau = 1/(4a)",
      sp.diff(G, tau) - sp.diff(G, t, 2))

# 4. pole identity
pole = h_at.subs(r, sp.I / 2) + h_at.subs(r, -sp.I / 2)
check(
    "h_{a,t}(i/2) + h_{a,t}(-i/2) = 4 exp(a/4 - a t^2) cos(a t)",
    sp.expand_complex(pole - 4 * sp.exp(a / 4 - a * t**2) * sp.cos(a * t)),
)

# 5. probe derivative formula
check(
    "d/da [sqrt(a) exp(-a D^2)] = sqrt(a) (1/(2a) - D^2) exp(-a D^2)",
    sp.diff(sp.sqrt(a) * sp.exp(-a * D**2), a)
    - sp.sqrt(a) * (1 / (2 * a) - D**2) * sp.exp(-a * D**2),
)

print("\nAll Route 005 cycle-1 identities verified in exact symbolic arithmetic.")
print("scope=recorded derivation only; admissibility bridge and backward-heat "
      "invariant remain open as stated in the route document")
