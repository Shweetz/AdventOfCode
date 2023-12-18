from dataclasses import dataclass

@dataclass
class Beam:
	i : int
	j : int
	direction : str


def move(beam):
	if beam.direction == "N": beam.i -= 1
	if beam.direction == "W": beam.j -= 1
	if beam.direction == "S": beam.i += 1
	if beam.direction == "E": beam.j += 1

def beam_advance(beam):
	global beams_todo
	global beams_done

	# beam being explored, remove from todo
	beams_todo.pop(0)

	# move beam in its direction
	move(beam)
	
	i = beam.i
	j = beam.j
	direction = beam.direction
	
	if i < 0 or j < 0 or i >= len(lines) or j >= len(lines[0]):
		# OOB/out of grid
		print("oob")
		return

	if beam in beams_done:
		# already explored this beam on this tile and direction, skip
		print(beam, "done")
		return

	# add to explored beams
	beams_done.add(beam)

	# explore
	char = lines[i][j]
	
	if char == ".":
		beams_todo.append(Beam(i, j, direction))

	elif char == "/":
		if   direction == "N": beams_todo.append(Beam(i, j, "E"))
		elif direction == "W": beams_todo.append(Beam(i, j, "S"))
		elif direction == "S": beams_todo.append(Beam(i, j, "W"))
		elif direction == "E": beams_todo.append(Beam(i, j, "N"))

	elif char == "\\":
		if   direction == "N": beams_todo.append(Beam(i, j, "W"))
		elif direction == "W": beams_todo.append(Beam(i, j, "N"))
		elif direction == "S": beams_todo.append(Beam(i, j, "E"))
		elif direction == "E": beams_todo.append(Beam(i, j, "S"))

	elif char == "|":
		if   direction in "NS":
			beams_todo.append(Beam(i, j, direction))
		elif direction in "WE":
			beams_todo.append(Beam(i, j, "N"))
			beams_todo.append(Beam(i, j, "S"))

	elif char == "-":
		if   direction in "WE":
			beams_todo.append(Beam(i, j, direction))
		elif direction in "NS":
			beams_todo.append(Beam(i, j, "W"))
			beams_todo.append(Beam(i, j, "E"))

# script start
with open("input.txt", "r") as f:
    lines = f.readlines()

lines = [l.replace("\n", "") for l in lines]

beams_todo = [] # list of beams to explore
beams_done = set() # list of beams explored
energized = []

beams_todo.append(Beam(0, -1, "E"))

while beams_todo:
	beam_advance(beams_todo[0])

print(len(beams_done))

for e in beams_done:
	if (e.i, e.j) not in energized:
		energized.append((e.i, e.j))

print(len(energized))
