from dataclasses import dataclass

@dataclass
class Range:
    start: int
    end: int
    diff: int = 0


with open("input.txt", "r") as f:
	lines = f.readlines()

lowest_location = None

seeds_str = lines[0].replace("seeds: ", "").split(" ")

# create maps for every transition src to dst (seed-to-soil, soil-to-fertilizer ...)
maps = []
state = -1
for line in lines[2:]:
	if line.strip() == "":
		continue

	elif "map" in line:
		# reached next map
		state += 1
		maps.append([])
		continue
	
	else:
		dst, src, size = line.split(" ")
		# store src_start, src_end, diff
		maps[state].append(Range(int(src), int(src) + int(size), int(dst) - int(src)))

# create list of src ranges (seed ranges at the start)
src_ranges = []
x = range(0, len(seeds_str), 2)
for i in x:
	src_ranges.append(Range(int(seeds_str[i]), int(seeds_str[i]) + int(seeds_str[i+1])))

# for every transition src to dst (seed-to-soil, soil-to-fertilizer ...)
for map_state in maps:
	dst_ranges = []

	# create a sorted list of map range split limits aka points to split src ranges
	# example for input_s seed-to-soil map: 50, 98, 100
	map_split_points = []
	for map_range in map_state:
		map_split_points.append(map_range.start)
		map_split_points.append(map_range.end)
	map_split_points.sort()
	map_split_points = list(dict.fromkeys(map_split_points)) # remove duplicates

	# step 1: split every src range at every split point and store in dst_ranges
	# example for [(20, 30), (40, 60), (95, 103)] => [(20, 30), (40, 50), (50, 60), (95, 98), (98, 100), (100, 103)] 
	for src_range in src_ranges:
		split_start = src_range.start
		for split_point in map_split_points:
			if split_start < split_point < src_range.end:
				dst_ranges.append(Range(split_start, split_point))
				split_start = split_point
			
		dst_ranges.append(Range(split_start, src_range.end))

	# step 2: apply the diffs to the properly splitted dst ranges
	for dst_range in dst_ranges:
		for map_range in map_state:
			if map_range.start <= dst_range.start < map_range.end:
				dst_range.start += map_range.diff
				dst_range.end += map_range.diff
				break
		# do nothing if dst_range isn't matched

	# prepare next transition
	src_ranges = dst_ranges

# dst_ranges contains final location ranges
lowest_location = min([location.start for location in dst_ranges])

print(lowest_location)
