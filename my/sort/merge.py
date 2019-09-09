def merge(x: list, left: int, mid: int, right: int):
    i, j = left, mid
    y = []
    while i < mid and j < right:
        if x[i] < x[j]:
            y.append(x[i])
            i += 1
        else:
            y.append(x[j])
            j += 1
    if i == mid:
        y.extend(x[j: right])
    else:
        y.extend(x[i: mid])
    x[left:right] = y


def merge_sort(target: list, left: int, right: int):
    if left == right or left == right - 1:
        return
    mid = (left + right) // 2
    merge_sort(target, left, mid)
    merge_sort(target, mid, right)
    merge(target, left, mid, right)


def sort(target):
    merge_sort(target, 0, len(target))
