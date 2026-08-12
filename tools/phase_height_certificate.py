#!/usr/bin/env python3
"""Phase-height certificate for a = 3.4 on the dangerous window.

Implements the height-coupled reduction demanded by Route 005 cycle 4
(docs/ROUTE_005_PHASE_HEIGHT_CERTIFICATE.md). Overview:

  Positivity of Q_a(t) on [T_F, T_END] (a = 17/5, T_F = 3e12-100,
  T_END = 4.5e12) fails only if the alignment penalty

      Pen(t) = sum_n w_a(n) (1 - cos(t log n)) ,   w_a(n) = Lambda(n)/sqrt(n) e^{-(log n)^2/(4a)}

  satisfies Pen(t) < tau, where tau is computed rigorously below from the
  cycle-3 machinery (Lemma S1). Since Pen(t) >= Pen_2(theta_2) using only
  powers of two (Lemma S2), any bad t lies in an interval I_{m2} around
  2*pi*m2/log 2 with |theta_2| <= theta2max (Lemma S3). The C sieve
  (tools/phase_sieve.c, generated constants in phase_sieve_constants.h)
  enumerates every m2 and clears each interval by proving

      sum_{p in P0} w_a(p) (1 - cos(theta_p)) >= tau   throughout I_{m2},

  using exact 64-bit fixed-point phase accumulators (the accumulator model
  is exact modular arithmetic; the only error is the initial rounding of
  alpha_p = log p / log 2, whose accumulated drift over the whole range is
  < 1e-7 rad and is absorbed into the sweep slack s_p). Surviving m2 are
  re-examined here at stage 2 with mpmath interval-grade arithmetic, finer
  theta_2 subdivision, and more primes. Empty final survivor list =>
  Q_a(t) > 0 on [T_F, T_END].

All constants written for the C stage are rounded conservatively:
w_p down, tau up, s_p up, and the (1-cos) lookup table stores lower
bounds. Doubles in C carry ~1e-16 relative error; a 1e-6 absolute guard
is added to tau for the C comparison.

Run: python tools/phase_height_certificate.py [--skip-sieve]
"""
from __future__ import annotations

import os
import subprocess
import sys
import time

import mpmath as mp
from mpmath import iv
from sympy import primerange

iv.dps = 30
mp.mp.dps = 50

A_NUM, A_DEN = 17, 5                      # a = 3.4 exactly; override with --a NUM DEN
if "--a" in sys.argv:
    i = sys.argv.index("--a")
    A_NUM, A_DEN = int(sys.argv[i + 1]), int(sys.argv[i + 2])
H = 3 * 10**12
T_F = H - 100
T_END = 45 * 10**11                        # 4.5e12; override with --tend T
if "--tend" in sys.argv:
    T_END = int(sys.argv[sys.argv.index("--tend") + 1])
N_PRIME = 300_000
N_SERIES = 100_000
SIEVE_PRIMES = [5, 3, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
                113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
                179, 181, 191, 193, 197, 199]
STAGE2_PMAX = 500
HERE = os.path.dirname(os.path.abspath(__file__))

a_iv = iv.mpf(A_NUM) / A_DEN

try:
    EULER = +iv.euler
except AttributeError:
    EULER = iv.mpf(["0.577215664901532860606512090082",
                    "0.577215664901532860606512090083"])
LOGPI = iv.log(iv.pi)


def omega_lower(r: int) -> mp.mpf:
    """Lemma N1' lower bound for Omega(r), r a positive even integer."""
    series = iv.mpf(0)
    for n in range(N_SERIES):
        fn = 4 * n + 1
        series += iv.mpf(1) / (n + 1) - iv.mpf(4 * fn) / (fn * fn + 4 * r * r)
    c = (r * r) // 4
    M = c - 1
    intN = (iv.log(iv.mpf(M + 1)) - iv.log(iv.mpf(N_SERIES + 1))
            - (iv.log(iv.mpf((4 * M + 1) ** 2 + 16 * c))
               - iv.log(iv.mpf((4 * N_SERIES + 1) ** 2 + 16 * c))) / 2)
    beyond = iv.mpf(3) / (4 * (M - 1)) + iv.log(1 + iv.mpf(c) / (M - 1) ** 2) / 2
    return mp.mpf((-EULER - LOGPI + series + intN - beyond).a)


def S_upper():
    s = iv.mpf(0)
    for p in primerange(2, N_PRIME + 1):
        lp = iv.log(p)
        pk = p
        while pk <= N_PRIME:
            u = iv.log(pk)
            s += lp / iv.sqrt(pk) * iv.exp(-u * u / (4 * a_iv))
            pk *= p
    v0 = iv.log(iv.mpf(N_PRIME)) - a_iv
    tail = iv.exp(a_iv / 4) * iv.exp(-v0 * v0 / (4 * a_iv)) * (2 * a_iv + 2 * a_iv * a_iv / v0)
    return iv.mpf(mp.mpf((s + tail).b))


def M_bound(omega_lo: mp.mpf, S_ub: iv.mpf):
    q_a = iv.exp(-16 * a_iv) / (4 * a_iv)
    pole = 4 * iv.exp(a_iv / 4) / (a_iv * iv.mpf(T_F) ** 2)
    omega0 = -EULER - iv.pi / 2 - 3 * iv.log(2) - LOGPI
    arch_lo = (iv.mpf(omega_lo) * (iv.sqrt(iv.pi / a_iv) - q_a) + omega0 * q_a) / iv.pi
    return arch_lo - (2 / iv.sqrt(iv.pi * a_iv)) * S_ub - pole


def w_at(n: int) -> iv.mpf:
    from sympy import factorint
    f = factorint(n)
    assert len(f) == 1
    p = next(iter(f))
    u = iv.log(n)
    return iv.log(p) / iv.sqrt(n) * iv.exp(-u * u / (4 * a_iv))


def pen2_lower(theta: iv.mpf) -> iv.mpf:
    """Penalty from powers of two, interval-valued."""
    s = iv.mpf(0)
    k, pk = 1, 2
    while pk <= N_PRIME:
        s += w_at(pk) * (1 - iv.cos(k * theta))
        k += 1
        pk *= 2
    return s


def main() -> int:
    t0 = time.time()
    print("[1] rigorous budget tau ...")
    om_TF = omega_lower(T_F - 4)
    S_ub = S_upper()
    M_TF = M_bound(om_TF, S_ub)
    a_str = f"{A_NUM}/{A_DEN}"
    tau = mp.mpf((iv.sqrt(iv.pi * a_iv) / 2 * (-M_TF)).b) + mp.mpf("1e-6")
    print(f"    Omega({T_F - 4}) >= {mp.nstr(om_TF, 12)}   S_{a_str} <= {mp.nstr(mp.mpf(S_ub.b), 10)}")
    print(f"    M_{a_str}(T_F) in [{mp.nstr(mp.mpf(M_TF.a), 8)}, {mp.nstr(mp.mpf(M_TF.b), 8)}]")
    if mp.mpf(M_TF.a) > 0:
        print(f"\nDIRECT CERTIFICATION: M_{a_str}(T_F) >= {mp.nstr(mp.mpf(M_TF.a), 8)} > 0.")
        print(f"The plain tail theorem holds from T_F on; chained with the scale-window")
        print(f"theorem (|t| <= T_F), Q_{a_str}(t) > 0 for every real t. No sieve needed.")
        return 0
    print(f"    tau = {mp.nstr(tau, 8)}  (Pen(t) >= tau  =>  Q_{a_str}(t) > 0)")
    assert mp.mpf(M_TF.a) < 0 < tau

    print("[2] tail takeover at T_END ...")
    om_END = omega_lower(T_END - 4)
    M_END = M_bound(om_END, S_ub)
    print(f"    Omega({T_END - 4}) >= {mp.nstr(om_END, 12)}  =>  M_{a_str}(T_END) >= {mp.nstr(mp.mpf(M_END.a), 8)}")
    assert mp.mpf(M_END.a) > 0, "tail theorem must hold unconditionally at T_END"

    print("[3] theta2 anchor ...")
    # bisect at 1.25*tau so the boundary check below has headroom; the sieve
    # then uses the slightly wider anchor window (conservative direction)
    tau_anchor = tau * mp.mpf("1.25")
    lo, hi = iv.mpf(0), iv.mpf(1)
    for _ in range(50):
        mid = (lo + hi) / 2
        if mp.mpf(pen2_lower(mid).a) < tau_anchor:
            lo = mid
        else:
            hi = mid
    theta2max = mp.mpf(hi.b)
    # Pen_2 >= tau on [theta2max, pi]: grid + Lipschitz (L2 = sum k w_{2^k})
    L2 = iv.mpf(0)
    k, pk = 1, 2
    while pk <= N_PRIME:
        L2 += k * w_at(pk)
        k += 1
        pk *= 2
    L2 = mp.mpf(L2.b)
    step = mp.mpf("0.001")
    th = theta2max
    ok = True
    while th < mp.pi:
        v = mp.mpf(pen2_lower(iv.mpf(th)).a)
        if v - L2 * step < tau:
            ok = False
            break
        th += step
    assert ok, "Pen_2 must exceed tau outside the anchor window"
    print(f"    theta2max = {mp.nstr(theta2max, 8)} rad; Pen_2 >= tau verified on [theta2max, pi]")

    m2_lo = int(mp.floor(T_F * mp.log(2) / (2 * mp.pi)))
    m2_hi = int(mp.ceil(T_END * mp.log(2) / (2 * mp.pi))) + 1
    print(f"    m2 in [{m2_lo}, {m2_hi}]  ({m2_hi - m2_lo:.3e} intervals)")

    print("[4] emitting C constants ...")
    tw = 2 * theta2max / mp.log(2)          # width of I_{m2} in t
    lines = [
        "#pragma once",
        "#include <stdint.h>",
        f"#define M2_LO {m2_lo}ULL",
        f"#define M2_HI {m2_hi}ULL",
        f"#define NPRIMES {len(SIEVE_PRIMES)}",
        f"#define TAU {mp.nstr(tau * (1 + mp.mpf('1e-9')) + mp.mpf('1e-6'), 20)}",
    ]
    alphas, weights, sweeps = [], [], []
    for p in SIEVE_PRIMES:
        alpha = mp.log(p) / mp.log(2)
        frac = alpha - mp.floor(alpha)
        A_fixed = int(mp.floor(frac * mp.mpf(2) ** 64 + mp.mpf("0.5")))
        alphas.append(A_fixed % (1 << 64))
        wp = mp.mpf(w_at(p).a) - mp.mpf("1e-12")           # lower bound
        weights.append(wp)
        s_p = theta2max * alpha + mp.mpf("1e-6")           # sweep + drift slack (rad)
        sweeps.append(s_p)
    lines.append("static const uint64_t ALPHA[NPRIMES] = {"
                 + ",".join(f"{x}ULL" for x in alphas) + "};")
    lines.append("static const double W[NPRIMES] = {"
                 + ",".join(mp.nstr(x, 17) for x in weights) + "};")
    lines.append("static const double SWEEP[NPRIMES] = {"
                 + ",".join(mp.nstr(x, 17) for x in sweeps) + "};")
    with open(os.path.join(HERE, "phase_sieve_constants.h"), "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"    wrote phase_sieve_constants.h ({len(SIEVE_PRIMES)} primes)")

    if "--skip-sieve" in sys.argv:
        print("    (sieve skipped)")
        return 0

    print("[5] compiling and running C sieve ...")
    src = os.path.join(HERE, "phase_sieve.c")
    exe = os.path.join(HERE, "phase_sieve")
    subprocess.check_call(["cc", "-O3", "-march=native", "-o", exe, src, "-lm"])
    t1 = time.time()
    ncpu = os.cpu_count() or 4
    total = m2_hi - m2_lo + 1
    chunk = total // ncpu + 1
    procs = []
    for i in range(ncpu):
        lo_i = m2_lo + i * chunk
        hi_i = min(m2_lo + (i + 1) * chunk - 1, m2_hi)
        if lo_i > hi_i:
            break
        procs.append(subprocess.Popen([exe, str(lo_i), str(hi_i)],
                                      stdout=subprocess.PIPE, text=True))
    survivors = []
    for pr in procs:
        out, _ = pr.communicate()
        if pr.returncode != 0:
            raise SystemExit("sieve chunk failed")
        for line in out.splitlines():
            if line.startswith("SURVIVOR "):
                survivors.append(int(line.split()[1]))
    survivors.sort()
    with open(os.path.join(HERE, "phase_sieve_survivors.txt"), "w") as f:
        f.write("\n".join(map(str, survivors)))
    print(f"    sieve done in {time.time() - t1:.0f}s on {len(procs)} cores; "
          f"stage-1 survivors: {len(survivors)}")

    print("[6] stage-2 refinement ...")
    mp.mp.dps = 60
    pen_primes = [(p, mp.mpf(w_at(p).a)) for p in primerange(3, STAGE2_PMAX)]
    two_pi = 2 * mp.pi
    unresolved = []
    NCELL = 64
    for m2 in survivors:
        base_t = two_pi * m2 / mp.log(2)
        cleared_all = True
        for j in range(NCELL):
            th_lo = -theta2max + 2 * theta2max * j / NCELL
            th_hi = th_lo + 2 * theta2max / NCELL
            pen_min = mp.mpf(0)
            for p, wp in pen_primes:
                lp = mp.log(p)
                ph_lo = (base_t + th_lo / mp.log(2)) * lp
                ph_hi = (base_t + th_hi / mp.log(2)) * lp
                # distance of the phase arc from 0 mod 2pi (rigorous via mp at 60 dps)
                c_lo = ph_lo - two_pi * mp.floor(ph_lo / two_pi + mp.mpf("0.5"))
                width = ph_hi - ph_lo
                lo_edge, hi_edge = c_lo, c_lo + width
                if lo_edge <= 0 <= hi_edge:
                    d = mp.mpf(0)
                else:
                    d = min(abs(lo_edge), abs(hi_edge))
                    d = min(d, mp.pi)
                pen_min += wp * (1 - mp.cos(d)) - mp.mpf("1e-30")
                if pen_min >= tau:
                    break
            if pen_min < tau:
                cleared_all = False
                unresolved.append((m2, j))
        if not cleared_all:
            pass
    print(f"    stage-2 unresolved cells: {len(unresolved)}")
    if unresolved:
        print("    UNRESOLVED:", unresolved[:20])
        return 1

    print(f"\nCERTIFIED: Pen(t) >= tau on [T_F, T_END]; hence Q_{a_str}(t) > 0 on [{T_F}, {T_END}].")
    print(f"Chained with the scale-window theorem (|t| <= T_F) and the tail theorem at T_END")
    print(f"(margin {mp.nstr(mp.mpf(M_END.a), 6)}), Q_{a_str}(t) > 0 for every real t;")
    print(f"heat propagation extends this to every 0 < a <= {A_NUM}/{A_DEN}.")
    print(f"total {time.time() - t0:.0f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
