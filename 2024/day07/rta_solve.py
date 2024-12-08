from collections import Counter, defaultdict
from dataclasses import dataclass
import re

from aoc_tools import *

@dataclass
class Object: pass

with open("2024/day07/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

# dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
# dir = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, 1], [1, 1], [1, -1], [-1, -1]]
# di = 0
# (a,b) = dir[di]

# g = Grid()
# g.read(lines)
# x,y,_,_ = g.find("^")[0]
# vis = set()
# print(f"{g.g=}")
# print(f"{g.g[(0,0)]=}")
# print(f"{g.adj(0,0,0)=}")
# print(f"{len(g.find("XMAS", 0))=}")

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
	l = get_ints(line)

	poss = [l[1]]

	for i in range(2, len(l)):
		nposs = []
		for p in poss:
			nposs.append(p + l[i])
			nposs.append(p * l[i])
			nposs.append(p * pow(10, len(str(l[i]))) + l[i])
		poss = nposs.copy()

	# print(f"{l=}")

	# ll.append(l)

	if l[0] in poss:
		total += l[0]

# ll2 = zip(*ll)
# print(f"{list(ll2) = }")

print(f"{total = }")
