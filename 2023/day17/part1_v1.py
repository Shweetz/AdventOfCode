from dataclasses import dataclass, field
from time import time

@dataclass
class Beam:
	i : int
	j : int
	heat : int = 0
	visited : set = field(default_factory=set)
	direction : str = "-" # ex: "N", "SS", "EEE"
	path : list = field(default_factory=list)


def move(beam, direction):
	if beam.direction[-1] != direction:
		beam.direction = ""
	
	if direction == "N": beam.i -= 1
	if direction == "W": beam.j -= 1
	if direction == "S": beam.i += 1
	if direction == "E": beam.j += 1
		
	beam.heat += int(lines[beam.i][beam.j])
	beam.visited.add((beam.i, beam.j))
	beam.direction += direction
	beam.path.append((beam.i, beam.j))

def beam_advance(beam):
	i = beam.i
	j = beam.j
	direction = beam.direction
	# print(i, j)
	# print(direction)

	beams_todo.remove(beam)

	if beam.i == len(lines) - 1 and beam.j == len(lines[0]) - 1:
		print(beam.path)
		return beam.heat
	
	# if i < 0 or j < 0 or i >= len(lines) or j >= len(lines[0]):
	# 	# OOB/out of grid
	# 	print("oob")
	# 	return False

	if beam.heat > best_heat - int(lines[-1][-1]):
		# worse than another path to the end
		return False

	key = (i, j, direction)
	if key in beams_done:
		if beam.heat >= beams_done[key]:
			# worse than another path to this tile/drection
			return
	beams_done[key] = beam.heat

	# explore
	possibilities = ["N", "W", "S", "E"]
	imp = []

	# no turnaround
	if   direction[-1] == "N": imp.append("S")
	elif direction[-1] == "W": imp.append("E")
	elif direction[-1] == "S": imp.append("N")
	elif direction[-1] == "E": imp.append("W")

	if len(direction) == 3:
		# no more than 3 in a direction
		if   direction[-1] == "N": imp.append("N")
		elif direction[-1] == "W": imp.append("W")
		elif direction[-1] == "S": imp.append("S")
		elif direction[-1] == "E": imp.append("E")

	# no out of bounds
	if i == 0:                 imp.append("N")
	if j == 0:                 imp.append("W")
	if i == len(lines) - 1:    imp.append("S")
	if j == len(lines[0]) - 1: imp.append("E")

	# if len(possibilities) == 0:
	# 	# print(direction)
	# 	# print("no poss")
	# 	return False

	for poss in [p for p in possibilities if p not in imp]:
		newBeam = Beam(i, j, beam.heat, beam.visited.copy(), beam.direction, list(beam.path))
		move(newBeam, poss)

		if not (newBeam.i, newBeam.j) in beam.visited:
			beams_todo.append(newBeam)
		# print(beam.path)
	
	# move beam
	# if i == j:
	# 	move(beam, "E")
	# else:
	# 	move(beam, "S")
		
	# move(beam, possibilities[0])

def calculate_shortest_paths():
	global best_heat
	global nb_paths_to_end

	beams_todo.append(Beam(0, 0, 0))

	while beams_todo:
		beam = beams_todo[-1]
		# while beam.i != len(lines) - 1 or beam.j != len(lines[0]) - 1:
		# 	if not beam_advance(beam):
		# 		beams_todo.remove(beam)
		# 		break
		
		beam_heat = beam_advance(beam)
		if beam_heat:
			nb_paths_to_end += 1
			print(beam_heat)
			best_heat = min(best_heat, beam_heat)
				# break
	
	# print(beam.heat)

# script start
t1 = time()
with open("input_50.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

best_heat = 1000000
nb_paths_to_end = 0
# best_path_to = [[-1 for _ in range(len(lines[0]))] for _ in range(len(lines))]
# print(best_path_to)
beams_todo = []
beams_done = {}
energized = []

calculate_shortest_paths()

print(f'Execution time: {(time() - t1):.3f}s')
print(nb_paths_to_end)
print(best_heat)
