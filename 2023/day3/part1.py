from dataclasses import dataclass

@dataclass
class Gear:
    gear: str
    i: int
    j_s: int
    j_e: int


def search_symbol(gear):
    min_i = max(gear.i - 1, 0)
    max_i = min(gear.i + 2, len(lines) - 1)
    min_j = max(gear.j_s - 1, 0)
    max_j = min(gear.j_e + 1, len(lines[0]) - 1)
    for i in range (min_i, max_i):
        for j in range (min_j, max_j):
            if not lines[i][j].isdigit() and lines[i][j] not in [".", "\n"]:
                print(lines[i][j] + str(gear))
                # found symbol
                return True
    print(str(gear))
    return False

with open("input.txt", "r") as f:
# with open("input_small.txt", "r") as f:
    lines = f.readlines()

total = 0
    
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
                gear = Gear(line[start_j:j], i, start_j, j)
                #print(gear)
                if search_symbol(gear):
                    total += int(gear.gear)
                start_j = -1

print(total)
