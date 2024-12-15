from collections import defaultdict
from time import time

from aoc_tools import *

t1 = time()
with open("2024/day15/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

L, LU, U, RU, R, RD, D, LD = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
dirs = {"<":L, "^":U, ">":R, "v":D}

total = 0

grid_lines = []
move_lines = []
for i, line in enumerate(lines):
	if line:
		if line[0] == "#":
			grid_lines += [line]
		else:
			move_lines += line

g = Grid()
g.read(grid_lines)
x,y = g.find("@")[0]

for move in move_lines:
	a,b = x,y
	dx,dy = dirs[move]
	
	# test if move from (a,b) in direction (dx,dy) is possible
	while True:
		a,b=a+dx,b+dy

		if g.g[(a,b)] == ".":
			# can move, swap elements 2 by 2 backwards (from "." to "@") so that all elements move by 1
			while (a,b) != (x,y):
				g.g[(a,b)], g.g[(a-dx,b-dy)] = g.g[(a-dx,b-dy)], g.g[(a,b)]
				a,b=a-dx,b-dy

			x,y=a+dx,b+dy # update x,y position instead of looking for "@"in grid
			break

		elif g.g[(a,b)] == "#":
			# can not move
			break

l = g.find("O")

for x,y in l:
	total += x * 100 + y

print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")
assert total == 1457740
