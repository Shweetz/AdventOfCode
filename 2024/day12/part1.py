from time import time

from aoc_tools import *

def search_region_plots(i,j,c):
	area = 0
	perim = 0

	q = [(i,j)]
	while q:
		i,j = q.pop()
		if ((i,j)) in vis:
			continue
		vis.add((i,j))

		area += 1
		# perimeter for the cell is (4 - nb adjacent with same letter)
		perim += 4
		
		# search adjacent with same letter
		for x,y,v in g.adj(i,j):
			if v == c:
				q.append((x,y))
				perim -= 1

	# print(f"{c=} {area=} {perim=}")
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
assert total == 1424006
