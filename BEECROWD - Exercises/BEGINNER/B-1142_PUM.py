"""
Write a program that reads an integer N. This N is the number of output lines printed by this program.

Input
The input file contains an integer N.

Output
Print the output according to the given example.

1 2 3 PUM
5 6 7 PUM
9 10 11 PUM
13 14 15 PUM
17 18 19 PUM
21 22 23 PUM
25 26 27 PUM
"""
n1 = 1
n2 = 2
n3 = 3

N = int(input())

for c in range(0, N):
    print('{} {} {} PUM'.format(n1, n2, n3))
    n1 += 4
    n2 += 4
    n3 += 4

