"""
In mathematics, a perfect number is an integer for which the sum of all its own positive divisors (excluding itself)
is equal to the number itself. For example the number 6 is perfect, because 1+2+3 is equal to 6. Your task is to write
a program that read integer numbers and print a message informing if these numbers are perfect or are not perfect.

Input
The input contains several test cases. The first contains the number of test cases N (1 ≤ N ≤ 100).
Each one of the following N lines contains an integer X (1 ≤ X ≤ 108), that can be or not a perfect number.

Output
For each test case print the message “X eh perfeito” (X is perfect) or “X nao eh perfeito” (X isn't perfect)
according with to above specification.
"""

def perfect_number(n):
    for i in range(n):
        x = int(input())
        count = 0
        for j in range(1, x):
            if x % j == 0:
                count += j
        if count == x:
            print(f"{x} eh perfeito")
        else:
            print(f"{x} nao eh perfeito")


perfect_number(int(input()))


#
# N = int(input())
#
# for c in range(0, N):
#     X = int(input())
#     sum1 = 0
#     for i in range(1, X):
#         if X % i == 0:
#             sum1 += i
#     if sum1 == X:
#         print('{} eh perfeito'.format(X))
#     else:
#         print('{} nao eh perfeito'.format(X))
