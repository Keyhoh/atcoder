def swap(target: list, x: int, y: int):
    target[x], target[y] = target[y], target[x]


def push_down(target: list, start: int, end: int):
    parent = start
    child = parent * 2 + 1
    while child < end:
        if child < end - 1 and target[child] < target[child + 1]:
            child += 1
        if target[child] <= target[parent]:
            break
        swap(target, parent, child)
        parent = child
        child = parent * 2 + 1


def sort(target: list):
    length = len(target)
    for i in range(length // 2)[::-1]:
        push_down(target, i, length)
    for i in range(1, length)[::-1]:
        swap(target, 0, i)
        push_down(target, 0, i)
