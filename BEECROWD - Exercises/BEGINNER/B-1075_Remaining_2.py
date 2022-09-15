"""
Read an integer N. Print all numbers between 1 and 10000, which divided by N will give the rest = 2.

Input
The input is an integer N (N < 10000)

Output
Print all numbers between 1 and 10000, which divided by n will give the rest = 2, one per line.
"""

def remaining(N):

    if N < 10000:
        for i in range(10000):
            if i % N == 2:
                print(i)

remaining(int(input()))


# N = int(input())
#
# for c in range(1, 10001):
#     if c % N == 2:
#         print(c)
