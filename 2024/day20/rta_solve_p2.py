
from collections import Counter, defaultdict
from dataclasses import dataclass, field
import functools
import math
import re
from queue import PriorityQueue
import sympy
import sys
from time import sleep, time

from aoc_tools import *

sys.setrecursionlimit(1000000)

L, LU, U, RU, R, RD, D, LD = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
dirs = {"<":L, "^":U, ">":R, "v":D}
dirs = [L, U, R, D] # directions
di = 0 # direction index

def pprint(s):
	print(s)
	pass

# @dataclass
# class O:
# 	p: int # position
# 	v: int # value
# 	l: int # length
# 	c: list = field(default_factory=list) # path

t1 = time()
with open("2024/day20/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

g = Grid()
g.read(lines)
g.print()
start = g.find("S")[0]
end = g.find("E")[0]
pprint(f"{start,end=}")
# visited = set()

score, path = g.bfs(start, end)

pprint(f"{score,path=}")

g2 = Grid()
g2.read(lines)

for i in range(0, len(lines), 1):
	for j in range(0, len(lines[i]), 1):
		g2.g[(i,j)] = "."

pos_list = []
for i, pos in enumerate(path[::-1]):
	g2.g[pos] = i

cheats = {}
for p0 in path:
	# p0 = (i,j)
	if g2.g[p0] != ".":
		s = int(g2.g[p0])
		# dist = 1
		# while dist <= 2:
		# 	for d in range(4):
		# 		p1 = g2.move(p0, d)
		# 		# p2 = g2.move(p1, d)
		# 		if p1 in g2.g and g2.g[p1] != ".":
		# 			e = int(g2.g[p1])
		# 			if g2.g[p1] == "." and e < s:
		# 				cheats[(p0, p1)] = s - e - dist
	
		cheats.update(g2.bfs2(p0, 20))


# g.build(size, size, pos_list)

# g.print()

cheats = Counter(cheats)
cheats = {k:v for k, v in cheats.items() if v > 99}
# for k,v in cheats.items():
# 	if v < 50:
# 		cheats.pop(k, None)

# pprint(f"{cheats=}")
pprint(f"{len(cheats)=}")
cc = defaultdict(int)
for k,v in cheats.items():
	cc[v] += 1
pprint(f"{cc=}")

total = 0
total = len([1 for k,v in cheats.items() if v > 99])
print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")
