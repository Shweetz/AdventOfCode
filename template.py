
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

with open("2024/day15/input1.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

L, LU, U, RU, R, RD, D, LD = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
dirs = {"<":L, "^":U, ">":R, "v":D}
dirs = [L, U, R, D]
di = 0

# g = Grid()
# g.read(lines)
# g.print()
# x,y = g.find("^")[0]
# pprint(f"{x,y=}")
# vis = set()

total, best, cur = 0, 0, 0

lo = [] # list of objects O

# lines = zip(*lines) # transpose

# for i in range(0, len(lines), 1):
# 	for j in range(0, len(lines[i]), 1):
# 		c = g.g[(i,j)]

# for l1, l2, l3 in zip(lines[::3], lines[1::3], lines[2::3]): # read lines 3 by 3
for i, line in enumerate(lines):
	# pprint(f"{line=}")
	# for j, c in enumerate(line):
		
	# l = get_ints(line)
	# pprint(f"{l=}")

	pass

	total += 1

total = total
print(f"{total = }")
