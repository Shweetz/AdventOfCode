from time import time

t1 = time()
with open("input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

i = 0
j = 0
coords = set() # coordinates of perimeter points of the shape (vertices + perimeter points)
low_i = 0
hig_i = 0
low_j = 0
hig_j = 0
total = 0

shape_str = ""

# find perimeter points of the shape
for line in lines:
	dir, leng, color = line.split()
	leng = int(leng)

	if   dir == "U":
		for x in range(i - leng, i + 1):
			coords.add((x, j))
		i -= leng
	elif dir == "D":
		for x in range(i, i + leng + 1):
			coords.add((x, j))
		i += leng
	elif dir == "L":
		for y in range(j - leng, j + 1):
			coords.add((i, y))
		j -= leng
	elif dir == "R":
		for y in range(j, j + leng + 1):
			coords.add((i, y))
		j += leng

	low_i = min(low_i, i)
	hig_i = max(hig_i, i)
	low_j = min(low_j, j)
	hig_j = max(hig_j, j)

# go through the shape row by row
for i in range(low_i, hig_i + 1):
	inside = False
	up_crossed = False
	dn_crossed = False
	for j in range(low_j, hig_j + 1):
		if (i, j) in coords:
			# perimeter point
			shape_str += "#"
			total += 1

			if (i-1, j) in coords: up_crossed = not up_crossed
			if (i+1, j) in coords: dn_crossed = not dn_crossed
			
			# if above and below there are perimeter points, we exited or re-entered the shape
			if up_crossed and dn_crossed:
				inside = not inside
				up_crossed = False
				dn_crossed = False

		else:
			# point inside the shape
			shape_str += "."
			
			if inside:
				total += 1
				
	shape_str += "\n"
	print(total)

print(total)
print(shape_str)
print(f"Execution time: {(time() - t1):.3f}s")
