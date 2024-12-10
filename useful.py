class Grid: pass
lines = []

# transpose lines and columns
l1, l2 = zip(*[line.split() for line in lines])

# timing execution
from time import time

t1 = time()

print(f"Execution time: {(time() - t1):.3f}s")

# read grid and find all paths from 0 to 9 moving adjacent every time, using a queue
g = Grid()
g.read(lines)

total = 0
q = []
for i in range(0, len(lines), 1):
	for j in range(0, len(lines[i]), 1):
		if g.g[(i,j)] == "0":
			q.append((i,j,0)) # fill q with starting cells "0"

while q:
	i,j,v = q.pop()
	for x,y,v2 in g.adj(i,j): # look in adj
		if int(v2) == v+1:
			if int(v2) == 9:
				total += 1
			else:
				q.append((x,y,int(v2)))
