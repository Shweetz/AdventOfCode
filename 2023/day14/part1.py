with open("input.txt", "r") as f:
	lines = f.readlines()

total = 0

# transpose input so that north is east (pushing rocks to the right instead of to the top)
rows = []
for i in range(len(lines[0].strip())):
	rows.append([lines[x][i] for x in range(len(lines))][::-1])

# move rocks in each row (to the east)
for row in rows:
	done = False
	while not done:
		done = True
		for i in range(len(row)-1):
			# swap "O" and "." (very slow)
			if row[i] == "O" and row[i+1] == ".":
				row[i], row[i+1] = ".", "O"
				done = False
	
# calculate load (more east = more load)
for row in rows:
	for i, char in enumerate(row):
		if char == "O":
			# 1 point for index 0 (full west)
			total += i + 1
	
print(total)
