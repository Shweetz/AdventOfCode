# RecursionError: maximum recursion depth exceeded in comparison

from dataclasses import dataclass

# @dataclass
# class Pos:
# 	i : int
# 	j : int

# @dataclass
# class Beam:
# 	pos : Pos
# 	direction : str

@dataclass
class Beam:
	i : int
	j : int
	direction : str


def move(beam):
	# global x, y, loop_length, coming_from

	if beam.direction == "N": beam.i -= 1
	if beam.direction == "W": beam.j -= 1
	if beam.direction == "S": beam.i += 1
	if beam.direction == "E": beam.j += 1
	# loop_length += 1
	# return pos

def try_recursive(beam):
	# pos = beam.pos
	direction = beam.direction

	global energized

	pos = move(beam)
	# print(beam.i, beam.j)
	# print("2", pos.i, pos.j)

	if beam.i < 0 or beam.j < 0 or beam.i >= len(lines) or beam.j >= len(lines[0]):
		# OOB/out of grid
		print("oob")
		return

	beam = Beam(beam.i, beam.j, direction)
	# print(energized, "energized")
	if beam in energized:
		# already explored this beam on this tile and direction
		print(beam, "done")
		return

	energized.append(beam)
	# print(energized, "energized")
	# print(beam, "append")

	char = lines[beam.i][beam.j]
	# print(char)
	if char == ".":
		try_recursive(Beam(beam.i, beam.j, direction))

	elif char == "/":
		if   direction == "N": try_recursive(Beam(beam.i, beam.j, "E"))
		elif direction == "W": try_recursive(Beam(beam.i, beam.j, "S"))
		elif direction == "S": try_recursive(Beam(beam.i, beam.j, "W"))
		elif direction == "E": try_recursive(Beam(beam.i, beam.j, "N"))

	elif char == "\\":
		if   direction == "N": try_recursive(Beam(beam.i, beam.j, "W"))
		elif direction == "W": try_recursive(Beam(beam.i, beam.j, "N"))
		elif direction == "S": try_recursive(Beam(beam.i, beam.j, "E"))
		elif direction == "E": try_recursive(Beam(beam.i, beam.j, "S"))

	elif char == "|":
		if   direction in "NS": try_recursive(Beam(beam.i, beam.j, direction))
		elif direction in "WE":
			# print("direction in we")
			try_recursive(Beam(beam.i, beam.j, "N"))
			try_recursive(Beam(beam.i, beam.j, "S"))

	elif char == "-":
		if   direction in "WE": try_recursive(Beam(beam.i, beam.j, direction))
		elif direction in "NS":
			try_recursive(Beam(beam.i, beam.j, "W"))
			try_recursive(Beam(beam.i, beam.j, "E"))

# script start
with open("input.txt", "r") as f:
    lines = f.readlines()

lines = [l.replace("\n", "") for l in lines]

energized = []

try_recursive(Beam(0, -1, "E"))

print(len(energized))
# print(energized)

energ2 = []
for e in energized:
	if (e.i, e.j) not in energ2:
		energ2.append((e.i, e.j))

print(len(energ2))
# for e2 in energ2:
# 	print(e2)
