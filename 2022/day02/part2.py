with open("2022/day02/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total = 0
for i, line in enumerate(lines):
	print(f"{line=}")
	l = [s for s in line.split()]
	
	# Option 1: easy
	if l[0] + l[1] == "AY": total += 1
	if l[0] + l[1] == "BZ": total += 3
	if l[0] + l[1] == "CX": total += 2
	if l[0] + l[1] == "AX": total += 3
	if l[0] + l[1] == "BY": total += 2
	if l[0] + l[1] == "CZ": total += 1
	if l[0] + l[1] == "AZ": total += 2
	if l[0] + l[1] == "BX": total += 1
	if l[0] + l[1] == "CY": total += 3

	if l[1] == "X": total += 0
	if l[1] == "Y": total += 3
	if l[1] == "Z": total += 6

	# Option 2: diff
	# total += (ord(l[1]) - ord("A") + ord(l[0]) - ord("A")) % 3 + 1

	# total += (ord(l[1]) - ord("A") - 23) * 3

print(f"{total = }")
assert total == 14859
