from time import time

def explore(to_explore):
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
				# print(f"to_explore={to_explore}")
				# print(f"compo={compo}")
				# print(f"neighbors[{adj}]={neighbors[adj]}")
				# print(f"")
				pass

			if neighbors[adj] == 2 and adj not in visited and adj:
				to_explore.append(adj)

with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

# script start
t1 = time()
components = {}
neighbors = {}
visited = set()

for line in lines:
	compos = line.replace(":", "").split()
	for compo in compos:
		if compo not in components:
			components[compo] = set()

		if compo != compos[0]:
			components[compos[0]].add(compo)
			components[compo].add(compos[0])
		
		neighbors[compo] = 0

for compo in components:
	# print(compo)
	if len(components[compo]) < 4:
		print(len(components[compo]))

links = set()
for compo in components:
	for adj in components[compo]:
		links.add((compo, adj))

print(f"{len(links)=}")
# if 3 nodes are connected in a triangle, then none of those 3 links can be a bridge between both clusters
links_imp = set()
for compo in components:
	for adj in components[compo]:
		for adj2 in components[compo]:
			if adj2 in components[adj]:
				links_imp.add((compo, adj))
				links_imp.add((compo, adj2))
				links_imp.add((adj, adj2))

				links_imp.add((adj2, adj))
				links_imp.add((adj, compo))
				links_imp.add((adj2, compo))

print(f"{len(links_imp)=}")
for link in links:
	if link not in links_imp:
		print(f"{link=}")

for compo in components.keys():
	# explore from another start node
	to_explore = [compo]

	for adj in components[compo]:
		# add all adjacent nodes in the start exploration
		to_explore.append(adj)
	
	explore(to_explore)

	nb_val = [v for v in neighbors.values() if v == 1]
	# print(f"{len(nb_val)=}")
	if len(nb_val) == 3:
		print("found")
		# found = True
		break
	
	# if found:
	# 	break
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
