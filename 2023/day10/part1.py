with open("input.txt", "r") as f:
    lines = f.readlines()

def move(direction):
	global x, y, loop_length, coming_from

	if direction == "north":
		coming_from = "S"
		x -= 1
	if direction == "west":
		coming_from = "E"
		y -= 1
	if direction == "south":
		coming_from = "N"
		x += 1
	if direction == "east":
		coming_from = "W"
		y += 1
	loop_length += 1

loop_length = 0
x, y = 0, 0
coming_from = ""

# find S coordinates
for i, line in enumerate(lines):
	if "S" in line:
		x = i
		y = line.find("S")
		break

# find 1 pipe connected to S
# ! warning ! this only works because it is said that S has exactly 2 pipes connecting (no junk pipe)
if   x-1 >= 0            and lines[x-1][y] in ["|", "7", "F"]: move("north")
elif y-1 >= 0            and lines[x][y-1] in ["-", "L", "F"]: move("west")
elif x+1 < len(lines)    and lines[x+1][y] in ["|", "L", "J"]: move("south")
elif y+1 < len(lines[0]) and lines[x][y+1] in ["-", "J", "7"]: move("east")

# follow the path until back to S
while lines[x][y] != "S":
	# "|"
	if   lines[x][y] == "|" and coming_from == "S": move("north")
	elif lines[x][y] == "|" and coming_from == "N": move("south")
	# "-"
	elif lines[x][y] == "-" and coming_from == "E": move("west")
	elif lines[x][y] == "-" and coming_from == "W": move("east")
	# "L"
	elif lines[x][y] == "L" and coming_from == "E": move("north")
	elif lines[x][y] == "L" and coming_from == "N": move("east")
	# "J"
	elif lines[x][y] == "J" and coming_from == "W": move("north")
	elif lines[x][y] == "J" and coming_from == "N": move("west")
	# "7"
	elif lines[x][y] == "7" and coming_from == "W": move("south")
	elif lines[x][y] == "7" and coming_from == "S": move("west")
	# "F"
	elif lines[x][y] == "F" and coming_from == "E": move("south")
	elif lines[x][y] == "F" and coming_from == "S": move("east")

print(int(loop_length/2))
