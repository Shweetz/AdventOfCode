from collections import defaultdict
from time import time

from aoc_tools import *

t1 = time()
with open("2024/day11/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

# use a dict where (key,value) is (stone_number,stone_count)
l = defaultdict(int)
for i in get_ints(lines[0]):
	l[i] += 1

blinks = 75

d = {} # dict to remember what a stone becomes on next blink

for i in range(blinks):
	l2 = defaultdict(int) # next step dict

	for s, n in l.items():
		if s in d:
			# stone already been transformed and remembered, do the same again
			for e in d[s]:
				l2[e] += n
		
		else:
			# new stone, transform and store (value,result) in d
			a = []
			if s == 0:
				a = [1]
			elif len(str(s)) % 2 == 0:
				# split in 2
				j = len(str(s)) // 2
				m = 1
				for _ in range(j):
					m *= 10
				a = [s // m, s % m]
			else:
				a = [s*2024]
			
			for e in a:
				l2[e] += n

			d[s] = a

	l = l2

total = 0
for k,v in l2.items():
	total += v

print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")
assert total == 216318908621637
