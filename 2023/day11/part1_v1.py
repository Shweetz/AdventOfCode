# expand universe (strings) and then calculate position difference

from dataclasses import dataclass

@dataclass
class Pos:
    x: int
    y: int


with open("input.txt", "r") as f:
    lines = f.readlines()

total = 0

# expand lines in the image
expanded_lines = []
empty_line = "." * len(lines[0])
for line in lines:
	expanded_lines.append(line.strip())
	if not "#" in line:
		expanded_lines.append(empty_line)

# find empty columns
galaxy_column = [False for _ in lines]
for line in lines:
	for i, char in enumerate(line):
		if char == "#":
			galaxy_column[i] = True
			
# expand columns in the image
expanded_columns = []
for x, line in enumerate(expanded_lines):
	expanded_column = []
	for y, present in enumerate(galaxy_column):
		# append char by char the line "expanded_lines[x]" into a new line that will be added to "expanded_columns"
		expanded_column.append(line[y])
		if not present:
			# extra column if no galaxy
			expanded_column.append(".")

	expanded_columns.append(expanded_column)

# for line in expanded_lines:
# 	print(line)
# print()
# for line in expanded_columns:
# 	print(line)

# find all galaxy coordinates in expanded universe
gala_coord = []
for x, line in enumerate(expanded_columns):
	for y, char in enumerate(line):
		if char == "#":
			gala_coord.append(Pos(x, y))

# calculate galaxy distances
for i, gala1 in enumerate(gala_coord):
	for j, gala2 in enumerate(gala_coord[i+1:]):
		total += abs(gala1.x - gala2.x) + abs(gala1.y - gala2.y)

print(total)
