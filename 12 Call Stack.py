#!/usr/bin/python3

def funcThree():
    print('Three')

def funcTwo():
    funcThree()
    print('Two')

def funcOne():
    funcTwo()
    print('One')

def factorial(n):
    factorial = 1
    if n ==1:
        return 1
    return n * factorial(n-1)


funcOne()

print(factorial(4))
