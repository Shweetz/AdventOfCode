from time import time

from aoc_tools import *

t1 = time()
with open("2024/day11/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

l = get_ints(lines[0])

blinks = 25

for i in range(blinks):
	l2 = []

	for s in l:
		if s == 0:
			l2.append(1)
		elif len(str(s)) % 2 == 0:
			j = len(str(s)) // 2
			l2.append(int(str(s)[:j]))
			l2.append(int(str(s)[j:]))
		else:
			l2.append(s*2024)

	l = l2

total = len(l2)
print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")
assert total == 182081
