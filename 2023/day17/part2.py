from dataclasses import dataclass
from queue import PriorityQueue
from time import time

@dataclass(order=True)
class Beam:
	heat : int
	i : int
	j : int
	direction : int = 0 # 0 = next move horizontal, 1 = vertical


def move(beam, i, j):
	if i < 0 or j < 0 or i >= height or j >= width:
		# invalid
		return False

	while beam.i != i or beam.j != j:
		if   beam.i > i: beam.i -= 1
		elif beam.j > j: beam.j -= 1
		elif beam.i < i: beam.i += 1
		elif beam.j < j: beam.j += 1
		
		beam.heat += int(lines[beam.i][beam.j])

	beam.direction = 1 - beam.direction # swap 1 and 0
	return True

def beam_advance(beam):
	i = beam.i
	j = beam.j
	d = beam.direction

	if beam.i == height - 1 and beam.j == width - 1:
		# reached end
		return beam.heat

	# if beam.heat > best_heat - int(lines[-1][-1]) - (height - 1 - i) - (width - 1 - j):
	# 	# worse than another path to the end
	# 	return False

	key = (i, j, d)
	if key in beams_done:
		if beam.heat >= beams_done[key]:
			# worse than another path to this tile/drection
			return False
	beams_done[key] = beam.heat

	# explore
	for y in range(4, 11):
		for x in [-1, 1]:
			newBeam = Beam(beam.heat, i, j, d)

			# direction 0 stays in the row, direction 1 in the column
			# valid = move(newBeam, i + y*x*(1 - d), j + y*x*d) # dirty 1-line
			if (d == 0):
				valid = move(newBeam, i + y*x, j)
			else:
				valid = move(newBeam, i, j + y*x)

			if valid and not (newBeam.i, newBeam.j, newBeam.direction) in beams_done:
				beams_queue.put(newBeam)

# script start
t1 = time()
with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

height = len(lines)
width = len(lines[0])
best_heat = 1000000
beams_queue = PriorityQueue()
beams_done = {}

beams_queue.put(Beam(0, 0, 0, 0)) # next (first) move horizontal
beams_queue.put(Beam(0, 0, 0, 1)) # next (first) move vertical

while not beams_queue.empty():
	beam = beams_queue.get()
	beam_heat = beam_advance(beam)
	if beam_heat:
		best_heat = min(best_heat, beam_heat)

print(f"Execution time: {(time() - t1):.3f}s")
print(f"{best_heat=}")
