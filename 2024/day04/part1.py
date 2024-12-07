from aoc_tools import *

with open("2024/day04/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

g = Grid()
g.read(lines)

# find XMAS horizontally, vertically and diagonally
total = len(g.find("XMAS", 2))

print(f"{total=}")
assert total == 2434
