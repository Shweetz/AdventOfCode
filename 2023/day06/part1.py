with open("input.txt", "r") as f:
    lines = f.readlines()

total = 0

time = lines[0].split(":")[1].split()
dist = lines[1].split(":")[1].split()

for i in range(len(time)):
	time_i = int(time[i])
	dist_i = int(dist[i])
	faster_ways = 0

	# try all button holding from 0 to max time
	for j in range(time_i):
		if j * (time_i - j) > dist_i:
			faster_ways += 1

	if total == 0:
		total = faster_ways
	else:
		total *= faster_ways

print(total)
