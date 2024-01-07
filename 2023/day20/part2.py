from time import time

from dataclasses import dataclass, field
import math
from queue import Queue

@dataclass
class Flip:
	name : str
	outputs : set = field(default_factory=set)
	is_on : bool = False

@dataclass
class Conj:
	name : str
	outputs : set = field(default_factory=set)
	connected_inputs : dict = field(default_factory=dict) # False = low pulse

@dataclass
class Glob:
	low_signals : int = 0
	high_signals : int = 0


def receive_signal(sender, receiver, signal):
	# print(sender, receiver, signal)
	
	if (receiver, signal) == (rx_input, "high"):
		# rx_input received a high signal, indicating the periodicity of 1 of the 4 cycles, store that info
		rx_input_inputs[sender] = button_count

	if signal == "low":
		g.low_signals += 1
	else:
		g.high_signals += 1

	if receiver == "broadcast":
		for output in broadcast_outputs:
			queue.put((receiver, output, signal))
			# print(receiver + " -" + signal + "-> " + output)
	
	elif receiver in flips.keys():
		if signal == "low":
			flip = flips[receiver]
			send_type = "low" if flip.is_on else "high"
			flip.is_on = not flip.is_on

			for output in flip.outputs:
				queue.put((receiver, output, send_type))
				# print(receiver + " -" + send_type + "-> " + output)
				
	elif receiver in conjs.keys():
		conj = conjs[receiver]

		# remember if last signal is high
		conj.connected_inputs[sender] = (signal == "high")
		
		# send low only if all inputs sent high
		send_type = "high" if False in conj.connected_inputs.values() else "low"

		for output in conj.outputs:
			queue.put((receiver, output, send_type))
			# print(receiver + " -" + send_type + "-> " + output)

# script start
t1 = time()
with open("input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

flips = {}
conjs = {}
broadcast_outputs = []
g = Glob()
queue = Queue()

for line in lines:
	name, outputs = line.split(" -> ")
	outputs = outputs.split(", ")

	if name == "broadcaster":
		broadcast_outputs = outputs
		continue

	if line[0] == "%":
		flips[name[1:]] = Flip(name[1:], outputs)
	else:
		conjs[name[1:]] = Conj(name[1:], outputs)

# add connected_inputs in the conjs from the outputs of conjs and flips
for conj_i in conjs.values():
	for output in conj_i.outputs:
		if output in conjs.keys():
			conjs[output].connected_inputs[conj_i.name] = False

for flip_i in flips.values():
	for output in flip_i.outputs:
		if output in conjs.keys():
			conjs[output].connected_inputs[flip_i.name] = False

# push the button until rx receives a single low pulse
# but it takes way too long, actually rx is only powered though qb (conj), which needs to remember only high pulses
for conj_i in conjs.values():
	if "rx" in conj_i.outputs:
		rx_input = conj_i.name

# qb inputs are 4 conjs: qb <- kv, jg, rz, mr
rx_input_inputs = {}
for conj in conjs[rx_input].connected_inputs.keys():
	# prepare the dict to store the periodicity of these 4 conjs, they are 4 independent cycles
	rx_input_inputs[conj] = 0

button_count = 0

while 0 in rx_input_inputs.values():
	button_count += 1

	queue.put(("button", "broadcast", "low"))
	# print("button -low-> broadcaster")

	while not queue.empty():
		receive_signal(*queue.get())

print(button_count)

# lowest common multiplicator for the 4 cycles
print(math.lcm(*rx_input_inputs.values()))
print(f"Execution time: {(time() - t1):.3f}s")
