def hash(str):
	value = 0
	for char in str:
		value += ord(char)
		value *= 17
		value %= 256
	return value

# script start
with open("input.txt", "r") as f:
	lines = f.readlines()

total = 0
steps = lines[0].split(",")

for step in steps:
	total += hash(step)
	
print(total)

# 1 line alternative
# print(sum(hash(step) for step in lines[0].split(",")))
