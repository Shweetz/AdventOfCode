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

L, LU, U, RU, R, RD, D, LD = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
dirs = {"<":L, "^":U, ">":R, "v":D}
dirs = [L, U, R, D] # directions
di = 0 # direction index

def move(pos, di):
	"""Move from a position to a direction, "di" is the index in the "dirs" list"""
	d = dirs[di]
	return (pos[0] + d[0], pos[1] + d[1])

def pprint(s):
	print(s)
	pass


def dfs(c, visited=set()):
	# print(f"{c,visited=}")
	global best

	# cur.add(c)
	visited.add(c)
	
	if len(visited) > len(best):
		best = visited.copy()
		print(",".join(sorted(best)))

		for c2 in graph:
			if len(graph[c2]) == len(best) - 1:
				bad.add(c2)
	
	inter = graph[c]
	for cx in visited:
		inter = inter.intersection(graph[cx])
		inter = set(c2 for c2 in inter if c2 not in bad)

	if len(visited) + len(inter) > len(best):
		for c2 in inter:
			# if c2 not in visited:
				# if visited.issubset(graph[c2]):
			dfs(c2, visited)

	visited.remove(c)

t1 = time()
with open("2024/day23/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

# g = Grid()
# g.read(lines)
# g.print()
# x,y = g.find("^")[0]
# pprint(f"{x,y=}")

# visited = set()

total, best, cur = 0, sys.maxsize, 0

lo = [] # list of objects O

# lines = zip(*lines) # transpose

# for i in range(0, len(lines), 1):
# 	for j in range(0, len(lines[i]), 1):
# 		c = g.g[(i,j)]

graph = defaultdict(set)
sets = set()

for i, line in enumerate(lines):
	# pprint(f"{line=}")
	# for j, c in enumerate(line):
		
	c1, c2 = line.split("-")
	graph[c1].add(c2)
	graph[c2].add(c1)
	# pprint(f"{l=}")

best = set()
visited = set()
bad = set()
seen_cr = False
for c1 in graph:
	print(f"dfs on {c1=}")
	if c1 == "fs":
		seen_cr = True
	if seen_cr:
		dfs(c1)
	bad.add(c1)
	# end_pos = c1
	# for c2 in graph[c1]:
	# 	dfs(c2)
# 	for c2 in graph:
# 		if c2 in graph[c1]:
# 			inter = graph[c1].intersection(graph[c2])
# 			for c3 in inter:
# 				sets.add(tuple(sorted([c1,c2,c3])))
# for s in sets:
# 	print(s)
total = ",".join(sorted(best))
print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")

# ey,ft,fv,pr,qp,rk,sb,ve,vn,wq,xb,ya
# cy,ey,ft,fv,pr,qp,rk,ve,vn,wq,xb,ya
# ca,gf,hf,hh,ih,nb,ne,qr,sd,wu,xh,yl
# ai,bu,cn,ex,fs,lq,nr,qy,rf,rq,xq,yz
# cw,dy,ef,iw,ji,jv,ka,ob,qv,ry,ua,wt,xz