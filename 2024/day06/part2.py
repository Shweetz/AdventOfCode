from time import time

from aoc_tools import *

t1 = time()
with open("2024/day06/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total = 0

dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
di = 0

g = Grid()
g.read(lines)
gg_copy = g.g.copy()

# find start pos with my tool :D
x1,y1,_,_ = g.find("^")[0]
x, y = x1, y1

# Optimisation: only place the obstacle on the obstacle-less path (algo done in part1)
vis_p1 = set() # represents the cells on the obstacle-less path
while (x,y) in g.g:
	# cell visited
	vis_p1.add((x,y))

	# try new position by moving in dir[di]
	(a,b) = dir[di]
	np = (x+a,y+b)

	if np not in g.g:
		# grid exit
		break
	
	if g.g[np] in ".^":
		# move to new position
		x,y = np

	if g.g[np] == "#":
		# turn right
		di = (di + 1) % 4

# Optimisation end

for i in range(len(lines)):
	for j in range(len(lines[0])):

		# Optimisation
		if not (g.g[(i,j)] == "." and (i,j) in vis_p1):
			continue
		
		# reset variables
		di = 0
		vis = set()
		x,y = x1,y1
		(a,b) = dir[di]

		# place the obstacle
		g.g[(i,j)] = "#"

		while (x,y) in g.g:
			(a,b) = dir[di]
			if ((x,y,a,b) in vis):
				# already visited cell with the same direction: loop found
				total += 1
				break

			# cell visited
			vis.add((x,y,a,b))

			# try new position by moving in dir[di]
			np = (x+a,y+b)

			if np not in g.g:
				# grid exit
				break
			
			if g.g[np] in ".^":
				# move to new position
				x,y = np

			if g.g[np] == "#":
				# turn right
				di = (di + 1) % 4
		
		# place back the "." that was changed in "#" for this iteration
		g.g[(i,j)] = "."

print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")
assert total == 1729
