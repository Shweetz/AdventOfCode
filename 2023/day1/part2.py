from dataclasses import dataclass

with open("input.txt", "r") as f:
    lines = f.readlines()

total = 0

nums_str = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for i, line in enumerate(lines):
    first = None
    first_j = 10
    # look for digits
    for j, char in enumerate(line):
        if char.isdigit():
            if first is None:
                first = int(char)
                first_j = j
            last = int(char)
            last_j = j
    
    # look for strings better than digits
    for n, num_str in enumerate(nums_str):
        if line.find(num_str) == -1:
            # string not found
            continue
        if line.find(num_str) < first_j:
            # earlier than first
            first = n+1
            first_j = line.find(num_str)
        if line.rfind(num_str) > last_j:
            # later than last
            last = n+1
            last_j = line.rfind(num_str)
        
    total += first * 10 + last

print(total)
