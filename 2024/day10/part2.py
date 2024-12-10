from time import time

from aoc_tools import *

t1 = time()
with open("2024/day10/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

g = Grid()
g.read(lines)

total = 0
q = []
for i in range(0, len(lines), 1):
	for j in range(0, len(lines[i]), 1):
		if g.g[(i,j)] == "0":
			q.append((i,j,0))

while q:
	i,j,v = q.pop()
	for x,y,v2 in g.adj(i,j):
		if int(v2) == v+1:
			if int(v2) == 9:
				total += 1
			else:
				q.append((x,y,int(v2)))


print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")
assert total == 1657
