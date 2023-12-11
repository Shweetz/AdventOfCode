with open("input.txt", "r") as f:
    lines = f.readlines()

def move(direction):
	global x, y, coming_from

	if direction == "N":
		coming_from = "S"
		x -= 1
	if direction == "W":
		coming_from = "E"
		y -= 1
	if direction == "S":
		coming_from = "N"
		x += 1
	if direction == "E":
		coming_from = "W"
		y += 1

x, y = 0, 0
coming_from = ""
inside_tiles = 0

# create a clean board of the same size filled with "." so junk (unconnected pipes) is cleared
clean_board = [ [ "." for y in range(len(lines[0]))] for x in range(len(lines))]

# find S coordinates
for i, line in enumerate(lines):
	if "S" in line:
		x = i
		y = line.find("S")
		break

# add the true symbol of S in the clean board
s_connections = []
if x-1 >= 0            and lines[x-1][y] in ["|", "7", "F"]: s_connections.append("N")
if y-1 >= 0            and lines[x][y-1] in ["-", "L", "F"]: s_connections.append("W")
if x+1 < len(lines)    and lines[x+1][y] in ["|", "L", "J"]: s_connections.append("S")
if y+1 < len(lines[0]) and lines[x][y+1] in ["-", "J", "7"]: s_connections.append("E")

if s_connections == ["N", "S"]: clean_board[x][y] = "|"
if s_connections == ["W", "E"]: clean_board[x][y] = "-"
if s_connections == ["N", "E"]: clean_board[x][y] = "L"
if s_connections == ["N", "W"]: clean_board[x][y] = "J"
if s_connections == ["W", "S"]: clean_board[x][y] = "7"
if s_connections == ["S", "E"]: clean_board[x][y] = "F"

# add all main loop pipes in the clean board by following the path until back to S
move(s_connections[0])

while lines[x][y] != "S":
	clean_board[x][y] = lines[x][y]

	# "|"
	if   lines[x][y] == "|" and coming_from == "S": move("N")
	elif lines[x][y] == "|" and coming_from == "N": move("S")
	# "-"
	elif lines[x][y] == "-" and coming_from == "E": move("W")
	elif lines[x][y] == "-" and coming_from == "W": move("E")
	# "L"
	elif lines[x][y] == "L" and coming_from == "E": move("N")
	elif lines[x][y] == "L" and coming_from == "N": move("E")
	# "J"
	elif lines[x][y] == "J" and coming_from == "W": move("N")
	elif lines[x][y] == "J" and coming_from == "N": move("W")
	# "7"
	elif lines[x][y] == "7" and coming_from == "W": move("S")
	elif lines[x][y] == "7" and coming_from == "S": move("W")
	# "F"
	elif lines[x][y] == "F" and coming_from == "E": move("S")
	elif lines[x][y] == "F" and coming_from == "S": move("E")

# rest here and print the clean board before the last part :)
for l in clean_board:
	print("".join(l))

# go through the clean board line by line, char by char
# we're outside the main loop before hitting the 1st pipe of every line
# hitting | will swap between outside and inside
# hitting - will not swap
# other pipes go in pairs since we'll be "on" the loop in-between them:
# hitting LJ will not swap
# hitting L7 will swap
# hitting FJ will swap
# hitting F7 will not swap
for line in clean_board:
	is_inside = False
	enter_char = "" # possible states: "", "F", "L"
	for char in line:
		if char == "." and is_inside:
			inside_tiles += 1
		if char in ["L", "F"]:
			enter_char = char
		if char == "|":
			is_inside = not is_inside
		if char == "7" and enter_char == "L":
			is_inside = not is_inside
		if char == "J" and enter_char == "F":
			is_inside = not is_inside

print(inside_tiles)
