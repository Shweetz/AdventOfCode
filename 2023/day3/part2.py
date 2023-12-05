from dataclasses import dataclass

@dataclass
class Gear:
    gear: str
    i: int
    j_s: int
    j_e: int

@dataclass
class Star:
    i: int
    j: int


def find_adj(star):
    adj = []
    for gear in gears:
        min_i = max(gear.i - 1, 0)
        max_i = min(gear.i + 2, len(lines) - 1)
        min_j = max(gear.j_s - 1, 0)
        max_j = min(gear.j_e + 1, len(lines[0]) - 1)
        if min_i <= star.i < max_i and min_j <= star.j < max_j:
            adj.append(gear)
    return adj

with open("input.txt", "r") as f:
# with open("input_small.txt", "r") as f:
    lines = f.readlines()

total = 0
gears = []
stars = []
    
for i, line in enumerate(lines):
    start_j = -1
    for j, char in enumerate(line):
        #print(line.split("."))
        if char.isdigit():
            #print(char)
            if start_j == -1:
                start_j = j
        else:
            if start_j != -1:
                gears.append(Gear(line[start_j:j], i, start_j, j))
                
                start_j = -1

        if (char == "*"):
            stars.append(Star(i, j))

for star in stars:
    adj_nums = find_adj(star)
    if len(adj_nums) == 2:
        total += int(adj_nums[0].gear) * int(adj_nums[1].gear)

print(total)