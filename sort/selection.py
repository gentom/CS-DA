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
    #print(array)

if __name__ == "__main__":

    print("---- Random Data ----")

    l1 = RNAGen(100)
    #print(l1)
    selection_sort(l1)
    print()

    l2 = RNAGen(200)
    selection_sort(l2)
    print()

    l3 = RNAGen(300)
    selection_sort(l3)
    print()

    l4 = RNAGen(400)
    selection_sort(l4)
    print()

    l5 = RNAGen(500)
    selection_sort(l5)
    print()



    print("---- Ascending Data ----")

    data = RNAGen(100)
    #print(data)
    data.sort()
    #print(data)
    selection_sort(data)
    print()

    data = RNAGen(200)
    #print(data)
    data.sort()
    #print(data)
    selection_sort(data)
    print()

    data = RNAGen(300)
    #print(data)
    data.sort()
    #print(data)
    selection_sort(data)
    print()

    data = RNAGen(400)
    #print(data)
    data.sort()
    #print(data)
    selection_sort(data)
    print()

    data = RNAGen(500)
    #print(data)
    data.sort()
    #print(data)
    selection_sort(data)
    print()



    print("---- Descending Data ----")

    data = RNAGen(100)
    #print(data)
    data.sort(reverse=True)
    #print(data)
    selection_sort(data)
    print()

    data = RNAGen(200)
    #print(data)
    data.sort(reverse=True)
    #print(data)
    selection_sort(data)
    print()

    data = RNAGen(300)
    #print(data)
    data.sort(reverse=True)
    #print(data)
    selection_sort(data)
    print()

    data = RNAGen(400)
    #print(data)
    data.sort(reverse=True)
    #print(data)
    selection_sort(data)
    print()

    data = RNAGen(500)
    #print(data)
    data.sort(reverse=True)
    #print(data)
    selection_sort(data)
    print()