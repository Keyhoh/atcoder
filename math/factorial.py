def factorial(n: int):
    if n < 0:
        return 0
    else:
        result = 1
        for i in range(n):
            result *= (i + 1)

        return result
