def permutation(n: int, m: int):
    if n < 0 or m < 0 or n - m < 0:
        return 0

    result = 1
    for i in range(n - m, n):
        result *= (i + 1)

    return result
