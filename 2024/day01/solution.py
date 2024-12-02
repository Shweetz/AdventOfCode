# Solution 1
l1, l2 = zip(*[map(int, line.split()) for line in open('2024/day01/input.txt')])

# Part 1
print(sum(abs(x - y) for x, y in zip(sorted(l1), sorted(l2))))

# Part 2
print(sum(x for x in l2 if x in l1))
print(sum(a * l2.count(a) for a in l1))
print()

# Solution 2: numpy
from numpy import loadtxt, sort, isin

A, B = sort(loadtxt('2024/day01/input.txt', int).T)
print(sum(abs(A - B)))
print(sum(isin(B, A) * B))