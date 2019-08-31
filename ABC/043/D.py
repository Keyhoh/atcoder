S = input()
L = len(S)

if L == 2:
    print('1 2' if S[0] == S[1] else '-1 -1')
else:
    result = False
    for i in range(L - 2):
        s = S[i:i + 3]
        if s[0] == s[1] or s[1] == s[2] or s[2] == s[0]:
            print(str(i + 1) + ' ' + str(i + 3))
            result = True
            break

    result or print('-1 -1')
