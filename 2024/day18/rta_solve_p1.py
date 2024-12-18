
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

with open("2024/day18/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

g = Grid()
# g.read(lines)
# g.print()
# x,y = g.find("^")[0]
# pprint(f"{x,y=}")
# visited = set()

total, best, cur = 0, sys.maxsize, 0

lo = [] # list of objects O

# lines = zip(*lines) # transpose

size = 71
bytes = 1024
for i in range(0, size, 1):
	for j in range(0, size, 1):
		g.g[(i,j)] = "."

pprint(f"{len(g.g)=}")
g.print()

# for l1, l2, l3 in zip(lines[::3], lines[1::3], lines[2::3]): # read lines 3 by 3
for i, line in enumerate(lines[:bytes]):
	# pprint(f"{line=}")
	# for j, c in enumerate(line):
		
	y,x = get_ints(line)
	# pprint(f"{l=}")
	g.g[(x,y)] = "#"

g.print()

visited = defaultdict(lambda:best)
q = PriorityQueue()
q.put((0, (0,0), 2))
q.put((0, (0,0), 3))

while not q.empty():
	score, pos, di = q.get()

	if pos not in g.g or g.g[pos] == "#":
		continue

	if score >= best:
		# worse than a path to the end
		continue
	
	if score >= visited[pos]:
		# worse than another path to this tile/direction
		continue
	else:
		# new best score from start to here
		visited[pos] = score
		pprint(f"{pos=}")

	if pos == (size-1,size-1):
		# reached finish
		if score < best:
			best = score

	else:
		# take a new step to neighbors: same direction, right, left
		for new_di in [di, di+1, di-1]:
			new_di = new_di % 4
			
			new_score = score + 1
			# if new_di != di:
			# 	# change direction = 1000 pts
			# 	new_score += 1000

			new_pos = move(pos, new_di)
			q.put((new_score, new_pos, new_di))

total = best
print(f"{total = }")
