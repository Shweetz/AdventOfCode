from dataclasses import dataclass
import re

with open("input.txt", "r") as f:
    lines = f.readlines()

@dataclass
class Instruction:
	start : str
	left : str
	right : str


total = 0
steps = lines[0].strip()
instructions = []
for line in lines[2:]:
	# print(re.split('\W+', line, maxsplit=3))
	# print(re.findall(r'[A-Z]{3}', line))
	start, left, right = re.findall(r'[A-Z]{3}', line)
	instructions.append(Instruction(start, left, right))

node = "AAA"
while node != "ZZZ":
	for step in steps:
		instruction = [x for x in instructions if x.start == node][0]
		if step == "L":
			node = instruction.left
		else:
			node = instruction.right

		print(node)
		total += 1
print(total)
