with open("2022/day01/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

cur = 0
best = 0

for i, line in enumerate(lines):
	print(f"{line=}")
	l = [int(s) for s in line.split()]

	if l:
		cur += l[0]
		if cur > best:
			best = cur
	else:
		cur = 0
	
total = best
print(f"{best = }")
assert total == 71924
