from time import time

from aoc_tools import *

def combo_value(operand):
	if operand <= 3: return operand
	if operand == 4: return a
	if operand == 5: return b
	if operand == 6: return c

t1 = time()
with open("2024/day17/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

total = []

a = get_ints(lines[0])[0]
b = get_ints(lines[1])[0]
c = get_ints(lines[2])[0]
program = get_ints(lines[4])

i = 0
while i < len(program):
	opcode, operand = program[i], program[i+1]
	combo = combo_value(operand)

	if opcode == 0:	a = int(a / 2 ** combo)
	if opcode == 1: b = b ^ operand
	if opcode == 2: b = combo % 8
	if opcode == 3 and a != 0: i = operand - 2
	if opcode == 4: b = b ^ c
	if opcode == 5: total.append(combo % 8)
	if opcode == 6: b = int(a / 2 ** combo)
	if opcode == 7: c = int(a / 2 ** combo)

	i += 2

total = ",".join(map(str,total))
# tot = ",".join(str(i) for i in total) # equivalent
print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")
assert total == "7,3,0,5,7,1,4,0,5"
