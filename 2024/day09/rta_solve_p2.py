from collections import Counter, defaultdict
from dataclasses import dataclass
import re
import time
from aoc_tools import *

@dataclass
class Object: pass

with open("2024/day09/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

# dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
# dir = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, 1], [1, 1], [1, -1], [-1, -1]]
# di = 0
# (a,b) = dir[di]

# g = Grid()
# g.read(lines)
# x,y,_,_ = g.find("^")[0]
# vis = set()
# print(f"{g.g=}")
# print(f"{g.g[(0,0)]=}")
# print(f"{g.adj(0,0,0)=}")
# print(f"{len(g.find("^", 0))=}")

total = 0
best = 0
cur = 0

id = 0
file = True
rep = []
repn = []

for i in range(0, len(lines[0]), 1):
	if file:
		c = id
		id += 1
	else:
		c = "." 
	
	file = not file

	# for j in range(int(lines[0][i])):
	# 	rep += str(c)
	rep.append(c)
	repn.append(int(lines[0][i]))

print(f"{rep=}")
print(f"{repn=}")

# i = 0
# z = len(rep) - 1

# while i <= z:
# 	if rep[i] != ".":
# 		i += 1
# 		continue

# 	if rep[z] == ".":
# 		z -= 1
# 		continue
	
# 	rep = rep[:i] + rep[z] + rep[i+1:z]
# 	i += 1
# 	z -= 1

# 	print(f"{rep=}")
# 	time.sleep(1000)

# print(f"{rep=}")

z = len(rep) - 1
# p = 0
# c = 0
# rep2 = []
# repn2 = []

for z in range(len(rep) - 1, 1, -1):
	co = False
	# if rep[c] != ".":
	# 	rep2.append(rep[c])
	# 	repn2.append(repn[c])

	if rep[z] == ".":
		continue

	c = 0
	while rep[c] != "." or repn[c] < repn[z]:
		c += 1
		if c >= z:
			co = True
			break
	# print(f"{z=}")
	if co:
		continue
	
	repn[c] -= repn[z]
	rep.insert(c, rep[z])
	repn.insert(c, repn[z])
	z += 1
	rep[z] = "."

	# print(f"{rep=}")
	# print(f"{repn=}")

p = 0
c = 0
z = len(rep) - 1

for i, v in enumerate(rep):
	l = repn[i]
	for j in range(l):
		if v != ".":
			total += p * int(v)
		p += 1
		# print(f"{total=} {v=} {p=}")

# for l1, l2, l3 in zip(lines[::3], lines[1::3], lines[2::3]):
# for i, line in enumerate(lines):
	# print(f"{line=}")
	# for j, c in enumerate(line):
		
	# l = get_ints(line)
	# print(f"{l=}")

	# pass

	# total += 1

total = total
print(f"{total = }")
