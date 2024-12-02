with open("2024/day1/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total = 0
l1 = []
l2 = []
for i, line in enumerate(lines):
	print(f"{line=}")
	e1, e2 = line.split("   ")
	l1.append(int(e1))
	l2.append(int(e2))

for e1 in l1:
	n = 0
	for e2 in l2:
		if e1 == e2:
			n += 1
	
	total += e1 * n

print(f"{total = }")
assert total == 23609874
