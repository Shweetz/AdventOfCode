from collections import Counter, defaultdict
from dataclasses import dataclass, field
import functools
import re
from time import sleep, time

from aoc_tools import *

# @dataclass
# class O:
# 	p: int # position
# 	v: int # value
# 	l: int # length
# 	c: list = field(default_factory=list) # path

def search_region_plots(i,j,c):
	# print(f"s:{(i,j,c)=}")
	area = 0
	perim = 0
	perim2 = {}
	perim2 = defaultdict(int)
	q = [(i,j)]

	while q:
		i,j = q.pop()
		if ((i,j)) in vis:
			continue

		# print(f"{i,j=}")
		vis.add((i,j))
		area += 1
		# perim += 4 - len([1 for _,_,v in g.adj(i,j) if v ==c])
		perim2[("L",i,j)] = 1
		perim2[("U",i,j)] = 1
		perim2[("R",i,j)] = 1
		perim2[("D",i,j)] = 1
		# print(f"{perim=}")
		# print(f"{[(i,j) for i,j,v in g.adj(i,j) if v ==c]=}")
		for x,y,v in g.adj(i,j): # look in adj
			if v == c:
				q.append((x,y))

		# print(f"{perim2=}")

	perim3 = set()
	l = len(perim2)
	p2 = dict(perim2)
	for i in range(0, len(lines), 1):
		for j in range(0, len(lines[i]), 1):
			for d in ["L", "R", "U", "D"]:
				# if c != g.g[(i,j)] or not perim2[(d,i,j)]:
				if not perim2[(d,i,j)]:
					continue
	# for k,v in perim2.items():
		# (d,i,j) = k
				if d == "L":
					x,y=i-1,j
					e,a,b="R",i,j-1
				if d == "R":
					x,y=i-1,j
					e,a,b="L",i,j+1
				if d == "U":
					x,y=i,j-1
					e,a,b="D",i-1,j
				if d == "D":
					x,y=i,j-1
					e,a,b="U",i+1,j

				if ((d,x,y)) in perim2 and perim2[(d,x,y)] != 0 and g.g[(x,y)] == c:
					# print(f"{(d,i,j)=} {(d,x,y)=}")
					perim2[(d,i,j)] = -1
					# continue
				if ((e,a,b)) in perim2 and g.g[(a,b)] == c:
					# print(f"{(d,i,j)=} {(e,a,b)=}")
					perim2[(d,i,j)] = 0
					perim2[(e,a,b)] = 0
					# continue
				
				if perim2[(d,i,j)] == 1:
					perim3.add((d,i,j))
				# print(f"{perim3=}")
	perim = len(perim3)
	# perim = len([v for k,v in perim2.items() if v])
	# print(f"{c=} {area=} {perim=}")
	# print(f"")
	return area, perim

with open("2024/day12/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

dir = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, 1], [1, 1], [1, -1], [-1, -1]]
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
di = 0

g = Grid()
g.read(lines)
# x,y,_,_ = g.find("^")[0]
vis = set()
# print(f"{g.g=}")
# print(f"{g.adj(0,0,0)=}")
# print(f"{len(g.find("^", 0))=}")

total = 0

for i in range(0, len(lines), 1):
	for j in range(0, len(lines[i]), 1):
		if (i,j) not in vis:
			c = g.g[(i,j)]

			# search other plots in same region
			a, p = search_region_plots(i,j,c)

			total += a*p

total = total
print(f"{total = }")
