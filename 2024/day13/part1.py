from time import time

from aoc_tools import *

t1 = time()
with open("2024/day13/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total = 0

for l1, l2, l3, l4 in zip(lines[::4], lines[1::4], lines[2::4], lines[3::4]):		
	l1 = get_ints(l1)
	l2 = get_ints(l2)
	l3 = get_ints(l3)

	best = -1

	for i in range(0, 101, 1):
		for j in range(0, 101, 1):
			x = (l1[0] * i) + (l2[0] * j)
			y = (l1[1] * i) + (l2[1] * j)

			if x == l3[0] and y == l3[1]:
				s = 3 * i + j
				if s < best or best == -1:
					best = s

	if best != -1:
		total += best

print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")
assert total == 30973
