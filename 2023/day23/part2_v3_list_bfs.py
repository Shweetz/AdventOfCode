from time import time

from queue import PriorityQueue

with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]


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

def fill_adj(x, y):
	start = (x, y)
	adj[start] = set()
	
	l = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
	for p in l:
		if p in grid:
			# every grid neighbor is a forced path to the next intersection
			queue.put((0, *p, {start}, False))

			# follow the path until next intersection (where qsize > 1)
			while queue.qsize() == 1:
				steps, x, y, visited = take_step(*queue.get())
	
			if (x, y) == end_pos:
				steps += 1
			adj[start].add((x, y, steps))

			queue.queue.clear()

	print(start, adj[start])

def take_step(steps, x, y, visited, solving):
	steps = -steps # negative steps to start with highest steps are an optimization, but why?
	# print(steps, x, y)
	pos = (x, y)

	if pos == end_pos:
		return steps, x, y, visited
	
	visited.add(pos)

	if solving:
		for (ax, ay, asteps) in adj[pos]:
			if (ax, ay) not in visited:
				# enter a forced path
				queue.put((-(steps+asteps), ax, ay, visited.copy(), solving))

		return steps, x, y, visited
	
	steps += 1
	l = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
	for p in l:
		if p in grid and p not in visited:
			# add neighbors to queue
			queue.put((-steps, *p, visited.copy(), solving))

	return steps, x, y, visited

# script start
t1 = time()
grid = {}
adj = {}
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
fill_adj(0, start_j)

for (i, j) in intersections:
	fill_adj(i, j)

# solve using list and pseudo-dfs
l = [(0, start_j, 0, set())]

while l:
	x, y, steps, vis = l.pop()
	# print(x, y, steps)
	pos = (x, y)

	if pos == end_pos:
		# reached finish
		if (steps > max_steps):
			print(steps)
			max_steps = steps

	elif pos not in vis:
		vis2 = vis.copy()
		vis2.add(pos)
		
		for (ax, ay, asteps) in adj[pos]:
			l.append((ax, ay, steps+asteps, vis2))

		# vis.remove(pos)

print(max_steps)
print(f"Execution time: {(time() - t1):.3f}s")
