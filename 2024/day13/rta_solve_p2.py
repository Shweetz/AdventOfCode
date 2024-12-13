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

with open("2024/day13/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total = 0
cur = 0

for l1, l2, l3, l4 in zip(lines[::4], lines[1::4], lines[2::4], lines[3::4]): # read lines 3 by 3
# for i, line in enumerate(lines):
	# ppprint(f"{line=}")
	# for j, c in enumerate(line):
		
	l1 = get_ints(l1)
	l2 = get_ints(l2)
	l3 = get_ints(l3)
	l3[0] += 10000000000000
	l3[1] += 10000000000000
	# pprint(f"{l1=}")
	best = -1
	cur = 0

	# for i in range(0, math.floor(math.sqrt(l3[0])), 1):
	# 	for j in range(0, math.floor(math.sqrt(l3[1])), 1):
	# 		if (l1[0] * i) + (l2[0] * j) == l3[0] and (l1[1] * i) + (l2[1] * j) == l3[1]:
	# 			s = 3 * i + j
	# 			if s < best or best == -1:
	# 				best = s


	# max_b = min(l3[0] // l2[0], l3[1] // l2[1])

	# i = 0
	# j = max_b
	# while True:
	# 	a = (l1[0] * i) + (l2[0] * j)
	# 	b = (l1[1] * i) + (l2[1] * j)

	# 	if a > l3[0] or b > l3[1]:
	# 		j -= 1
	# 	elif a < l3[0] or b < l3[1]:
	# 		i += 1
	# 	else:
	# 		total += 3 * i + j
	# 		break

	# 	pprint(f"{i,j=}")


	# 4 2
	# 1 2
	# 24 24
	# A:4 B:8

	# 6 2
	# 1 2
	# 10 10
	# A:1 B:4

	# 50 10
	# 2  10
	# 60 60
	# A:1 B:5

	# 50 10
	# 12 20
	# 110 110
	# A:1 B:5

	# 4 1
	# 1 3
	# 11 11
	# A:2 B:3


	# bigger_x = 0 if l1[0] > l1[1] else 1

	# x1 = l1[0] - l1[1]
	# x2 = l2[0] - l2[1]

	# r = - x1 / x2
	# assert r > 0

	# if bigger_x == 1:
	# 	x1,x2 = x2,x1

	# n1 = l1[0] * abs(x2)
	# n2 = l2[0] * abs(x1)
	# n = n1 + n2
	# n = l3[0] // max(l1[0], l2[0])

	# s1 = sorted(l1)
	# s2 = sorted(l2)
	# a = int(l3[0] / (l1[0] / r + l2[0] * r))
	# b = int(l3[1] / (l1[1] * r + l2[1] / r))

	# seen = set()
	# x = (l1[0] * a) + (l2[0] * b)
	# y = (l1[1] * a) + (l2[1] * b)
	# print(f"{n1,n2,r,a,b,x,l3[0],y,l3[1]=}")
	# while True:
	# 	x = (l1[0] * a) + (l2[0] * b)
	# 	y = (l1[1] * a) + (l2[1] * b)

	# 	if x == l3[0] and y == l3[1]:
	# 		total += 3 * a + b
	# 		break

	# 	if bigger_x == 0:
	# 		# if abs(x - l3[0]) > abs(y - l3[1]):
	# 			pprint(f"{abs(x - l3[0])=}")
	# 			pprint(f"{abs(y - l3[1])=}")
	# 			m = abs(x - l3[0]) / a + 1
	# 			if x > l3[0]:
	# 				a -= m
	# 			if x < l3[0]:
	# 				a += m
					
	# 			x = (l1[0] * a) + (l2[0] * b)
	# 			y = (l1[1] * a) + (l2[1] * b)
	# 		# else:
	# 			m = abs(y - l3[1]) / b + 1
	# 			if y > l3[1]:
	# 				b -= 1
	# 			if y < l3[1]:
	# 				b += 1
	# 	else:
	# 			m = abs(x - l3[0]) / b + 1
	# 			if x > l3[0]:
	# 				b -= 1
	# 			if x < l3[0]:
	# 				b += 1
					
	# 			x = (l1[0] * a) + (l2[0] * b)
	# 			y = (l1[1] * a) + (l2[1] * b)
	# 		# else:
	# 			m = abs(y - l3[1]) / a + 1
	# 			if y > l3[1]:
	# 				a -= 1
	# 			if y < l3[1]:
	# 				a += 1
		
	# 	if ((a,b)) in seen:
	# 		break
	# 	seen.add((a,b))
		
	# 	pprint(f"{x    =}")
	# 	pprint(f"{l3[0]=}")
	# 	pprint(f"{total=}")
	# 	pprint(f"{a,b=}")
	# 	pprint(f"{x,y=}")
		# sleep(0.1)

	# if best != -1:
	# 	total += best


	# sympy.symbols('ax ay bx by x y')
	a, b = sympy.symbols('a b', integer=True)
	ax, bx, x = l1[0], l2[0], l3[0]
	ay, by, y = l1[1], l2[1], l3[1]
	eq1 = sympy.Eq(ax * a + bx * b, x)
	eq2 = sympy.Eq(ay * a + by * b, y)
	sol = sympy.solve((eq1, eq2),(a, b))
	print(f"{sol=}")
	if sol:
		total += sol[a] * 3 + sol[b]


total = total
print(f"{total = }")
