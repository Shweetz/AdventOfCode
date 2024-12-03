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
is_doing = True
ll = []
# l1, l2 = zip(*[line.split() for line in lines])

# for l1, l2, l3 in zip(lines[::3], lines[1::3], lines[2::3]):
for i, line in enumerate(lines):
	while line:
		print(f"{line=}")
		# l = [int(s) for s in spl(line, ",-")]
		# l = [int(s) for s in line.split()]
		# ll.append(l)
		i = line.find("mul(")

		if is_doing:
			don = line.find("don't()")
			print(f"{don=}")
			if don > 0 and don < i:
				is_doing = False
				line = line[don+7:]
				continue
		else:
			do = line.find("do()")
			if do > 0:
				is_doing = True
				line = line[do+4:]
				continue
			else:
				line = []
				continue

		i += 4
		print(f"{i=}")
		if i < len(line) and line[i].isdigit():
			n = int(line[i])
			j = i+1
			if line[i+1].isdigit():
				n = int(line[i:i+2])
				print(f"{n=}")
				j = i+2
				if line[i+2].isdigit():
					n = int(line[i:i+3])
					j = i+3
		else:
			line = line[i:]
			continue

		print(f"{j=}")
		if j < len(line) and line[j] == ",":
			i = j+1
		else:
			line = line[j:]
			continue

		print(f"{i=}")
		i = j+1
		if i < len(line) and line[i].isdigit():
			n2 = int(line[i])
			j = i+1
			if line[i+1].isdigit():
				n2 = int(line[i:i+2])
				j = i+2
				if line[i+2].isdigit():
					n2 = int(line[i:i+3])
					j = i+3
		else:
			line = line[i:]
			continue

		print(f"{j=}")
		if j < len(line) and line[j] == ")":
			total += n * n2
			print(f"{total=}")		

		line = line[j:]

# print(f"{ll = }")

ll2 = zip(*ll)
# print(f"{list(ll2) = }")
#38748987
#69247082
print(f"{total = }")
