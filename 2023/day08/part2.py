# idea 2 for optimization: follow all nodes one at a time and find the lowest common multiplicator
from dataclasses import dataclass
import math
import re

with open("input.txt", "r") as f:
    lines = f.readlines()

@dataclass
class Instruction:
	start : str
	left : str
	right : str


total_per_node = []
steps = lines[0].strip()
instructions = []
nodes = []
for line in lines[2:]:
	# print(re.split('\W+', line, maxsplit=3))
	# print(re.findall(r'[A-Z]{3}', line))
	start, left, right = re.findall(r'[A-Z]{3}', line)
	instructions.append(Instruction(start, left, right))
	if start.endswith("A"):
		nodes.append(start)

for node in nodes:
	nb_steps = 0
	while not node.endswith("Z"):
		for step in steps:
			instruction = [x for x in instructions if x.start == node][0]
			if step == "L":
				node = instruction.left
			else:
				node = instruction.right
			nb_steps += 1

	total_per_node.append(nb_steps)

print(total_per_node)
# lowest common multiplicator
print(math.lcm(*total_per_node))
