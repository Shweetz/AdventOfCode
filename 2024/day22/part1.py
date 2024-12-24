from time import time

from aoc_tools import *

t1 = time()
with open("2024/day18/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

size = 71
bytes = 1024

g = Grid()

pos_list = []
for line in lines[:bytes]:
	y,x = get_ints(line)
	pos_list.append((x,y))

g.build(size, size, pos_list)

g.print()

score, _ = g.bfs((0,0), (70,70))

total = score
print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")
assert total == 184180
