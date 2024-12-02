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
