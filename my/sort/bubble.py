def sort(target: list):
    length = len(target)

    for i in range(1, length - 1):
        for j in range(length - i):
            if target[j] > target[j + 1]:
                target[j + 1], target[j] = target[j], target[j + 1]



