# easy but slow and takes a lot of memory: create new_seeds_str
# do the process one seed at a time

from dataclasses import dataclass

with open("input.txt", "r") as f:
	lines = f.readlines()

lowest_location = None

seeds_str = lines[0].replace("seeds: ", "").split(" ")

new_seeds_str = []
for i in range(0, len(seeds_str), 2):
	# for every range (pair of numbers in input)
	range_start = int(seeds_str[i])
	range_end = range_start + int(seeds_str[i+1])
	for seed in range(range_start, range_end):
		# do the process one seed at a time
		value = seed
		seed_state = 0
		line_state = 0

		for line in lines[2:]:
			if line.strip() == "":
				continue

			elif "map" in line:
				# reached next map
				line_state += 1
				if seed_state < line_state:
					# seed wasn't matched => value doesn't change
					seed_state += 1
				continue
			
			elif seed_state == line_state:
				dst, src, range = line.split(" ")
				if int(src) <= value < int(src) + int(range):
					# seed matches the current line
					value += int(dst) - int(src)
					seed_state += 1

		if lowest_location:
			lowest_location = min(lowest_location, value)
		else:
			lowest_location = value

print(lowest_location)
