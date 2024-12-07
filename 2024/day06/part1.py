from aoc_tools import *

with open("2024/day06/input1.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

g = Grid()
g.read(lines)
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
di = 0

vis = set()

# find start pos
for p, c in g.g.items():
	if c not in ".#":
		(x,y) = p
		break

# find start pos with my tool :D
x,y,_,_ = g.find("^")[0]

while (x,y) in g.g:
	# cell visited
	vis.add((x,y))

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

total = len(vis)
print(f"{total = }")
assert total == 4977
