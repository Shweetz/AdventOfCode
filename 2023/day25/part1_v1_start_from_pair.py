from time import time

def explore():
	global neighbors
	global visited
	
	# reset dict, set all values to 0
	neighbors = neighbors.fromkeys(neighbors, 0)
	visited = set()
	
	while to_explore:
		compo = to_explore.pop(0)
		visited.add(compo)
		for adj in components[compo]:
			neighbors[adj] += 1
			if neighbors[adj] >= 2:
				print(f"to_explore={to_explore}")
				print(f"compo={compo}")
				print(f"neighbors[{adj}]={neighbors[adj]}")
				print(f"")

			if neighbors[adj] == 2 and adj not in visited and adj:
				to_explore.append(adj)

with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

# script start
t1 = time()
components = {}
neighbors = {}
visited = set()
to_explore = []
to_explore_backup = []

for line in lines:
	compos = line.replace(":", "").split()
	for compo in compos:
		if compo not in components:
			components[compo] = set()

		if compo != compos[0]:
			components[compos[0]].add(compo)
			components[compo].add(compos[0])

			if to_explore and not to_explore_backup:
				to_explore_backup.append(compos[0])
				to_explore_backup.append(compo)

			if not to_explore:
				to_explore.append(compos[0])
				to_explore.append(compo)
		
		
		neighbors[compo] = 0

print(components)

# queue.put(components[0])
# queue.put(components[1])

# while not queue.empty():
# 	steps, finished = take_step(*queue.get())
# 	if finished:
# 		max_steps = max(-steps, max_steps) # steps were negative

found = False

for compo in components.keys():
	for adj in components[compo]:
		# explore with another start pair
		to_explore = [compo, adj]
		explore()

		nb_val = [v for v in neighbors.values() if v == 1]
		if nb_val == 3:
			found = True
			break
	
	if found:
		break
# explore()

# if len(visited) == 2:
# 	# if the start pair is 1 of the 3 connections to cut, visited will only be equal to 2
# 	# then, try again with another pair

# 	# reset dict, set all values to 0
# 	neighbors = neighbors.fromkeys(neighbors, 0)

# 	# explore with another start pair
# 	to_explore = to_explore_backup
# 	explore()

print(visited)
print(len(visited) * (len(components) - len(visited))) # start is not a step
print(f"Execution time: {(time() - t1):.3f}s")
