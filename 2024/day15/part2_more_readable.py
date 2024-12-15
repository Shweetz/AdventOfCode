from collections import defaultdict
from time import time

from aoc_tools import *

t1 = time()
with open("2024/day15/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

L, LU, U, RU, R, RD, D, LD = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
dirs = {"<":L, "^":U, ">":R, "v":D}

total = 0

grid_lines = []
move_lines = []
for i, line in enumerate(lines):
	if line:
		if line[0] == "#":
			line2 = ""
			for c in line:
				if c == "#": line2 += "##"
				if c == "O": line2 += "[]"
				if c == ".": line2 += ".."
				if c == "@": line2 += "@."
			grid_lines += [line2]
		else:
			move_lines += line

g = Grid()
g.read(grid_lines)
x,y = g.find("@")[0]

for move in move_lines:
	a,b = x,y
	dx,dy = dirs[move]
	
	i = 0
	# moves is a dict where key is (pos+dir) and value is the position of 1st "." (end of move), 0 if position is unknown or impossible
	# moves = {(x,y,dx,dy):0}
	moves = [(x,y,dx,dy)]
	endpos = [None] # position of the 1st "." in the move (linked by index with "moves"), can be False if doesn't exist or None if unknown
	
	while endpos[-1] == None:
		a,b=a+dx,b+dy

		if g.g[(a,b)] == ".":
			# current move is possible
			endpos[i] = (a,b)
			i += 1
			if i < len(moves):
				# must check other moves forced by 1st move
				a,b,dx,dy = moves[i]
				continue
			else:
				# current move is possible with its implications
				break

		if g.g[(a,b)] in "[]" and dirs[move] in [U,D]:
			# create a new vertical move to update the other half of the moved box
			# warning: this can create "fake moves" because a move starting earlier will already push the same cells
			if g.g[(a,b)] == "[": col = b+1
			if g.g[(a,b)] == "]": col = b-1
			moves.append((a,col,dx,dy))
			endpos.append(None)

		elif g.g[(a,b)] == "#":
			# can not move
			endpos[i] = False
			break

	if not False in endpos:
		# move is possible, so every cell implicated must be moved exactly once
		moved = set()
		for i, move in enumerate(moves):
			a,b = endpos[i]
			p,q,dx,dy = move
			if ((a,b)) in moved:
				# do not move a cell twice
				# this is needed because some moves can overlap because of "fake moves", example: (0,1,1,0) and (2,1,1,0)
				continue
			
			# can move, swap elements 2 by 2 backwards (from endpos to 1st cell moving, like "." to "@") so that all elements move by 1
			while (a,b) != (p,q):
				g.g[(a,b)], g.g[(a-dx,b-dy)] = g.g[(a-dx,b-dy)], g.g[(a,b)]
				moved.add((a,b))
				a,b=a-dx,b-dy
				
		x,y = x+dx, y+dy # update x,y position instead of looking for "@"in grid

l = g.find("[")

for x,y in l:
	total += x * 100 + y

print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")
assert total == 1467145
