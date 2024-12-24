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

cache = defaultdict(lambda:-1)

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

	cache[number] = evolved
	return evolved

t1 = time()
with open("2024/day22/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total = 0
# for i in range(0, len(lines), 1):
# 	for j in range(0, len(lines[i]), 1):
# 		c = g.g[(i,j)]

# print(evolve(123)) # 15887950

for i, line in enumerate(lines):
	number = int(line)
	for _ in range(2000):
		number = evolve(number)

	total += number

	# print(number)

total = total
print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")