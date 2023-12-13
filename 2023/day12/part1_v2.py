# early return if early impossible:  part 1 solving = 12sec
# symbols is string instead of list: part 1 solving = 10sec

import re

with open("input.txt", "r") as f:
    lines = f.readlines()

# print only a specific set of symbols
def pprint(str):
	if symbols == ['#', '#', '#', '.', '.', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.']:
		print(str)

def try_recursive(symbols, numbers, depth=0):
	global total

	if not is_possible_early(symbols, numbers):
		return
	
	# find first "?" in the list
	if "?" in symbols:
		i = symbols.index("?")

		# try one symbol, then the other, then put it back for other instances
		symbols = symbols[:i] + "." + symbols[i+1:]
		try_recursive(symbols, numbers, depth+1)
		symbols = symbols[:i] + "#" + symbols[i+1:]
		try_recursive(symbols, numbers, depth+1)
		symbols = symbols[:i] + "?" + symbols[i+1:]

	else:
		# no "?" left, check if possible
		if is_possible(symbols, numbers):
			pprint(f"{depth=}, " + symbols + " possible")
			total += 1
		else:
			pprint(f"{depth=}, " + symbols + " impossible")

def is_possible(symbols, numbers):
	# make groups of # like this: ["##", "#", "#####"]
	groups = re.findall(r'[#]+', symbols)
	
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

def is_possible_early(symbols, numbers):
	# make groups of # like this: ["##", "#", "#####"]
	i = len(symbols)
	if "?" in symbols:
		i = symbols.index("?")
	groups = re.findall(r'[#]+', symbols[0:i])
	
	for i, group in enumerate(groups):
		# every group must contain the correct number of #
		if i < len(numbers) and len(group) > numbers[i]:
			pprint(f"{len(group)=} {numbers[i]=}")
			return False
	
	return True


# script start
total = 0

for line in lines:
	symbols, raw_numbers = line.split()
	numbers = [int(n) for n in raw_numbers.split(",")]

	try_recursive(symbols, numbers)

	print(total)
