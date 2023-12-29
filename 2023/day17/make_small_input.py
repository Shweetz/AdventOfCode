with open("input.txt", "r") as f:
    lines = f.readlines()
	
size = 50

with open(f"input_{size}.txt", "w") as f:
	for l in lines[:size]:
		f.write(l[:size] + "\n")


