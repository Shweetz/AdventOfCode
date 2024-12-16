from collections import defaultdict
from queue import PriorityQueue
import sys
from time import time

from aoc_tools import *

sys.setrecursionlimit(1000000)

L, LU, U, RU, R, RD, D, LD = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
dirs = [L, U, R, D] # directions
di = 2 # direction index: face east => R

def move(pos, di):
	"""Move from a position to a direction, "di" is the index in the "dirs" list"""
	d = dirs[di]
	return (pos[0] + d[0], pos[1] + d[1])

t1 = time()
with open("2024/day16/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

g = Grid()
g.read(lines)
g.print()
x,y = g.find("S")[0]

best = sys.maxsize
visited = defaultdict(lambda:best) # value holds min score from start to dict key (default value=inf to override asap)

# queue with tuples (score, pos, direction) where lowest score is evaluated first
q = PriorityQueue()
q.put((0, (x,y), di))

while not q.empty():
	score, pos, di = q.get()

	if g.g[pos] == "#":
		continue

	if score >= best:
		# worse than a path to the end
		continue
	
	if score >= visited[(pos, di)]:
		# worse than another path to this tile/direction
		continue
	else:
		# new best score from start to here
		visited[(pos, di)] = score

	if g.g[pos] == "E":
		# reached finish
		if score < best:
			best = score

	else:
		# take a new step to neighbors: same direction, right, left
		for new_di in [di, di+1, di-1]:
			new_di = new_di % 4
			
			new_score = score + 1
			if new_di != di:
				# change direction = 1000 pts
				new_score += 1000

			new_pos = move(pos, new_di)
			q.put((new_score, new_pos, new_di))

total = best
print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")
assert total == 88416
