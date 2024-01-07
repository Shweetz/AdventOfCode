from time import time

from dataclasses import dataclass, field
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


def receive_signal(sender, receiver, signal):
	global low_signals
	global high_signals

	if signal == "low":
		low_signals += 1
	else:
		high_signals += 1

	if receiver == "broadcast":
		for output in broadcast_outputs:
			queue.put((receiver, output, signal))
			# print(receiver + " -" + signal + "-> " + output)
	
	elif receiver in flip_dict:
		if signal == "low":
			flip = flips[flip_dict[receiver]]
			send_type = "low" if flip.is_on else "high"
			flip.is_on = not flip.is_on

			for output in flip.outputs:
				queue.put((receiver, output, send_type))
				# print(receiver + " -" + send_type + "-> " + output)
				
	elif receiver in conj_dict:
		conj = conjs[conj_dict[receiver]]
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

flips = []
conjs = []
flip_dict = {} # dict of flip indexes
conj_dict = {} # dict of conj indexes
broadcast_outputs = []
low_signals = 0
high_signals = 0
queue = Queue()

for line in lines:
	name, outputs = line.split(" -> ")
	outputs = outputs.split(", ")

	if name == "broadcaster":
		broadcast_outputs = outputs
		continue

	if line[0] == "%":
		flips.append(Flip(name[1:], outputs))
	else:
		conjs.append(Conj(name[1:], outputs))

# add connected_inputs in the conjs from the outputs of conjs and flips
for conj_i in conjs:
	for output in conj_i.outputs:
		for i, conj_o in enumerate(conjs):
			if conjs[i].name == output:
				conjs[i].connected_inputs[conj_i.name] = False

for flip_i in flips:
	for output in flip_i.outputs:
		for i, conj_o in enumerate(conjs):
			if conjs[i].name == output:
				conjs[i].connected_inputs[flip_i.name] = False

# fill flip_dict and conj_dict
for i, flip in enumerate(flips):
	flip_dict[flip.name] = i
	# print(flip)

for i, conj in enumerate(conjs):
	conj_dict[conj.name] = i
	# print(conj)

# push the button until state is back in start position or reach 1000 pushes
back_in_start_position = False
button_count = 0

while not back_in_start_position and button_count < 1000:
	button_count += 1

	queue.put(("button", "broadcast", "low"))
	# print("button -low-> broadcaster")

	while not queue.empty():
		receive_signal(*queue.get())
	
	# back_in_start_position = all flips are off and all conjs remember only low pulses
	back_in_start_position = True

	for flip in flips:
		if flip.is_on:
			back_in_start_position = False

	for conj in conjs:
		if True in conj.connected_inputs.values():
			back_in_start_position = False

print(f"{low_signals=}")
print(f"{high_signals=}")
print(int(low_signals * 1000 / button_count * high_signals * 1000 / button_count))
print(f"Execution time: {(time() - t1):.3f}s")
