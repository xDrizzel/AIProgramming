from z3 import *

Amer, Brit, Can, Ir = Ints('Amer Brit Can Ir')
But, Dol, Hor, Tur = Ints('But Dol Hor Tur')
Bowl, Hand, Swim, Ten = Ints('Bowl Hand Swim Tur')
Black, Blue, Red, White = Ints('Black, Blue, Red, White')

s = Solver()

s.add([And(x >= 1, x <= 4) for x in [Amer, Brit, Can, Ir, But, Dol, Hor, Tur, Bowl, Hand, Swim, Tur, Black, Blue, Red, White]])
s.add(Distinct([Amer, Brit, Can, Ir]))
s.add(Distinct([But, Dol, Hor, Tur]))
s.add(Distinct([Bowl, Hand, Swim, Ten]))
s.add(Distinct([Black, Blue, Red, White]))

s.add(Ir == Hand + 2)
s.add(Black == 2)
s.add(Hor == Red -2)
s.add(Amer == Tur - 1)
s.add(Bowl > Ten)
s.add(Hand == White - 2)

print(s.check())
print(s.model())