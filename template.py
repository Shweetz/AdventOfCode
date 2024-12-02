from collections import Counter, defaultdict
from dataclasses import dataclass

@dataclass
class Object: pass

def spl(s, seps):
	"""Split a string over every char in the seps string"""
	for sep in seps:
		s = s.replace(sep, seps[-1])
	return s.split(seps[-1])

def rem(s, seps):
	"""Remove chars from a string"""
	return "".join([c for c in s if c not in seps])

# input file

with open("2024/day1/input_s.txt", "r") as f:
# with open("2024/day1/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total = 0

# l1, l2 = zip(*[line.split() for line in lines])

for i, line in enumerate(lines):
	print(f"{line=}")
	l = [int(s) for s in line.split()]

	total += 1

print(f"{total = }")
