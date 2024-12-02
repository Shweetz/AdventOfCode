# works but a bit complicated

from dataclasses import dataclass

@dataclass
class Hand:
    hand: str
    bid: int


with open("input.txt", "r") as f:
    lines = f.readlines()

total = 0

hand_types = {}
hand_types["five"] = []
hand_types["four"] = []
hand_types["full"] = []
hand_types["thre"] = []
hand_types["twop"] = []
hand_types["onep"] = []
hand_types["high"] = []

for line in lines:
	hand, bid = line.split()
	curHand = Hand(hand, int(bid))

	# count card occurences
	unique_cards = list(dict.fromkeys(hand))
	card_counts = []
	for unique_card in unique_cards:
		card_counts.append(hand.count(unique_card))
	
	# sort hands by type
	card_counts.sort(reverse=True)
	if   card_counts == [5]:          hand_types["five"].append(curHand)
	elif card_counts == [4, 1]:       hand_types["four"].append(curHand)
	elif card_counts == [3, 2]:       hand_types["full"].append(curHand)
	elif card_counts == [3, 1, 1]:    hand_types["thre"].append(curHand)
	elif card_counts == [2, 2, 1]:    hand_types["twop"].append(curHand)
	elif card_counts == [2, 1, 1, 1]: hand_types["onep"].append(curHand)
	else:                             hand_types["high"].append(curHand)

current_rank = len(lines)
for hand_type in hand_types:
	# replace letters in strength order (letters are already stronger than digits)
	for i, hand in enumerate(hand_types[hand_type]):
		hand_types[hand_type][i].hand = hand.hand.replace("T", "B")
		hand_types[hand_type][i].hand = hand.hand.replace("J", "C")
		hand_types[hand_type][i].hand = hand.hand.replace("Q", "D")
		hand_types[hand_type][i].hand = hand.hand.replace("K", "E")
		hand_types[hand_type][i].hand = hand.hand.replace("A", "F")
	
	# sort hands
	hand_types[hand_type].sort(key=lambda hand: hand.hand, reverse=True)
	
	# give rank and calculate
	for hand in hand_types[hand_type]:
		total += current_rank * hand.bid
		current_rank -= 1

print(total)
