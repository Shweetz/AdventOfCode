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
can_dis = set()

# read list of bricks and give them an id
for i, line in enumerate(lines):
	# sort z1/z2 ?
	values = line.replace("~", ",").split(",")
	values = [int(v) for v in values]
	raw_bricks.append(Brick(*values, i))

# sort bricks from lowest to highest, a brick can only be supported by a brick that is fully lower
raw_bricks.sort(key=lambda b:b.z1)

# make bricks fall, write their final position and the bricks supporting the current one
for brick in raw_bricks:
	bricks[len(bricks)] = brick
	fall(brick)

# if a brick is supported by only 1 brick, then the supporting brick cannot be disintegrated
can_dis = set(bricks) # bricks.keys() to set
for brick in bricks.values():
	if len(brick.supported_by) == 1:
		# 1 support = remove it from can_disintegrate
		for supp in brick.supported_by:
			if supp in can_dis:
				can_dis.remove(supp)

print(len(can_dis))
print(f"Execution time: {(time() - t1):.3f}s")
