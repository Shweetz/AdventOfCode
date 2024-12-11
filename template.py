from collections import Counter, defaultdict
from dataclasses import dataclass, field
import functools
import re
from time import sleep, time

from aoc_tools import *

# @dataclass
# class O:
# 	p: int # position
# 	v: int # value
# 	l: int # length
# 	c: list = field(default_factory=list) # path

with open("2024/day10/input1.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

dir = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, 1], [1, 1], [1, -1], [-1, -1]]
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
di = 0

# g = Grid()
# g.read(lines)
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

# for i in range(0, len(lines), 1):
# 	for j in range(0, len(lines[i]), 1):
# 		c = g.g[(i,j)]

# for l1, l2, l3 in zip(lines[::3], lines[1::3], lines[2::3]): # read lines 3 by 3
for i, line in enumerate(lines):
	# print(f"{line=}")
	# for j, c in enumerate(line):
		
	# l = get_ints(line)
	# print(f"{l=}")

	pass

	total += 1

total = total
print(f"{total = }")
