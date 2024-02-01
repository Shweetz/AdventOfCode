from time import time

from queue import PriorityQueue
import sys

def take_step(steps, map_steps, poss, x, y):
	# print(x, y)
		
	if steps > map_steps:
	# 	poss.add((pos.x, pos.y))
		return
	
	steps += 1
	l = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
	for p in l:
		# print(grid[p])
		if p in grid and p not in poss:
		# if p in grid:
			if steps % 2 == map_steps % 2:
				poss.add(p)
				# print(grid[p], p)
			# del grid[p]
			# grid.pop(p, None)
			queue.put((steps, map_steps, poss, *p))
	# print(grid[(x, y)], (x, y))

# explore the map from a start pos in a number of steps
def explore(start, map_steps):
	# special case
	if map_steps == 0:
		return 1
	
	# regular case
	poss = set()

	queue.put((0, map_steps, poss, *start))

	while not queue.empty():
		take_step(*queue.get())
	
	# print(poss)
	return len(poss)

def reverse_p(parity):
	return "even" if parity == "odd" else "odd"

# script start
t1 = time()
with open("input_5.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

size = len(lines)
grid = {}
nb_steps = 26501365
if len(sys.argv) > 1:
	nb_steps = int(sys.argv[1])
queue = PriorityQueue()
total = 0

for i, line in enumerate(lines):
	for j, char in enumerate(line):
		if char == "." or char == "S":
			grid[(i, j)] = char

#######################
# IN MAP LOCALIZATION #
#######################
# size 131, center = (66, 66), indexing start at 0 => center = (65, 65), bottom right = (130, 130)
full = size - 1  # 130
half = full // 2 # 65

center = (half, half)

#################
# NOT FULL MAPS #
#################

# center map
total += explore(center, nb_steps)
print(total, "+ center")

with open("mass_output.txt", "a") as f:
	f.write(str(nb_steps) + " " + str(total) + "\n")

print(f"Execution time: {(time() - t1):.3f}s")

# 64  steps = 3748
# 66  steps = 4012 (no inf : 4008)
# 132 steps = ? (no inf : -4)

# 616951781284108 too low
# 616957838150001 too high

# je veux
# 132       start corner outer
# 132 + 131 start corner outer, outer -> inner
# 132 + 260 inner -> full, outer -> inner
# 132 + 262 start corner outer

# 26501365 % 131 = 65