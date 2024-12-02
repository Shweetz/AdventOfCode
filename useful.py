line = "".join([char for char in line if char.isdigit()])

# inversion des lignes et des colonnes
l1, l2 = zip(*[line.split() for line in lines])

splits = line.split(" ")
for i, split in enumerate(splits):
	pass
