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

def get_ints_pos(s):
	"""Return the list of the ints in a string, formatted as tuples (integer, position)"""
	return [(int(m.group(0)), m.start()) for m in re.finditer(r"\d+", s)]

def sub(s):
	"""Replace a substring with nothing in a string"""
	return re.sub(r"\n", "", s)

# grid
class Grid:
	g = {}

	def read(self, lines):
		"""Fills self.g with dict key as 2D tuple"""
		for x, line in enumerate(lines):
			for y, c in enumerate(line):
				self.g[(x, y)] = c

	def adj(self, x, y, mode=0):
		"""Return the list of the values in the neighbors: ["X", "M", "A", "S"]
		mode = 0: 4 adj [L, U, R, D]
		mode = 1: 4 corners [LU, RU, RD, LD]
		mode = 2: 8 adj [L, LU, U, RU, R, RD, D, LD]"""
		L, LU, U, RU, R, RD, D, LD = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
		dir = [L, U, R, D]
		if mode == 1: dir = [LU, RU, RD, LD]
		if mode == 2: dir = [L, LU, U, RU, R, RD, D, LD]
		
		adjs = []
		for a, b in dir:
			adj = (x+a, y+b)
			if adj in self.g:
				adjs.append(self.g[adj])
		return adjs

	# optimisation: for R, read s in line, for L in reversed line
	# for U/D, in the transposed line
	# for diagonals, just splice the lines properly to create a new line to read in
	# splice all with zip?
	def find(self, s, mode=0):
		"""Return the list of tuples of all occurences of a word: [(x, y, dir(x), dir(y)), ...]"""
		L, LU, U, RU, R, RD, D, LD = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
		dir = [L, U, R, D]
		if mode == 1: dir = [LU, RU, RD, LD]
		if mode == 2: dir = [L, LU, U, RU, R, RD, D, LD]
		
		found = []
		l = len(s) - 1
		for x, y in self.g: # x,y = position of 1st char in grid
			for a, b in dir: # a,b = search direction
				if (x+a*l, y+b*l) in self.g: # if last char in grid
					dir_poss = True
					for i in range(l+1): # check each char
						if s[i] != self.g[(x+a*i, y+b*i)]: # if wrong char in grid, break
							dir_poss = False
							break
					if dir_poss:
						found.append((x, y, a, b))
		return found
