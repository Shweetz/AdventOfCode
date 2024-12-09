from time import time

t1 = time()
with open("2024/day09/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total = 0

# data structure: 2 lists, v holds values (fileId or ".") and l holds their length
# so the lists work together with the same index
v = []
l = []

# 1. parse input

id = 0 # fileId
file = True # next elem is file?

for i in range(0, len(lines[0]), 1):
	if file:
		c = id
		id += 1
	else:
		c = "." 
	
	file = not file

	v.append(c) # id or "."
	l.append(int(lines[0][i])) # length

print(f"{v=}")
print(f"{l=}")

# 2. calculate score using 2 indexes: if free space is found in left index, use the value of the file in right index

p = 0 # block's position (in expanded version)
c = 0 # incrementing index in lists
z = len(v) - 1 # decrementing index in lists

while True:
	while l[c] <= 0:
		c += 1
	while l[z] <= 0 or v[z] == ".":
		z -= 1

		if z < 0:
			break
	if c > z:
		break

	if v[c] != ".":
		# file found, calculate it
		total += p * int(v[c])
		l[c] -= 1

	else:
		# free space found, calculate with the last unused file
		total += p * int(v[z])
		l[c] -= 1
		l[z] -= 1

	p += 1

print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")
assert total == 6201130364722
