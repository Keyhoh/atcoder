def median(x: int, y: int, z: int) -> int:
    if x < y:
        return y if y < z else z if x < z else x
    else:
        return x if x < z else y if y < z else z


def quick_sort(target: list, left: int, right: int):
    if left < right:
        i, j = left, right
        pivot = median(target[i], target[(i + j) // 2], target[j])
        while True:
            while i < right and target[i] < pivot:
                i += 1
            while j > 0 and pivot < target[j]:
                j -= 1
            if i >= j:
                break
            target[i], target[j] = target[j], target[i]
            i += 1
            j -= 1
        quick_sort(target, left, i - 1)
        quick_sort(target, j + 1, right)


def sort(target: list):
    quick_sort(target, 0, len(target) - 1)
