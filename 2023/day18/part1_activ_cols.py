from time import time

# script start
t1 = time()
with open("input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

i = 0
j = 0
coords = {} # coordinates of vertices of the shape
active_cols = []
low_i = 0
hig_i = 0
total = 0

# find vertices coordinates of the shape
for line in lines:
	dir, leng, color = line.split()
	leng = int(leng)

	if dir == "U": i -= leng
	if dir == "D": i += leng
	if dir == "L": j -= leng
	if dir == "R": j += leng

	if not i in coords.keys():
		coords[i] = []
	coords[i].append(j)

	low_i = min(low_i, i)
	hig_i = max(hig_i, i)

for x in range(low_i, hig_i + 1):
	if x in coords.keys():
		new_x = sorted(coords[x])
		
		for y in range(0, len(new_x), 2):
			if new_x[y] in active_cols and new_x[y+1] in active_cols:
				if active_cols.index(new_x[y]) % 2 == 0:
					# end of subshape like this:
					# .#.#.
					# .###. <- add 3 for the end of subshape
					# .....
					total += new_x[y+1] - new_x[y] + 1
					# print("heh")
				
				# pop the ended active cols
				active_cols.pop(active_cols.index(new_x[y]))
				active_cols.pop(active_cols.index(new_x[y+1]))
				continue

			index = None
			if new_x[y] in active_cols:
				index = active_cols.index(new_x[y])
			elif new_x[y+1] in active_cols:
				index = active_cols.index(new_x[y+1])
			
			if index is not None:
				if   index % 2 == 0 and active_cols[index] == new_x[y]:
					total += new_x[y+1] - active_cols[index]
					# print(total)
					
				elif index % 2 == 1 and active_cols[index] == new_x[y+1]:
					total += active_cols[index] - new_x[y]
					# print(total)
				
				if   active_cols[index] == new_x[y]:
					active_cols[index] = new_x[y+1]

				elif active_cols[index] == new_x[y+1]:
					active_cols[index] = new_x[y]

			else:
				active_cols.append(new_x[y])
				active_cols.append(new_x[y+1])

				# case for new cols inside shape like this:
				# .#######
				# .#.....#
				# .#.###.# <- add 1 for the center #
				# .#.#.#.#
				if len([col for col in active_cols if col < new_x[y]]) % 2 == 1:
					total += new_x[y+1] - new_x[y] - 1
	
	active_cols.sort()

	# print(f"{active_cols=}")
	for y in range(0, len(active_cols), 2):
		total += active_cols[y+1] - active_cols[y] + 1
		# print(total)
	print(total)
	# print()

print(total)
print(f"Execution time: {(time() - t1):.3f}s")
