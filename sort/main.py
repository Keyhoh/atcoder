import copy
import random
import time

from sort.my import bubble
from sort.my import insertion


def measure(name: str, sort: callable, size: int):
    random_list = [random.randint(0, size - 1) for i in range(size)]
    sorted_list = sorted(copy.copy(random_list))
    begin = time.time()
    sort(random_list)
    end = time.time()
    print(name)
    print(end - begin if random_list == sorted_list else 'Failed')


measure('bubble', bubble.sort, 10 ** 4)
measure('insertion', insertion.sort, 10 ** 4)
