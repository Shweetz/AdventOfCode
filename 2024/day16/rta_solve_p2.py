
from collections import Counter, defaultdict
from dataclasses import dataclass, field
import functools
import math
import re
from queue import PriorityQueue
import sympy
import sys
from time import sleep, time

from aoc_tools import *

sys.setrecursionlimit(1000000)

def pprint(s):
	print(s)
	pass

# @dataclass
# class O:
# 	p: int # position
# 	v: int # value
# 	l: int # length
# 	c: list = field(default_factory=list) # path

def dfs(pos, di, score):
	global best
	# print(x, y, steps)
	# pprint(f"{pos=} {di=} {score=}")
	# if ((pos, di)) in visited:
	# 	return
	
	if g.g[pos] == "#":
		return
	
	# pprint(f"{pos=} {di=} {score=}")
	if score > best:
		# pprint(f"{score,best=}")
		return
	# pprint(f"{pos=} {di=} {score=}")

	if g.g[pos] == "E":
		# reached finish
		if (score < best):
			print(score)
			best = score

	else:
		visited.add(pos)
		
		new_di = di
		d = dirs[new_di]
		new_pos = (pos[0] + d[0], pos[1] + d[1])
		if new_pos not in visited:
			dfs(new_pos, new_di, score + 1)

		new_di = (di+1) % 4
		d = dirs[new_di]
		new_pos = (pos[0] + d[0], pos[1] + d[1])
		if new_pos not in visited:
			dfs(new_pos, new_di, score + 1001)

		new_di = (di-1) % 4
		d = dirs[new_di]
		new_pos = (pos[0] + d[0], pos[1] + d[1])
		if new_pos not in visited:
			dfs(new_pos, new_di, score + 1001)
		

		# for (ax, ay, asteps) in adj[pos]:
			# if (ax, ay) not in visited:
				# dfs((ax, ay), steps+asteps)

		visited.remove(pos)

with open("2024/day16/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

L, LU, U, RU, R, RD, D, LD = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
dirs = {"<":L, "^":U, ">":R, "v":D}
dirs = [L, U, R, D]
di = 2 # face east

g = Grid()
g.read(lines)
g.print()
x,y = g.find("S")[0]
pprint(f"{x,y=}")
visited = set()

total, best, cur = 0, 8000000, 0
q = PriorityQueue()
beams_done = {}
best_tiles = set()
best = 88416
# best = 7036

# dfs((x,y), di, 0)
q.put((0, (x,y), di, []))
pscore = 1

while not q.empty():
	score, pos, di, path = q.get()
	
	if score >= pscore + 1000:
		pscore = score
		pprint(f"{pscore, pos, di=}")

	if score > best:
		continue
	# if score == best:
	# 	pprint(f"{path=}")
	# 	for p in path:
	# 		best_tiles.add(p)
	# 	continue

	if g.g[pos] == "#":
		continue
	
	key = (pos, di)
	if key in beams_done:
		if score > beams_done[key]:
			# worse than another path to this tile/drection
			continue
	beams_done[key] = score

	# pprint(f"{score=} {pos=} {di=}")
	if g.g[pos] == "E":
		# reached finish
		path.append(pos)
		if score == best:
			for p in path:
				best_tiles.add(p)
	else:
		visited.add(pos)
		# path.append(pos)

		new_di = di
		d = dirs[new_di]
		new_pos = (pos[0] + d[0], pos[1] + d[1])
		if new_pos not in visited:
			q.put((score + 1, new_pos, new_di, path + [pos]))

		new_di = (di+1) % 4
		d = dirs[new_di]
		new_pos = (pos[0] + d[0], pos[1] + d[1])
		if new_pos not in visited:
			q.put((score + 1001, new_pos, new_di, path + [pos]))

		new_di = (di-1) % 4
		d = dirs[new_di]
		new_pos = (pos[0] + d[0], pos[1] + d[1])
		if new_pos not in visited:
			q.put((score + 1001, new_pos, new_di, path + [pos]))

		visited.remove(pos)
	
lo = [] # list of objects O

# lines = zip(*lines) # transpose

# for i in range(0, len(lines), 1):
# 	for j in range(0, len(lines[i]), 1):
# 		c = g.g[(i,j)]

# for l1, l2, l3 in zip(lines[::3], lines[1::3], lines[2::3]): # read lines 3 by 3
# for i, line in enumerate(lines):
# 	# pprint(f"{line=}")
# 	# for j, c in enumerate(line):
		
# 	# l = get_ints(line)
# 	# pprint(f"{l=}")

# 	pass

# 	total += 1

total = len(best_tiles)
print(f"{total = }")
