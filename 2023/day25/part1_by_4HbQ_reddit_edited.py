import collections as C


# G is the graph
G = C.defaultdict(set)

for line in open('input_s.txt'):
    u, *vs = line.replace(':','').split()
    for v in vs: G[u].add(v); G[v].add(u)


# S is cluster 1, it starts as the set of vertices in G and we'll take out vertices 1 at a time
S = set(G)
# S.remove('hfx') #hfx-pzl is a bridge in small input
# S.remove('pzl')

# for vertex v, count his neighbors that are not in S
count = lambda v: len(G[v]-S)

# stop when the sum=3, for every node in S, of neighbors that are not in S
while sum(map(count, S)) != 3:
	# m is the vertex in S with max ("neighbors not in S" - "neighbors in S")
	# if tied, pick randomly between bests
	v = max(S, key=lambda v: len(G[v]-S) - len(G[v]-(G.keys()-S)))
	S.remove(v)

	# print to understand
	for v in S:
		print(len(G[v]-(G.keys()-S)))
		print(len(G[v]-S))
		print(G[v]-S)
		print(G[v])
		print(S)
		print()
	# for m2 in map(count, S):
	# 	print(m2)
	print(sum(map(count, S)), v)
	print()

print(len(S) * len(set(G)-S))