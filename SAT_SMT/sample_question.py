from z3 import *

consumption = [4, 8, 3, 7, 2]
fuel = [10, 5, 10, 9, 8]

pick_ups = [Bool(f"stop[{i}]") for i in range(len(fuel))]

pick_up_cond = [Sum([If(pick_ups[j], fuel[j], 0) for j in range(i+1)]) >= Sum([consumption[j] for j in range(i+1)]) for i in range (len(fuel))]
fuel_stops = Sum([If(pick_ups[i], 1, 0) for i in range(len(pick_ups))])

s = Optimize()

s.add(pick_up_cond)
s.minimize(fuel_stops)

print(s.check())
m = s.model()
print(f"Car should stop at {[i for i in range(1,len(pick_ups)) if m[pick_ups[i]]]}")