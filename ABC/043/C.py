N = int(input())
A = list(map(int, input().split()))

ave = round(sum(A) / N)

var = 0

for a in A:
    var += (a - ave) ** 2

print(var)
