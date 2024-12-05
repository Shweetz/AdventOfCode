from collections import Counter, defaultdict
from dataclasses import dataclass
import re

from aoc_tools import *

@dataclass
class Object: pass

with open("2024/day05/input1.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

# g = Grid()
# g.read(lines)
# print(f"{g.g=}")
# print(f"{g.g[(0,0)]=}")
# print(f"{g.adj(0,0,0)=}")
# print(f"{len(g.find("XMAS", 0))=}")
# dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
# dir = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, 1], [1, 1], [1, -1], [-1, -1]]

total = 0
best = 0
cur = 0

ll = []
# l1, l2 = zip(*[line.split() for line in lines])

# for l1, l2, l3 in zip(lines[::3], lines[1::3], lines[2::3]):
for i, line in enumerate(lines):
	# print(f"{line=}")
	# for j, c in enumerate(line):
		
	# l = [int(s) for s in line.split()]
	# l = get_ints(line)
	# print(f"{l=}")

	# ll.append(l)

	pass

	total += 1

# ll2 = zip(*ll)
# print(f"{list(ll2) = }")

print(f"{total = }")
