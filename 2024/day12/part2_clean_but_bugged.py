from collections import defaultdict
from time import time

from aoc_tools import *

def search_region_plots(i,j,c):
	area = 0
	corners = defaultdict(int)

	q = [(i,j)]
	while q:
		i,j = q.pop()
		if ((i,j)) in vis:
			continue
		vis.add((i,j))

		area += 1
		# clean way to get perimeter: toggle corners in a boolean map
		for d in [(0,0), (0,1), (1,0), (1,1)]:
			nd = (i+d[0],j+d[1])
			corners[nd] = 1 - corners[nd]
		
		# bug for diagonal join, manual fix not working...
		if (i-1,j-1) in g.g and g.g[(i-1,j-1)] == c and g.g[(i-1,j)] != c and g.g[(i,j-1)] != c:
			# print(f"1")
			corners[(i-1,j-1)] += 2
		if (i-1,j+1) in g.g and g.g[(i-1,j+1)] == c and g.g[(i-1,j)] != c and g.g[(i,j+1)] != c:
			# print(f"2")
			corners[(i-1,j+1)] += 2

		# search adjacent with same letter
		for x,y,v in g.adj(i,j):
			if v == c:
				q.append((x,y))

	perim = sum(v for _,v in corners.items())

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
