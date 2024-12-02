from time import time

# return shortest held time with better distance than target dist
def binary_search(race_time, dist):
	min = 0
	max = race_time // 2

	while min < max - 1:
		m = (max + min) // 2
		# print(min, max, m)

		# special case, only
		if min == max - 1:
			m += 1

		d = m * (race_time - m)

		if d > dist:
			# better than target
			max = m
		else:
			min = m
	
	# here min == max or min == max - 1
	return max

# script start
t1 = time()
with open("input.txt", "r") as f:
    lines = f.readlines()

total = 0

race_time = int(lines[0].split(":")[1].replace(" ", ""))
dist = int(lines[1].split(":")[1].replace(" ", ""))
print(race_time)
print(dist)

# binary search to find S = shortest held time with better distance
min_held_time_success = binary_search(race_time, dist)
print(f"{min_held_time_success=}")

# total = T + 1 - (S * 2) with T = race_time
total = race_time + 1 - (min_held_time_success * 2)

print(total)
print(f"Execution time: {(time() - t1):.3f}s")
assert total == 33875953

# explanation:
# T+1 is the number of ways to play the race counting from "0 ms" to "race_time ms"
# S   is the number of ways to lose the race counting from "0 ms" to "S ms" AND from "race_time ms" to "(race_time - S) ms"

# example in input_s: race_time = 7ms, S = 2ms, total = 4
# time: 0 1 2 3 4 5 6 7
# win : 0 0 1 1 1 1 0 0

# other example: 8 + 1 - (2 * 2) = 5
# time: 0 1 2 3 4 5 6 7 8
# win : 0 0 1 1 1 1 1 0 0
