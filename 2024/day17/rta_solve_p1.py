
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

def move(pos, di):
	"""Move from a position to a direction, "di" is the index in the "dirs" list"""
	d = dirs[di]
	return (pos[0] + d[0], pos[1] + d[1])

def pprint(s):
	print(s)
	pass

# @dataclass
# class O:
# 	p: int # position
# 	v: int # value
# 	l: int # length
# 	c: list = field(default_factory=list) # path

def get_value(operand):
	if operand <= 3:
		return operand
	if operand == 4:
		return a
	if operand == 5:
		return b
	if operand == 6:
		return c
	
with open("2024/day17/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

# g = Grid()
# g.read(lines)
# g.print()
# x,y = g.find("^")[0]
# pprint(f"{x,y=}")
# visited = set()

total, best, cur = 0, sys.maxsize, 0

lo = [] # list of objects O

# lines = zip(*lines) # transpose

# for i in range(0, len(lines), 1):
# 	for j in range(0, len(lines[i]), 1):
# 		c = g.g[(i,j)]

# for l1, l2, l3 in zip(lines[::3], lines[1::3], lines[2::3]): # read lines 3 by 3
# for i, line in enumerate(lines):
# 	# pprint(f"{line=}")
# 	# for j, c in enumerate(line):
		
# 	# pprint(f"{l=}")

# 	pass

# 	total += 1

total = ""

a = get_ints(lines[0])[0]
b = get_ints(lines[1])[0]
c = get_ints(lines[2])[0]
program = get_ints(lines[4])

i = 0
while i < len(program):
	opcode, operand = program[i], program[i+1]
	pprint(f"{opcode, operand=}")

	ope = get_value(operand)

	if opcode == 0:	
		a = int(a / pow (2, ope))

		pprint(f"{a=}")
		
	if opcode == 1:
		b = b ^ operand

		pprint(f"{b=}")
		
	if opcode == 2:
		b = ope % 8

		pprint(f"{b=}")
		
	if opcode == 3:
		if a != 0:
			i = operand - 2

		pprint(f"{i=}")
		
	if opcode == 4:
		b = b ^ c

		pprint(f"{b=}")
		
	if opcode == 5:
		total += str(ope % 8) + ","

		pprint(f"{total=}")
		
	if opcode == 6:
		b = int(a / pow (2, ope))

		pprint(f"{b=}")
		
	if opcode == 7:
		c = int(a / pow (2, ope))

		pprint(f"{c=}")

	i += 2

total = total[:-1]
print(f"{total = }")
