from time import time

from dataclasses import dataclass, field
from queue import PriorityQueue

with open("input_s.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

@dataclass
class ForcedPath:
	steps : int # path length
	x1 : int # start
	y1 : int # start
	x2 : int # end
	y2 : int # end
	visited : set = field(default_factory=set)


def find_intersections():
	intersections = set()
	for (x, y) in grid.keys():
		neighbors_count = 0
		l = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
		for p in l:
			if p in grid:
				neighbors_count += 1
		
		if neighbors_count > 2:
			intersections.add((x, y))
	
	return intersections

def fill_forced_path(x, y):
	# start is real start or any symbol
	start = (x, y)
	
	l = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
	for p in l:
		if p in grid and p not in intersections:
			# should have only 1 neighbor that is not an intersection
			queue.put((0, *p, {start}, False))

			# follow the path until next intersection (where qsize > 1)
			while queue.qsize() == 1:
				steps, x, y, visited = take_step(*queue.get())
	
			forced_paths[start] = ForcedPath(steps-1, *start, x, y, visited)
			print(forced_paths[start])

			queue.queue.clear()

def take_step(steps, x, y, visited, solving):
	steps = -steps # negative steps to start with highest steps are an optimization, but why?
	print(steps, x, y)
	steps += 1
	
	visited.add((x, y))

	if (x, y) in forced_paths and solving:
		# enter a forced path
		fp = forced_paths[(x, y)]
		
		if (fp.x2, fp.y2) not in visited:
			# the forced path exit has not been visited yet: can travel the path: add the path steps and tp to its exit
			vis = visited.copy()
			vis.add((fp.x2, fp.y2))
			queue.put((-(steps+fp.steps), fp.x2, fp.y2, vis, solving))

		return steps, x, y, visited
	
	l = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
	for p in l:
		if p in grid and p not in visited:
			# add neighbors to queue
			queue.put((-steps, *p, visited.copy(), solving))

	return steps, x, y, visited

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
end_pos = (len(lines) - 1, end_j)

# intersections
intersections = find_intersections()
print(f"{intersections=}")

# forced paths
fill_forced_path(0, start_j)

for (i, j), char in grid.items():
	if char != ".":
		fill_forced_path(i, j)

print("forced paths nb =", len(forced_paths))

# solve using forced paths to tp
queue.queue.clear()
queue.put((0, 0, start_j, set(), True))

while not queue.empty():
	steps, x, y, visited = take_step(*queue.get())

	if (x, y) == end_pos:
		# reached finish
		if (steps > max_steps):
			print(steps - 1)
			max_steps = steps

print(max_steps - 1) # start is not a step
print(f"Execution time: {(time() - t1):.3f}s")
