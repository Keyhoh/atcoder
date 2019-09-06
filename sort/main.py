import random
import copy
import time
from sort.my import bubble


def measure(name: str, sort: callable, size: int):
    random_list = [random.randint(0, size - 1) for i in range(size)]
    sorted_list = sorted(copy.copy(random_list))
    begin = time.time()
    sort(random_list)
    end = time.time()
    print(name)
    print(end - begin if random_list == sorted_list else 'Failed')


measure('bubble', bubble.sort, 10 ** 4)
