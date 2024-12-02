with open("input.txt", "r") as f:
    lines = f.readlines()

total = 0

hand_types = { "five": [], "four": [], "full": [], "thre": [], "twop": [], "onep": [], "high": [] }
bids = {}

for line in lines:
	hand, bid = line.split()
	
	# replace letters in ASCII strength order (letters are already stronger than digits)
	hand = hand.replace("T", "B")
	hand = hand.replace("J", "0") # joker weaker than 2
	hand = hand.replace("Q", "D")
	hand = hand.replace("K", "E")
	hand = hand.replace("A", "F")
	bids[hand] = int(bid)

	# count card occurences
	unique_cards = list(dict.fromkeys(hand))
	card_counts = []
	joker_count = 0
	for unique_card in unique_cards:
		if unique_card == "0":
			joker_count = hand.count(unique_card)
		else:
			card_counts.append(hand.count(unique_card))
	
	# add joker occurences to highest count card
	card_counts.sort(reverse=True)
	if len(card_counts) == 0:
		# 5 jokers in hand
		card_counts = [5]
	else:
		card_counts[0] += joker_count

	# sort hands by type
	if   card_counts == [5]:          hand_types["five"].append(hand)
	elif card_counts == [4, 1]:       hand_types["four"].append(hand)
	elif card_counts == [3, 2]:       hand_types["full"].append(hand)
	elif card_counts == [3, 1, 1]:    hand_types["thre"].append(hand)
	elif card_counts == [2, 2, 1]:    hand_types["twop"].append(hand)
	elif card_counts == [2, 1, 1, 1]: hand_types["onep"].append(hand)
	else:                             hand_types["high"].append(hand)

# rank strongest to weakest
current_rank = len(lines)
for key, hands in hand_types.items():	
	# sort hands
	hands.sort(reverse=True)
	
	# multiply rank and bid
	for hand in hands:
		total += current_rank * bids[hand]
		current_rank -= 1

print(total)
