from z3 import *

xs = [1, 2, 9, 1, -1, -7, -3, -2, 9000, 5, 8, -9, 5, -3]

N = len(xs)

ds = [Bool(f"ds[{i}]") for i in range(N)]

zero_sum = Sum([If(ds[i], xs[i], 0) for i in range(N)]) == 0
sol_len = Sum([If(ds[i], 1, 0) for i in range(N)])
length = Int("length")

s = Optimize()
s.add(sol_len > 0)
s.add(length == sol_len)
s.add(zero_sum)

# s.maximize(sol_len)
s.maximize(length)
m = None

if s.check() == unsat:
    print("No Solution")
else:
    m = s.model()
    print(m)