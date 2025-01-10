from z3 import *

a, b, c = Reals('a b c')

x = Real('x')

s = Solver()

s.add(b**2 * x**2 + (b**2 + c**2 - a**2) * x + c**2 == 0)

s.add(a + b > c, b + c > a, c + a > b) # properties of a triangle

print(s.check())