from time import time

import dataclasses
from queue import Queue

@dataclasses.dataclass
class Rule:
	letter: str
	inf: bool
	value: int
	result: str


def calc(poss, workflow):
	# print(workflow, poss)
	if workflow == "A":
		# multiply the 4 ranges to have the count of possible parts through the current workflow path
		x = poss["xmax"] - poss["xmin"] + 1
		m = poss["mmax"] - poss["mmin"] + 1
		a = poss["amax"] - poss["amin"] + 1
		s = poss["smax"] - poss["smin"] + 1

		if x <= 0 or m <= 0 or a <= 0 or s <= 0:
			# 0 possible parts if max < min for any of the 4 
			return 0
		
		return x * m * a * s
	
	if workflow == "R":
		return 0
	
	rules = workflows[workflow]
	for rule in rules:
		# print(rule)
		l = rule.letter

		if l == "":
			# last rule, all possibilities go to the next workflow
			queue.put((poss, rule.result))

		else:
			# copy the state to create a rule accept version
			poss_acc = poss.copy()
			if rule.inf:
				poss_acc[l + "max"] = rule.value - 1 # accept
				poss    [l + "min"] = rule.value     # reject

			else:
				poss_acc[l + "min"] = rule.value + 1
				poss    [l + "max"] = rule.value
			
			queue.put((poss_acc, rule.result))

	return 0

# script start
t1 = time()
with open("input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

workflows = {}

for line in lines:
	if len(line) == 0:
		continue

	elif line[0] == "{":
		continue

	else:
		name, rest = line.split("{")
		workflows[name] = []
		for rule in rest.split(","):
			if ":" in rule:
				rule_compare, result = rule.split(":")
				inf = "<" in rule_compare
				workflows[name].append(Rule(rule_compare[0], inf, int(rule_compare[2:]), result))
			else:
				workflows[name].append(Rule("", True, 0, rule.replace("}", "")))

total = 0
queue = Queue()
d = {"xmin": 1, "mmin": 1, "amin": 1, "smin": 1, "xmax": 4000, "mmax": 4000, "amax": 4000, "smax": 4000}
queue.put((d, "in"))

while not queue.empty():
	# print(queue.qsize())
	total += calc(*queue.get())
	# print(f"{total=}")

print(f"{total=}")
print(f"Execution time: {(time() - t1):.3f}s")
