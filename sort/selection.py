# -*- coding: utf-8 -*-
import random

def RNAGen(maxnum):
    l = list(range(maxnum))
    random.shuffle(l)
    return l

def timeCounter(name):
    def _timer(func):
        import functools, datetime
        import time
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.clock()
            print(name)
            func(*args,**kwargs)
            runtime = time.clock() - start
            print(runtime)
        return wrapper
    return _timer

@timeCounter("selection_sort")
def selection_sort(array):
    n = len(array)
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if array[min] > array[j]:
                min = j
        tmp = array[min]
        array[min] = array[i]
        array[i] = tmp
    print(array)

if __name__ == "__main__":
    l = RNAGen(1000)
    selection_sort(l)
    print()