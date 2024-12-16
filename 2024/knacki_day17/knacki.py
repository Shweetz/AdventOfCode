
from collections import defaultdict, deque

from aoc_tools import *

class MinCostMaxFlow:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.INF = float('inf')

    def add_edge(self, u, v, capacity, cost):
        self.graph[u].append([v, capacity, cost, len(self.graph[v])])
        self.graph[v].append([u, 0, -cost, len(self.graph[u]) - 1])

    def bellman_ford(self, source, sink):
        dist = [self.INF] * self.n
        parent = [-1] * self.n
        edge_used = [-1] * self.n
        in_queue = [False] * self.n

        dist[source] = 0
        queue = deque([source])
        in_queue[source] = True

        while queue:
            u = queue.popleft()
            in_queue[u] = False

            for i, (v, capacity, cost, rev) in enumerate(self.graph[u]):
                if capacity > 0 and dist[u] + cost < dist[v]:
                    dist[v] = dist[u] + cost
                    parent[v] = u
                    edge_used[v] = i
                    if not in_queue[v]:
                        queue.append(v)
                        in_queue[v] = True

        return dist, parent, edge_used

    def min_cost_max_flow(self, source, sink):
        max_flow = 0
        min_cost = 0

        while True:
            dist, parent, edge_used = self.bellman_ford(source, sink)
            if dist[sink] == self.INF:
                break

            # Find the maximum flow along the path found
            flow = self.INF
            v = sink
            while v != source:
                u = parent[v]
                edge_idx = edge_used[v]
                flow = min(flow, self.graph[u][edge_idx][1])
                v = u

            # Apply the flow to the graph
            v = sink
            while v != source:
                u = parent[v]
                edge_idx = edge_used[v]
                self.graph[u][edge_idx][1] -= flow
                rev_idx = self.graph[u][edge_idx][3]
                self.graph[v][rev_idx][1] += flow
                min_cost += flow * self.graph[u][edge_idx][2]
                v = u

            max_flow += flow

        return max_flow, min_cost

with open("2024/knacki_day17/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

for i, line in enumerate(lines):
	if i == 0:
		n, m = get_ints(line)
		network = MinCostMaxFlow(n)

	elif i == len(lines)-1:
		source, sink = get_ints(line)
            
	else:
		u, v, capacity, cost = get_ints(line)
		network.add_edge(u, v, capacity, cost)


max_flow, min_cost = network.min_cost_max_flow(source, sink)
print("Flux maximum :", max_flow)
print("Coût minimum :", min_cost)

# total = total
# print(f"{total = }")
