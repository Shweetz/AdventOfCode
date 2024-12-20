from collections import defaultdict
import math
import re
from queue import PriorityQueue
import sys

# strings
def spl(s, seps):
	"""Split a string over multiple separators (every char in 'seps')"""
	for sep in seps:
		s = s.replace(sep, seps[-1])
	return s.split(seps[-1])

def rem(s, seps):
	"""Remove chars from a string"""
	return "".join([c for c in s if c not in seps])

# sets & lists
def intersect(*lists):
	"""Return a list of the intersection of lists"""
	s = set(lists[0])
	for l in lists[1:]:
		s = s & set(l)
	return list(s)

# regex
def get_digits(s):
	"""Return the string without non-digit chars"""
	return "".join([char for char in s if char.isdigit()])

def get_ints(s):
	"""Return the list of the ints (including negative) in a string"""
	return [int(d) for d in re.findall(r"-?\d+", s)]
	# return [int(d) for d in re.findall(r"\d+", s)]

def get_nums(s):
	"""Return the list of the numbers (including negative and decimal) in a string"""
	return [float(d) for d in re.findall(r"-?\d*\.?\d+", s)]

def get_words(s):
	"""Return the list of the words in a string"""
	return [w for w in re.findall(r"\w+", s)]

def get_ints_pos(s):
	"""Return the list of the ints in a string, formatted as tuples [(int, pos), ...]"""
	return [(int(m.group(0)), m.start()) for m in re.finditer(r"\d+", s)]

def sub(s):
	"""Replace a substring with nothing in a string"""
	return re.sub(r"\n", "", s)

# grid
class Grid:
	g = {}
	lines = []
	h = 0
	w = 0
	L, LU, U, RU, R, RD, D, LD = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
	dirs = [L, U, R, D]

	def read(self, lines):
		"""Fills self.g with dict key as 2D tuple"""
		self.lines = lines
		self.h = len(self.lines)
		self.w = len(self.lines[0])
		for x, line in enumerate(lines):
			for y, c in enumerate(line):
				self.g[(x, y)] = c

	def build(self, height, width, pos_list):
		self.h = height
		self.w = width
		for x in range(height):
			for y in range(width):
				self.g[(x, y)] = "."

		for (x,y) in pos_list:
			self.g[(x, y)] = "#"

	def grid_to_lines(self):
		self.lines = []
		self.h = 0
		self.w = 0
		for x,y in self.g:
			self.h = max(x, self.h)
			self.w = max(y, self.w)

		for x in range(self.h + 1):
			line = ""
			for y in range(self.w + 1):
				line += self.g[(x, y)]
			self.lines.append(line + "\n")

	def set_dirs(self, dirs):
		self.dirs = dirs
	
	def move(self, pos, di):
		"""Move from a position to a direction, "di" is the index in the "dirs" list
		Example: pos = (1,3), di = 2 => d = (0,1), return (1,4)"""
		d = self.dirs[di]
		return (pos[0] + d[0], pos[1] + d[1])

	def print(self):
		"""Update self values and print grid"""
		self.grid_to_lines()

		print("".join(self.lines))

	def transpose(self):
		"""Transposition (diagonal symmetry)"""
		self.lines = list(zip(*self.lines))
		self.read(self.lines)

	def rotate_cw(self):
		"""Clockwise rotation (1st line becomes last column)"""
		self.lines = list(zip(*self.lines[::-1]))
		self.read(self.lines)

	def rotate_ccw(self):
		"""Counter-clockwise rotation (1st line becomes 1st column)"""
		self.lines = list(zip(*self.lines))[::-1]
		self.read(self.lines)

	def adj(self, x, y, dirs=[]):
		"""Return the list of the values in the neighbors: ["X", "M", "A", "S"]
		default dirs: 4 adj [L, U, R, D]"""
		if not dirs:
			L, LU, U, RU, R, RD, D, LD = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
			dirs = [L, U, R, D]
		
		adjs = []
		for a, b in dirs:
			adj = (x+a, y+b)
			if adj in self.g:
				adjs.append((x+a, y+b, self.g[adj]))
		return adjs

	def find_char(self, c):
		"""Return the list of tuples of all occurences of a char: [(x, y), ...]"""
		found = []
		for (x,y),v in self.g.items():
			if v == c:
				found.append((x, y))
		return found

	def find(self, s, dirs=[]):
		"""Return the list of tuples of all occurences of a word: [(x, y, dir(x), dir(y)), ...]
		default dirs: 4 adj [L, U, R, D]"""
		if len(s) == 1:
			return self.find_char(s)
		
		if not dirs:
			L, LU, U, RU, R, RD, D, LD = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
			dirs = [L, U, R, D]

		found = []
		l = len(s) - 1
		for x, y in self.g: # x,y = position of 1st char in grid
			for a, b in dirs: # a,b = search direction
				if (x+a*l, y+b*l) in self.g: # if last char in grid
					dir_poss = True
					for i in range(l+1): # check each char
						if s[i] != self.g[(x+a*i, y+b*i)]: # if wrong char in grid, break
							dir_poss = False
							break
					if dir_poss:
						found.append((x, y, a, b))
		return found
	
	def find2(self, s, mode=0):
		"""Return the list of tuples of all occurences of a word: [(x, y, dir(x), dir(y)), ...]
		Optimisation vs find(): for R, read s in line, for L in reversed line, for U/D in transposed line
		"""
		L, LU, U, RU, R, RD, D, LD = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
		
		found = []
		if mode in [0, 2]:
			# R + L
			for i, line in enumerate(self.lines):
				found += [(i, m.start(), *R) for m in re.finditer(s, line)]
				found += [(i, self.w - 1 - m.start(), *L) for m in re.finditer(s, line[::-1])]
			
			# D + U
			for i, line in enumerate(map("".join, zip(*self.lines))):
				found += [(m.start(), i, *D) for m in re.finditer(s, line)]
				found += [(self.h - 1 - m.start(), i, *U) for m in re.finditer(s, line[::-1])]
		
		if mode in [1, 2]:
			# make lines with all cells that have equal x+y
			pass

		# print(f"{found=}")
		return found

	def bfs(self, start, end):
		# priority queue
		best = sys.maxsize
		best_tiles = set()
		visited = defaultdict(lambda:best)
		q = PriorityQueue()
		q.put((0, start, 0, []))
		# q.put((0, start, 2, []))

		while not q.empty():
			score, pos, di, path = q.get()

			if pos not in self.g or self.g[pos] == "#":
				continue

			if score >= best:
				# worse than a path to the end
				continue
			
			if score >= visited[(pos, di)]:
				# worse than another path to this tile/direction
				continue
			else:
				# new best score from start to here
				visited[(pos, di)] = score

			if pos == end:
			# if self.g[pos] == "E": # if end is a symbol
				# reached finish
				if score < best:
					# new best found, clear the old tiles
					best = score
					best_tiles.clear()

				if score == best:
					best = score
					for p in path:
						best_tiles.add(p)

					best_tiles.add(pos) # add finish

			else:
				# take a new step to neighbors: same direction, right, left
				for new_di in [di, di+1, di-1]:
					new_di = new_di % 4
					
					new_score = score + 1
					# if new_di != di:
					# 	# change direction = 1000 pts
					# 	new_score += 1000

					new_pos = self.move(pos, new_di)
					q.put((new_score, new_pos, new_di, path + [pos]))
					# q.put((new_score, new_pos, 0, path + [pos])) # if direction doesn't matter
		
		return best, best_tiles
