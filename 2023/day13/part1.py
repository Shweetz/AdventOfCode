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
	found = False
	
	# search symmetry in rows
	for i in range(1, len(pattern)):
		# number of rows to compare (1, 2, 3, ... 3, 2, 1)
		nb = min(i, len(pattern) - i)
		
		rows_above = pattern[i-nb:i]
		rows_below = pattern[i:i+nb]
		
		if rows_above == rows_below[::-1]: # reverse order of rows_below
			total += i*100
			found = True
			break
	
	# if row symmetry, don't look for column symmetry
	if found:
		print(total)
		continue
	
	# build columns list
	cols = []
	for i in range(len(pattern[0])):
		cols.append([pattern[x][i] for x in range(len(pattern))])
	
	# search symmetry in columns
	for i in range(1, len(cols)):
		# number of columns to compare (1, 2, 3, ... 3, 2, 1)
		nb = min(i, len(cols) - i)
		
		cols_left  = cols[i-nb:i]
		cols_right = cols[i:i+nb]
		
		if cols_left == cols_right[::-1]: # reverse order of cols_right
			total += i
	
	print(total)
