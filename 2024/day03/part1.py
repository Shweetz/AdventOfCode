import re

with open("2024/day03/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total = 0

for line in lines:
	
	matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
	print(f"{matches=}")

	total += sum(int(a)*int(b) for a,b in matches)

print(f"{total = }")
assert total == 189527826


# 2-line solution
# import re;
# with open("2024/day03/input.txt", "r") as f: print(f"{sum(int(a)*int(b) for a,b in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", "-".join([l.strip() for l in f.readlines()]))) = }")
# assert total == 189527826
