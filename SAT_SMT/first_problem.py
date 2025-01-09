from z3 import *

# 3*x**2 + 2*y + z = 15
# x - y**2 = 1
# y + 2*z = 3

x, y, z = Reals('x y z')

s = Solver()

s.add(3*x**2 + 2*y + z == 15)
s.add(x - y**2 == 1)
s.add(y + 2*z == 3)

print(s.check())
print(s.model())
