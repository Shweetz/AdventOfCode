from collections import Counter, defaultdict
from dataclasses import dataclass
import re
import time

from aoc_tools import *

@dataclass
class O:
	p: int # position
	v: int # value
	l: int # length

with open("2024/day10/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

dir = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, 1], [1, 1], [1, -1], [-1, -1]]
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
di = 0

g = Grid()
g.read(lines)
# x,y,_,_ = g.find("^")[0]
# vis = set()
# print(f"{g.g=}")
# print(f"{g.adj(0,0,0)=}")
# print(f"{len(g.find("^", 0))=}")

total = 0
best = 0
cur = 0

lo = [] # list of objects O

# lines = zip(*lines) # transpose

found = set()
q = []
for i in range(0, len(lines), 1):
	for j in range(0, len(lines[i]), 1):
		if g.g[(i,j)] == "0":
			q.append((i,j,i,j,0))

while q:
	a,b,i,j,v = q.pop()
	for x,y,v2 in g.adj(i,j):
		if int(v2) == v+1:
			if int(v2) == 9:
				found.add((a,b,x,y))
			else:
				q.append((a,b,x,y,int(v2)))

total = len(found)
print(f"{total = }")
