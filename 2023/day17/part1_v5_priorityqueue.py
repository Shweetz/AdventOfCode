from dataclasses import dataclass, field
from queue import PriorityQueue
from time import time

@dataclass(order=True)
class Beam:
	i : int
	j : int
	direction : int = 0 # 0 = next move horizontal, 1 = vertical
	heat : int = 0
	visited : set = field(default_factory=set)
	path : list = field(default_factory=list)


def move(beam, i, j):
	if i < 0 or j < 0 or i >= len(lines) or j >= len(lines[0]):
		# invalid
		return False

	while beam.i != i or beam.j != j:
		if beam.i > i: beam.i -= 1
		if beam.j > j: beam.j -= 1
		if beam.i < i: beam.i += 1
		if beam.j < j: beam.j += 1
		
		beam.heat += int(lines[beam.i][beam.j])
		beam.path.append((beam.i, beam.j))

	beam.direction = 1 - beam.direction # swap 1 and 0
	beam.visited.add((beam.i, beam.j, beam.direction))
	return True

def beam_advance(beam):
	i = beam.i
	j = beam.j
	d = beam.direction
	# print(i, j, direction)
	# print(direction)

	global cur_depth
	if beam.heat > cur_depth:
		cur_depth = beam.heat
		print(f"{cur_depth=}")
	
	# beams_queue.remove(beam)

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

	# tmp_dir = direction
	# if tmp_dir == "WWW": tmp_dir = "EEE"
	# if tmp_dir == "NNN": tmp_dir = "SSS"
	key = (i, j, d)
	if key in beams_done:
		if beam.heat >= beams_done[key]:
			# worse than another path to this tile/drection
			return False
	beams_done[key] = beam.heat

	# explore

	for y in range(1, 4):
		for x in [-1, 1]:
			newBeam = Beam(i, j, d, beam.heat, beam.visited.copy(), list(beam.path))

			# direction 0 stays in the row, direction 1 in the column
			# move(newBeam, i + y*x*(1 - d), j + y*x*d) # dirty 1-line
			if (d == 0):
				valid = move(newBeam, i + y*x, j)
			else:
				valid = move(newBeam, i, j + y*x)

			if valid and not (newBeam.i, newBeam.j, newBeam.direction) in beam.visited:
				beams_queue.put(newBeam)
			# print(beam.path)

def calculate_shortest_paths():
	global best_heat
	global nb_paths_to_end

	beams_queue.put(Beam(0, 0, 0))
	beams_queue.put(Beam(0, 0, 1))

	while not beams_queue.empty():
		# print("in queue")
		beam = beams_queue.get()
		# while beam.i != len(lines) - 1 or beam.j != len(lines[0]) - 1:
		# 	if not beam_advance(beam):
		# 		beams_todo.remove(beam)
		# 		break
		
		# print("in queue2")
		beam_heat = beam_advance(beam)
		if beam_heat:
			nb_paths_to_end += 1
			print(beam_heat)
			best_heat = min(best_heat, beam_heat)
				# break

		# print("in queue4")
	# print(beam.heat)

# script start
t1 = time()
with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

best_heat = 1000000
nb_paths_to_end = 0
# best_path_to = [[-1 for _ in range(len(lines[0]))] for _ in range(len(lines))]
# print(best_path_to)
beams_queue = PriorityQueue()
beams_done = {}
energized = []
cur_depth = 0

calculate_shortest_paths()

print(f'Execution time: {(time() - t1):.3f}s')
print(nb_paths_to_end)
print(best_heat)
