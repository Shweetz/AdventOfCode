# using recursion on only the remaining symbols: part 1 solving < 1sec

# printing only if toggled
def pprint(*str):
	if False:
		print(*str)

def try_recursive(symbols, groups, depth=0):
	global total
	pprint(" "*depth, symbols, groups)
	
	def dot():
		# skip useless dot
		try_recursive(symbols[1:], groups, depth+1)
		
	def pound():
		# there must not be "." in the next groups[0] chars
		if len(symbols) < groups[0] or "." in symbols[:groups[0]]:
			return False
		
		# after the next groups[0] chars, there can't be a "#"
		if len(symbols) > groups[0] and "#" == symbols[groups[0]]:
			return False
		
		# skip (groups[0]+1) chars and remove first group
		try_recursive(symbols[groups[0]+1:], groups[1:], depth+groups[0]+1)

	if not symbols:
		if not groups:
			total += 1
		
	elif not groups:
		if not "#" in symbols:
			total += 1
	
	elif "." == symbols[0]:
		dot()
		
	elif "#" == symbols[0]:
		pound()
		
	elif "?" == symbols[0]:
		dot()
		pound()


# script start
with open("input.txt", "r") as f:
    lines = f.readlines()

total = 0

for line in lines:
	symbols, raw_groups = line.split()
	groups = [int(n) for n in raw_groups.split(",")]

	try_recursive(symbols, groups)

	print(total)
