from time import time

from aoc_tools import *

t1 = time()
with open("2024/day18/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

size = 7
bytes = 12
size = 71
bytes = 1024

pos_list = []
for line in lines[:bytes]:
	y,x = get_ints(line)
	pos_list.append((x,y))

g = Grid()

g.build(size, size, pos_list)

g.print()

i = bytes
best = 0
while best != sys.maxsize:
	best, best_tiles = g.bfs((0,0), (size-1,size-1))

	if best != sys.maxsize:
		# an exit path has been found (it is the shortest path: best_tiles)
		
		while True:
			# can add walls as long as they are not on the exit path
			y,x = get_ints(lines[i])
			g.g[(x,y)] = "#"

			if ((x,y)) in best_tiles:
				# once a wall is added on the exit path, need to do another bfs to check if another path exists
				break
			i += 1

total = lines[i]
print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")
assert total == 231309103124520
