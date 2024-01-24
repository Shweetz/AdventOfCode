from time import time

from queue import PriorityQueue

def take_step(steps, x, y):
	if steps > nb_steps:
		return
	
	steps += 1
	l = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
	for p in l:
		if p in grid and grid[p] == ".":
			# write if garden neighbor is even or odd
			if steps % 2 == 0:
				grid[p] = "even"
			else:
				grid[p] = "odd"
			
			# add neighbor to explore
			queue.put((steps, *p))


# script start
t1 = time()
with open("input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

grid = {}
nb_steps = 64
queue = PriorityQueue()

for i, line in enumerate(lines):
	for j, char in enumerate(line):
		grid[(i, j)] = char

		if char == "S":
			start = (i, j)
			grid[start] = "even"

queue.put((0, *start))

while not queue.empty():
	take_step(*queue.get())

# count the "even" or "odd" in grid
target = "even" if (nb_steps % 2 == 0) else "odd"
print(len([p for p in grid.values() if p == target]))
print(f"Execution time: {(time() - t1):.3f}s")

# ideas:
# hold a set of poss and delete from grid once visited to remove "if grid[p] == ".""
# add all visited tiles in poss and at the end filter with xS + yS - (xi + yi) % 2 == 0 when nb_steps is even