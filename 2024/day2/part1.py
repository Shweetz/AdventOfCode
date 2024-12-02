from dataclasses import dataclass

@dataclass
class Object: pass

def spl(s, seps):
	"""Split a string over every char in the seps string"""
	for sep in seps:
		s = s.replace(sep, seps[-1])
	return s.split(seps[-1])

def rem(s, seps):
	"""Remove chars from a string"""
	return "".join([c for c in s if c not in seps])

# input file

with open("2024/day2/input.txt", "r") as f:
# with open("2024/day2/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total = 0

for i, line in enumerate(lines):
	print(f"{line=}")
	splits = [int(e) for e in line.split()]
	v = 1

	# Reverse the list if decreasing
	if splits[0] > splits[1]:
		splits = splits[::-1]
		
	for i in range(1, len(splits)):
		if not splits[i-1] + 1 <= splits[i] <= splits[i-1] + 3:
			v = 0
			break
			
	print(f"{v=}")
	total += v

print(f"{total = }")
assert total == 564
