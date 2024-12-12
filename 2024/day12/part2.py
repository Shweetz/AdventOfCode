from collections import defaultdict
from time import time

from aoc_tools import *

dirs = ["L", "R", "U", "D"]

def search_region_plots(i,j,c):
	area = 0
	perim2 = defaultdict(int)

	q = [(i,j)]
	while q:
		i,j = q.pop()
		if ((i,j)) in vis:
			continue
		vis.add((i,j))

		area += 1
		for d in dirs:
			# default: 1 wall in every direction around each cell
			perim2[(d,i,j)] = 1
		
		# search adjacent with same letter
		for x,y,v in g.adj(i,j):
			if v == c:
				q.append((x,y))

	perim = set()
	for i in range(0, len(lines), 1):
		for j in range(0, len(lines[i]), 1):
			for d in dirs:
				if not perim2[(d,i,j)]:
					continue

				if d == "L":
					o = "R"
					x,y=i-1,j
					a,b=i,j-1

				if d == "R":
					o = "L"
					x,y=i-1,j
					a,b=i,j+1

				if d == "U":
					o = "D"
					x,y=i,j-1
					a,b=i-1,j

				if d == "D":
					o = "U"
					x,y=i,j-1
					a,b=i+1,j

				# if previous adjacent also has the same wall, don't count the current one
				# example: (0,0) has a left wall    => perim2[("L",0,0)] != 0
				#     then (1,0)'s left wall is out => perim2[("L",1,0)] = -1
				#      and (2,0)'s left wall is out => perim2[("L",2,0)] = -1
				if ((d,x,y)) in perim2 and perim2[(d,x,y)] != 0 and g.g[(x,y)] == c:
					perim2[(d,i,j)] = -1
					
				# common walls cancel each other
				# example: (0,0) has a right wall and (0,1) has a left wall
				# => perim2[("R",0,0)] = 0 and perim2[("L",0,1)] = 0
				if ((o,a,b)) in perim2 and g.g[(a,b)] == c:
					perim2[(d,i,j)] = 0
					perim2[(o,a,b)] = 0
				
				# if current wall is not cancelled and needs to be counted
				if perim2[(d,i,j)] == 1:
					perim.add((d,i,j))

	perim = len(perim)

	print(f"{c=} {area=} {perim=}")
	return area, perim

t1 = time()
with open("2024/day12/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

g = Grid()
g.read(lines)

vis = set()

total = 0

for i in range(0, len(lines), 1):
	for j in range(0, len(lines[i]), 1):
		if (i,j) not in vis:
			c = g.g[(i,j)]

			# search other plots in same region (same letter c)
			a, p = search_region_plots(i,j,c)

			total += a*p

print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")
assert total == 858684
