from sympy import symbols, Eq, solve
from time import time

from aoc_tools import *

t1 = time()
with open("2024/day13/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total = 0

for l1, l2, l3, l4 in zip(lines[::4], lines[1::4], lines[2::4], lines[3::4]):		
	ax, ay = get_ints(l1)
	bx, by = get_ints(l2)
	px, py = get_ints(l3)

	px += 10000000000000
	py += 10000000000000
	
	# use sympy to solve linear equations
	a, b = symbols('a b', integer=True) # only int solutions
	eq1 = Eq(ax * a + bx * b, px)
	eq2 = Eq(ay * a + by * b, py)
	sol = solve((eq1, eq2),(a, b))
	
	if sol:
		total += sol[a] * 3 + sol[b]

print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")
assert total == 95688837203288
