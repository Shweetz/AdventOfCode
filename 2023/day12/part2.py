# use memoisation (functools.cache) to cheat time (part 2 in < 1sec)

import functools

# printing only if toggled
def pprint(*str):
	if False:
		print(*str)

@functools.cache
def try_recursive(symbols, groups):
	pprint(symbols, groups)
	
	# my shit optimization attempt lol
	if not is_possible_early(symbols, groups):
		return 0

	def dot():
		# skip useless dot
		return try_recursive(symbols[1:], groups)
		
	def pound():
		# there must not be "." in the next groups[0] chars
		if len(symbols) < groups[0] or "." in symbols[:groups[0]]:
			return 0
		
		# after the next groups[0] chars, there can't be a "#"
		if len(symbols) > groups[0] and "#" == symbols[groups[0]]:
			return 0
		
		# skip (groups[0]+1) chars and remove first group
		return try_recursive(symbols[groups[0]+1:], groups[1:])

	if not symbols:
		if not groups:
			return 1
		
	elif not groups:
		if not "#" in symbols:
			return 1
	
	elif "." == symbols[0]:
		return dot()
		
	elif "#" == symbols[0]:
		return pound()
		
	elif "?" == symbols[0]:
		return dot() + pound()
	
	return 0

def is_possible_early(symbols, groups):
	space_needed = sum(g for g in groups) + len(groups) - 1
	return len(symbols) >= space_needed


# script start
with open("input.txt", "r") as f:
    lines = f.readlines()

total = 0

for line in lines:
	symbols, raw_groups = line.split()
	groups = [int(n) for n in raw_groups.split(",")]

	symbols = "?".join([symbols for _ in range(5)]) # equivalent to: (symbols + "?") * 4 + symbols
	groups = groups * 5

	# tuple so "groups" is immutable and can be used by cache
	total += try_recursive(symbols, tuple(groups))

	print(total)
