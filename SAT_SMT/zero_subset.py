from z3 import *

xs = [1, 2, 9, 1, -1, -7, -3, -2, 9000, 5, 8, -9, 5, -3]

N = len(xs)

ds = [Bool(f"ds[{i}]") for i in range(N)]

zero_sum = Sum([If(ds[i], xs[i], 0) for i in range(N)]) == 0
sol_len = Sum([If(ds[i], 1, 0) for i in range(N)])

s = Solver()
target = 0

s.add(zero_sum)
s.push()
m = None

s.add(sol_len > target)

while s.check() == sat:
    m = s.model()
    target = len([xs[i] for i in range(N) if m[ds[i]]])
    s.pop()
    s.push()
    s.add(sol_len > target)

if m is None:
    print("No Solution!")
else:
    print([xs[i] for i in range(N) if m[ds[i]]])
