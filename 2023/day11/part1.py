# assign a weight to every line/column to calculate distances

from dataclasses import dataclass

with open("input.txt", "r") as f:
    lines = f.readlines()

@dataclass
class Pos:
	i : int
	j : int


total = 0
galas_pos = []
# assign a weight (expanded_size=2) to every line/column
lines_weight = [2 for i in lines]
cols_weight = [2 for j in lines[0].strip()]

for i, line in enumerate(lines):
	for j, char in enumerate(line):
		if "#" == char:
			# if a galaxy is found, line and column weight must be 1
			galas_pos.append(Pos(i, j))
			lines_weight[i] = 1
			cols_weight[j] = 1

for i, gala1 in enumerate(galas_pos):
	for j, gala2 in enumerate(galas_pos[i+1:]):
		# sort the coordinates of the galaxy pair
		[min_i, max_i] = sorted([gala1.i, gala2.i])
		[min_j, max_j] = sorted([gala1.j, gala2.j])

		# distance is the sum of every line and column weight separating the pair
		dist = sum(lines_weight[min_i:max_i]) + sum(cols_weight[min_j:max_j])
		
		total += dist

print(total)
