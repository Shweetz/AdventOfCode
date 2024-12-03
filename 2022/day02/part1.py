with open("2022/day02/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total = 0
for i, line in enumerate(lines):
	print(f"{line=}")
	l = [s for s in line.split()]

	# Option 1: easy
	# if l[1] == "X": total += 1
	# if l[1] == "Y": total += 2
	# if l[1] == "Z": total += 3

	if l[0] + l[1] == "AY": total += 6
	if l[0] + l[1] == "BZ": total += 6
	if l[0] + l[1] == "CX": total += 6
	if l[0] + l[1] == "AX": total += 3
	if l[0] + l[1] == "BY": total += 3
	if l[0] + l[1] == "CZ": total += 3

	# Option 2: diff
	total += ord(l[1]) - ord("X") + 1

	# ord(l[1]) - 23 => X, Y, Z = A, B, C
	# + 1 % 3 * 3 because 0, 1, 2 => draw, win, loss = 3, 6, 0
	# total += ((ord(l[1]) - 23 - ord(l[0]) + 1) % 3) * 3

print(f"{total = }")
assert total == 10310
