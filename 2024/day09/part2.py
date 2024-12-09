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

# 2. compact files in free space

z = len(v) - 1

for z in range(len(v) - 1, 1, -1):
	# find last file (those that don't fit anywhere will be skipped) 
	if v[z] == ".":
		continue

	# find 1st space where last file fits
	c = 0
	while v[c] != "." or l[c] < l[z]:
		c += 1
		if c >= z:
			break
		
	if c >= z:
		continue
	
	# insert the file in front of free space (index is preserved because z-1 is free space, so no file is skipped)
	l[c] -= l[z]
	v.insert(c, v[z])
	l.insert(c, l[z])
	# z += 1
	v[z+1] = "."

# 3. calculate score using 2 indexes: if free space is found in left index, use the value of the file in right index

p = 0

for i, v in enumerate(v):
	for _ in range(l[i]):
		if v != ".":
			total += p * int(v)
		p += 1

print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")
assert total == 6221662795602
