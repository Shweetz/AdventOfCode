# def spl(s, seps):
# 	"""Split a string over multiple separators (every char in 'seps')"""
# 	for sep in seps:
# 		s = s.replace(sep, seps[-1])
# 	return s.split(seps[-1])

with open("2022/day04/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total = 0

for i, line in enumerate(lines):
	print(f"{line=}")
	# l = [int(s) for s in spl(line, ",-")]
	l = [int(s) for s in line.replace("-", ",").split(",")]

	# if one of the 4 IDs is contained in the other assignment
	if l[0] <= l[2] <= l[1] or l[0] <= l[3] <= l[1] or l[2] <= l[0] <= l[3] or l[2] <= l[1] <= l[3]:
		total += 1

print(f"{total = }")
assert total == 801
