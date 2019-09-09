import copy
import random
import time

from my.sort import bubble
from my.sort import heap
from my.sort import insertion
from my.sort import merge
from my.sort import quick


def measure(name: str, sort: callable, src: list):
    random_list = copy.copy(src)
    sorted_list = sorted(copy.copy(random_list))
    begin = time.time()
    sort(random_list)
    end = time.time()
    print(name)
    print(end - begin if random_list == sorted_list else 'Failed')


size = 10 ** 4
src = [random.randint(0, size - 1) for i in range(size)]
measure('bubble', bubble.sort, src)
measure('insertion', insertion.sort, src)
measure('heap', heap.sort, src)
measure('merge', merge.sort, src)
measure('quick', quick.sort, src)
