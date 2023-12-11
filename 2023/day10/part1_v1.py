# improvement idea: create methods go_north, go_west, go_south, go_east
with open("input.txt", "r") as f:
    lines = f.readlines()

loop_length = 0
x, y = 0, 0
coming_from = ""

# find S
for i, line in enumerate(lines):
	# print(line)
	if "S" in line:
		x = i
		y = line.find("S")
		# print(x)
		# print(y)

# find 1 pipe connected to S
if   x-1 >= 0 and lines[x-1][y] in ["|", "7", "F"]:
	coming_from = "S"
	x -= 1
elif y-1 >= 0 and lines[x][y-1] in ["-", "L", "F"]:
	coming_from = "E"
	y -= 1
elif x+1 < len(lines) and lines[x+1][y] in ["|", "L", "J"]:
	coming_from = "N"
	x += 1
elif y+1 < len(lines[0]) and lines[x][y+1] in ["-", "J", "7"]:
	coming_from = "W"
	y += 1
loop_length = 1

# follow the path until back to S
while lines[x][y] != "S":
	# "|"
	if   lines[x][y] == "|" and coming_from == "S":
		x -= 1
	elif lines[x][y] == "|" and coming_from == "N":
		x += 1
	# "-"
	elif lines[x][y] == "-" and coming_from == "E":
		y -= 1
	elif lines[x][y] == "-" and coming_from == "W":
		y += 1
	# "L"
	elif lines[x][y] == "L" and coming_from == "E":
		coming_from = "S"
		x -= 1
	elif lines[x][y] == "L" and coming_from == "N":
		coming_from = "W"
		y += 1
	# "J"
	elif lines[x][y] == "J" and coming_from == "W":
		coming_from = "S"
		x -= 1
	elif lines[x][y] == "J" and coming_from == "N":
		coming_from = "E"
		y -= 1
	# "7"
	elif lines[x][y] == "7" and coming_from == "W":
		coming_from = "N"
		x += 1
	elif lines[x][y] == "7" and coming_from == "S":
		coming_from = "E"
		y -= 1
	# "F"
	elif lines[x][y] == "F" and coming_from == "E":
		coming_from = "N"
		x += 1
	elif lines[x][y] == "F" and coming_from == "S":
		coming_from = "W"
		y += 1

	loop_length += 1

print(int(loop_length/2))
