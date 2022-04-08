"""
Write a program that reads an integer N (1 < N < 1000). This N is the number of output lines printed by this program.

Input
The input file contains an integer N.

Output
Print the output according to the given example.

1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
"""
from math import sqrt
from math import pow

N = int(input())

nu = 1
nu2 = 1
nu3 = 1

for c in range(0, N):
    print('{:.0f} {:.0f} {:.0f}'.format(nu, nu2, nu3))
    nu += 1
    nu2 = pow(nu, 2)
    nu3 = pow(nu, 3)
