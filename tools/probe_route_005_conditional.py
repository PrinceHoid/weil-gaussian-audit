#!/usr/bin/env python3
"""Preregistered conditional forecast for Route 005.

This is deliberately NOT an unconditional evaluation of the prime-side
Guinand--Weil functional.  It inserts a short list of published critical-line
zero ordinates into the RH-side Gaussian sum in order to:

1. forecast the scale and sign expected at the eight preregistered points;
2. test the naive pointwise monotonicity of G(a,t) = sqrt(a) Q_a(t);
3. catch normalization errors before any rigorous prime-side implementation.

Omitted-zero and rounding errors are not certified here.
"""

from decimal import Decimal, getcontext


getcontext().prec = 100

D = Decimal

# First three positive ordinates, used as non-certified decimal inputs.
ZEROS = (
    D("14.134725141734693790457251983562470270784257115699"),
    D("21.022039638771554992628479593896902777334340524902"),
    D("25.010857580145688763213790992562821818659549672558"),
)

A_VALUES = (D(2), D(4))
T_VALUES = (D(0), D(11), D("14.1347"), D("17.58"))


def zero_side_q(a: Decimal, t: Decimal) -> Decimal:
    total = D(0)
    for gamma in ZEROS:
        total += (-a * (gamma - t) ** 2).exp()
        total += (-a * (gamma + t) ** 2).exp()
    return D(2) * total


def zero_side_d_sqrt_a_q_da(a: Decimal, t: Decimal) -> Decimal:
    """Derivative of sqrt(a) times the truncated RH-side sum."""
    total = D(0)
    half_over_a = D(1) / (D(2) * a)
    for gamma in ZEROS:
        for displacement in (gamma - t, gamma + t):
            total += (
                half_over_a - displacement**2
            ) * (-a * displacement**2).exp()
    return D(2) * a.sqrt() * total


def scientific(x: Decimal, digits: int = 14) -> str:
    return f"{x:.{digits}E}"


print("scope=conditional truncated zero-side forecast; not an RH test or certificate")
print("a,t,Q_truncated,d_da(sqrt(a)Q_truncated),naive_monotonicity")
for a in A_VALUES:
    for t in T_VALUES:
        q = zero_side_q(a, t)
        derivative = zero_side_d_sqrt_a_q_da(a, t)
        monotonicity = "passes-at-point" if derivative >= 0 else "fails-at-point"
        print(
            ",".join(
                (
                    str(a),
                    str(t),
                    scientific(q),
                    scientific(derivative),
                    monotonicity,
                )
            )
        )


