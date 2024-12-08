# transpose lines and columns
l1, l2 = zip(*[line.split() for line in lines])

# enumerate on line split
for i, split in enumerate(line.split()):
	pass

# timing execution
from time import time

t1 = time()

print(f"Execution time: {(time() - t1):.3f}s")

