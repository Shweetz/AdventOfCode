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

l1.sort()
l2.sort()

for i in range(len(l1)):
	total += abs(l1[i] - l2[i])

print(f"{total = }")
assert total == 1646452
