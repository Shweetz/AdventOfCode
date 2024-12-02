with open("input.txt", "r") as f:
    lines = f.readlines()

total = 0

for line in lines:
    first = None
    for char in line:
        if char.isdigit():
            if first is None: # first digit found
                first = int(char)
            last = int(char)
    
    total += first * 10 + last

print(total)
