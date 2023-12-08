# from enum import Enum
from dataclasses import dataclass

# class State(Enum):
#     SEED = 1
#     GREEN = 2
#     BLUE = 3


with open("input.txt", "r") as f:
	lines = f.readlines()

lowest_location = None

states = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]

seeds_str = lines[0].replace("seeds: ", "").split(" ")

for seed_str in seeds_str:
	value = int(seed_str)
	seed_state = 0
	line_state = 0

	for line in lines[2:]:
		# if states[line_state+1] in line:
		if line.strip() == "":
			# reached the next map
			line_state += 1
			# print(f"{line_state=}")
			continue

		elif "map" in line:
			print(line)
			if seed_state < line_state:
				# reached next map but seed wasn't matched => number doesn't change
				seed_state += 1
				# print(value)
			continue

		elif seed_state > line_state:
			# wait for next map
			continue
		
		elif seed_state == line_state:
			# print(line)
			dst, src, range = line.split(" ")
			if int(src) <= value < int(src) + int(range):
				# seed matches the current line
				value += int(dst) - int(src)
				seed_state += 1
				# print(value)

	# print(seed_state)
	# print(line_state)
	print(value)
	if lowest_location:
		lowest_location = min(lowest_location, value)
	else:
		lowest_location = value


print(lowest_location)
