from time import time

from aoc_tools import *

t1 = time()
with open("2024/day07/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total = 0

for i, line in enumerate(lines):
	l = get_ints(line)

	poss = [l[1]]

	for i in range(2, len(l)):
		nposs = []
		for p in poss:
			nposs.append(p + l[i])
			nposs.append(p * l[i])
		poss = nposs.copy()

	if l[0] in poss:
		total += l[0]

print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")
assert total == 1582598718861
