# sweep_extension_1737_2000.py
# Extension of rigorous_weil_sweep.py to the segment [1737, 2000], closing the gap
# between the original finite certificate (which reaches t = 1737.09375) and the
# tail theorem certified by tools/tail_certificate.py (Q(t) > 0 for t >= 2000).
# This file is a copy of src/rigorous_weil_sweep.py with ONLY the sweep range and
# output path changed (plus plain-decimal CSV formatting, resolving handoff
# section 6.6 for this artifact); it inherits the original trust base and every open
# numerical proof obligation listed in docs/RH_Weil_Gaussian_Handoff.md section 6.
# Trust base: IEEE 754 correct rounding of +,-,*,/ ; numpy elementwise semantics ;
#             mpmath.iv (true interval arithmetic) for one-time constants only.
# NO libm exp/log/cos is used in the sweep: log and cos are implemented below with
# explicit series remainders; exp appears only in precomputed interval constants.
import numpy as np, math, time
import mpmath as mp
from mpmath import iv
from sympy import primerange
from fractions import Fraction

INF = np.inf
def up(x):  return np.nextafter(x, INF)
def dn(x):  return np.nextafter(x, -INF)
def c(x):   x = np.asarray(x, float); return (x, x)          # exact value as degenerate interval

def i_add(a,b): return dn(a[0]+b[0]), up(a[1]+b[1])
def i_sub(a,b): return dn(a[0]-b[1]), up(a[1]-b[0])
def i_mul(a,b):
    p1,p2,p3,p4 = a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1]
    return dn(np.minimum(np.minimum(p1,p2),np.minimum(p3,p4))), \
           up(np.maximum(np.maximum(p1,p2),np.maximum(p3,p4)))
def i_div(a,b):
    q1,q2,q3,q4 = a[0]/b[0], a[0]/b[1], a[1]/b[0], a[1]/b[1]
    return dn(np.minimum(np.minimum(q1,q2),np.minimum(q3,q4))), \
           up(np.maximum(np.maximum(q1,q2),np.maximum(q3,q4)))
def i_sumpad(lo, hi, axis=1):    # rigorous vector sum: |fl(sum)-sum| <= n*u*sum|x|
    n = lo.shape[axis]; mag = np.sum(np.maximum(np.abs(lo),np.abs(hi)),axis=axis)
    pad = up(1.2e-16*n*mag)
    return dn(np.sum(lo,axis=axis)-pad), up(np.sum(hi,axis=axis)+pad)

# ---------------- one-time interval constants (mpmath.iv, dps 40-50) ----------------
iv.dps = 40
def iv2d(x): return dn(float(mp.mpf(x.a))), up(float(mp.mpf(x.b)))
PI    = iv2d(iv.pi);    PI2  = iv2d(2*iv.pi);   LOG2 = iv2d(iv.log(2))
LOGPI = iv2d(iv.log(iv.pi)); TWO_SQPI = iv2d(2/iv.sqrt(iv.pi))

# ---- rigorous log at exact double points: frexp (exact) + atanh series, remainder explicit
K_L = 18; REM_L = (1/3.0)**(2*K_L+2)/((2*K_L+3)*(8/9.0))
def logpt(x):
    m, e = np.frexp(x)                                   # x = m*2^e exactly, m in [0.5,1)
    s  = i_div(c(m-1.0), (dn(m+1.0), up(m+1.0)))         # m-1 exact (Sterbenz); |s|<=1/3
    s2 = i_mul(s,s); acc = c(1.0/(2*K_L+1))
    for k in range(K_L-1,-1,-1): acc = i_add(i_mul(acc,s2), c(1.0/(2*k+1)))
    at = i_mul(s,acc); at = (dn(at[0]-REM_L), up(at[1]+REM_L))
    return i_add(i_mul(c(2.0),at), i_mul(c(e.astype(float)), LOG2))
def i_log(a):  return logpt(a[0])[0], logpt(a[1])[1]      # log increasing

# ---- rigorous cos on narrow intervals: reduce mod certified 2pi + Taylor, remainder explicit
K_C = 17; COSC = [((-1)**k*Fraction(1,math.factorial(2*k))) for k in range(K_C+1)]
COSC = [(dn(float(f.numerator)/float(f.denominator)), up(float(f.numerator)/float(f.denominator))) for f in COSC]
REM_C = 3.2**(2*K_C+2)/math.factorial(2*K_C+2)
def i_cos(a):
    lo, hi = a; mid = 0.5*(lo+hi); hw = up(up(hi-lo)*0.5)
    q  = np.floor(mid/6.283185307179586 + 0.5)
    y  = i_sub(c(mid), i_mul(c(q), PI2)); y2 = i_mul(y,y)
    acc = COSC[K_C]
    for k in range(K_C-1,-1,-1): acc = i_add(i_mul(acc,y2), COSC[k])
    return dn(acc[0]-REM_C-hw), up(acc[1]+REM_C+hw)

# ---- x-partition on [-4,4], h = 1/64 (exact dyadics); W, Ea, J via interval erf/exp series
h = 1/64.0; edges = -4.0 + np.arange(513)*h; mids = 0.5*(edges[:-1]+edges[1:])   # all exact
iv.dps = 50
def iv_erf(x):
    if mp.mpf(x.b) < 0: return -iv_erf(-x)
    s = iv.mpf(0); term = x; x2 = x*x; k = 0
    while True:
        s += (-1)**k * term/(2*k+1); k += 1; term = term*x2/k
        if k > float(mp.mpf(x2.b)) and mp.mpf((term/(2*k+1)).b) < mp.mpf('1e-42'):
            s += iv.mpf([-1,1])*(term/(2*k+1)); break
    return s*2/iv.sqrt(iv.pi)
erf_iv = [iv_erf(iv.mpf(x)) for x in edges]
Ea_iv  = [iv.exp(-iv.mpf(x)**2) for x in edges]
W_iv   = [(iv.sqrt(iv.pi)/2)*(erf_iv[j+1]-erf_iv[j]) for j in range(512)]
J_iv   = [(Ea_iv[j]-Ea_iv[j+1])/2 - iv.mpf(mids[j])*W_iv[j] for j in range(512)]
W_lo = np.array([dn(float(mp.mpf(w.a))) for w in W_iv]); W_hi = np.array([up(float(mp.mpf(w.b))) for w in W_iv])
JNEG = dn(float(mp.mpf(sum(min(j, iv.mpf(0)) for j in J_iv).a)))          # sum of negative parts, lower
SUMW_HI = up(float(mp.mpf(sum(W_iv).b)))
TAIL_ARCH = up(float(mp.mpf((iv.mpf('5.3722')*iv.exp(-16)/(8*iv.pi)).b)))  # |Om(0)|*mass(|x|>4)/pi
POLE_HI = up(float(mp.mpf((4*iv.exp(iv.mpf('0.25')-121)).b)))              # |pole| for t>=11

# ---- prime tables (interval coefficients) + Lemma-3 tails, and L2 via iv
def ptable(N, dps=40):
    iv.dps = dps; ul, cl = [], []
    for p in primerange(2, N+1):
        lp = iv.log(p); pk = p
        while pk <= N:
            u = iv.log(pk); ul.append(u); cl.append(lp/iv.sqrt(pk)*iv.exp(-u*u/4)); pk *= p
    vN = (iv.log(N)-1)/2
    tail = (2/iv.sqrt(iv.pi))*iv.exp(iv.mpf('0.25'))*iv.exp(-vN*vN)*(2+1/vN)
    U  = (np.array([dn(float(mp.mpf(u.a))) for u in ul]), np.array([up(float(mp.mpf(u.b))) for u in ul]))
    Cf = (np.array([dn(float(mp.mpf(x.a))) for x in cl]), np.array([up(float(mp.mpf(x.b))) for x in cl]))
    return U, Cf, up(float(mp.mpf(tail.b)))
U_c, C_c, TAIL_c = ptable(3000)      # coarse table
U_f, C_f, TAIL_f = ptable(20000)     # fine table
iv.dps = 40
SQc = iv.mpf(0); 
for p in primerange(2,100001):
    lp = iv.log(p); pk = p
    while pk <= 100000:
        u = iv.log(pk); SQc += lp/iv.sqrt(pk)*iv.exp(-u*u/4)*u*u; pk *= p
def T2iv(b,M=2000):
    s = iv.mpf(0)
    for n in range(M): a = iv.mpf(n)+iv.mpf('0.25'); s += a/((a*a+b*b)**2)
    # decreasing-series tail from n=M needs the first term plus the integral:
    # sum_{n>=M} f(n) <= f(M) + int_M^inf f(x) dx  (2026-07-28 audit fix)
    aM = iv.mpf(M)+iv.mpf('0.25')
    return s + iv.mpf([0, up(float(mp.mpf((1/aM**3 + 1/(2*aM**2)).b)))])
L2 = (2/iv.sqrt(iv.pi))*(SQc+iv.mpf('1e-6')) + iv.mpf('2.5')*T2iv(iv.mpf('3.5'))/iv.sqrt(iv.pi) \
     + iv.mpf('2.5')*T2iv(iv.mpf(0))*iv.exp(-16)/(4*iv.pi) + iv.mpf('1e-40')
L2_hi = up(float(mp.mpf(L2.b)))
print(f"[constants] L2 <= {L2_hi:.6f}; tables coarse {len(U_c[0])} / fine {len(U_f[0])} prime powers")

NSEQ = np.arange(400) + 0.25
def Q_lower(ts, U, Cf, TAILP):
    out = np.empty(len(ts))
    for i0 in range(0, len(ts), 300):
        T = ts[i0:i0+300]; nt = len(T)
        x  = i_mul((T[:,None], T[:,None]), (U[0][None,:], U[1][None,:]))
        cv = i_cos(x)
        pr = i_mul((Cf[0][None,:], Cf[1][None,:]), cv)
        Ps = i_sumpad(pr[0], pr[1])
        P  = i_mul(c(-1.0), i_mul(TWO_SQPI, Ps))
        P_lo = dn(P[0] - TAILP)
        r  = T[:,None] + mids[None,:]                                    # exact dyadic
        r2 = i_mul(c(r), c(r)); den = i_add(c(1/16.0), i_mul(c(0.25), r2))
        A  = i_sub(c(1/16.0), i_mul(c(0.25), r2)); B2 = i_mul(c(1/16.0), r2)
        d2 = i_mul(den,den); d4 = i_mul(d2,d2)
        f  = i_sub(i_mul(c(0.5), i_log(den)), LOGPI)
        f  = i_sub(f, i_div(c(0.125), den))
        f  = i_sub(f, i_div(i_mul(c(1/12.0), A), d2))
        f  = i_add(f, i_div(i_mul(c(1/120.0), i_sub(i_mul(A,A), B2)), d4))
        remB = up(1.0/(63*dn(d2[0])*r))
        Om_lo = dn(f[0]-remB)
        assert Om_lo.min() > 0, "Omega lower bound must be positive for r >= 7"
        a1_lo, _ = i_sumpad(Om_lo*W_lo[None,:], up(f[1]+remB)*W_hi[None,:])
        bmin = (T-4.0)/2.0                                               # exact
        aN = c(NSEQ[None,:]*np.ones((nt,1)))
        dd = i_add(i_mul(aN,aN), i_mul(c(bmin[:,None]), c(bmin[:,None])))
        t2 = i_div(aN, i_mul(dd,dd))
        T2_lo, T2_hi = i_sumpad(t2[0], t2[1])
        T2_hi = up(up(T2_hi + up(1/(2*400.25**2))) + up(1/400.25**3))
        sup_dO  = up(((T+4.0)/2.0)*T2_hi)
        sup_d2O = up(2.5*T2_hi)
        arch_lo = dn(a1_lo + sup_dO*JNEG - (h*h/8)*SUMW_HI*sup_d2O)
        arch_lo = dn(arch_lo/PI[1] - TAIL_ARCH)
        out[i0:i0+300] = dn(P_lo + arch_lo - POLE_HI)
    return out

# ---------------- certified second-order mesh over exact dyadic grids ----------------
t0 = time.time(); certs = []
segs = [(1737.0, 2000.0)]
DELTAS = [5/32.0, 1/32.0, 1/256.0, 1/1024.0, 1/4096.0]
for pi_, d in enumerate(DELTAS):
    thr = up(up(up(L2_hi*d)*d)/8); U,Cf,TP = (U_c,C_c,TAIL_c) if pi_==0 else (U_f,C_f,TAIL_f)
    nxt = []; npts = 0
    for (a,b) in segs:
        n = int(math.ceil((b-a)/d - 1e-12)); ts = a + np.arange(n+1)*d   # exact dyadics, grid end >= b
        Ql = Q_lower(ts, U, Cf, TP); npts += len(ts)
        pair = np.minimum(Ql[:-1], Ql[1:]); ok = pair >= thr
        for k in np.where(ok)[0]:
            certs.append((ts[k], ts[k+1], d, pair[k], thr))
        idx = np.where(~ok)[0]
        if len(idx):
            s = e = idx[0]
            for k in idx[1:]:
                if k <= e+1: e = k
                else: nxt.append((ts[s], ts[e+1])); s = e = k
            nxt.append((ts[s], ts[e+1]))
    print(f"[pass {pi_}] d={d:.10f}  pts={npts:>6}  thr={thr:.3e}  certified pairs so far={len(certs)}  "
          f"uncert. measure={sum(y-x for x,y in nxt):.6f}")
    segs = nxt
    if not segs: break
assert not segs, "certification incomplete"

# ---------------- exact coverage proof over the rationals ----------------
fr = sorted((Fraction(a), Fraction(b)) for a,b,_,_,_ in certs)          # floats are exact dyadics
cur = Fraction(1737); i = 0
while i < len(fr) and fr[i][0] <= cur:
    j = i
    while j < len(fr) and fr[j][0] <= cur: cur = max(cur, fr[j][1]); j += 1
    if j == i: break
    i = j
covered = cur >= Fraction(2000)
print(f"[coverage] union of {len(certs)} certified intervals reaches t = {float(cur)}  "
      f"=> [1737, 2000] covered: {covered}")
assert covered

with open('data/certificates_extension.csv','w') as f:
    f.write("t_lo,t_hi,delta,pair_Q_lowerbound,threshold_L2d2_over_8,certified_margin\n")
    for a,b,d,q,th in certs:
        f.write(f"{float(a)!r},{float(b)!r},{float(d)!r},{q:.6e},{th:.6e},{dn(q-th):.6e}\n")
    f.write(f"# Tail theorem (tools/tail_certificate.py): Q(t) >= 0.079 for all t >= 2000\n")
    f.write(f"# Union of rows proven (exact rational arithmetic) to cover [1737, 2000] with no gaps.\n")
worst = min(dn(q-th) for _,_,_,q,th in certs)
print(f"[result] Q(t) >= 0 certified on [1737, 2000]; worst certified margin = {worst:.3e}")
print(f"[result] elapsed {time.time()-t0:.1f}s; certificates written: {len(certs)} rows")
