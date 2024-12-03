from collections import Counter, defaultdict
from dataclasses import dataclass
import re

from aoc_tools import *

@dataclass
class Object: pass

with open("2024/day03/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total = 0
best = 0
cur = 0

ll = []
# l1, l2 = zip(*[line.split() for line in lines])

# for l1, l2, l3 in zip(lines[::3], lines[1::3], lines[2::3]):
for i, line in enumerate(lines):
	print(f"{line=}")
	# l = [int(s) for s in line.split()]

	ints = re.findall(r"\d+", line)
	# print(f"{ints=}")
	
	total += 1

ll2 = zip(*ll)
# print(f"{list(ll2) = }")

print(f"{total = }")
