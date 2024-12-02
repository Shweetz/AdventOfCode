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

# with open("2024/day2/input_s.txt", "r") as f:
with open("2024/day2/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total = 0

for i, line in enumerate(lines):
	print(f"{line=}")
	splits1 = [int(e) for e in line.split()]
	v = 0

	# Pop elements 1 by 1
	for j in range(0, len(splits1)):
		c = False
		splits = splits1[:]
		splits.pop(j)
		print(f"{splits=}")

		# Reverse the list if is
		if splits[0] > splits[1]:
			splits = splits[::-1]
		
		# Option #1: the easy way, double continue
		for i in range(1, len(splits)):				
			if not splits[i-1] + 1 <= splits[i] <= splits[i-1] + 3:
				c = True
				continue

		if c:
			continue

		# Option #2: the pythonic way
		if not sum(a + 1 <= b <= a + 3 for a, b in zip(splits, splits[1::])) == len(splits) - 1:
			continue
		
		# Option end

		v = 1
		break

	print(f"{v=}")
	total += v

print(f"{total = }")
assert total == 604
