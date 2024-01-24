from time import time

from dataclasses import dataclass, field

with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

@dataclass
class Brick:
	x1 : int
	y1 : int
	z1 : int
	x2 : int
	y2 : int
	z2 : int
	id : int
	supported_by : set = field(default_factory=set) # this is supported by other bricks


def stabilize(brick):
	for x in range(brick.x1, brick.x2 + 1):
		for y in range(brick.y1, brick.y2 + 1):
			for z in range(brick.z1, brick.z2 + 1):
				occupied[(x, y, z)] = brick.id

def fall(brick):
	can_lower = brick.z1 > 1
	while can_lower:
		# try 1 position lower
		for x in range(brick.x1, brick.x2 + 1):
			for y in range(brick.y1, brick.y2 + 1):
				for z in range(brick.z1 - 1, brick.z2):
					if (x, y, z) in occupied:
						# hit another brick: it supports the current brick
						# store the bricks this brick is supported by
						brick.supported_by.add(occupied[(x, y, z)])

						# store bricks supporting this brick
						# bricks[occupied[(x, y, z)]].supports.add(brick.id)
		
		if brick.supported_by:
			can_lower = False
		else:
			brick.z1 -= 1
			brick.z2 -= 1
			can_lower = brick.z1 > 1

	# brick is at final position, fill "occupied"
	stabilize(brick)

# script start
t1 = time()
raw_bricks = []
bricks = {} # 0 = Brick() - raw_bricks sorted, the key in dict is their index for "occupied"
occupied = {} # (1, 1, 1) = 2
total = 0

# read list of bricks and give them an id
for i, line in enumerate(lines):
	# sort z1/z2 not needed because z1 <= z2
	values = line.replace("~", ",").split(",")
	values = [int(v) for v in values]
	raw_bricks.append(Brick(*values, i))

# sort bricks from lowest to highest, a brick can only be supported by a brick that is fully lower
raw_bricks.sort(key=lambda b:b.z1)

# make bricks fall, write their final position and the bricks supporting the current one
for brick in raw_bricks:
	brick.id = len(bricks) # order bricks
	bricks[brick.id] = brick
	fall(brick)

# disintegrate a brick, check how many fall
# a brick disintegrating or falling only affects the bricks after it
for i, brick in bricks.items():
	removed_bricks = set()
	removed_bricks.add(i)
	for j, brick2 in bricks.items():
		if j <= i:
			# only bricks after i can fall
			continue
		if not brick2.supported_by:
			# brick not supported => already on ground => cannot fall
			continue
	
		# the other brick is only falling if all its supports have fallen (or original disintegrate)
		falling = True
		for supp in brick2.supported_by:
			if supp not in removed_bricks:
				falling = False
				break
		
		if falling:
			removed_bricks.add(j)
			
	total += len(removed_bricks) - 1 # disintegrated brick doesn't count as "fallen"

print(total)
print(f"Execution time: {(time() - t1):.3f}s")
