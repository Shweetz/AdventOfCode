with open("input.txt", "r") as f:
	lines = f.readlines()

lowest_location = None

seeds_str = lines[0].replace("seeds: ", "").split(" ")

for seed_str in seeds_str:
	value = int(seed_str)
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
