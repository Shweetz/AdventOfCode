
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

def try_move(move):
	pass

with open("2024/day15/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

L, LU, U, RU, R, RD, D, LD = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
dirs = [L, U, R, D]
dirs = {"<":L, "^":U, ">":R, "v":D}
di = 0

total = 0

# for i in range(0, len(lines), 1):
# 	for j in range(0, len(lines[i]), 1):
# 		c = g.g[(i,j)]

grid_lines = []
move_lines = []
for i, line in enumerate(lines):
	if line:
		if line[0] == "#":
			grid_lines += [line]
		else:
			move_lines += line

	# total += 1

# pprint(f"{grid_lines=}")
# pprint(f"{move_lines=}")

g = Grid()
g.read(grid_lines)
x,y,_,_ = g.find("@")[0]
# vis = set()

pprint(f"{x,y=}")

for move in move_lines:
	a,b = x,y
	dx,dy = dirs[move]
	try_move(move)
	poss = 0
	while poss == 0:
		a,b=a+dx,b+dy
		if g.g[(a,b)] == ".":
			poss = 1
		elif g.g[(a,b)] == "#":
			poss = -1
	# pprint(f"{poss=}")

	if poss == 1:
		while (a,b) != (x,y):
			g.g[(a,b)], g.g[(a-dx,b-dy)] = g.g[(a-dx,b-dy)], g.g[(a,b)]
			a,b=a-dx,b-dy
		x,y=a+dx,b+dy

	# g.print()

l = g.find("O")

for x,y,_,_ in l:
	# pprint(f"{x,y=}")
	total += x * 100 + y

total = int(total / 4)
print(f"{total = }")
