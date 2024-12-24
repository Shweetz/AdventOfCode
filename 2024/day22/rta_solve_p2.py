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

def pprint(s):
	print(s)
	pass

cache = defaultdict(lambda:0)

def evolve(number):
	# actually useless, very few cache hits lol
	# if number in cache:
	# 	return cache[number]
	
	evolved = number
	
	# evolved *= 64
	evolved ^= evolved * 64
	evolved %= 16777216
	
	# number = evolved

	# evolved //= 32
	evolved ^= evolved // 32
	evolved %= 16777216
	
	# number = evolved
	
	# evolved *= 2048
	evolved ^= evolved * 2048
	evolved %= 16777216

	# cache[number] = evolved
	return evolved

t1 = time()
with open("2024/day22/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total1 = 0
total = 0
# for i in range(0, len(lines), 1):
# 	for j in range(0, len(lines[i]), 1):
# 		c = g.g[(i,j)]

# print(evolve(123)) # 15887950

for i, line in enumerate(lines):
	done = defaultdict(bool)
	number = int(line)
	last = int(line)
	d0 = -10
	d1 = 0
	d2 = 0
	d3 = 0
	for i in range(2000):
		number = evolve(number)
		# number %= 10
		# l.append(number)
		d0 = d1
		d1 = d2
		d2 = d3
		d3 = number % 10 - last % 10
		if i > 0:
			if i-3 >= 0 and not done[(d0,d1,d2,d3)]:
				cache[(d0,d1,d2,d3)] += number % 10
				done[(d0,d1,d2,d3)] = True

		# if i < 10:
		# 	print(f"{d0,d1,d2,d3=}")

		last = number % 10

	total1 += number

	print(cache[(2,1,1,3)])

print(f"{total1=}")
total = max(cache.values())
print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")