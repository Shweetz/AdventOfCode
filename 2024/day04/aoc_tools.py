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
		pass

	def adj(self, x, y, mode=0):
		"""Return the list of the ints in a string
		mode = 0: 4 adj [L, U, R, D]
		mode = 1: 4 corners [LU, RU, RD, LD]
		mode = 2: 8 adj [L, LU, U, RU, R, RD, D, LD]"""
		adj = []
		L, LU, U, RU, R, RD, D, LD = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
		dir = [L, U, R, D]
		if mode == 1: dir = [LU, RU, RD, LD]
		if mode == 2: dir = [L, LU, U, RU, R, RD, D, LD]
		for a, b in dir:
			if (x+a, y+b) in self.g:
				adj.append(self.g[(x+a, y+b)])
		return adj

	def find(self, s, mode=0):
		"""Return the list of all occurences of a word, formatted as tuples (x, y, dir)"""
		found = []
		L, LU, U, RU, R, RD, D, LD = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
		dir = [L, U, R, D]
		if mode == 1: dir = [LU, RU, RD, LD]
		if mode == 2: dir = [L, LU, U, RU, R, RD, D, LD]
		l = len(s) - 1
		for x, y in self.g:
			for a, b in dir:
				# if (x+a*l, y+b*l) in self.g: and (sum(self.g[(x+a*i, y+b*i)] for i in range(l)) == s):
				if (x+a*l, y+b*l) in self.g:
					dir_poss = True
					for i in range(l+1):
						if not self.g[(x+a*i, y+b*i)] == s[i]:
							dir_poss = False
							break
					if dir_poss:
						found.append((x, y, a, b))
		return found
