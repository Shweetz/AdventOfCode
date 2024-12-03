import re

def spl(s, seps):
	"""Split a string over multiple separators (every char in 'seps')"""
	for sep in seps:
		s = s.replace(sep, seps[-1])
	return s.split(seps[-1])

with open("2024/day03/input1.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total = 0
doing = True

lines = "-".join(lines)
# print(f"{lines=}")

option = 4

ints = re.findall(r"\d+", lines)
print(f"{ints=}")
if option == 1:
	# - Option 1: string split + part1 findall
	don = lines.find("don't()")
	while don != -1:
		# find next "do()"
		do = don + lines[don:].find("do()")
		if do != don - 1:
			lines = lines[:don] + lines[do:]
		else:
			# no "do()" found, remove everything after the "don't()"
			lines = lines[:don]
		don = lines.find("don't()")

	matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", lines)
	total = sum(int(a)*int(b) for a,b in matches)

if option == 2:
	# - Option 2: re.sub + part1 findall
	# remove everything from a "don't()" to the next "do()"
	# the '?' in the regex is necessary to stop on the very next "do()"
	lines = re.sub(r"don't\(\).*?do\(\)", "", lines)

	# no "do()" found, remove everything after the "don't()"
	lines = re.sub(r"don't\(\).*", "", lines)

	matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", lines)
	total = sum(int(a)*int(b) for a,b in matches)

if option == 3:
	# - Option 3: findall to search all 3: "mul()", "don't()" and "do()" 
	matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", lines)
	print(f"{matches=}")
	for m in matches:
		if m == "don't()":
			doing = False
		elif m == "do()":
			doing = True
		elif doing:
			_, n1, n2, _ = spl(m, "(,)")
			total += int(n1) * int(n2)

print(f"{total = }")
assert total == 63013756
