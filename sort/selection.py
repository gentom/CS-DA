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

def counter(i):
    return i + 1

@timeCounter("selection_sort")
def selection_sort(array):
    exchageCount = 0
    turnoverCount = 0
    n = len(array)
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
            if array[min] > array[j]:
                exchageCount = counter(exchageCount)
                min = j
        tmp = array[min]
        array[min] = array[i]
        array[i] = tmp
        turnoverCount = counter(turnoverCount)
    print("ExchangeCountNum: {}".format(exchageCount))
    print("TurnoverCountNum: {}".format(turnoverCount))
    print(array)

if __name__ == "__main__":
    l = RNAGen(100)
    selection_sort(l)
    print()