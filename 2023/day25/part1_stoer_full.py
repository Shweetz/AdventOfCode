from time import time

import random
import sys
sys.setrecursionlimit(1000000)

def contract_link(graph, a, b):
	new_graph = {}
	for k in graph:
		ka, kb = k

		# "link_contract" (a, b) is gone
		if k == (a, b):
			continue
			
		# replace "b" with "a" everywhere else
		if b == ka:
			new_key = tuple(sorted([a, kb]))
		elif b == kb:
			new_key = tuple(sorted([ka, a]))
		else:
			new_key = k

		if new_key not in new_graph:
			new_graph[new_key] = 0
		new_graph[new_key] += graph[k]

	return new_graph

def contract_graph(graph, a):
	"""Contract links recursively to implement Stoer-Wagner's algorithm"""
	# find links between cluster and outside, so links between "a" and any node
	links_with_a = {k:v for (k,v) in graph.items() if a in k} # dict comprehension

	# find the heaviest of those links (find the key with highest value)
	a, b = max(links_with_a, key=links_with_a.get)

	# contract link "ab"
	new_graph = contract_link(graph, a, b)
	
	if len(new_graph) > 1:
		return contract_graph(new_graph, a)
	else:
		return new_graph, b


# script start
with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

t1 = time()
nodes = {}
graph = {}
nodes_count = {} # for each node, itself + all nodes "merged" into it

# fill "nodes"
for line in lines:
	compos = line.replace(":", "").split()
	for compo in compos:
		if compo not in nodes:
			nodes[compo] = set()

		if compo != compos[0]:
			nodes[compos[0]].add(compo)
			nodes[compo].add(compos[0])

# fill "graph" and "nodes_count"
for compo in nodes:
	for adj in nodes[compo]:
		a, b = sorted([compo, adj]) # sort all keys of "graph", so links don't appear in both directions
		graph[(a, b)] = 1

	nodes_count[compo] = set()
	nodes_count[compo].add(compo)

best_cut_count = len(nodes)
best_total = 0

# choose 1st node in alphabetical order as cluster core, "a"
a = min(nodes)

# contract graph
while len(graph) > 1:
	last_link, b = contract_graph(graph, a)

	assert len(last_link) == 1

	for k, v in last_link.items():
		merge_link = sorted((b, k[1]))

		if v < best_cut_count:
			best_cut_count = v
			best_total = len(nodes_count[merge_link[0]]) * (len(nodes) - len(nodes_count[merge_link[0]]))
			print(f"{best_cut_count=}, {best_total=}")

		nodes_count[merge_link[0]].update(nodes_count[merge_link[1]])

		# merge last 2 nodes of the iteration: b and k[1] (a = k[0], 1st node alphabetically)
		graph = contract_link(graph, *merge_link)

	print(f"{len(graph)=}")

print(f"{best_total=}")
	
print(f"Execution time: {(time() - t1):.3f}s")
