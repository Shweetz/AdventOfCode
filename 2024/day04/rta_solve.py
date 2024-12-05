from collections import Counter, defaultdict
from dataclasses import dataclass
import re

# from aoc_tools import *

@dataclass
class Object: pass

with open("2024/day04/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total = 0

grid = {}
for i, line in enumerate(lines):
	for j, c in enumerate(line):
		grid[(i, j)] = c

# rta
# dir = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

# alt, pas fait rta
dir = []
for i in [-1, 0, 1]:
	for j in [-1, 0, 1]:
		if (i, j) != (0, 0):
			dir.append((i, j))
print(f"{dir=}")

#p1
for i, line in enumerate(lines):
	for j, c in enumerate(line):
		if c == "X":
			for x, y in dir:
				if (i+x*3, j+y*3) in grid and grid[(i+x, j+y)] + grid[(i+x*2, j+y*2)] + grid[(i+x*3, j+y*3)] == "MAS":
					# print(f"{i,j=}")
					# total += 1
					pass
# print(f"{total = }")

#p2
for i, line in enumerate(lines):
	for j, c in enumerate(line):
		if c == "A":
			# for x, y in dir:
			if (i+1, j+1) in grid and (i-1, j-1) in grid:
				# ma méthode rta nulle 
				# if grid[(i+1, j+1)] == grid[(i+1, j-1)] == "M" and grid[(i-1, j-1)] == grid[(i-1, j+1)] == "S":
				# 	total += 1
				# if grid[(i+1, j-1)] == grid[(i-1, j-1)] == "M" and grid[(i-1, j+1)] == grid[(i+1, j+1)] == "S":
				# 	total += 1
				# if grid[(i-1, j-1)] == grid[(i-1, j+1)] == "M" and grid[(i+1, j+1)] == grid[(i+1, j-1)] == "S":
				# 	total += 1
				# if grid[(i-1, j+1)] == grid[(i+1, j+1)] == "M" and grid[(i+1, j-1)] == grid[(i-1, j-1)] == "S":
				# 	total += 1
					
				# la méthode que j'aurais pu trouver xd
				corners = grid[(i+1, j+1)] + grid[(i+1, j-1)] + grid[(i-1, j-1)] + grid[(i-1, j+1)]
				print(f"{corners=}")
				if corners in "MMSSMMS":
					total += 1

print(f"{total = }")



	# total += 1

# ll2 = zip(*ll)
# print(f"{list(ll2) = }")

print(f"{total = }")
