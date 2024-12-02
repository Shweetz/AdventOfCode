from time import time

# script start
t1 = time()
with open("input.txt", "r") as f:
    lines = f.readlines()

total = 0

race_time = int(lines[0].split(":")[1].replace(" ", ""))
dist = int(lines[1].split(":")[1].replace(" ", ""))
print(race_time)
print(dist)

# try all button holding from 0 to max time
for j in range(race_time):
	if j * (race_time - j) > dist:
		total += 1

print(total)
print(f"Execution time: {(time() - t1):.3f}s")
assert total == 33875953
