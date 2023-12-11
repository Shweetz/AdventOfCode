with open("input.txt", "r") as f:
    lines = f.readlines()

def is_only_zeroes(seq):
	for n in seq:
		if n != 0:
			return False
	return True

total = 0
for line in lines:
	# for each line, create a list of sequences
	seqs = []
	# 1st sequence is input line with str -> int
	seqs.append([int(x) for x in line.split()])

	# create a new sequence until the last one is all zeroes
	while not is_only_zeroes(seqs[-1]):
		last_seq = seqs[-1]
		new_seq = []
		for n in range(1, len(last_seq)): 
			new_seq.append(last_seq[n] - last_seq[n-1])
		seqs.append(new_seq)

	# calculate the last value in all sequences, starting from the last sequence
	last_value = 0
	for seq in seqs[::-1]:
		last_value += seq[-1]
		# seq.append(last_value)
	
	total += last_value
	
print(total)
