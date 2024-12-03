with open("2022/day04/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total = 0

for i, line in enumerate(lines):
	print(f"{line=}")
	l = [int(s) for s in line.replace("-", ",").split(",")]

	# if one assignment is contained in the other
	if l[0] <= l[2] <= l[3] <= l[1] or l[2] <= l[0] <= l[1] <= l[3]:
		total += 1

print(f"{total = }")
assert total == 444
