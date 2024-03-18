from time import time

from dataclasses import dataclass
import re

@dataclass
class Stone:
	x : int
	y : int
	z : int
	vx : int # named v in equations
	vy : int # named w in equations
	vz : int


with open("input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

# script start
t1 = time()
stones = []
min_x = 200000000000000
max_x = 400000000000000
total = 0

for line in lines:
	# put line's numbers in a list in different ways:
	# 1. string replace
	num_list = line.replace(",", "").replace("@", "").split()
	# print(num_list)

	# 2. re match
	num_list = re.match("(.*), (.*), (.*) @ (.*), (.*), (.*)", line).groups()
	# print(num_list)

	# 3. re findall
	num_list = re.findall(r'[-0-9]+', line)
	# print(num_list)

	x, y, z, vx, vy, vz = [int(e) for e in num_list]
	print(x, y, z, vx, vy, vz)

	stones.append(Stone(x, y, z, vx, vy, vz))

for i, s1 in enumerate(stones):
	for s2 in stones[i+1:]:
		# find a, b time coefficients (in nanosecs) to find the intersection of lines of stones
		# a/b positive means future encounter, negative means past encounter, 0 means present encounter

		# s1.x + a * s1.vx = s2.x + b * s2.vx
		# s1.y + a * s1.vy = s2.y + b * s2.vy
		# <=> (s1.vx != 0 and s1.vy != 0)
		# a = (s2.x + b * s2.vx - s1.x) / s1.vx
		# a = (s2.y + b * s2.vy - s1.y) / s1.vy
		# <=>
		# (s2.x + b * s2.vx - s1.x) / s1.vx = (s2.y + b * s2.vy - s1.y) / s1.vy
		# <=> (renaming)
		# (x2   + bv2       - x1)   / v1    = (y2   + bw2       - y1)   / w1
		# <=>
		# bv2 = (y2v1 + bv1w2 - y1v1) / w1 + x1 - x2
		# <=>
		# bv2 - bv1w2/w1 = v1(y2 - y1)/w1 + x1 - x2
		# <=>
		# b((v2w1 - v1w2)/w1) = (v1(y2 - y1) + x1w1 - x2w1) / w1
		# <=>
		# b(v2w1 - v1w2) = v1(y2 - y1) + x1w1 - x2w1
		# <=> (v2w1 - w2v1 != 0)
		# b = (y2v1 - y1v1 + x1w1 - x2w1) / (v2w1 - v1w2)
		
		denominator = (s2.vx * s1.vy - s2.vy * s1.vx)
		if denominator == 0:
			# lines parallel, but maybe they are on the same trajectory
			print("parallel")

		else:
			# plug values in the equations
			b = (s2.y * s1.vx - s1.y * s1.vx + s1.x * s1.vy - s2.x * s1.vy) / denominator
			a = (s2.x + b * s2.vx - s1.x) / s1.vx
			# print(a, b)

			x = s1.x + a * s1.vx
			y = s1.y + a * s1.vy
			# print(x, y)

			# future_path = a >= 0 and b >= 0
			if a >= 0 and b >= 0 and min_x <= x <= max_x and min_x <= y <= max_x:
				total += 1

		# print()

print(total)
print(f"Execution time: {(time() - t1):.3f}s")
		
# other way: find y = ax + b (where a = slope and b = offset) for both stones
# a = s1.vy / s1.vx
# b = y - ax = s1.y - s1.x * s1.vy / s1.vx
# then when both lines intersect (y is equal): a1x + b1 = a2x + b2
# <=>
# x = (b2 - b1)/(a1 - a2)
# y = a1x + b1 = a1 (b2 - b1)/(a1 - a2) + b1
