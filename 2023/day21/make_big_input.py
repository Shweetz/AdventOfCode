with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
	
size = 5

with open(f"input_{size}.txt", "w") as f:
	for s in range(size):
		for line in lines:
			f.write(line * size + "\n")
