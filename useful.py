from queue import PriorityQueue
from sympy import symbols, Eq, solve

class Grid: pass
lines = []

# ---------------------------------------

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

# priority queue
def move(): pass
di = 0
visited = set()

q = PriorityQueue()
q.put((0, (x,y), di))

while not q.empty():
	score, pos, di = q.get()

	if g.g[pos] == "#":
		continue

	if score >= best:
		# worse than a path to the end
		continue
	
	if score >= visited[(pos, di)]:
		# worse than another path to this tile/direction
		continue
	else:
		# new best score from start to here
		visited[(pos, di)] = score

	if g.g[pos] == "E":
		# reached finish
		if score < best:
			best = score

	else:
		# take a new step to neighbors: same direction, right, left
		for new_di in [di, di+1, di-1]:
			new_di = new_di % 4
			
			new_score = score + 1
			if new_di != di:
				# change direction = 1000 pts
				new_score += 1000

			new_pos = move(pos, new_di)
			q.put((new_score, new_pos, new_di))
			
# linear equations with sympy
ax,bx,px,ay,by,py = 0
a, b = symbols('a b', integer=True) # only int solutions
eq1 = Eq(ax * a + bx * b, px)
eq2 = Eq(ay * a + by * b, py)
sol = solve((eq1, eq2),(a, b))
