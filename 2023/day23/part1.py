from time import time

from queue import PriorityQueue

with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

def take_step(steps, x, y, visited):
	# print(steps, x, y)
	# print(len(visited))
	steps -= 1 # negative steps to start with highest steps are an optimization, but why?

	visited.add((x, y))
	
	l = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
	for p in l:
		# if p in grid:
		# 	print(p)
		# 	print(grid[p])
		if p in grid and p not in visited:
			if p[0] == x - 1 and grid[p] == "v": continue
			if p[1] == y - 1 and grid[p] == ">": continue
			queue.put((steps, *p, visited.copy()))

	finished = (x, y) == (len(lines) - 1, end_j)
	return steps, finished

# script start
t1 = time()
grid = {}
forced_paths = {}
queue = PriorityQueue()
max_steps = 0

for i, line in enumerate(lines):
	for j, char in enumerate(line):
		if char != "#":
			grid[(i, j)] = char


start_j = lines[0].find(".")
end_j = lines[-1].find(".")

queue.put((0, 0, start_j, set()))

while not queue.empty():
	steps, finished = take_step(*queue.get())
	if finished:
		max_steps = max(-steps, max_steps) # steps were negative

print(max_steps - 1) # start is not a step
print(f"Execution time: {(time() - t1):.3f}s")
