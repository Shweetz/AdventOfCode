with open("input.txt", "r") as f:
    lines = f.readlines()

total = 0

time = int(lines[0].split(":")[1].replace(" ", ""))
dist = int(lines[1].split(":")[1].replace(" ", ""))
print(time)
print(dist)

# try all button holding from 0 to max time
for j in range(time):
	if j * (time - j) > dist:
		total += 1

print(total)

# optimization idea:
# dichotomy to find S = shortest held time with better distance, then total = time + 1 - (S * 2)
# example in part 1: 7ms, S = 2ms, total = 4
