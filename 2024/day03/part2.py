import re

with open("2024/day03/input1.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total = 0

lines = "-".join(lines)

# don = lines.find("don't()")
# while don != -1:
# 	# print(f"{lines=}")
# 	do = don + lines[don:].find("do()")
# 	if do != don - 1:
# 		lines = lines[:don] + lines[do:]
# 	else:
# 		lines = lines[:don]
# 	don = lines.find("don't()")
# 	# print(f"{don=}")
# print(f"{lines=}")

lines = re.findall(r"(.*)don't\(\).*(do\(\))?", lines)
print(f"{lines=}")
matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", lines)
total = sum(int(a)*int(b) for a,b in matches)

print(f"{total = }")
assert total == 63013756
