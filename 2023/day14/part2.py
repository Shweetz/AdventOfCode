# cache not needed once you catch the infinitely repeating pattern

# transpose input 90° clockwise, so old north is now east
def transpose(lines):
	rows = []
	for i in range(len(lines[0])):
		rows.append([lines[x][i] for x in range(len(lines))][::-1])
	return rows

# move rocks in the row (to the east)
def move_rocks(row):
	done = False
	while not done:
		done = True
		for j in range(len(row)-1):
			# swap "O" and "." (very slow)
			if row[j] == "O" and row[j+1] == ".":
				row[j], row[j+1] = row[j+1], row[j]
				done = False
	return row

# script start
with open("input.txt", "r") as f:
	lines = f.readlines()

total_pushes = 1000000000 * 4
rows = [line.strip() for line in lines]
board_after_push = []
final_board = []
total = 0

for push_count in range(total_pushes):
	# transpose input 90° clockwise, so old north is now east
	rows = transpose(rows)

	# move rocks in each row
	for i, row in enumerate(rows):
		rows[i] = move_rocks(row)
	
	for i, board in enumerate(board_after_push):
		if rows == board:
			# the current board has been reached before: repeating pattern of length "period"
			period = len(board_after_push) - i

			# figure out how many pushes in the pattern are needed to reach "total_pushes"
			remaining_pushes = (total_pushes - push_count) % period
			
			# figure out which board in the pattern would be hitting "total_pushes"
			final_board = board_after_push[i + remaining_pushes - 1]
			break
	
	if final_board:
		break

	board_after_push.append(rows)

# transpose to ease load calculation
final_board = transpose(final_board)

# calculate load (more east = more load)
for row in final_board:
	for i, char in enumerate(row):
		if char == "O":
			# 1 point for index 0 (full west)
			total += i + 1
	
print(total)
