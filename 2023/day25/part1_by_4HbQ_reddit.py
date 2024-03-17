# by u/4HbQ

import collections as C


G = C.defaultdict(set)

for line in open('input_s.txt'):
    u, *vs = line.replace(':','').split()
    for v in vs: G[u].add(v); G[v].add(u)


S = set(G)
S.remove('hfx')
S.remove('pzl')
count = lambda v: len(G[v]-S)

while sum(map(count, S)) != 3:
	print(G)
	print(S)
	m = max(S, key=count)
	print(sum(map(count, S)), m)
	S.remove(max(S, key=count))
	print()

print(len(S) * len(set(G)-S))