from z3 import *

x, y, z = Bools('x y z')

s = Solver()

f = And(Or(x, y), Or(Not(x), z), Or(y, Not(z)))

s.add(Exists(x, ForAll(y, Exists(z, f))))

print(s.check())