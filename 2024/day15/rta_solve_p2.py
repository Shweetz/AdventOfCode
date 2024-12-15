
from collections import Counter, defaultdict
from dataclasses import dataclass, field
import functools
import math
import re
import sympy
from time import sleep, time

from aoc_tools import *

def pprint(s):
	# print(s)
	pass

# @dataclass
# class O:
# 	p: int # position
# 	v: int # value
# 	l: int # length
# 	c: list = field(default_factory=list) # path

def try_move(move):
	pass

with open("2024/day15/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

L, LU, U, RU, R, RD, D, LD = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
dirs = [L, U, R, D]
dirs = {"<":L, "^":U, ">":R, "v":D}
di = 0

total = 0

# for i in range(0, len(lines), 1):
# 	for j in range(0, len(lines[i]), 1):
# 		c = g.g[(i,j)]

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

	# total += 1

pprint(f"{grid_lines=}")
# pprint(f"{move_lines=}")

g = Grid()
g.read(grid_lines)
x,y,_,_ = g.find("@")[0]
# vis = set()
g.print()

pprint(f"{x,y=}")

for move in move_lines:
	movep = move
	a,b = x,y
	dx,dy = dirs[move]
	try_move(move)

	moves = [(x,y,dx,dy)]
	# poss = 0
	# while poss < len(moves) and poss != -1:
	i = 0
	poss = [0]
	possb = True
	while poss[-1] == 0:
		a,b=a+dx,b+dy
		if g.g[(a,b)] == ".":
			poss[i] = 1
			i += 1
			# pprint(f"{i, len(moves)=}")
			if i >= len(moves):
				break
			else:
				poss.append(0)
				a,b,dx,dy = moves[i]
				continue

		if g.g[(a,b)] == "[" and dirs[move] in [U,D]:
			# cs = set([b for _,b,_,_ in moves])
			# if not b+1 in cs:
				moves.append((a,b+1,dx,dy))
		if g.g[(a,b)] == "]" and dirs[move] in [U,D]:
			# for _,c,_,_ in moves:
			# 	if c == b-1:
			# 		continue
			# cs = set([b for _,b,_,_ in moves])
			# if not b-1 in cs:
				moves.append((a,b-1,dx,dy))
		elif g.g[(a,b)] == "#":
			possb = False
			break


	if possb:
		pprint(f"{moves=}")
		moved = set()
		for move in moves:
			a,b,dx,dy = move
			if ((a,b)) in moved:
				continue
			cur_e = "."
			next_e = g.g[(a,b)]
			while next_e != ".":
				next_e = g.g[(a,b)]
				# g.g[(a,b)], g.g[(a+dx,b+dy)] = g.g[(a+dx,b+dy)], g.g[(a,b)]
				g.g[(a,b)] = cur_e
				moved.add((a,b))
				cur_e = next_e
				a,b=a+dx,b+dy
				# g.print()

			# chars = []
			# while g.g[(a+dx,b+dy)] != ".":
			# 	chars += g.g[(a,b)]
			# 	a,b=a+dx,b+dy
				# if g.g[(a,b)] == ".":
				# 	break
			# g.print()
			# sleep(0.3)
		
		# x,y,_,_ = g.find("@")[0]
		x,y = x+dx, y+dy

	# print(f"{movep=}")
	# g.print()
	# input()
	# sleep(0.5)

g.print()
l = g.find("[")
for x,y,_,_ in l:
	# pprint(f"{x,y=}")
	total += x * 100 + y

total = int(total / 4)
print(f"{total = }")

#1483263 too high