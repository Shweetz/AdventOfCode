with open("2022/day01/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total = 0
cur = 0
best = [0, 0, 0]

for i, line in enumerate(lines):
	print(f"{line=}")
	l = [int(s) for s in line.split()]

	if l:
		cur += l[0]
	else:
		if cur > best[0]:
			best[0] = cur
			best.sort()
		cur = 0

total = sum(best)
print(f"{total = }")
assert total == 210406
