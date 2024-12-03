def intersect(*lists):
	s = set(lists[0])
	for l in lists[1:]:
		s = s & set(l)
	return list(s)

with open("2022/day03/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total = 0

for l1, l2, l3 in zip(lines[::3], lines[1::3], lines[2::3]):
	
	# Option 1: for + if
	# for e in l1:
	# 	if e in l2 and e in l3:
	# 		if ord(e) < ord("a") - 1:
	# 			p = ord(e) - ord("A") + 27
	# 		else:   
	# 			p = ord(e) - ord("a") + 1
	# 		break
	
	# Option 2: set intersection
	e = intersect(l1, l2, l3)[0]

	if ord(e) < ord("a"):
		p = ord(e) - ord("A") + 27
	else:   
		p = ord(e) - ord("a") + 1
	# Option end

	total += p

print(f"{total = }")
assert total == 2581
