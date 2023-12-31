from time import time

from dataclasses import dataclass
import re

@dataclass
class Rule:
	letter: str
	inf: bool
	value: int
	result: str

def compare_part(part, rules):
	for rule in rules:
		print(rule)
		if rule.letter == "":
			return rule.result
		if rule.inf and part[rule.letter] < rule.value:
			return rule.result
		if not rule.inf and part[rule.letter] > rule.value:
			return rule.result
		# else try next rule

# script start
t1 = time()
with open("input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

workflows = {}
total = 0

for line in lines:
	if len(line) == 0:
		continue

	elif line[0] == "{":
		x, m, a, s = re.findall(r'[0-9]+', line)
		part = {"x": int(x), "m": int(m), "a": int(a), "s": int(s)}
		workflow = "in"
		while workflow not in ["A", "R"]:
			workflow = compare_part(part, workflows[workflow])

		if workflow == "A":
			total += part["x"]
			total += part["m"]
			total += part["a"]
			total += part["s"]

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


print(total)
print(f"Execution time: {(time() - t1):.3f}s")
