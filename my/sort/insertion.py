def sort(target: list):
    length = len(target)

    for i in range(1, length):
        tmp = target[i]
        if target[i - 1] > tmp:
            j = i
            while j > 0 and target[j - 1] > tmp:
                target[j] = target[j - 1]
                j -= 1
            target[j] = tmp
