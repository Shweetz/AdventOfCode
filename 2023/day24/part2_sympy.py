# sympy is for symbolic python, a library solving equations

# video reference for the code: https://www.youtube.com/watch?v=guOyA7Ijqgk + https://www.youtube.com/watch?v=AQygaKH6rfc

import sympy
from time import time

# script start
t1 = time()

stones = [tuple(map(int, line.replace("@", ",").split(","))) for line in open("input.txt")]

xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

equations = []

for i, (sx, sy, sz, vx, vy, vz) in enumerate(stones):
	equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
	equations.append((xr - sx) * (vz - vzr) - (zr - sz) * (vx - vxr))
	if i < 2:
		continue
	answers = sympy.solve(equations)
	if len(answers) == 1:
		break

print(answers[0][xr] + answers[0][yr] + answers[0][zr])
print(f"Execution time: {(time() - t1):.3f}s")
