def permutation(n: int, m: int):
    if n < 0 or m < 0:
        return 0
    elif m < 1:
        return 1
    else:
        return n * permutation(n - 1, m - 1)
