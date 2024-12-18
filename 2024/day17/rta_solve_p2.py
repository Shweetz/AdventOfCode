
from collections import Counter, defaultdict
from dataclasses import dataclass, field
import functools
import math
import re
from queue import PriorityQueue
import sympy
import sys
from time import sleep, time

from aoc_tools import *

sys.setrecursionlimit(1000000)

L, LU, U, RU, R, RD, D, LD = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
dirs = {"<":L, "^":U, ">":R, "v":D}
dirs = [L, U, R, D] # directions
di = 0 # direction index

def move(pos, di):
	"""Move from a position to a direction, "di" is the index in the "dirs" list"""
	d = dirs[di]
	return (pos[0] + d[0], pos[1] + d[1])

def pprint(s):
	# print(s)
	pass

# @dataclass
# class O:
# 	p: int # position
# 	v: int # value
# 	l: int # length
# 	c: list = field(default_factory=list) # path

def get_value(operand):
	if operand <= 3:
		return operand
	if operand == 4:
		return a
	if operand == 5:
		return b
	if operand == 6:
		return c
	
with open("2024/day17/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

# g = Grid()
# g.read(lines)
# g.print()
# x,y = g.find("^")[0]
# pprint(f"{x,y=}")
# visited = set()

total, best, cur = 0, sys.maxsize, 0

lo = [] # list of objects O

# lines = zip(*lines) # transpose

# for i in range(0, len(lines), 1):
# 	for j in range(0, len(lines[i]), 1):
# 		c = g.g[(i,j)]

# for l1, l2, l3 in zip(lines[::3], lines[1::3], lines[2::3]): # read lines 3 by 3
# for i, line in enumerate(lines):
# 	# pprint(f"{line=}")
# 	# for j, c in enumerate(line):
		
# 	# pprint(f"{l=}")

# 	pass

# 	total += 1

a = get_ints(lines[0])[0]
bb = get_ints(lines[1])[0]
cc = get_ints(lines[2])[0]
pprogram = get_ints(lines[4])

min = pow(8, len(pprogram) - 1)
max = pow(8, len(pprogram))
print(f"{min,max=}")
# 12748000

j = 35184372088832
j = 35184372099626 # +3 +5
j = 35184982895146
j = 97419059014186
# s,j=('2,4,1,1,7,5,4,6,0,', 35185117112874)
# s,j=('2,4,1,1,7,5,4,6,0,3,', 35185251330602)
while j < 281474976710655:
	if j % 1000 == 0:
		print(f"{j=}")

	total = ""

	a = j
	# a = 281474976710655
	b = bb
	c = cc
	program = pprogram

	i = 0
	while i < len(program):
		opcode, operand = program[i], program[i+1]
		pprint(f"{opcode, operand=}")

		ope = get_value(operand)

		if opcode == 0:	
			a = int(a / pow (2, ope))

			pprint(f"{a=}")
			
		if opcode == 1:
			b = b ^ operand

			pprint(f"{b=}")
			
		if opcode == 2:
			b = ope % 8

			pprint(f"{b=}")
			
		if opcode == 3:
			if a != 0:
				i = operand - 2

			pprint(f"{i=}")
			
		if opcode == 4:
			b = b ^ c

			pprint(f"{b=}")
			
		if opcode == 5:
			total += str(ope % 8) + ","

			pprint(f"{total=}")
			
		if opcode == 6:
			b = int(a / pow (2, ope))

			pprint(f"{b=}")
			
		if opcode == 7:
			c = int(a / pow (2, ope))

			pprint(f"{c=}")

		i += 2

	total = total[:-1]

	sprogram = ",".join([str(i) for i in program])
	# if j == 117440:
	# 	print(f"{total=}")
	# 	print(f"{program=}")
	# 	print(f"{",".join([str(i) for i in program])=}")

	s = ""
	for k in range(len(total)):
		if total[k] == sprogram[k]:
			s += total[k]
		else:
			break
	if len(s) > 22:
		print(f"{s,j=}")
	
	if total == sprogram:
		total = j
		break

	# if total.startswith("2,4"):
	# 	print(f"2{j=}")
	
	j += 2199023255552

print(f"program= {sprogram}")
print(f"{total = }")

# ideas after solve
"""
knacki
24 b = a % 8
11 b = b ^ 1 
75 c = a / 2pb
15 b = b ^ 5
43 b = b ^ c
55 print(b % 8)
03 a = a / 2p3 (8)
30 loop until a == 0

moi
24 b = a % 8
11 b = b ^ 1 
75 c = a / 2pb
46 b = b ^ c
03 a = a / 2p3 (8)
14 b = b ^ 4
55 print(b % 8)
30 loop until a == 0

a % 8 = xyz en binaire (- = inverser le bit x, y ou z)

24 b = a % 8        : b = +x +y +z
11 b = b ^ 1        : b = +x +y -z
75 c = a / 2pb
46 b = b ^ c        : b = dépend de c
03 a = a / 2p3 (8)
14 b = b ^ 4        : b = -x +y +z
55 print(b % 8)
30 loop until a == 0

b % 8 = a % 8 si a/32 = 5

b % 8 = xyz : (0 = inverser le bit x, y ou z)
a/32 % 8 = 0 : a % 8 = 0y0 
a/32 % 8 = 1 : a % 8 = 0yz 
a/32 % 8 = 2 : a % 8 = 000 
a/32 % 8 = 3 : a % 8 = 00z 
a/32 % 8 = 4 : a % 8 = xy0 
a/32 % 8 = 5 : a % 8 = xyz 
a/32 % 8 = 6 : a % 8 = x00 
a/32 % 8 = 7 : a % 8 = x0z

a % 8 = b % 8 ^ 5   ^ (a/32     ) 2p5
a % 8 = b % 8 ^ 101 ^ (a/100_000) en binaire

output, a =
2411754603145530
5611504432025052

valeurs input en partant de la fin
0 => b % 8 = 0, a / 32 % 8 = 0 => a % 8 = 0y0 = 010 = 2 donc A % 8 = 2 
3 => b % 8 = 3, a / 32 % 8 = 2 => a % 8 = 000 = 100 = 5 donc A / 8 % 8 = 5

valeurs input en partant du début
2 => a / 32 % 8 = 0 => a % 8 = b % 8 (2) & 0y0 = 020 = 2 donc A = 2... 
4 => a / 32 % 8 = 2 => a % 8 = b % 8 (4) & 000 = 100 = 5 donc A / 8 % 8 = 5
non pas faisable avec a/32

valeurs input en partant de la fin
a =  5 = 000 101
a / 32 = 0-- --- 
0 => b % 8 = 000, ^ 101 = 101, ^ a / 32 % 8 (000) = 010 donc A % 8 = 2 

a = 56 = 101 110
a / 32 = 1-- ---
3 => b % 8 = 011, ^ 101 = 110, ^ a / 32 % 8 (001) = 111 donc A / 8 % 8 = 7
ça devrait etre 6

putain c'est pas 2**5 (32) mais 2**b !!!
l'assembly ne se reverse pas, il faut bf
"""