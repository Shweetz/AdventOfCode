from collections import Counter, defaultdict
from dataclasses import dataclass
import re

from aoc_tools import *

@dataclass
class Object: pass

with open("2024/day06/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

g = Grid()
g.read(lines)
# print(f"{g.g=}")
# print(f"{g.g[(0,0)]=}")
# print(f"{g.adj(0,0,0)=}")
# print(f"{len(g.find("XMAS", 0))=}")
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
# dir = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, 1], [1, 1], [1, -1], [-1, -1]]
# L, LU, U, RU, R, RD, D, LD = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]

total = 0
best = 0
cur = 0

#p1
vis = set()
di = 0

# for l1, l2, l3 in zip(lines[::3], lines[1::3], lines[2::3]):
for p, c in g.g.items():
	if c not in ".#":
		print(f"{p,c=}")
		(x,y) = p
		(a,b) = dir[di]

while (x,y) in g.g:
	print(f"{x,y=}")
	vis.add((x,y))

	np = (x+a,y+b)
	if np in g.g:
		if g.g[np] == ".":
			x,y = x+a,y+b
		while g.g[np] == "#":
			di = (di + 1) % 4
			(a,b) = dir[di]
			np = (x+a,y+b)
		x,y = np
	else:
		break

#p2
total = 0
di = 0
start = (0,0)
# for l1, l2, l3 in zip(lines[::3], lines[1::3], lines[2::3]):
for p, c in g.g.items():
	if c not in ".#":
		print(f"{p,c=}")
		start = p
		(x,y) = p
		(a,b) = dir[0]

for i in range(len(lines)):
	for j in range(len(lines[0])):
# if True:
# 	if True:
# 		i,j=9,7
		# if (i,j)==(9,7):
		# 	print(f"test")
		di = 0
		(x,y) = start
		(a,b) = dir[di]
		print(f"{i,j=}")
		g = Grid()
		g.read(lines)
		# if g.g[(i,j)] == "^":
		# 	continue
		# old = g.g[(i,j)]
		g.g[(i,j)] = "#"
		# if (i,j)==(9,7): print(f"{g.g[(1,5)]=}")
		vis = set()
		while (x,y) in g.g:
			# if (i,j)==(9,7): print(f"{x,y,a,b=}")
			
			if ((x,y,a,b) in vis):
				# if (i,j)==(9,7): print(f"{i,j=}")
				total += 1
				break
			vis.add((x,y,a,b))

			np = (x+a,y+b)
			if np in g.g:
				if g.g[np] == ".":
					x,y = x+a,y+b
				while g.g[np] == "#":
					# print(f"{np=}")
					di = (di + 1) % 4
					(a,b) = dir[di]
					np = (x+a,y+b)
				x,y = np
			else:
				break
			
		# g.g[(i,j)] = old
		# print(f"{g.g[(i,j)]=}")

# ll2 = zip(*ll)
# print(f"{list(ll2) = }")
total = len(vis)
print(f"{total = }")
