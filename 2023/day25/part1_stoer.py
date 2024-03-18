from time import time

import random
import sys
sys.setrecursionlimit(1000000)

def contract_graph(links):
	"""Contract links recursively to implement Stoer-Wagner's algorithm"""
	global nodes_count

	# choose 1st node in alphabetical order as cluster core, "a"
	a = min(components)

	# find links between cluster and outside, so links between "a" and any node
	links_with_a = {k:v for (k,v) in links.items() if a in k} # dict comprehension

	# find the heaviest of those links (find the key in "links_with_a" with highest value)
	a, b = max(links_with_a, key=links_with_a.get)

	# contract link
	new_links = {}
	for k in links:
		ka, kb = k

		# link (a, b) is gone
		if k == (a, b):
			continue
			
		# replace "b" with "a" everywhere else
		if b == ka:
			new_key = tuple(sorted([a, kb]))
		elif b == kb:
			new_key = tuple(sorted([ka, a]))
		else:
			new_key = k

		if new_key not in new_links:
			new_links[new_key] = 0
		new_links[new_key] += links[k]

	# add the node in the cluster count
	nodes_count += 1

	# count links out of the cluster
	cut_count = sum(new_links[k] for k in new_links if a in k)
	
	if cut_count == best_cut_count:
		return nodes_count * (len(components) - nodes_count)
	else:
		return contract_graph(new_links)


# script start
with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

t1 = time()
components = {}
links = {}
nodes_count = 1 # "a" is in the cluster
best_cut_count = 3

# fill "components"
for line in lines:
	compos = line.replace(":", "").split()
	for compo in compos:
		if compo not in components:
			components[compo] = set()

		if compo != compos[0]:
			components[compos[0]].add(compo)
			components[compo].add(compos[0])

# fill "links"
for compo in components:
	for adj in components[compo]:
		a, b = sorted([compo, adj]) # sort all keys of "links", so links don't appear in both directions
		links[(a, b)] = 1

# contract graph
print(contract_graph(links))
	
print(f"Execution time: {(time() - t1):.3f}s")
