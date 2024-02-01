from time import time

from queue import PriorityQueue
import sys

def take_step(steps, map_steps, poss, x, y):
	# print(x, y)
		
	if steps > map_steps:
		return
	
	steps += 1
	l = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
	for p in l:
		# print(grid[p])
		if p in grid and p not in poss:
			if steps % 2 == map_steps % 2:
				poss.add(p)

			queue.put((steps, map_steps, poss, *p))

# explore the map from a start pos in a number of steps
def explore(start, map_steps):
	# special case
	if map_steps == 0:
		return 1
	
	# regular case
	poss = set()

	queue.put((0, map_steps, poss, *start))

	while not queue.empty():
		take_step(*queue.get())
	
	# print(poss)
	return len(poss)

# script start
t1 = time()
with open("input.txt", "r") as f:
	lines = [line.strip() for line in f.readlines()]

nb_steps = 26501365
if len(sys.argv) > 1:
	nb_steps = int(sys.argv[1])
size = len(lines)
grid = {}
queue = PriorityQueue()
total = 0

for i, line in enumerate(lines):
	for j, char in enumerate(line):
		if char == "." or char == "S":
			grid[(i, j)] = char

###############
# MAP OF MAPS #
###############
# Here's how i represent the maps:
# ....E....
# ...CeC...
# ..CcFcC..
# .CcFfFcC.
# EeFfFfFeE
# .CcFfFcC.
# ..CcFcC..
# ...CeC...
# ....E....
#
# F = full map (fully explored)
# E = edge map
# C = corner map
# higher case letters represent one parity (outer maps), lower case letters represent the other parity (inner maps)
# there are 2 parities even for E and C because new maps can be reached before the ones with reversed parity are full
# every step away from the center, parity is reversed, there are still 4 edge maps but 4 more corner maps than before
# there are outer and inner maps maps, because it takes less steps to reach a new edge map than fully explore the current one
# exploring from center goes in this order:
# 1. find a new map              -> outer map
# 2. find another new map        -> new map is outer map, old outer map is inner map
# 3. fully explore the inner map -> inner map is full map, outer map stays outer
# 4. find another new map        -> new map is outer map, old outer map is inner map, full map stays
# Repeat from 3.

#######################
# IN MAP LOCALIZATION #
#######################
# size 131, center = (66, 66), indexing start at 0 => center = (65, 65), bottom right = (130, 130)
full = size - 1  # 130
half = full // 2 # 65

center = (half, half)

#############
# FULL MAPS #
#############
# count maps full, separating the ones with the same parity than center map, and the ones with the other parity
parity_with_center = True
nb_maps_full = {True : 0, False: 0}

steps_left = nb_steps - 130 # 130 steps = center full
nb_maps_in_layer = 0
while steps_left >= 131:
	# 4 more maps around center with reversed parity every time
	# center is alone, expand there are 4 maps with reverse parity, then 8 maps with center parity, then 12...
	parity_with_center = not parity_with_center
	nb_maps_in_layer += 4
	nb_maps_full[parity_with_center] += nb_maps_in_layer

	steps_left -= 131

last_layer_maps_full_nb = nb_maps_in_layer
last_layer_maps_full_parity = parity_with_center

# compute possibilities in map full with both parities
poss_map_full_center_parity = explore(center, nb_steps)
poss_map_full_other_parity  = explore(center, nb_steps+1)

total += nb_maps_full[True ] * poss_map_full_center_parity
total += nb_maps_full[False] * poss_map_full_other_parity
print(total, "full maps")

#################
# NOT FULL MAPS #
#################

# center map
if nb_steps >= 129:
	# technically a bug because it can take more than 129 steps to fully explore center, but it's an optimization
	total += poss_map_full_center_parity

else:
	total += explore(center, nb_steps)
print(total, "+ center")

# edges, up/down/left/right
starts = [(full, half), # map up, go up 66 steps from center, start bottom of the most up map reachable
		  (0   , half), # map down
		  (half, full), # map left
		  (half, 0   )] # map right

# outer edge maps (OEM)
oem_steps = nb_steps - (half + 1) # remove the number of steps to reach an edge map (66)
if oem_steps > 0:
	oem_steps %= size

for start in starts:
	total += explore(start, oem_steps)

# inner edge maps (IEM)
iem_steps = nb_steps - (half + 1) - size # also remove the map size to add it back after modulo
if iem_steps > 0:
	iem_steps %= size
iem_steps += size

if full < iem_steps < full + half:
	# only add those if inner maps are not counted in full maps already
	for start in starts:
		total += explore(start, iem_steps)
print(total, "+ edge")

# corners
starts = [(full, full), # map top left, go up 66 steps + left 66 steps from center, start bottom right
		  (full, 0   ), # map top right
		  (0   , full), # map bottom left
		  (0   , 0   )] # map bottom right

# inner corner maps have same count buf diff parity from last layer full because it's next layer minus the 4 edge
corner_inner_maps_nb = last_layer_maps_full_nb

# outer corner maps are just the next layer
corner_outer_maps_nb = corner_inner_maps_nb + 4

# outer corner maps (OCM)
ocm_steps = nb_steps - full
if ocm_steps > 0:
	ocm_steps %= size
ocm_steps += -2

for start in starts:
	outer_poss = explore(start, ocm_steps)
	total += outer_poss * (corner_outer_maps_nb // 4)

# inner corner maps (ICM)
icm_steps = nb_steps - full - size
if icm_steps > 0:
	icm_steps %= size
icm_steps += -2 + size

for start in starts:
	inner_poss = explore(start, icm_steps)
	total += inner_poss * (corner_inner_maps_nb // 4)

print(total, "+ corner")
with open("mass_output.txt", "a") as f:
	f.write(str(nb_steps) + " " + str(total) + "\n")

print(f"Execution time: {(time() - t1):.3f}s")
