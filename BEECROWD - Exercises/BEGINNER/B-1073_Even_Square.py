"""
Read an integer N. Print the square of each one of the even values from 1 to N including N if it is the case.

Input
The input contains an integer N (5 < N < 2000).

Output
Print the square of each one of the even values from 1 to N, as the given example.

Be carefull! Some language automaticly print 1e+006 instead 1000000. Please configure your program to print the correct format setting the output precision.
"""

def print_square(N):

    if 5 < N < 10000:
        for i in range(1, N+1):
            if i % 2 == 0:
                square = i ** 2
                print(f"{i}^2 = {square}")


print_square(int(input()))

# N = int(input())
#
# for c in range(2, N+1, 2):
#     square = c ** 2
#     print('{}^{} = {}'.format(c, 2, square))
