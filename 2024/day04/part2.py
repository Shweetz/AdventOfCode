from aoc_tools import *
from collections import Counter, defaultdict

with open("2024/day04/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

g = Grid()
g.read(lines)

l = []
# find all diagonal "MAS" 
for x,y,a,b in g.find("MAS", 1):
	# append the position of the "A"
	l.append((x+a, y+b))

# the number of X-MAS is the number of doubles of "A" positions
option = 1

if option == 1:
	# Option 1: count doubles by diffing len of "l" and "uniques in l" (hack that only works if no elem appears 3x or more)
	total = len(l) - len(set(l))

if option == 2:
	# Option 2: make a Counter and check true duplicates
	l = Counter(l)
	total = sum(1 for k,v in l.items() if v > 1)

print(f"{total=}")
assert total == 1835
