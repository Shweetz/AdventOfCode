# now runs in 2sec instead of 1h, only turned beams_done and energized from lists to sets OMG

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
	global exits

	# beam being explored, remove from todo
	beams_todo.pop(0)

	# move beam in its direction
	move(beam)
	
	i = beam.i
	j = beam.j
	direction = beam.direction
	
	if i < 0 or j < 0 or i >= len(lines) or j >= len(lines[0]):
		# OOB/out of grid
		# print("oob")
		# exit reached, reverse the direction to remember to remove this start later
		if   direction == "N": rev_dir = "S"
		elif direction == "W": rev_dir = "E"
		elif direction == "S": rev_dir = "N"
		elif direction == "E": rev_dir = "W"
		exits.append(Beam(i, j, rev_dir))
		return

	if (i, j, direction) in beams_done:
		# already explored this beam on this tile and direction, skip
		# print(beam, "done")
		return

	# add to explored beams
	beams_done.add((i, j, direction))
	energized.add((i, j))

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
best_energized = 0

# starts to explore
starts_todo = []
for i in range(len(lines)):
	starts_todo.append(Beam(i, -1, "E"))
	starts_todo.append(Beam(i, len(lines[0]), "W"))
for j in range(len(lines[0])):
	starts_todo.append(Beam(-1, j, "S"))
	starts_todo.append(Beam(len(lines), j, "N"))

while starts_todo:
	beams_todo = [] # list of beams to explore with the current start
	beams_done = set() # beams explored with the current start
	energized = set()
	exits = [] # exits reached with the current start

	beams_todo.append(starts_todo[0])

	while beams_todo:
		beam_advance(beams_todo[0])
	
	# print(starts_todo[0], "done, remaining:", len(starts_todo), "/ 440")
	starts_todo.pop(0)

	# all exits reached by the start are at best equal, so they can be safely not explored
	for exit in exits:
		# remove 1 by 1 because of potential issues with pop indexes
		for x, start in enumerate(starts_todo):
			if exit == start:
				# print(starts_todo[x], "pop, remaining:", len(starts_todo), "/ 440")
				starts_todo.pop(x)

	# print(len(beams_done))

	print(len(energized))
	if len(energized) > best_energized:
		best_energized = len(energized)

print(f"{best_energized=}")
