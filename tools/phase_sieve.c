/* Phase sieve for the a = 3.4 height-coupled certificate (Route 005 cycle 5).
 *
 * For every integer m2 in [M2_LO, M2_HI] this program clears the interval
 * I_{m2} = { t : t*log2 in [2*pi*m2 - theta2max, 2*pi*m2 + theta2max] }
 * by proving  sum_p W[p] * (1 - cos(theta_p(t)))  >= TAU  throughout I_{m2},
 * where theta_p(t) = t*log p mod 2*pi.
 *
 * Phase model: acc[p] = frac(m2 * alpha_p) in turns * 2^64, alpha_p =
 * log p / log 2. Initialization uses an exact 128-bit multiply mod 2^64;
 * the per-step update acc += ALPHA[p] (mod 2^64) is exact integer
 * arithmetic. The only model error is the initial rounding of ALPHA[p]
 * (<= 1 ulp of 2^-64), whose accumulated drift over the full m2 range is
 * below 1e-7 rad and is absorbed into SWEEP[p] by the generator.
 *
 * Per-prime lower bound on the penalty over the whole interval I_{m2}:
 *   d = circular distance of the phase center from 0, minus SWEEP[p];
 *   contribution >= W[p] * onemcos_lb(max(d, 0)),
 * where onemcos_lb is a 4096-entry lower-bound table for 1 - cos on
 * [0, pi] (left endpoints; 1 - cos is nondecreasing there, and the index
 * is floored while the sweep offset is ceiled, so the bound is safe).
 * Early exit once the accumulated sum reaches TAU. Any m2 not cleared is
 * printed as SURVIVOR and passed to the rigorous Python stage 2.
 *
 * Usage: phase_sieve [m2_start m2_end]   (defaults to [M2_LO, M2_HI])
 * Generated constants: phase_sieve_constants.h (written by
 * tools/phase_height_certificate.py; W rounded down, TAU padded up,
 * SWEEP rounded up).
 */
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <math.h>
#include "phase_sieve_constants.h"

#define TBL 4096
static double onemcos_lb[TBL];

int main(int argc, char **argv) {
    uint64_t lo = M2_LO, hi = M2_HI;
    if (argc == 3) {
        lo = strtoull(argv[1], NULL, 10);
        hi = strtoull(argv[2], NULL, 10);
    }
    for (int i = 0; i < TBL; i++)
        onemcos_lb[i] = 1.0 - cos(M_PI * (double)i / (double)TBL);

    int sweep_idx[NPRIMES];
    for (int j = 0; j < NPRIMES; j++)
        sweep_idx[j] = (int)ceil(SWEEP[j] / M_PI * (double)TBL);

    uint64_t acc[NPRIMES];
    for (int j = 0; j < NPRIMES; j++)
        acc[j] = (uint64_t)((unsigned __int128)ALPHA[j] * (unsigned __int128)lo);

    uint64_t survivors = 0, count = 0;
    for (uint64_t m2 = lo; m2 <= hi; m2++, count++) {
        double sum = 0.0;
        int cleared = 0;
        for (int j = 0; j < NPRIMES; j++) {
            int64_t e = (int64_t)acc[j];
            uint64_t mag = (e < 0) ? (uint64_t)(-e) : (uint64_t)e;
            int idx = (int)(mag >> 51);            /* [0, pi] -> [0, TBL) */
            idx -= sweep_idx[j];
            if (idx > 0) {
                if (idx >= TBL) idx = TBL - 1;
                sum += W[j] * onemcos_lb[idx];
                if (sum >= TAU) { cleared = 1; break; }
            }
        }
        if (!cleared) {
            printf("SURVIVOR %llu\n", (unsigned long long)m2);
            if (++survivors > 50000000ULL) {
                printf("ABORT too many survivors\n");
                return 2;
            }
        }
        for (int j = 0; j < NPRIMES; j++) acc[j] += ALPHA[j];
    }
    fprintf(stderr, "chunk [%llu, %llu]: processed %llu, survivors %llu\n",
            (unsigned long long)lo, (unsigned long long)hi,
            (unsigned long long)count, (unsigned long long)survivors);
    return 0;
}
