
from collections import Counter, defaultdict
from dataclasses import dataclass, field
import functools
import math
import re
from queue import PriorityQueue
import sympy
import sys
import functools
from time import sleep, time

from aoc_tools import *

sys.setrecursionlimit(1000000)

L, LU, U, RU, R, RD, D, LD = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
dirs = {"<":L, "^":U, ">":R, "v":D}
dirs = [L, U, R, D] # directions
di = 0 # direction index

def pprint(s):
	# print(s)
	pass

# @functools.cache
# def find_part(j, design_part):
	
@functools.cache
def find(j, design):
	pprint(f"{j, design=}")
	if poss[j]:
		return True
	
	if design in patterns:
		poss[j] = True
		return True
	
	for i in range(1, p_max_l + 1):
		if design[:i] in patterns: 
			pprint(f"{j, design[:i], design[i:]=}")
			find(j, design[i:])

	# for p in patterns:
	# 	l = len(p)
	# 	if design[:l] == p: 
	# 		pprint(f"{j, design[:i], design[i:]=}")
	# 		find(j, design[l:])

# @dataclass
# class O:
# 	p: int # position
# 	v: int # value
# 	l: int # length
# 	c: list = field(default_factory=list) # path

t1 = time()
with open("2024/day19/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total, best, cur = 0, sys.maxsize, 0

patterns = lines[0].split(", ")
pprint(f"{patterns=}")

patterns = Counter(patterns)
pprint(f"{patterns=}")

p_max_l = max(len(p) for p in patterns)
pprint(f"{p_max_l=}")

# for i in range(0, len(lines), 1):
# 	for j in range(0, len(lines[i]), 1):
# 		c = g.g[(i,j)]

designs = []
for i, line in enumerate(lines[2:]):
	designs.append(line)

pprint(f"{designs=}")

poss = defaultdict(bool)

for j, design in enumerate(designs):

	poss[j] = False

	# for i in len(design):
	find(j, design)

pprint(f"{poss=}")
total = sum(poss.values())
print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")
