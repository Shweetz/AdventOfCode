from collections import Counter, defaultdict
import re

def get_ints(s):
	"""Return the list of the ints in a string"""
	return [int(d) for d in re.findall(r"\d+", s)]

with open("2024/day05/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total = 0

order = defaultdict(set)

for i, line in enumerate(lines):
	l = get_ints(line)
	
	if len(l) == 2:
		order[l[0]].add(l[1])
		
	elif len(l) > 2:
		x = int((len(l)-1)/2)
		value = l[x]

		for i in range(len(l)):
			for j in range(i+1, len(l)):
				if l[i] in order[l[j]]:
					value = 0
	
		total += value

print(f"{total = }")
assert total == 4662
