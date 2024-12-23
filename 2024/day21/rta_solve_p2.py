
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from functools import cache
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
	# print(s)
	pass

def dist(grid, start, end):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == start:
				a,b = i,j
			if grid[i][j] == end:
				c,d = i,j
	
	return abs(c-a) + abs(d-b)

@cache
def paths(start, end):
	print(start, end)
	# sleep(0.01)
	pad = dirpadd if (start in "<^v>" or end in "<^v>") else numpadd
	pad_r = dirpadd_r if (start in "<^v>" or end in "<^v>") else numpadd_r
	buttons = ""
	nb = defaultdict(int)
	a,b = pad[start]
	c,d = pad[end]
	# for i in range(len(pad)):
	# 	for j in range(len(pad[0])):
	# 		if pad[i][j] == start:
	# 			a,b = i,j
	# 		if pad[i][j] == end:
	# 			c,d = i,j
	
	nb[L] = max(b - d, 0)
	nb[U] = max(a - c, 0)
	nb[R] = max(d - b, 0)
	nb[D] = max(c - a, 0)
	# print(start, end, c)
	if pad_r[(c,b)] == "x": # moving i first would mean getting out of pad
		for d in [R, L, U, D]:
			buttons += d * nb[d]
	elif pad_r[(a,d)] == "x": # moving j first would mean getting out of pad
		for d in [U, D, R, L]:
			buttons += d * nb[d]
	else:
		for d in [L, U, D, R]: # preference when not getting out of pad
			buttons += d * nb[d]

	return buttons

a = 0
@cache
def find_buttons_from_code(code, depth):
	if depth == 0:
		return len(code)
	
	print(f"{code=}")
	global a
	moves = []
	path = []
	buttons = ""
	c1 = "A"
	s = 0
	for c2 in code:
		a += 1
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

		buttons = paths(c1, c2) + "A"
		s += find_buttons_from_code(buttons, depth - 1)
		# print(total)
		# pprint(buttons)

		# if nb[U] and not nb[R]: # U or UL
		# 	# 1st move is left on keypad
		# 	pass
		# else:
		# 	# 1st move is down on keypad
		# 	pass

		c1 = c2
	
	return s

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
# pprint(numpad)
# for i in range(numpad):
# 	for j in range(numpad[0]):
# 		c = g.g[(i,j)]
dirpad = "x,^,A <,v,>"
# for i, n in enumerate(numpad):
dirpad = [a.split(",") for a in dirpad.split()]
# pprint(dirpad)

# pprint(dist(numpad, "7", "2"))

numpadd = {
	"7": (0,0), "8": (0,1), "9": (0,2),
	"4": (1,0), "5": (1,1), "6": (1,2),
	"1": (2,0), "2": (2,1), "3": (2,2),
	"x": (3,0), "0": (3,1), "A": (3,2)
}
numpadd_r = { v:k for k,v in numpadd.items() }
dirpadd = {
	"x": (0,0), "^": (0,1), "A": (0,2),
	"<": (1,0), "v": (1,1), ">": (1,2)
}
dirpadd_r = { v:k for k,v in dirpadd.items() }

total = 0

for i, code in enumerate(lines):
	# pprint(code)

	# moves = []
	# path = []
	# buttons = []

	# 1st robot
	buttons = find_buttons_from_code(code, 26)
	
	# nth robot
	# for _ in range(15):
	# 	nbuttons = ""
	# 	sbuttons = buttons.replace("A","A,").split(",")
	# 	for sbutton in sbuttons:
	# 		nbuttons += find_buttons_from_code(sbutton)

	# 	print(nbuttons)
	# 	buttons = nbuttons
	# pprint("")
	# pprint("me")
	code = buttons
	# pprint("".join(code))
	# pprint(len(code))
	# pprint(int(lines[i].replace("A", "")))
	total += code * int(lines[i].replace("A", ""))

total = total
print(f"nb iterations in the 'for loop' of 'find_buttons_from_code': {a}")
print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")
# v<<A^>>AvA^Av<<A^>>AAv<A<A^>>AA<A>vAA^Av<A^>AA<A>Av<A<A^>>AAA<A>vA^A

# v<<A>>^AvA^A v<<A>>^AAv<A <A>>^AAvA A^<A>A v<A>^AA<A>Av<A<A>>^AAAvA^<A>A
# <v<A>>^AvA^A <vA<AA>>^A AvA<^A>A    AvA^A  <vA>^AA<A>A<v<A>A>^AAAvA<^A>A

# s = "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"
# s2= "v<<A>>^AvA^Av<<A>>^AAv<A<A>>^AAvAA^<A>Av<A>^AA<A>Av<A<A>>^AAAvA^<A>A"
# print(s[12:])
# print(s2[12:])
# s = decode(s)
# s2 = decode(s2)
# print(s[4:14])
# print(s2[4:14])
# s = decode(s)
# s2 = decode(s2)
# print(s[2:6])
# print(s2[2:6])

# print(s)
# s = decode(s)
# print(s)
# s = decode(s)
# print(s)
