from collections import defaultdict
from time import time

from aoc_tools import *

t1 = time()
with open("2024/day14/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

width, height = 101,103

q = defaultdict(set)

for i, line in enumerate(lines):
	# parse input of the current line representing a robot
	line = spl(line, "=, ")
	px, py, vx, vy = int(line[1]), int(line[2]), int(line[4]), int(line[5])
	q[(px, py)].add((vx, vy))

k = 0
do_break = False
while not do_break:
	# string to print the christmas tree
	s = ""
	for j in range(0, height, 1):
		c = 0
		for i in range(0, width, 1):
			if ((i,j)) in q:
				s += "X"
				c += 1
			else:
				s += "."
				c = 0

			if c > 15:
				print(s)
				print("\n")
				# sleep(0.5)
				total = k
				do_break = True

		s += "\n"

	q2 = defaultdict(set)
	for (px, py),v in q.items():
		for vx, vy in v:
			px2 = (px + vx) % width
			py2 = (py + vy) % height
			q2[(px2, py2)].add((vx, vy))

	q = q2
	k += 1
	
	# column loops after 101 iterations (width size) and line after 103, so position loops after 101 * 103 iterations
	if k > 101 * 103:
		do_break = True

print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")
assert total == 6243
