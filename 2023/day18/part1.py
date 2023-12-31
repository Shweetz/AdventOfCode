from time import time

# return area of shape using shoelace formula
def shoelace(coords):
	area = 0
	for i in range(len(coords)):
		if i+1 < len(coords):
			area += coords[i][0] * coords[i+1][1] - coords[i][1] * coords[i+1][0]

	return abs(int(area/2))

# return nb of interior points using pick's theorem
def pick(area, b):
	return int(area - b/2 + 1)

# script start
t1 = time()
with open("input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

b_p = 0 # number of points on the boundary (perimeter) of the shape
i = 0
j = 0
coords = [(i, j)] # coordinates of vertices of the shape

for line in lines:
	dir, leng, color = line.split()
	leng = int(leng)

	b_p += leng

	if dir == "U": i -= leng
	if dir == "D": i += leng
	if dir == "L": j -= leng
	if dir == "R": j += leng

	coords.append((i, j))

area = shoelace(coords)
print(f"{area=}")

i_p = pick(area, b_p)
print(b_p+i_p) # number of points = number of boundary points + interior points
print(f"Execution time: {(time() - t1):.3f}s")
