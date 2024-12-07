from collections import Counter, defaultdict
from dataclasses import dataclass
import re

def get_ints(s):
	"""Return the list of the ints in a string"""
	return [int(d) for d in re.findall(r"\d+", s)]

@dataclass
class Object: pass

with open("2024/day05/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

# g = Grid()
# g.read(lines)
# print(f"{g.g=}")
# print(f"{g.g[(0,0)]=}")
# print(f"{g.adj(0,0,0)=}")
# print(f"{len(g.find("XMAS", 0))=}")
# dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
# dir = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, 1], [1, 1], [1, -1], [-1, -1]]

total = 0
best = 0
cur = 0

ll = []
# l1, l2 = zip(*[line.split() for line in lines])

order = defaultdict(set)

# for l1, l2, l3 in zip(lines[::3], lines[1::3], lines[2::3]):
for i, line in enumerate(lines):
	print(f"{line=}")
	# for j, c in enumerate(line):
		
	# l = [int(s) for s in line.split()]
	l = get_ints(line)
	# print(f"{l=}")

#p1
	# if len(l) == 2:
	# 	order[l[0]].add(l[1])
	# elif len(l) > 2:
	# 	x = int((len(l)-1)/2)
	# 	# print(f"{x=}")
	# 	value = l[x]
	# 	for i, j in enumerate(l):
	# 		for k in range(i+1, len(l)):
	# 			m = l[k]
	# 			# print(f"{j,m,order[m]=}")
	# 			if j in order[m]:
	# 				value = 0
	
	# 	total += value
	# 	print(f"{total = }")		

	#p2
		
	if len(l) == 2:
		order[l[0]].add(l[1])
	elif len(l) > 2:

		loop = True
		add = False
		while loop:
			loop = False
			x = int((len(l)-1)/2)
			value = l[x]
			for i, j in enumerate(l):
				for k in range(i+1, len(l)):
					m = l[k]
					if j in order[m]:
						print(f"{i,k,m,j,l[i], l[k]=}")
						l[i], l[k] = m, j
						print(f"{l=}")
						loop = True
						add = True
						break
				if loop:
					break
		
		print(f"{l=}")
	
		if add:
			total += value
		print(f"{total = }")	

# print(f"{order=}")
# ll2 = zip(*ll)
# print(f"{list(ll2) = }")

print(f"{total = }")
