
from collections import Counter, defaultdict
from dataclasses import dataclass, field
import functools
import math
import re
from queue import PriorityQueue
import sys
from time import sleep, time

from aoc_tools import *

sys.setrecursionlimit(1000000)

L, LU, U, RU, R, RD, D, LD = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
dirs = {"<":L, "^":U, ">":R, "v":D}
dirs = [L, U, R, D] # directions
di = 0 # direction index
L, U, R, D = "<", "^", ">", "v"

def pprint(s):
	print(s)
	pass

def dist(grid, start, end):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == start:
				a,b = i,j
			if grid[i][j] == end:
				c,d = i,j
	
	return abs(c-a) + abs(d-b)

def paths(pad, start, end):
	buttons = []
	nb = defaultdict(int)
	for i in range(len(pad)):
		for j in range(len(pad[0])):
			if pad[i][j] == start:
				a,b = i,j
			if pad[i][j] == end:
				c,d = i,j
	
	nb[L] = max(b - d, 0)
	nb[U] = max(a - c, 0)
	nb[R] = max(d - b, 0)
	nb[D] = max(c - a, 0)

	# for d in [U, L, R, D]:
	# 	for _ in range(nb[d]):
	# 		buttons.append(d)
	start_hor = True

	if nb[R] and pad[c][b] != "x":
		for d in [U, D]:
			for _ in range(nb[d]):
				buttons.append(d)
		for d in [R, L]:
			for _ in range(nb[d]):
				buttons.append(d)
	elif pad[a][d] != "x":
		for d in [R, L]:
			for _ in range(nb[d]):
				buttons.append(d)
		for d in [U, D]:
			for _ in range(nb[d]):
				buttons.append(d)
	else:
		for d in [U, D]:
			for _ in range(nb[d]):
				buttons.append(d)
		for d in [R, L]:
			for _ in range(nb[d]):
				buttons.append(d)

	return buttons

def find_buttons_from_code(pad, code):
	moves = []
	path = []
	buttons = []
	c1 = "A"
	for c2 in code:
		# total += dist(pad, c1, c2) + 1
		# nb = paths(pad, c1, c2)
		# if len(pad) == 4:
		# 	for d in [U, L, R, D]:
		# 		for _ in range(nb[d]):
		# 			buttons.append(d)
		# else:
		# 	for d in [D, L, R, U]:
		# 		for _ in range(nb[d]):
		# 			buttons.append(d)

		for e in paths(pad, c1, c2):
			buttons.append(e)
		buttons.append("A")
		
		# print(total)
		print(buttons)

		# if nb[U] and not nb[R]: # U or UL
		# 	# 1st move is left on keypad
		# 	pass
		# else:
		# 	# 1st move is down on keypad
		# 	pass

		c1 = c2
	
	return buttons

def decode(s):
	decoded = ""
	i,j = 0,2
	for c2 in s:
		if c2 == "<": j -= 1
		if c2 == "^": i -= 1
		if c2 == ">": j += 1
		if c2 == "v": i += 1
		if c2 == "A": decoded += dirpad[i][j]

	return decoded

# @dataclass
# class O:
# 	p: int # position
# 	v: int # value
# 	l: int # length
# 	c: list = field(default_factory=list) # path

t1 = time()
with open("2024/day21/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

numpad = "7,8,9 4,5,6 1,2,3 x,0,A"
# for i, n in enumerate(numpad):
numpad = [a.split(",") for a in numpad.split()]
print(numpad)
# for i in range(numpad):
# 	for j in range(numpad[0]):
# 		c = g.g[(i,j)]
dirpad = "x,^,A <,v,>"
# for i, n in enumerate(numpad):
dirpad = [a.split(",") for a in dirpad.split()]
print(dirpad)

print(dist(numpad, "7", "2"))

total = 0

for i, code in enumerate(lines):
	print(code)

	# moves = []
	# path = []
	# buttons = []

	# 1st robot
	buttons = find_buttons_from_code(numpad, code)

	# 2nd robot
	print("")
	print("2nd robot")
	code = buttons
	print(code)

	buttons = find_buttons_from_code(dirpad, code)

	# 3rd robot
	print("")
	print("3rd robot")
	code = buttons
	print(code)
	buttons = find_buttons_from_code(dirpad, code)

	print("")
	print("me")
	code = buttons
	print("".join(code))
	print(len(code))
	print(int(lines[i].replace("A", "")))
	total += len(code) * int(lines[i].replace("A", ""))

total = total
print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")

# v<<A^>>AvA^Av<<A^>>AAv<A<A^>>AA<A>vAA^Av<A^>AA<A>Av<A<A^>>AAA<A>vA^A

# v<<A>>^AvA^A v<<A>>^AAv<A <A>>^AAvA A^<A>A v<A>^AA<A>Av<A<A>>^AAAvA^<A>A
# <v<A>>^AvA^A <vA<AA>>^A AvA<^A>A    AvA^A  <vA>^AA<A>A<v<A>A>^AAAvA<^A>A

s = "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"
s2= "v<<A>>^AvA^Av<<A>>^AAv<A<A>>^AAvAA^<A>Av<A>^AA<A>Av<A<A>>^AAAvA^<A>A"
print(s[12:])
print(s2[12:])
s = decode(s)
s2 = decode(s2)
print(s[4:14])
print(s2[4:14])
s = decode(s)
s2 = decode(s2)
print(s[2:6])
print(s2[2:6])

# print(s)
# s = decode(s)
# print(s)
# s = decode(s)
# print(s)
