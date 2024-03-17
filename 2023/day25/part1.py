from time import time

import random
import sys
sys.setrecursionlimit(1000000)

def contract_graph(links):
	"""Contract links recursively to implement Karger's algorithm"""

	link_contract = None

	# optimization: if a link has a value higher than best_cut_count, contract it
	for k in links:
		if links[k] > best_cut_count:
			link_contract = k

	# else, randomize it, with a weight towards high value links
	if link_contract is None:
		weighted_list = []
		for k in links:
			for _ in range(int(links[k])):
				weighted_list.append(k)

		link_contract = random.choice(weighted_list)

	a, b = link_contract

	# count nodes to know both clusters' size at the end
	nodes_count[a] += nodes_count[b]

	# contract link
	new_links = {}
	for k in links:
		ka, kb = k

		# "link_contract" (a, b) is gone
		if k == link_contract:
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
	
	if len(new_links) > 1:
		# recurse until 1 link remains
		return contract_graph(new_links)
	else:
		# 1 link remaining, return cut_count and multiplication of clusters' size
		for k, cut_count in new_links.items():
			ka, kb = k
			return cut_count, nodes_count[ka]*nodes_count[kb]


# script start
with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

t1 = time()
components = {}
nodes_count = {}
best_cut_count = 3

for line in lines:
	compos = line.replace(":", "").split()
	for compo in compos:
		if compo not in components:
			components[compo] = set()

		if compo != compos[0]:
			components[compos[0]].add(compo)
			components[compo].add(compos[0])
		
		nodes_count[compo] = 1

links = {}
for compo in components:
	for adj in components[compo]:
		a, b = sorted([compo, adj]) # sort
		links[(a, b)] = 1

cut_count = 0
while cut_count != 3:
	# reset nodes_count before every graph contraction
	for node in nodes_count:
		nodes_count[node] = 1
	
	# graph contraction
	cut_count, total = contract_graph(links)

	print(f"{cut_count=}, {total=}")
	
print(f"Execution time: {(time() - t1):.3f}s")
