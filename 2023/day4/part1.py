with open("input.txt", "r") as f:
# with open("input_s.txt", "r") as f:
    lines = f.readlines()

total = 0

for line in lines:
    # Transform line in 2 groups of strings containing ints
    score_line = 0
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
                if score_line == 0:
                    score_line = 1
                else:
                    score_line *= 2
        except:
            pass
            
    total += score_line

    print(playing)

print(total)