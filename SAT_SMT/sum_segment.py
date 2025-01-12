from z3 import *

def mss():
    xs = [-1, -2, -3]

    N = len(xs)

    l, r = Ints("l r")

    # l_range = (0 <= l) & (l < N)
    # r_range = (0 <= r) & (r < N)

    # do we want l <= r? no if we want to allow empty lists, yes otherwise
    # no empty lists:
    l_r_range = (0 <= l) & (l <= r) & (r < N)

    segsum_val = Sum([If((l<= i) & (i <= r), xs[i], 0) for i in range(N)])

    segsum = Int("segsum")

    segsum_def = segsum == segsum_val

    s = Optimize()

    s.add(l_r_range)
    s.add(segsum_def)

    s.maximize(segsum)

    m = None

    if s.check() == sat:
        m = s.model()
        print([xs[i] for i in range(N) if m[l].as_long() <= i <= m[r].as_long()])
    else:
        print("You should not see this!")

def widest_peak():
    xs = [3, 2, 1, 2, 3, 2, 1, 2]

    N = len(xs)

    l, p, r = Ints("l p r")

    l_p_r_range = (0 <= l) & (l <= p) & (p <= r) & (r < N)

    peak_cond_up = [Implies((l <= i) & (j <= p), xs[i] <= xs[j]) for i in range(N) for j in range(i+1, N)]
    peak_cond_down = [Implies((p <= i) & (j <= r), xs[i] >= xs[j]) for i in range(N) for j in range(i+1, N)]

    width = Int("width")
    width_def = width == (r - l + 1)

    s = Optimize()

    s.add(l_p_r_range)
    s.add(width_def)
    s.add(peak_cond_up)
    s.add(peak_cond_down)

    s.maximize(width)

    if s.check() == sat:
        m = s.model()
        print(m)
        print([xs[i] for i in range(N) if m[l].as_long() <= i <= m[r].as_long()])
    else:
        print("You should not see this!")

def widest_valley():
    xs = [3, 2, 1, 2, 3, 2, 1, 2]

    N = len(xs)

    l, r = Ints("l r")

    l_r_range = (0 <= l) & (l <= r) & (r < N)

    Xs = Function("Xs", IntSort(), IntSort())
    Xs_def = [Xs(i) == xs[i] for i in range(N)]

    # valley_cond = [Implies((l == L) & (r == R), (xs[L] >= xs[i]) & (xs[R] >= xs[i])) for L in range(N) for R in range(L, N) for i in range(L, R+1)]
    valley_cond = [Implies((l <= i) & (i <= r), (Xs(l) >= xs[i]) & (Xs(r) >= xs[i])) for i in range(N)]
    width = Int("width")
    width_def = width == (r - l + 1)

    s = Optimize()
    s.add(valley_cond)
    s.add(width_def)
    s.add(l_r_range)
    s.add(Xs_def)

    s.maximize(width)

    if s.check() == sat:
        m = s.model()
        print(m)
        print([xs[i] for i in range(N) if m[l].as_long() <= i <= m[r].as_long()])
    else:
        print("No valley!")



ws = [1, 2, 3]
vs = [1, 3, 5]
Max = 8

N = len(ws)

# ns = [Int(f"ns[{i}]") for i in range(N)]

ns = Function("ns", IntSort(), IntSort())
ns_range = [(ns(i) >= 0) for i in range(N)]

weight_cond = Max >= Sum([ns(i) * ws[i] for i in range(N)])

value = Int("value")
value_def = value == Sum([ns(i) * vs[i] for i in range(N)])

s = Optimize()
s.add(ns_range)
s.add(weight_cond)
s.add(value_def)

s.maximize(value)

if s.check() == sat:
    m = s.model()
    print(m)
else:
    print("No solution?")