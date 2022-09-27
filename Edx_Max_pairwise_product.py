#!/usr/bin/python3

from random import seed
from random import choice
from random import randint

from functools import wraps
import timeit

import functools
# from time import clock
#import sys
#sys.setrecursionlimit()





# n = int(input())
# a = [int(x) for x in input().split()]
# assert(len(a) == n)

def MaxpairwiseProductNaive(a):
    result = 0
    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
            if a[i]*a[j] > result:
                result = a[i]*a[j]
    print(result)


def MaxPairwiseProductFast(a):
    index1 = 0
    for i in range(len(a)):
        if a[i] > a[index1]:
            index1 = i
    if index1 == 0:
        index2 = 1
        for i in range(len(a)):
            if i != index1 and a[i] > a[index2]:
                index2 = i
    else:
        index2 = 0
        for i in range(len(a)):
            if i != index1 and a[i] > a[index2]:
                index2 = i
    print(a[index1] * a[index2])


# def timing(function):
#     @wraps(function)
#     def wrap(*args):
#         ts = timeit.default_timer()
#         result = function()
#         te = timeit.default_timer()
#         args = str(args)
#         print('function: {} took: {} seconds'.format(function.__name__, te-ts))
#         return result
#     return wrap

@functools.lru_cache(None)
def StressTest(number,raggio,variabilità):
    while True:
        seed(randint(1,variabilità))
        sequence = [i for i in range(2,number)]
        n = choice(sequence) 
        a = [randint(1,raggio) for _ in range(n)]
        print(a)
        result1 = MaxpairwiseProductNaive(a)
        result2 = MaxPairwiseProductFast(a)
        if result1 == result2:
            print('OK')
        else:
            print('Wrong answer: ', result1, result2)
            return False

StressTest(100,200,100)


