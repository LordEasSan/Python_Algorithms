#!/usr/bin/python3


# def calc_fib_naive(n):
#     if (n <= 1):
#         return n
#     return calc_fib_naive(n - 1) + calc_fib_naive(n - 2)

# n = int(input())
# print(calc_fib_naive(n))

def calc_fib_fast(n):
    f = [0,1]
    for i in range(2,n+1):
        f.append(f[i-1] + f[i-2])
        # f[i] = f[i-1] + f[i-2]
    return f[n]


# n = int(input())
# print(calc_fib_fast(n))


def calc_fib_fast2(n, computed = {0: 0, 1: 1}):
    if n not in computed:
        computed[n] = calc_fib_fast2(n-1, computed) + calc_fib_fast2(n-2, computed)
    return computed[n]


print(calc_fib_fast2(20))

