with open("input.txt", "r") as f:
	lines = f.readlines()

total = 0

for line in lines:
	game, cubes = line.split(":")
	gameId = int(game.replace("Game ", ""))

	min_red = 0
	min_green = 0
	min_blue = 0
	for draw in cubes.split(";"):
		for numColor in draw.split(","):
			num, color = numColor.strip().split(" ")
			if color == "red":
				min_red = max(min_red, int(num))
			if color == "green":
				min_green = max(min_green, int(num))
			if color == "blue":
				min_blue = max(min_blue, int(num))
		
	total += min_red * min_green * min_blue

print(total)
