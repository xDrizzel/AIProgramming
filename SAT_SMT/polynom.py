from z3 import *

# T = x**2 + a*x + b has integer roots
# x1, x2 are the integer roots
# T = (x - x1) * (x - x2) ==> a = -(x1 + x2), b = x1*x2

x1, x2 = Ints('x1 x2')
T = lambda x: (x - x1) * (x - x2)

c = Int('x')

s = Solver()

s.add(T(c) == 13)
s.add(If(T(c - 1) > T(c + 1), T(c - 1), T(c + 1)) != 28)

print(s.check())
print(s.model())