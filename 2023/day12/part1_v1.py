# no optimization, try all combinations: part 1 solving = 16sec

import re

with open("input.txt", "r") as f:
    lines = f.readlines()

# print only a specific set of symbols
def pprint(str):
	if symbols == ['#', '#', '#', '.', '.', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.']:
		print(str)

def try_recursive(symbols, numbers, depth=0):
	global total

	# find first "?" in the list
	if "?" in symbols:		
		i = symbols.index("?")

		# try one symbol, then the other, then put it back for other instances
		symbols[i] = "."
		try_recursive(symbols, numbers, depth+1)
		symbols[i] = "#"
		try_recursive(symbols, numbers, depth+1)
		symbols[i] = "?"

	else:
		# no "?" left, check if possible
		if is_possible(symbols, numbers):
			pprint(f"{depth=}, " + str(symbols) + " possible")
			total += 1
		else:
			pprint(f"{depth=}, " + str(symbols) + " impossible")

def is_possible(symbols, numbers):
	# make groups of # like this: ["##", "#", "#####"]
	groups = re.findall(r'[#]+', "".join(symbols))
	
	# there must as as many groups of # than numbers: [2, 1, 5]
	if len(groups) != len(numbers):
		pprint(f"{len(groups)=} {len(numbers)=}")
		return False
	
	for i, group in enumerate(groups):
		# every group must contain the correct number of #
		if len(group) != numbers[i]:
			pprint(f"{len(group)=} {numbers[i]=}")
			return False
	
	return True

# script start
total = 0

for line in lines:
	p1, p2 = line.split()
	symbols = [s for s in p1]
	numbers = [int(n) for n in p2.split(",")]

	try_recursive(symbols, numbers)

	print(total)
