#!/usr/bin/python3

import sys


 
def fastfib(n):
    """computes fib(n) iteratively using fast doubling method"""
    bin_of_n = bin(n)[2:]  # binary string of n
    f = [0, 1]  # [F(i), F(i+1)] => i=0
 
    for b in bin_of_n:
        f2i1 = f[1]**2 + f[0]**2  # F(2i+1)
        f2i = f[0]*(2*f[1]-f[0])  # F(2i)
 
        if b == '0':
            f[0], f[1] = f2i, f2i1  # [F(2i), F(2i+1)]
        else:
            f[0], f[1] = f2i1, f2i1+f2i  # [F(2i+1), F(2i+2)]
 
    return f[0]




if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    fib = fastfib(n)
    print(fib%10)