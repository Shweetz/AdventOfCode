from dataclasses import dataclass

@dataclass
class Lens:
	name : str
	focal : int


def hash(str):
	value = 0
	for char in str:
		value += ord(char)
		value *= 17
		value %= 256
	return value

# script start
with open("input.txt", "r") as f:
	lines = f.readlines()

total = 0
steps = lines[0].split(",")
boxes = [[] for _ in range(256)]

# move lenses as said in the input file
for step in steps:
	if "=" in step:
		lens_name = step.split("=")[0]
		focal = int(step.split("=")[1])
	else:
		lens_name = step.split("-")[0]

	box_index = hash(lens_name)
	box = boxes[box_index]
	
	if "=" in step:
		lens_found = False
		for lens in box:
			if lens.name == lens_name:
				# update lens focal
				lens_found = True
				lens.focal = focal
				break
		
		if not lens_found:
			# add lens
			box.append(Lens(lens_name, focal))

	else:
		for i, lens in enumerate(box):
			if lens.name == lens_name:
				# remove lens
				box.pop(i)

# calculate total focusing power
for i, box in enumerate(boxes):
	for j, lens in enumerate(box):
		total += (i+1) * (j+1) * lens.focal
		
print(total)
