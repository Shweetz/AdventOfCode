from time import time

from dataclasses import dataclass
import re

@dataclass
class Stone:
	x : int
	y : int
	z : int
	vx : int
	vy : int
	vz : int


def mat_calc(mat):
	""" calculate matrix determinant """
	if len(mat) == 1:
		return mat[0][0]
	sum = 0
	for j in range(len(mat)):
		sign = 1 if j % 2 == 0 else -1
		sum += sign * mat[0][j] * mat_calc(mat_reduce(mat, j))
	return sum

def mat_reduce(mat, j):
	""" remove row 0 and col j """
	new_mat = []
	for mat_line in mat[1:]:
		new_mat.append(mat_line[:j] + mat_line[j+1:])
	return new_mat

# script start
with open("input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

t1 = time()
stones = []

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

	# apply int() to all elements (cool trick: use map() to apply a function to all elements of a list)
	x, y, z, vx, vy, vz = [int(e) for e in num_list]
	x, y, z, vx, vy, vz = map(int, num_list)

	# stones.append(Stone(x, y, z, vx, vy, vz))
	stones.append(Stone(*map(int, num_list)))

# the rock (r) colling with a stone (s) at t0 means:
# pxr + t0*vxr = pxs + t0*vxs
# pyr + t0*vyr = pys + t0*vys
# pzr + t0*vzr = pzs + t0*vzs
#
# we can remove t0 with some manipulation and combining x and y (z is ignored)
# t0 = (pxs - pxr) / (vxr - vxs)
# t0 = (pys - pyr) / (vyr - vys)
# t0 = (pzs - pzr) / (vzr - vzs)
#
# (pxs - pxr) / (vxr - vxs) = (pys - pyr) / (vyr - vys)
#
# (pxs - pxr) * (vyr - vys) = (pys - pyr) * (vxr - vxs)
#
# pxs*vyr - pxs*vys - pxr*vyr + pxr*vys = pys*vxr - pys*vxs - pyr*vxr + pyr*vxs
#
# This is true for every hailstone n so we can use 2 hailstones and name them 0 and 1
# px0*vyr - px0*vy0 - pxr*vyr + pxr*vy0 = py0*vxr - py0*vx0 - pyr*vxr + pyr*vx0
# px1*vyr - px1*vy1 - pxr*vyr + pxr*vy1 = py1*vxr - py1*vx1 - pyr*vxr + pyr*vx1
#
# Substract both
# px0*vyr - px0*vy0 + pxr*vy0 - px1*vyr + px1*vy1 - pxr*vy1 = py0*vxr - py0*vx0 + pyr*vx0 - py1*vxr + py1*vx1 - pyr*vx1
#
# pxr(vy0 - vy1) + pyr(vx1 - vx0) + vxr(py1 - py0) + vyr(px0 - px1) = px0*vy0 - py0*vx0 - px1*vy1 + py1*vx1
#
# Use stones to have 4 equations and use Cramer's rule (here, stone 0 everywhere, and stone 1 to 4 for 4 equations)

A = [[], [], [], [], []] # A, A1, A2, A3, A4, each a 4x4 matrix
s = stones[0]
for i in range(4):
	t = stones[i+1]

	mat_line = [s.vy - t.vy, t.vx - s.vx, t.y - s.y, s.x - t.x]
	A[0].append(mat_line)

	Bi = s.x * s.vy - s.y * s.vx - t.x * t.vy + t.y * t.vx
	for n in range(4):
		A[n+1].append(list(mat_line)) # same line than A
		A[n+1][i][n] = Bi # change one value with Bi

A0 = mat_calc(A[0])
A1 = mat_calc(A[1])
A2 = mat_calc(A[2])
A3 = mat_calc(A[3])
A4 = mat_calc(A[4])

pxr = A1 / A0
pyr = A2 / A0
vxr = A3 / A0
vyr = A4 / A0

# Repeat with x and z to find pzr and vzr (replace all y with z)

# pxr(vz0 - vz1) + pzr(vx1 - vx0) + vxr(pz1 - pz0) + vzr(px0 - px1) = px0*vz0 - pz0*vx0 - px1*vz1 + pz1*vx1

A = [[], [], [], [], []] # A, A1, A2, A3, A4, each a 4x4 matrix
s = stones[0]
for i in range(4):
	t = stones[i+1]

	mat_line = [s.vz - t.vz, t.vx - s.vx, t.z - s.z, s.x - t.x]
	A[0].append(mat_line)

	Bi = s.x * s.vz - s.z * s.vx - t.x * t.vz + t.z * t.vx
	for n in range(4):
		A[n+1].append(list(mat_line)) # same line than A
		A[n+1][i][n] = Bi # change one value with Bi

A0 = mat_calc(A[0])
A2 = mat_calc(A[2])
A4 = mat_calc(A[4])

pzr = A2 / A0
vzr = A4 / A0

print(int(pxr + pyr + pzr))
print(f"Execution time: {(time() - t1):.3f}s")
