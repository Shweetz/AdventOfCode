with open("input.txt", "r") as f:
	lines = f.readlines()

total = 0

for line in lines:
	game, cubes = line.split(":")
	gameId = int(game.replace("Game ", ""))

	poss = True
	for draw in cubes.split(";"):
		for numColor in draw.split(","):
			num, color = numColor.strip().split(" ")
			if color == "red" and int(num) > 12:
				poss = False
			if color == "green" and int(num) > 13:
				poss = False
			if color == "blue" and int(num) > 14:
				poss = False
		
	if poss:
		total += gameId

print(total)
