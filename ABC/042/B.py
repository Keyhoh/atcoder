NL = list(map(int, input().split()))

ss = [input() for i in range(NL[0])]

ss.sort()

print(''.join(ss))
