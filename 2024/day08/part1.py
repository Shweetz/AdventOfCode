from time import time

from aoc_tools import *

t1 = time()
with open("2024/day08/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

g = Grid()
g.read(lines)

impacted = set()

for x1, line in enumerate(lines):
	for y1, c1 in enumerate(line):
		if c1 == ".":
			continue

		for x2, line in enumerate(lines):
			for y2, c2 in enumerate(line):
				if c2 == c1 and (x1,y1) != (x2,y2):
					# c1 and c2 are 2 antennas with same symbol
					dx, dy = (x1 - x2, y1 - y2)

					p1 = (x1 + dx, y1 + dy) # 2*x1 - x2, 2*y1 - y2
					p2 = (x2 - dx, y2 - dy)
					
					if p1 in g.g:
						impacted.add(p1)
					if p2 in g.g:
						impacted.add(p2)

total = len(impacted)
print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")
assert total == 423
