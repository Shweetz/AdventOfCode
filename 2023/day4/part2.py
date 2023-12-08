with open("input.txt", "r") as f:
    lines = f.readlines()

total = 0

# Store the amount of copies of each card
cards = []
for i in range(len(lines)):
    cards.append(1)
    
for i, line in enumerate(lines):
    # Transform line in 2 groups of strings containing ints
    win_line = 0
    line = line.split(":")[1].replace("\n", "")
    winning_s, playing_s = line.split("|")
    winning_s = winning_s.split(" ")
    playing_s = playing_s.split(" ")

    # Transform playing numbers strings in ints
    playing = []
    for p in playing_s:
        try:
            playing.append(int(p))
        except:
            pass
    
    # Check winning numbers for a match
    for w in winning_s:
        try:
            w = int(w)
            if w in playing:
                # Winning number found
                win_line += 1
        except:
            pass
    
    # Add X copies for N next cards, where X is amount of copies of current card and N is amount of winning numbers
    for j in range(i + 1, i + 1 + win_line):
        cards[j] += cards[i]

    total += cards[i]

print(total)
