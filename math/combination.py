def factorial(n: int):
    if n < 0:
        return 0
    else:
        result = 1
        for i in range(n):
            result *= (i + 1)

        return result


def permutation(n: int, m: int):
    if n < 0 or m < 0 or n - m < 0:
        return 0

    result = 1
    for i in range(n - m, n):
        result *= (i + 1)

    return result


def combination(n: int, m: int) -> int:
    if n < 0 or m < 0 or n - m < 0:
        return 0

    m = min(m, n - m)

    if m < 1:
        return 1
    else:
        return permutation(n, m) // factorial(m)
