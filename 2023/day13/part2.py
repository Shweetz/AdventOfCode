def count_diffs(pattern1, pattern2):
	nb_diff = 0
	for j in range(len(pattern1)):
		for k in range(len(pattern1[0])):
			if pattern1[j][k] != pattern2[j][k]:
				if nb_diff == 0:
					nb_diff = 1
				else:
					return 2
	return nb_diff

def search_symmetry(pattern):
	for i in range(1, len(pattern)):
		# number of rows to compare (1, 2, 3, ... 3, 2, 1)
		nb = min(i, len(pattern) - i)
		
		rows_above = pattern[i-nb:i]
		rows_below = pattern[i:i+nb]

		# there must be exactly 1 difference between "rows_above" and "rows_below" reversed
		if count_diffs(rows_above, rows_below[::-1]) == 1:
			return i
		
	return -1

# script start
with open("input.txt", "r") as f:
    lines = f.readlines()

total = 0

# split input file in a list of patterns, each pattern being a list of rows
patterns = [[]]
for line in lines:
	if line == "\n":
		# new pattern
		patterns.append([])
	else:
		# new row in last pattern
		patterns[-1].append(line.strip())

for pattern in patterns:
	# search symmetry in rows
	i = search_symmetry(pattern)
	if i != -1:
		total += i*100
		print(total)
		continue
	
	# build columns list
	cols = []
	for i in range(len(pattern[0])):
		cols.append([pattern[x][i] for x in range(len(pattern))])
	
	# search symmetry in columns
	i = search_symmetry(cols)
	if i != -1:
		total += i
		print(total)
