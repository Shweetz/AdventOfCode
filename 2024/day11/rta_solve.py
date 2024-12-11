from collections import Counter, defaultdict
from dataclasses import dataclass, field
import functools
import re
from time import sleep, time

from aoc_tools import *

# @dataclass
# class Stone:
# 	v: int # value
# 	c: list = field(default_factory=list)
# 	p: int # parent

@functools.cache
def try_recursive(s):
	a = []
	if s == 0:
		a = [1]
	elif len(str(s)) % 2 == 0:
		ss = str(s)
		j = len(ss) // 2
		# a,b = s,s
		m = 1
		for _ in range(j):
			m *= 10
		# x = 10
		a = [s // m, s % m]
	else:
		a = [s*2024]
	return a

t1 = time()
with open("2024/day11/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]


d = {}
d2 = {}
d3 = defaultdict(int)
l = defaultdict(int)
for i in get_ints(lines[0]):
	l[i] += 1
blinks = 75

# l = {0:1}
# blinks = 10
depth = 0

# for s in l:
# 	s2 = Stone(s, [], -1)

for i in range(blinks):
	# l = Counter(l)
	# print(f"{l=}")
	l2 = defaultdict(int)
	for s, n in l.items():
		# s2 = Stone(s, [], -1)

		if s in d:
			for e in d[s]:
				l2[e] += n
		else:
			a = try_recursive(s)
			
			for e in a:
				l2[e] += n
			d[s] = a
			# d2[(s,1)] = a

	l = l2
	# print(f"{i=} {len(l2)=} {sum(v for _,v in l2.items())=}")
	# print(f"{l2=}")
total = 0
for k,v in l2.items():
	total += v
print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")
