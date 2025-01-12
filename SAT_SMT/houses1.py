from z3 import *

Aus, Bra, Ger = Ints('Aus Bra Ger')
Cat, Dog, Fish = Ints('Cat Dog Fish')
Bas, Foot, Socc = Ints('Bas Foot Socc')
Blue, Green, Red = Ints('Blue Green Red')

s = Solver()

s.add([And(1 <= x, x <= 3) for x in [Aus, Bra, Ger, Cat, Dog, Fish, Blue, Green, Red, Bas, Foot, Socc]])

s.add(Distinct([Aus, Bra, Ger]))
s.add(Distinct([Cat, Dog, Fish]))
s.add(Distinct([Bas, Foot, Socc]))
s.add(Distinct([Blue, Green, Red]))

s.add(Bra != 2)
s.add(Dog == Bas)
s.add(Foot == Red - 2)
s.add(Fish == Cat - 1)
s.add(Dog == Green + 1)
s.add(Ger == 3)

print(s.check())
print(s.model())

def unique(s, xs):
    m = s.model()
    for x in xs:
        s.push()
        s.add(x != m.eval(x, model_completion=True))
        if s.check() == sat:
            return False
        s.pop()
    return True

xs = [Aus, Bra, Ger, Cat, Dog, Fish, Bas, Foot, Socc, Blue, Green, Red]

print(unique(s, xs))