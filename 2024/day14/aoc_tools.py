import re

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
	"""Return the list of the ints in a string"""
	return [int(d) for d in re.findall(r"\d+", s)]

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
                             
	def read(self, lines):
		"""Fills self.g with dict key as 2D tuple"""
		self.lines = lines
		self.h = len(self.lines)
		self.w = len(self.lines[0])
		for x, line in enumerate(lines):
			for y, c in enumerate(line):
				self.g[(x, y)] = c

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

	def adj(self, x, y, mode=0):
		"""Return the list of the values in the neighbors: ["X", "M", "A", "S"]
		mode = 0: 4 adj [L, U, R, D]
		mode = 1: 4 corners [LU, RU, RD, LD]
		mode = 2: 8 adj [L, LU, U, RU, R, RD, D, LD]"""
		L, LU, U, RU, R, RD, D, LD = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
		dirs = [L, U, R, D]
		if mode == 1: dirs = [LU, RU, RD, LD]
		if mode == 2: dirs = [L, LU, U, RU, R, RD, D, LD]
		
		adjs = []
		for a, b in dirs:
			adj = (x+a, y+b)
			if adj in self.g:
				adjs.append((x+a, y+b, self.g[adj]))
		return adjs

	def find(self, s, mode=0):
		"""Return the list of tuples of all occurences of a word: [(x, y, dir(x), dir(y)), ...]"""
		L, LU, U, RU, R, RD, D, LD = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
		dirs = [L, U, R, D]
		if mode == 1: dirs = [LU, RU, RD, LD]
		if mode == 2: dirs = [L, LU, U, RU, R, RD, D, LD]
		
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
