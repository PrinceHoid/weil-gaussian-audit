#!/usr/bin/env python3
"""Exact symbolic verification of the Route 002 separator identities.

Verifies, in exact arithmetic (sympy), every identity used by
docs/ROUTE_002_GAUSSIAN_CONE_OBSTRUCTION.md and the Lambda_c strengthening
recorded in docs/ROUTE_003_COUNTABLE_DETERMINING_FAMILIES.md:

  1. integral(h_t) = 2*sqrt(pi) and h_t(0) = 2*exp(-t^2), hence
     Lambda(h_t) = 2*sqrt(pi)*(1 - exp(-t^2)) >= 0 for all real t;
  2. Lambda(G_a) = sqrt(pi)*(a^(-1/2) - 1) < 0 for every a > 1;
  3. Lambda_c(h_t) = sqrt(pi)*(2 - exp(-(c-t)^2) - exp(-(c+t)^2)) >= 0
     for all real c and t;
  4. the positive-mixture identity
     integral_t exp(-beta*t^2) exp(-(r-t)^2) dt
       = sqrt(pi/(beta+1)) * exp(-(beta/(beta+1)) r^2),
     whose scale map a = beta/(beta+1) is increasing with range (0, 1):
     positive location mixing broadens Gaussians and never sharpens them.

Evidence level: exact algebraic derivation, machine-checked. This script does
NOT verify the topological step (continuity of Lambda_c on Schwartz space and
passage to the closed cone) and is corroboration, not human verification.
"""
from __future__ import annotations

import sympy as sp

r, t, c = sp.symbols("r t c", real=True)
a = sp.symbols("a", positive=True)
beta = sp.symbols("beta", positive=True)

h_t = sp.exp(-((r - t) ** 2)) + sp.exp(-((r + t) ** 2))


def lam(f: sp.Expr, at_point: sp.Expr = sp.Integer(0)) -> sp.Expr:
    """Lambda_c(f) = integral_R f(r) dr - sqrt(pi) * f(c)."""
    return sp.integrate(f, (r, -sp.oo, sp.oo)) - sp.sqrt(sp.pi) * f.subs(r, at_point)


def check(label: str, expr: sp.Expr, claimed: sp.Expr) -> None:
    diff = sp.simplify(expr - claimed)
    if diff != 0:
        raise SystemExit(f"FAILED {label}: residual {diff}")
    print(f"verified {label} = {claimed}")


check("integral(h_t)", sp.integrate(h_t, (r, -sp.oo, sp.oo)), 2 * sp.sqrt(sp.pi))
check("h_t(0)", h_t.subs(r, 0), 2 * sp.exp(-(t**2)))
check("Lambda(h_t)", lam(h_t), 2 * sp.sqrt(sp.pi) * (1 - sp.exp(-(t**2))))
print("  >= 0 for real t because exp(-t^2) <= 1")

check("Lambda(G_a)", lam(sp.exp(-a * r**2)), sp.sqrt(sp.pi) * (a ** sp.Rational(-1, 2) - 1))
print("  < 0 for every a > 1 because a^(-1/2) < 1")

check(
    "Lambda_c(h_t)",
    lam(h_t, at_point=c),
    sp.sqrt(sp.pi) * (2 - sp.exp(-((c - t) ** 2)) - sp.exp(-((c + t) ** 2))),
)
print("  >= 0 for real c, t because each exponential is <= 1")

check(
    "mixing identity",
    sp.integrate(sp.exp(-beta * t**2) * sp.exp(-((r - t) ** 2)), (t, -sp.oo, sp.oo)),
    sp.sqrt(sp.pi / (beta + 1)) * sp.exp(-(beta / (beta + 1)) * r**2),
)
assert sp.limit(beta / (beta + 1), beta, 0) == 0
assert sp.limit(beta / (beta + 1), beta, sp.oo) == 1
assert sp.simplify(sp.diff(beta / (beta + 1), beta) - 1 / (beta + 1) ** 2) == 0
print("  scale map a = beta/(beta+1) is increasing with range (0, 1)")

print("\nAll Route 002 identities verified in exact symbolic arithmetic.")
