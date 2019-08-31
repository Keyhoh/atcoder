s = []
for c in input():
    if c == 'B':
        s and s.pop()
    else:
        s.append(c)

print(''.join(s))
