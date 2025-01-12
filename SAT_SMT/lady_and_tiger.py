from z3 import *

def unique(s, xs):
    others = []
    m = s.model()
    for x in xs:
        s.push()
        s.add(x != m.eval(x, model_completion=True))
        if s.check() == sat:
            others.append(s.model())
        s.pop()
    if len(others) == 0:
        return True, []
    else:
        return False, others

def trial():
    r1, r2 = Bools("r1 r2")
    # ri true means there is a lady in room i
    # ri False --> tiger!

    sign2 = ~r2
    sign1 = ~r1 & ~r2

    cond1 = r1 == sign1
    cond2 = r2 != sign2

    s = Solver()

    s.add(cond1)
    s.add(cond2)
    print(s.check())
    print(s.model())
    print(unique(s, [sign1, sign2]))
    return s

def trial9():
    r1, r2, r3 = Bools("r1 r2 r3")
    # ri true means there is a lady in room i
    # ri False --> tiger!

    sign1 = ~r1
    sign2 = r2
    sign3 = ~r2

    one_lady = Sum([If(r, 1, 0) for r in [r1, r2, r3]]) == 1
    one_sign = Sum([If(sign, 1, 0) for sign in [sign1, sign2, sign3]]) <= 1

    s = Solver()

    s.add(one_lady)
    s.add(one_sign)
    print(s.check())
    print(s.model())
    print(unique(s, [r1, r2, r3]))
    return s

def trial11():
    r1, r2, r3 = Ints("r1 r2 r3")
    # ri = 0, if tiger in room i
    #      1, if lady in room i
    #      2, if room i is empty

    rs = [r1, r2, r3]
    range_cond = [And(0 <= r, r <= 2) for r in rs]
    distinct_cond = Distinct(rs)

    sign1 = r3 == 2
    sign2 = r1 == 0
    sign3 = r3 == 2

    signs = [sign1, sign2, sign3]
    sign_cond = [Implies(rs[i] == 0, ~signs[i]) & Implies(rs[i] == 1, signs[i]) for i in range(len(rs))]

    s = Solver()

    s.add(range_cond)
    s.add(distinct_cond)
    s.add(sign_cond)

    print(s.check())
    print(s.model())
    print(unique(s, [r1, r2, r3]))

    return s


def trial12():
    rs = [Int(f"r{i}") for i in range(9)]
    # ri = 0, if tiger in room i+1
    #      1, if lady in room i+1
    #      2, if room i+1 is empty

    range_cond = [And(0 <= r, r <= 2) for r in rs]
    one_lady = Sum([If(r == 1, 1, 0) for r in rs]) == 1

    sign1 = Or(rs[0] == 1, rs[2] == 1, rs[4] == 1, rs[6] == 1, rs[8] == 1)
    sign2 = rs[1] == 2
    sign4 = Not(sign1)
    sign5 = Or(sign2, sign4)
    sign7 = rs[0] != 1
    sign8 = And(rs[7] == 0, rs[8] == 2)
    sign3 = Or(sign5, Not(sign7))
    sign6 = Not(sign3)
    sign9 = And(rs[8] == 0, Not(sign6))

    room8 = rs[7] != 2


    signs = [sign1, sign2, sign3, sign4, sign5, sign6, sign7, sign8, sign9]

    sign_cond = [And(Implies(rs[i] == 0, Not(signs[i])), Implies(rs[i] == 1, signs[i])) for i in range(9)]

    s = Solver()

    s.add(range_cond)
    s.add(one_lady)
    s.add(sign_cond)
    s.add(room8)

    print(s.check())
    print(s.model())
    uni, others = unique(s, rs)
    print(others)
    print("unique: " + str(uni))
    print("princess in same room: " + str(one_princess_room(s, rs, others)[0]))
    print("princess is in room: " + str(one_princess_room(s, rs, others)[1]))

    return s

def one_princess_room(s, xs, models):
    s.check()
    m = s.model()
    princess = None
    for x in xs:
        if m[x].as_long() == 1:
            princess = str(x)
    for model in models:
        for x in xs:
            if model[x].as_long() == 1:
                if princess != str(x):
                    return False, None
    return True, princess

trial12()