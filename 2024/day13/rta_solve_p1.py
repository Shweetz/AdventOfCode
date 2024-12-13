from collections import Counter, defaultdict
from dataclasses import dataclass, field
import functools
import re
from time import sleep, time

from aoc_tools import *

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
	# print(f"{line=}")
	# for j, c in enumerate(line):
		
	l1 = get_ints(l1)
	l2 = get_ints(l2)
	l3 = get_ints(l3)
	print(f"{l1=}")
	best = -1
	cur = 0

	for i in range(0, 101, 1):
		for j in range(0, 101, 1):
			if (l1[0] * i) + (l2[0] * j) == l3[0] and (l1[1] * i) + (l2[1] * j) == l3[1]:
				s = 3 * i + j
				if s < best or best == -1:
					best = s

	if best != -1:
		total += best


total = total
print(f"{total = }")
