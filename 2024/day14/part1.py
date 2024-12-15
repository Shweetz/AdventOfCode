from collections import defaultdict
from time import time

from aoc_tools import *

t1 = time()
with open("2024/day14/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

width, height = 101,103

q = defaultdict(int)

for i, line in enumerate(lines):
	# parse input of the current line representing a robot
	line = spl(line, "=, ")
	px, py, vx, vy = int(line[1]), int(line[2]), int(line[4]), int(line[5])
	
	# move the robot
	for j in range(100):
		px = (px + vx) % width
		py = (py + vy) % height

	# check in which quadrant the robot is
	if px < (width - 1) / 2 and py < (height - 1) / 2:
		q[0] += 1
	if px > (width - 1) / 2 and py < (height - 1) / 2:
		q[1] += 1
	if px < (width - 1) / 2 and py > (height - 1) / 2:
		q[2] += 1
	if px > (width - 1) / 2 and py > (height - 1) / 2:
		q[3] += 1

total = q[0] * q[1] * q[2] * q[3]
print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")
assert total == 222901875
