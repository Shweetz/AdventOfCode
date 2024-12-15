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
	moves = [(x,y,dx,dy)]
	poss = [None] # represents if the move is possible (linked by index with "moves"), True/False/Unknown
	while poss[-1] == None:
		a,b=a+dx,b+dy

		if g.g[(a,b)] == ".":
			# current move is possible
			poss[i] = True
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
			if g.g[(a,b)] == "[": col = b+1
			if g.g[(a,b)] == "]": col = b-1
			moves.append((a,col,dx,dy))
			poss.append(None)

		elif g.g[(a,b)] == "#":
			# can not move
			poss[i] = False
			break

	if not False in poss:
		# move is possible, so every cell implicated must be moved exactly once
		moved = set()
		for move in moves:
			a,b,dx,dy = move
			if ((a,b)) in moved:
				# do not move a cell twice
				continue
			
			option = 1

			if option == 1:
				# place a "." at the start of the move, then push everything once until reaching the next "."
				cur_e = "."
				next_e = g.g[(a,b)]
				while next_e != ".":
					next_e = g.g[(a,b)]
					g.g[(a,b)] = cur_e
					moved.add((a,b))
					cur_e = next_e
					a,b=a+dx,b+dy
			
			elif option == 2:
				# create a string with "." + moved cells in order until next ".", example: ".@[]"
				new_cells = "."
				next_e = g.g[(a,b)]
				while next_e != ".":
					new_cells += next_e
					
					a,b=a+dx,b+dy
					next_e = g.g[(a,b)]
				
				# insert the string in grid
				a,b,dx,dy = move
				for i in range(len(new_cells)):
					pos = (a + dx * i, b + dy * i)
					g.g[pos] = new_cells[i]
					moved.add(pos)
				
		x,y = x+dx, y+dy # update x,y position instead of looking for "@"in grid

l = g.find("[")

for x,y in l:
	total += x * 100 + y

print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")
assert total == 1467145
