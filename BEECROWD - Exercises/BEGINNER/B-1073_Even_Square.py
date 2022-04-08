"""
Read an integer N. Print the square of each one of the even values from 1 to N including N if it is the case.

Input
The input contains an integer N (5 < N < 2000).

Output
Print the square of each one of the even values from 1 to N, as the given example.

Be carefull! Some language automaticly print 1e+006 instead 1000000. Please configure your program to print the correct format setting the output precision.
"""

N = int(input())

for c in range(2, N+1, 2):
    square = c ** 2
    print('{}^{} = {}'.format(c, 2, square))
