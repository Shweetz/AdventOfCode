# idea 1 for optimization: follow all nodes simultaneously and hope some of them merge paths
from dataclasses import dataclass
import re

with open("input.txt", "r") as f:
    lines = f.readlines()

@dataclass
class Instruction:
	start : str
	left : str
	right : str


def nodes_end_with_z():
	for node in nodes:
		if not node.endswith("Z"):
			return False
	return True

def remove_duplicates(nodes):
	nodes = list(dict.fromkeys(nodes))

total = 0
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

while not nodes_end_with_z():
	for step in steps:
		for node in nodes:
			instruction = [x for x in instructions if x.start == node][0]
			if step == "L":
				node = instruction.left
			else:
				node = instruction.right

		remove_duplicates(nodes)
		if len(nodes) != 6:
			print(len(nodes))

		# print(node)
		total += 1
print(total)
