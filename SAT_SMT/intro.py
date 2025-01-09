from z3 import *

x = Bool('x')
y = Bool('y')
z = Bool('z')

s = Solver()

s.add(Or(x, Not(y), Not(z)))
s.add(Or(Not(x), y))
s.add(Or(Not(y), z))

print(s.check())
print(s.model())