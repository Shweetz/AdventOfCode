from queue import PriorityQueue
from time import time

from aoc_tools import *

def combo_value(operand, a, b, c):
	if operand <= 3: return operand
	if operand == 4: return a
	if operand == 5: return b
	if operand == 6: return c

def run(program, a):
	b = get_ints(lines[1])[0]
	c = get_ints(lines[2])[0]
	
	output = []

	i = 0
	while i < len(program):
		opcode, operand = program[i], program[i+1]
		combo = combo_value(operand, a, b, c)

		if opcode == 0:	a = int(a / pow (2, combo))
		if opcode == 1: b = b ^ operand
		if opcode == 2: b = combo % 8
		if opcode == 3 and a != 0: i = operand - 2
		if opcode == 4: b = b ^ c
		if opcode == 5: output.append(combo % 8)
		if opcode == 6: b = int(a / pow (2, combo))
		if opcode == 7: c = int(a / pow (2, combo))

		i += 2

	return output

t1 = time()
with open("2024/day17/input.txt", "r") as f:
	lines = [l.strip() for l in f.readlines()]

program = get_ints(lines[4])

# contains the possible values of a for the n first digits, matching the n last digits of program 
prev_digit_possibilities = [0]

q = PriorityQueue()
for digit in program:
	for prev in prev_digit_possibilities:
		for i in range(8):
			# add an octal digit i to the previously possible value of a
			q.put(prev*8 + i)

	# digit added so clear previous possibilities
	prev_digit_possibilities = []
	while not q.empty():
		a = q.get()
		output = run(program, a)
		n = len(output)
		# if the n digits of output don't match the last n digits of program, the possibility is ruled out
		if output == program[-n:]:
			prev_digit_possibilities.append(a)

total = prev_digit_possibilities[0]
print(f"{total = }")
print(f"Execution time: {(time() - t1):.3f}s")
assert total == 202972175280682

"""
Explanation

Let's decode the program (= output):
2,4,1,1,7,5,4,6,0,3,1,4,5,5,3,0
24 b = a % 8
11 b = b ^ 1 
75 c = a / 2**b
46 b = b ^ c
03 a = a / 2**3 (8)
14 b = b ^ 4
55 print(b % 8)
30 loop until a == 0

So every loop, a is divided by 8 until it reaches 0, than the program stops
Since the output contains 16 digits, this means 8**15 <= answer < 8**16
It also means that the first octal digit of a is the only part used to calculate the last digit of output
Reversing the output to find the input register a is not possible (because some operations create data loss)
Instead, run the program with every first digit of a (octal, so 0 to 7), and keep only the one(s) giving the correct output (the last digit of output, here "0")
Then, run the program with every second digit of a alongside the possible first ones, and keep only the one(s) matching the last 2 digits of output
So if the first possible digit can be 4 or 6, then there are 16 possibilities for second digit: 40 to 47 and 60 to 67, keep only the ones outputting 30
And so on until the end.

Here: answer (= register a) = 202972175280682
in octal:
output = 2411754603145530
answer = 5611504432025052
For the 1st digit, try with a =    0 to    7, looking for   0 only gives a = 5 as possibility
For the 2nd digit, try with a =   50 to   57, looking for  30 only gives a = 56 as possibility
For the 3rd digit, try with a =  560 to  567, looking for 530 gives a = 560 and a = 561 as possibilities
For the 4th digit, try with a = 5600 to 5607 and 5610 to 5617...

Unused method but can be handy:
def list_to_octal(list):
	octal = 0
	for i in list:
		octal *= 8
		octal += i
	return octal
"""
