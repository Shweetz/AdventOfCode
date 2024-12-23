from functools import cache
# cache works best with recursion

# use imaginary part to represent j
N = {'7':0, '8':1, '9':2, '4':1j, '5':1+1j, '6':2+1j, 
      '1':2j, '2':1+2j, '3':2+2j, ' ':3j, '0':1+3j, 'A':2+3j}
R = {' ':0, '^':1, 'A':2, '<':1j, 'v':1+1j, '>':2+1j}
a = 0

@cache
def path(start, end):
    pad = N if (start in N and end in N) else R
    diff = pad[end] - pad[start]
    dx, dy = int(diff.real), int(diff.imag)
    yy = ("^"*-dy) + ("v"*dy)
    xx = ("<"*-dx) + (">"*dx)

	# either do all x moves and then all y moves, or the other way around
    # if one way lands on the non-key of the pad, choose the other
    # else, prefer left, then up/down, then right
    # this is because left has 2 presses in a row, which is good, and up/down start with left when expanded
    bad = pad[" "] - pad[start]
    prefer_yy_first = (dx>0 or bad==dx) and bad!=dy*1j
    return (yy+xx if prefer_yy_first else xx+yy) + "A"
    
@cache
def length(code, depth, s=0):
    global a
    print(f"length {code} {depth} {s}")
    if depth == 0: return len(code)
    for i, c in enumerate(code):
        a+=1
        s += length(path(code[i-1], c), depth-1)
    return s

codes = open("2024/day21/input.txt").read().split()
print(sum(int(code[:-1]) * length(code, 3) for code in codes))
print(sum(int(code[:-1]) * length(code, 26) for code in codes))
print(a)