
from collections import Counter, defaultdict
from dataclasses import dataclass, field
import functools
import math
import re
import sympy
from time import sleep, time

from aoc_tools import *

def pprint(s):
	print(s)
	pass

# @dataclass
# class O:
# 	p: int # position
# 	v: int # value
# 	l: int # length
# 	c: list = field(default_factory=list) # path

with open("2024/day14/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]
width, height = 101,103
# width, height = 11,7

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, 1], [1, 1], [1, -1], [-1, -1]]
dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
di = 0

# g = Grid()
# g.read(lines)
# x,y,_,_ = g.find("^")[0]
# vis = set()
# pprint(f"{g.g=}")
# pprint(f"{g.adj(0,0,0)=}")
# pprint(f"{len(g.find("^", 0))=}")

total = 0
best = 0
cur = 0

lo = [] # list of objects O

# lines = zip(*lines) # transpose

# for i in range(0, len(lines), 1):
# 	for j in range(0, len(lines[i]), 1):
# 		c = g.g[(i,j)]

q = defaultdict(int)

# for l1, l2, l3 in zip(lines[::3], lines[1::3], lines[2::3]): # read lines 3 by 3
for i, line in enumerate(lines):
	# pprint(f"{line=}")
	# for j, c in enumerate(line):
	line = spl(line, "=, ")
	px, py, vx, vy = int(line[1]), int(line[2]), int(line[4]), int(line[5])
	
	for j in range(100):
		# pprint(f"{px, py, vx, vy=}")
		px = (px + vx) % width
		py = (py + vy) % height
	
	pprint(f"")

	if px < (width - 1) / 2 and py < (height - 1) / 2:
		q[0] += 1
	if px < (width - 1) / 2 and py > (height - 1) / 2:
		q[2] += 1
	if px > (width - 1) / 2 and py < (height - 1) / 2:
		q[1] += 1
	if px > (width - 1) / 2 and py > (height - 1) / 2:
		q[3] += 1

pprint(f"{q[0]=}")
total = q[0] * q[1] * q[2] * q[3]
print(f"{total = }")
