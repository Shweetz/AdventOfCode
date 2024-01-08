from time import time

from dataclasses import dataclass, field
from queue import PriorityQueue

@dataclass(order=True)
class Pos:
    x: int
    y: int

def take_step(steps, x, y):
	# print(steps)
	if steps == nb_steps:
	# 	poss.add((pos.x, pos.y))
		return
	
	steps += 1
	l = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
	for p in l:
		# print(grid[p])
		if p in grid:
		# if p in grid:
			if steps % 2 == 1:
				poss.add(p)
				# print(grid[p], p)
			del grid[p]
			# grid.pop(p, None)
			queue.put((steps, *p))
	# print(grid[(x, y)], (x, y))


# script start
t1 = time()
with open("input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

grid = {}
poss = set()
nb_steps = 26501365
queue = PriorityQueue()

for i, line in enumerate(lines):
	for j, char in enumerate(line):
		if char == ".":
			grid[(i, j)] = char

		if char == "S":
			start = (i, j)
			grid[start] = "."

queue.put((0, *start))

while not queue.empty():
	take_step(*queue.get())

# target = "even" if (nb_steps % 2 == 0) else "odd"
# print(len([p for p in grid.values() if p == target]))
print(len(poss))
# print(poss)
print(f"Execution time: {(time() - t1):.3f}s")

# ideas:
# hold a set of poss and delete from grid once visited to remove "if grid[p] == ".""
# add all visited tiles in poss and at the end filter with xS + yS - (xi + yi) % 2 == 0 when nb_steps is even