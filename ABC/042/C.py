N, K = map(int, input().split())

Ds = set(input().split())

n = N

while set(str(n)) & Ds:
    n += 1

print(n)
