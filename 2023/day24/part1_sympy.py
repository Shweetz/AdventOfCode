# sympy is for symbolic python, a library solving equations

# video reference for the code: https://www.youtube.com/watch?v=guOyA7Ijqgk

import sympy
from time import time

# script start
t1 = time()

stones = [tuple(map(int, line.replace("@", ",").split(","))) for line in open("input.txt")]

total = 0

for i, s1 in enumerate(stones):
	print(f"{i}/{len(stones)}")

	for s2 in stones[i+1:]:
		px, py = sympy.symbols("px py")
		answers = sympy.solve([vy * (px - sx) - vx * (py - sy) for sx, sy, _, vx, vy, _ in [s1, s2]])
		if answers == []:
			continue
		x, y = answers[px], answers[py]
		if all(200000000000000 <= c <= 400000000000000 for c in (x, y)):
			if all((x - sx) * vx >= 0 and (y - sy) * vy >= 0 for sx, sy, _, vx, vy, _ in [s1, s2]):
				total += 1

print(total)
print(f"Execution time: {(time() - t1):.3f}s")
