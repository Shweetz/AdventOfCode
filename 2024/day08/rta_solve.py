from collections import Counter, defaultdict
from dataclasses import dataclass
import re

from aoc_tools import *

@dataclass
class Object: pass

with open("2024/day08/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

# dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
# dir = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, 1], [1, 1], [1, -1], [-1, -1]]
# di = 0
# (a,b) = dir[di]

g = Grid()
g.read(lines)
# x,y,_,_ = g.find("^")[0]
# vis = set()
# print(f"{g.g=}")
# print(f"{g.g[(0,0)]=}")
# print(f"{g.adj(0,0,0)=}")
# print(f"{len(g.find("^", 0))=}")

impacted = set()
cc = ("", 0, 0)

for i, line in enumerate(lines):
	for j, c in enumerate(line):
		if c == ".":
			continue

		for x, line in enumerate(lines):
			for y, c2 in enumerate(line):
				# if not cc[0]:
				# 	cc = (c, i, j)
				if c2 == c and (i,j) != (x,y):
					d = (i - x, j - y)
					p1 = (i, j)
					while p1 in g.g:
						impacted.add(p1)
						p1 = (p1[0] + d[0], p1[1] + d[1])
						# p1[1] += d[1]

					p2 = (x, y)
					# if p1 == (1,8) or p2 == (1,8):
					# 	print(f"{c, c2, i, j,x,y=}")
					while p2 in g.g:
						impacted.add(p2)
						p2 = (p2[0] - d[0], p2[1] - d[1])

print(f"{sorted(impacted)=}")
total = len(impacted)
print(f"{total = }")
